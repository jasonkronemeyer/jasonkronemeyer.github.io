# Dagg, Rhinesmith, Bauer, Byrum & Schill - Measurement Framework

The Digital Opportunities Compass team provides the **operational measurement framework** that translates theory and evidence into actionable metrics for your digital equity intelligence system.

## **The Research Team - Quick Overview**

**Pierrette Renée Dagg**
- **Director of Technology Impact Research, Merit Network** (University of Michigan)
- **PhD Candidate:** University of Toledo, Social and Philosophical Foundations of Education and Education Technology
- **Recognition:** Named you as a Broadband Champion in Benton Institute series
- **Bridge-builder:** Connects academic scholarship to practical application

**Colin Rhinesmith**
- **Founder and Director, Digital Equity Research Center** (Metropolitan New York Library Council)
- **Research Fellow, Quello Center**, Michigan State University
- **Co-Editor-In-Chief,** The Journal of Community Informatics
- **Expert in:** Community informatics, digital equity ecosystems

**Johannes M. Bauer** (CONNECTING FIGURE)
- **Professor and Director, Quello Center**, Michigan State University
- **On BOTH papers:** Hampton et al. (2020) empirical study AND Dagg et al. (2023) measurement framework
- **Ensures continuity:** From evidence → measurement → policy

**Greta Byrum**
- **Digital equity practitioner and researcher** since 2010 BTOP program
- **Founder:** Community Tech NY, New School's Digital Equity Lab
- **Expert in:** Community-owned broadband, collaborative ecosystems

**Aaron Schill**
- **Director of Research & Programs, National Digital Inclusion Alliance (NDIA)**
- **Expert in:** Data analytics, visualization, GIS, digital inclusion programming
- **Background:** Mid-Ohio Regional Planning Commission, urban planning

### **Their Major Contribution: "Digital Opportunities Compass" (2023)**

A comprehensive measurement framework with **six components** to guide BEAD and Digital Equity Act implementation, moving beyond infrastructure-only metrics to holistic digital equity assessment.

**Institution:** Quello Center (MSU), Benton Institute, NDIA, Merit Network  
**URL:** https://quello.msu.edu/digital-opportunities-compass-metrics-to-monitor-evaluate-and-guide-broadband-and-digital-equity-policy/  
**Purpose:** Support state agencies developing digital equity plans for IIJA funding  
**Significance:** Operationalizes 25 years of broadband and digital equity research

### **The Six Components:**

1. **Contexts** - Sociodemographic, economic, and community level factors
2. **Governance** - Local, state, and federal policy, governance, and power
3. **Connectivity** - Infrastructure, accessibility, affordability, adoption
4. **Skills** - Digital literacy, training, and skills attainment
5. **Application** - Uses and application in sociotechnical contexts
6. **Outcomes** - Broader effects on individuals, communities, and states

### **Why Dagg et al. Matter for Digital Equity:**

**Theory and evidence exist (Sen, Dweck, Toyama, Hampton & Bauer):**
- Tell us WHAT to do and WHY it works

**Dagg et al. Digital Opportunities Compass:**
- Tells us HOW TO MEASURE success
- Provides STANDARDIZED METRICS states can use
- Translates research into ACTIONABLE INDICATORS

### **Dagg et al.'s Key Insight:**

> **"Digital Equity Act requires five measurable objectives—but achieving outcomes requires consideration of additional factors beyond these five."**

**DEA's five objectives:**
1. Availability & affordability of broadband
2. Online accessibility of public resources
3. Digital literacy
4. Cybersecurity awareness
5. Device availability & technical support

**Compass adds:** Contexts (demographics) + Governance (policy) + Application (relevance) + integrated Outcomes assessment

**Why this matters:** Addresses Hampton & Bauer's findings—infrastructure + unclear value + affordability uncertainty = gaps

### **How Dagg et al. Ground Your Framework:**

**Your pathway:**
```
Opportunity → Aspiration → Growth Mindset → Digital Equity
```

