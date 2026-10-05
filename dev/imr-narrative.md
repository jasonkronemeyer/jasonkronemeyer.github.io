---
layout: post
title: "Built to Scale: Designing Data Infrastructure for Nationwide Broadband Measurement"
subtitle: "A narrative of my work designing the data layer for the NSF-funded Internet Measurement Research project"
author: "Jason F. Kronemeyer"
type: "essay"
status: draft
date: 2026-10-05
tags:
  - Internet Measurement Research
  - Research Data Infrastructure
  - Scalability
  - FCC Broadband Data Collection
  - Broadband Serviceable Location Fabric
  - Ookla Open Data
  - DuckDB
  - Parquet
  - Quadkeys
---

Most of the work behind a statistical paper never appears in the paper. On the Internet Measurement Research (IMR) project, my work was the part that does not: designing the data infrastructure so that an analysis of broadband availability could run on nationwide infrastructure data, not on a single state or a convenient sample.

The paper those authors produced, *Towards Unbiased Inference of Internet Broadband Availability Based on Observational Speed Test Data*, takes on a problem every crowd-sourced measurement faces: the people who run speed tests are not a random sample. Traditional survey methods do not apply, because the link between a measurement and the person behind it is often missing. The authors model the propensity of testing, the likelihood that a connected user runs a test, and use inverse probability weighting to correct for it. Applied to Ookla Open data with covariates derived from the FCC Broadband Data Collection (BDC) and Fabric data, the framework produces nationwide maps of broadband density at the census tract, county, state, and ZIP code levels.

A method like that is only as national as the data beneath it. The methodological and statistical contributions belong to Amy Stuyvesant, Stilian Stoev, and George Michailidis, and I will not claim them. My job was to build the ground they stood on, and to build it so that it would still hold as the data grew.

## Two datasets that did not agree on what a place is

The project joined two sources that describe the same country in incompatible ways. Ookla's open speed-test data records what people measured, aggregated to Bing tiles at zoom level 16. The FCC's Broadband Data Collection records what providers say they offer, attached to individual locations in the CostQuest Broadband Serviceable Location Fabric. One is a measurement of behavior. The other is a statement of availability. Neither is a clean version of the truth, which is exactly why comparing them is interesting.

The bridge was the quadkey. Every Fabric location got a zoom-16 quadkey, which put the FCC's addresses on the same grid Ookla already used. That sounds like a one-line decision. In practice it meant splitting a very large national CSV by state, computing a tile for every location, dropping the address columns we did not need, and writing the result to a form that could be queried again without starting over.

The choice served the statistics directly. A propensity-of-testing model needs a denominator: how many connections in a tile could have produced a test. Counts of connected locations per quadkey, derived from the FCC data, supplied it. The project notes define the raw testing propensity as devices divided by connected locations, and use a fitted model on those counts in practice. The covariates were the point of the infrastructure, not a by-product of it.

## From fragments to a working system

The FCC releases arrived as folders of CSVs, one set per technology and filing period. I loaded them into a DuckDB database, one table per technology and release, covering cable, copper, fiber to the premises, and three kinds of fixed wireless. For each state and release, the pipeline flagged which technologies served each location. It then aggregated those flags by quadkey, weighting by the number of units at each location, to produce the covariates the analysis needed. Each Ookla quarter was joined to the nearest FCC release in time, because the two sources do not share a calendar.

The pipeline ended in maps at several geographic scales: block, tract, zip code, and county. The paper reports nationwide results at the tract, county, state, and ZIP code levels. Every step was written to be rerun, and I kept notes on the order of operations because a process only one person can reproduce is not infrastructure. It is a habit.

The finished system covers all 56 states and territories and holds roughly one billion records. At that size, small decisions became visible. Reading GEOIDs without declaring them as text silently dropped leading zeros. Computing quadkeys row by row across the full national Fabric was far slower than it needed to be. An early Python prototype of the aggregation step had a bug that computed several technology counts from the cable table instead of their own. The R pipeline did not carry that bug forward, but I only knew that because I had written down what went wrong the first time.

## Designing for the whole country, not a single state

The design brief was nationwide from the start, and a billion records is not a number you can hold in memory on a shared research server. A workflow that works for one state and breaks for fifty is a prototype. So most of the design came down to one question: what does the analysis actually need to carry forward, and how do we keep every step cheap enough to repeat for the entire country?

The first answer was *less*. The Fabric arrived as one giant national CSV. I trimmed it to the columns the analysis used, kept only active serviceable locations, dropped the address fields, and split the result by state. The Ookla side was already narrowed to fixed (not mobile) tests. The biggest reduction came from changing the unit of analysis. Locations were aggregated up to zoom-16 quadkeys, weighted by unit count, so the join with Ookla happened between two tile-level tables and never between a billion location rows and anything else.