**Dagg Compass provides measurement for each stage:**

| Your Stage | Compass Component | Measurable Indicators |
|---|---|---|
| **Opportunity** | **Connectivity** | Infrastructure maps, speeds, costs, adoption rates, device access |
| **Aspiration** | **Application** | Use cases, engagement metrics, perceived relevance, application diversity |
| **Growth Mindset** | **Skills** | Literacy assessments, training completion, confidence surveys, secure practices |
| **Digital Equity** | **Outcomes** | Achievement gaps, economic effects, health outcomes, civic engagement |
| **Variables** | **Contexts** | Income, education, age, geography, disability status (Bayesian priors) |
| **Interventions** | **Governance** | BEAD funding, navigator programs, policy structures (Bayesian interventions) |

**Complete integration:** Every stage of your pathway has operational measurement through the Compass

### **The Digital Opportunities Compass Framework:**

**Designed to:**
- ✅ Identify key groups of factors influencing digital equity
- ✅ Measure and assess efforts and outcomes over time
- ✅ Utilize standardized core metrics (customizable to state needs)
- ✅ Build on existing data and indices (ACS, FCC, etc.)
- ✅ Augment with new qualitative and quantitative data
- ✅ Enable automated data collection where possible

**For policymakers:**
- **Planning phase:** "What factors should we assess?"
- **Implementation phase:** "Are our interventions working?"
- **Evaluation phase:** "Did we achieve digital equity outcomes?"

### **Integration with Your System:**

**Compass Component → Your System Implementation:**

```
1. CONTEXTS (Demographics, Economics)
   ↓ Feed into
   Bayesian Network as prior probabilities and conditional variables
   Example: P(Included | Income=Low) vs P(Included | Income=High)

2. GOVERNANCE (Policy, Power Structures)
   ↓ Modeled as
   Intervention nodes in Bayesian network
   Example: P(Included | NavigatorProgram=Yes) vs No

3. CONNECTIVITY (Infrastructure, Adoption)
   ↓ Operationalizes
   "Opportunity" stage measurement
   Example: Infrastructure_score, Affordability_index, Adoption_rate

4. SKILLS (Literacy, Training)
   ↓ Operationalizes
   "Growth Mindset" stage measurement
   Example: Literacy_level, Training_hours, Confidence_score

5. APPLICATION (Use, Relevance)
   ↓ Operationalizes
   "Aspiration" stage measurement
   Example: Use_diversity, Perceived_relevance, Engagement_frequency

6. OUTCOMES (Effects, Impacts)
   ↓ Operationalizes
   "Digital Equity" outcome measurement
   Example: Gini_coefficient, Achievement_gaps, Inclusion_rate
```

**Your Bayesian network ingests Compass metrics to predict outcomes!**

### **Practical Application Example:**

**Michigan County Assessment Using Compass:**

```cypher
// Store Compass assessment data in knowledge graph
CREATE (county:Region {name: 'Upper Peninsula County'})

// CONTEXTS component
SET county.income_median = 45000,
    county.education_bachelors_pct = 18,
    county.age_65plus_pct = 22,
    county.rural_pct = 85

// CONNECTIVITY component  
SET county.fiber_availability_pct = 35,
    county.broadband_adoption_pct = 52,
    county.affordability_index = 0.65

// SKILLS component
SET county.digital_literacy_score = 2.8,  // out of 5
    county.training_programs = 3,
    county.navigator_access = 'Limited'

// APPLICATION component
SET county.telehealth_use_pct = 28,
    county.remote_work_pct = 15,
    county.online_gov_services_pct = 40

// OUTCOMES component
SET county.gini_coefficient = 0.44,
    county.achievement_gap = 18,  // percentage points
    county.digital_inclusion_rate = 0.58

// Feed into Bayesian network
MATCH (model:BayesianModel)
CREATE (county)-[:GENERATES_PRIORS]->(model)
```

**System then predicts:** "If we deploy $10M BEAD + $2M navigators, predicted Gini → 0.39, inclusion → 0.72"

### **Why Standardized Metrics Matter:**

**Without Compass:**
```
State A measures: "Broadband availability"
State B measures: "Broadband adoption"  
State C measures: "Device ownership"

→ Can't compare across states
→ Can't learn from each other's successes
→ Federal evaluation is fragmented
```

**With Compass:**
```
All states measure:
  - Connectivity (availability, adoption, devices)
  - Skills (literacy, training)
  - Application (use cases)
  - Outcomes (achievement, economic, health)
  - Plus: Contexts and Governance

→ Cross-state comparison possible
→ Best practices identifiable
→ Federal evaluation coherent
```

### **The Research Foundation:**

From Compass paper:
> *"The approach presented here is closely tied to the findings of 25 years of research and experience of how broadband and device access, affordability, and digital literacy relate to digital equity and broader social and development outcomes."*

**25 years of research synthesized into:**
- 6 components
- Dozens of specific indicators
- Customizable to state/community needs
- Builds on existing data sources (efficiency)
- Allows for new data collection (comprehensiveness)

### **Integration with Other Researchers:**

| Researcher | Layer | Dagg et al.'s Role |
|---|---|---|
| **Sen (1999)** | Theory: Capabilities | Compass: Measures capabilities (Connectivity) and functionings (Outcomes) |
| **Dweck (2006)** | Mechanism: Mindset | Compass: Skills component includes confidence, training (growth mindset indicators) |
| **Toyama (2015)** | Principle: Amplification | Compass: Contexts + Connectivity = measures what gets amplified |
| **Hampton & Bauer (2020)** | Evidence: Michigan data | Compass: Operationalizes their findings (infrastructure, value, skills) |

**Bauer's continuity:** From empirical evidence (2020) → measurement framework (2023) → policy implementation (your system)

### **Dagg et al.'s Influence on Digital Equity:**

**Policy impact:**
- **NTIA guidance:** Influenced federal evaluation frameworks for BEAD/DEA
- **State planning:** Multiple states using Compass for digital equity plans
- **Research community:** Standard reference for comprehensive assessment

**Practitioner impact:**
- **Digital navigator programs:** Use Skills component metrics
- **Broadband planning:** Use Connectivity component indicators
- **Community organizations:** Use Application component for relevance assessment

**Your work:**
- **Bayesian network variables:** Directly from Compass components
- **Knowledge graph properties:** Store Compass metrics as node properties
- **GraphRAG queries:** "Show me Compass indicators for this region"

### **The Quote That Summarizes Everything:**

> *"The Digital Opportunities Compass is intended to be a starting point, rather than the final word, regarding the development of a comprehensive assessment framework to monitor, evaluate and guide state broadband and digital equity policy—now and in the future."*

**Translation:**
```
Flexible framework that:
  - Provides core structure (6 components)
  - Allows customization (state/community needs)
  - Evolves over time (learn and adapt)
  - Guides comprehensive assessment (beyond infrastructure)

Your system implements this:
  - Core variables from Compass components
  - Customizable to Michigan regions
  - Learns from data (Bayesian updates)
  - Assesses complete pathway (not just access)
```

### **Why Your Framework Needs Dagg et al.:**

**Without Dagg et al.:**
- Theory says what to do (Sen, Dweck, Toyama)
- Evidence says it works (Hampton & Bauer)
- BUT: How do we MEASURE if we're succeeding?

**With Dagg et al.:**
- Standardized metrics for every stage
- Operational definitions of abstract concepts
- Data sources identified
- State-level implementation guidance

**Your system operationalizes Compass:**
```
Compass provides metrics
  ↓
Your knowledge graph stores them
  ↓
Your Bayesian network models relationships
  ↓
Your GraphRAG answers policy questions
  ↓
BEAD/DEA implementation guided by evidence
```

### **The Michigan Advantage (Again):**