The second answer was *do not load it*. The FCC releases lived in a DuckDB database file on disk, one table per technology and release, and the work was done by querying that file in place. Ookla's data sat as partitioned Parquet by type, year, and quarter, so a query for one quarter touched one slice of the files. DuckDB, as my research notes put it, reads only the columns a query needs and pushes filters down into the files, which is why a laptop-sized engine can work against data far larger than its memory.

The third answer was *store it by column*. Parquet and DuckDB are both columnar, and that fits this data. The analysis asked narrow questions of wide tables, such as which technologies serve a quadkey or how many devices tested in it. Columnar storage compresses repeated values well, such as state codes, release labels, and technology flags, and it lets a query skip every column it does not touch. The quadkey step wrote its trimmed output to Parquet for that reason, with ZIP codes kept as strings so leading zeros survive.

The last answer was *keep it portable*. DuckDB is a single file with no server to administer, and Parquet is an open format that R, Python, and other engines read without conversion. Raw files moved between a cloud drive and the analysis server with rclone. None of the pieces depended on a particular vendor or a particular machine.

## Designed to keep scaling

The nationwide system as built is not the limit of the design. Three choices keep it extensible, and each one is a recommendation rather than a finished feature.

First, keep the unit of analysis coarse. Adding a new FCC release or Ookla quarter adds tiles, not locations, so growth is far slower than the raw record count suggests. Second, treat Parquet, partitioned by state and period, as the long-term storage layer, and let DuckDB query it directly. That is already how the Ookla data is laid out, and the pipeline's per-state RData outputs are the part most worth moving to the same pattern. RData ties the results to R, while Parquet does not. Third, if the data eventually needs versioning, concurrent writers, or cloud object storage, a table format such as DuckLake, which keeps metadata in a SQL database and the data in Parquet, is a natural next step. I have studied it but not used it on this project.

## Judgment calls hidden inside the data

Some of the most consequential work was deciding what to ignore. The advertised maximum speed field looked useful, but most copper locations report zero, so a filter built on it would have quietly erased a whole technology. I flagged technologies by whether they served a location, not by what they claimed to deliver. Similarly, the Ookla data from 2019 does not line up well with the latest FCC infrastructure data, which is the reason the project matches several FCC releases to the closest Ookla quarter instead of using one.

None of these choices is dramatic. Together they determine whether a downstream estimate means anything.

## What I would still say with caution

I did not produce the paper's findings, and I will not summarize them here. I am describing the system that supported them, not vouching for the inferences drawn from it. The paper itself describes its work as in progress, so the infrastructure and the analysis may both continue to change. The notes also record limits I know about. Some paths in the code assume the layout of the university server it ran on. An application folder in the repository is a placeholder. A few scripts were superseded or never finished. A data pipeline that admits where it is unfinished is easier to trust than one that does not.

## Why it still matters

Broadband policy is increasingly made on maps, and maps are only as good as the data under them. Observational speed tests and provider filings each carry their own bias. Reconciling them is slow, unglamorous work that decides whether a rural household is counted as served or overlooked.

The paper's bias-corrected broadband density and its measure of inequality in connectivity quality are meant to identify broadband deserts and well-served tracts, and to inform local infrastructure development, including in Michigan. Those classifications only mean something if the underlying join is complete and repeatable for every state.

That is the lesson I carry forward. Evidence-based policy needs good statistics, and good statistics need data infrastructure that someone has designed to scale, to be repeatable, and to be portable beyond the project that first needed it. The same pattern of coarse tiles, columnar files, and on-disk queries applies to any nationwide infrastructure dataset, not only broadband.

---

## What this narrative is based on

**Independent (peer-reviewed or working-paper source):** Stuyvesant, A., Stoev, S., & Michailidis, G. (2025). *Towards unbiased inference of Internet broadband availability based on observational speed test data* (SSRN Working Paper No. 5372801). NSF Public Access Repository. https://par.nsf.gov/servlets/purl/10668222 I drew on the published abstract and have not restated findings beyond it.

**My own records:** Project notes in `project-imr/Notes/notes.md` and `project-imr/R/README.txt`, covering data sources, pipeline steps, definitions, and lessons learned. The column trimming, Parquet output, and partitioned Ookla layout come from these.

**My own research:** The points about columnar reads, predicate pushdown, and DuckLake come from my research notes, "Data Infrastructure Performance: DuckDB Extensions, DuckLake, and Bayesian Network Inference" (`notes/research/BayesDuck.md`). Its benchmark figures are from third-party sources cited there and are not reproduced here.

**My own projection or inference:** The scaling recommendations in "Designed to keep scaling" are design recommendations, not measured results. I have not benchmarked the pipeline beyond its current size. The statement that the pattern applies to other nationwide infrastructure datasets is likewise my inference, not a tested result.

**My own account:** The description of my role and the roughly one-billion-record scale come from my own summary of the work (`dev/imr.md`), and the nationwide design goal is my own framing of the project. None of it is independently sourced. The coverage of all 56 states and territories is from `project-imr/R/README.txt`.