**Research ecosystem:**
```
Hampton & Bauer (2020)
  → Quello Center (MSU)
  → Empirical evidence from Michigan

Dagg et al. (2023)  
  → Quello Center (MSU) + Merit Network (UMich) + NDIA
  → Measurement framework FOR Michigan

Dr. Stilian Stoev (Statistics, UMich)
  → Gini coefficient & Hájek Estimator methodology
  → Statistical rigor for inequality measurement

Your system
  → Implements Compass using Michigan data
  → Uses Stoev's statistical methods for outcomes
  → Participates in Quello Center research ecosystem
  → "Research became our voice"
```

**Dagg's role:** 
- Recognized you as Broadband Champion
- Works at Merit Network (Michigan Moonshot partner)
- Co-created framework you're operationalizing

**This isn't coincidence—it's an integrated Michigan digital equity research and implementation ecosystem.**

### **Specific Compass Indicators Your System Can Use:**

**Connectivity Component:**
- Infrastructure availability maps (FCC data)
- Advertised vs. actual speeds (M-Lab)
- Subscription rates by demographics (ACS)
- Device ownership (ACS, surveys)
- Affordability as % of income (cost data + ACS)

**Skills Component:**
- Digital literacy assessments (Northstar, surveys)
- Training program enrollment/completion (navigator programs)
- Confidence/self-efficacy scales (survey instruments)
- Secure practices adoption (cybersecurity awareness)

**Application Component:**
- Use case diversity (telehealth, education, work, civic)
- Engagement frequency (survey data)
- Perceived relevance (qualitative + quantitative)
- Online service adoption (government, healthcare portals)

**Outcomes Component:**
- Gini coefficient (your Hájek estimator - learned from Dr. Stilian Stoev, UM Statistics)
- Achievement gaps (education data)
- Economic indicators (employment, income changes)
- Health outcomes (telehealth adoption, health metrics)
- Civic engagement (voter registration, participation)

### **Practical Example: Navigator Program Evaluation**

**Using Compass to measure your EUPConnect work:**

```
BASELINE (Pre-navigator program):
  Connectivity: 0.65 (infrastructure good, adoption low)
  Skills: 0.42 (low literacy, limited training)
  Application: 0.38 (narrow use cases, low relevance perception)
  Outcomes: Gini=0.44, Inclusion=0.58

INTERVENTION: $2M navigator program over 2 years

PREDICTED (Bayesian model using Compass metrics):
  Connectivity: 0.72 (adoption increases as navigators assist)
  Skills: 0.68 (literacy improves through training)
  Application: 0.65 (use cases expand as relevance demonstrated)
  Outcomes: Gini=0.38, Inclusion=0.74
  [Gini calculated using Hájek Estimator - Dr. Stilian Stoev, UM Statistics]

ACTUAL (Measured after 2 years):
  [Compare predictions to outcomes]
  [Update Bayesian priors based on results]
  [Refine model for future predictions]
```

**This is evidence-based policymaking using Compass framework!**

### **Bottom Line:**

Dagg et al. provide the **operational measurement layer** that makes your framework actionable for policy.

**Sen tells us:** Theory—what concepts matter (capabilities, agency, functionings)  
**Dweck tells us:** Mechanism—growth mindset enables learning  
**Toyama tells us:** Principle—technology amplifies capacity  
**Hampton & Bauer tell us:** Evidence—Michigan data validates the pathway  
**Dagg et al. tell us:** **Measurement—here's HOW to quantify every stage**  

**Together:** Complete framework from theory → evidence → measurement → implementation → policy

Without Dagg et al., you have theory and evidence but no standardized way to measure success. With Dagg et al., you have **operational metrics** that feed directly into your Bayesian network, enabling predictive modeling and evidence-based decision-making.

**Plus:** Dr. Dagg recognized you as a Broadband Champion and works in the Michigan research ecosystem you're part of. Your system **operationalizes her framework** for Michigan digital equity.

This is the measurement layer that makes everything actionable.

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Part of:** Project Compass (Merit Network) - Digital Opportunities Intelligence Network (DOIN) • Working draft
