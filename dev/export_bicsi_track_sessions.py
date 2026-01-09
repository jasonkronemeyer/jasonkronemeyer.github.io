#!/usr/bin/env python3
"""Export BICSI a2zinc session titles + descriptions for a given TrackID.

This script is intended to be run locally by you.

Example:
  python3 dev/export_bicsi_track_sessions.py --track-id 22 \
    --out tmp/bicsi-winter2026-track22-sessions-full.md

Notes:
- Be respectful of the site (adds a small delay between requests).
- Output is plain text extracted from HTML; you may want to spot-check formatting.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


DEFAULT_BASE = "https://s23.a2zinc.net/clients/BICSI/winter2026/public/"


@dataclass(frozen=True)
class SessionRef:
    title: str
    datetime: str
    room: str
    url: str
    session_id: str
    session_date_id: str


@dataclass(frozen=True)
class SessionDetails:
    title: str
    datetime: str
    room: str
    url: str
    description: str


def _fetch(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) export-script/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return data.decode("utf-8", errors="replace")


def _collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _strip_tags(fragment: str) -> str:
    # Basic HTML-to-text, good enough for these pages.
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"</p>\s*<p[^>]*>", "\n\n", fragment, flags=re.I)
    fragment = re.sub(r"<li[^>]*>", "- ", fragment, flags=re.I)
    fragment = re.sub(r"</li>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"</?(ul|ol)[^>]*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<.*?>", " ", fragment, flags=re.S)
    fragment = html.unescape(fragment)

    # Normalize whitespace while keeping paragraph breaks.
    fragment = fragment.replace("\r\n", "\n").replace("\r", "\n")
    fragment = re.sub(r"[ \t]+", " ", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    return fragment.strip()


def parse_track_sessions(track_html: str, base_url: str) -> list[SessionRef]:
    # Map positions in HTML to the nearest prior datetime heading.
    time_positions: list[tuple[int, str]] = []
    for m in re.finditer(
        r'<h4[^>]*class="sessionDateTime"[^>]*>\s*(.*?)\s*</h4>',
        track_html,
        flags=re.I | re.S,
    ):
        dt = html.unescape(re.sub(r"<.*?>", " ", m.group(1)))
        dt = _collapse_ws(dt)
        time_positions.append((m.start(), dt))
    time_positions.sort()

    def datetime_for(pos: int) -> str:
        dt = ""
        for p, s in time_positions:
            if p <= pos:
                dt = s
            else:
                break
        return dt

    sessions: list[SessionRef] = []

    # Titles are inside a JS call: showFeatures('SessionDetails','SessionDetails.aspx?...')
    for m in re.finditer(
        r"showFeatures\('SessionDetails','(SessionDetails\.aspx\?[^']*?SessionID=\d+[^']*?)'\);.*?<b>(.*?)</b>",
        track_html,
        flags=re.I | re.S,
    ):
        rel = m.group(1).replace("&amp;", "&")
        title = html.unescape(re.sub(r"<.*?>", " ", m.group(2)))
        title = _collapse_ws(title)

        sid = re.search(r"SessionID=(\d+)", rel, flags=re.I)
        sdate = re.search(r"SessionDateID=(\d+)", rel, flags=re.I)
        session_id = sid.group(1) if sid else ""
        session_date_id = sdate.group(1) if sdate else ""

        # Room is typically nearby.
        window = track_html[m.end() : m.end() + 800]
        rm = re.search(
            r'<div[^>]*class="yes-room"[^>]*>\s*<b>\s*Room:\s*(.*?)\s*</b>',
            window,
            flags=re.I | re.S,
        )
        room = ""
        if rm:
            room = html.unescape(re.sub(r"<.*?>", " ", rm.group(1)))
            room = _collapse_ws(room)

        sessions.append(
            SessionRef(
                title=title,
                datetime=datetime_for(m.start()),
                room=room,
                url=base_url + rel,
                session_id=session_id,
                session_date_id=session_date_id,
            )
        )

    # Deduplicate by SessionID (some pages can include repeats).
    dedup: dict[str, SessionRef] = {}
    for s in sessions:
        key = s.session_id or s.url
        dedup[key] = s
    return list(dedup.values())


def parse_session_description(details_html: str) -> str:
    # Grab everything after "Description" heading until next heading.
    m = re.search(
        r"<h4>\s*<b>\s*Description\s*</b>\s*</h4>(.*?)(?=<h4>\s*<b>|$)",
        details_html,
        flags=re.I | re.S,
    )
    if not m:
        return ""
    return _strip_tags(m.group(1))


def parse_session_title_from_title_tag(details_html: str) -> str:
    # Fallback if you ever want it: <title> ...: Session: XYZ </title>
    m = re.search(r"<title>(.*?)</title>", details_html, flags=re.I | re.S)
    if not m:
        return ""
    title = html.unescape(_collapse_ws(m.group(1)))
    # Prefer the part after "Session:" when present.
    m2 = re.search(r"Session:\s*(.*)$", title)
    return m2.group(1).strip() if m2 else title


def export_markdown(sessions: Iterable[SessionDetails], track_url: str) -> str:
    lines: list[str] = []
    lines.append("# BICSI Winter 2026 — Track Sessions Export")
    lines.append("")
    lines.append(f"Source: {track_url}")
    lines.append("")

    for s in sessions:
        lines.append(f"## {s.title}")
        lines.append("")
        if s.datetime:
            lines.append(f"- Time: {s.datetime}")
        if s.room:
            lines.append(f"- Room: {s.room}")
        lines.append(f"- Details: {s.url}")
        lines.append("")
        if s.description:
            lines.append(s.description)
            lines.append("")
        lines.append("---")
        lines.append("")

    # Trim trailing separator
    if lines[-2:] == ["---", ""]:
        lines = lines[:-2]

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Export BICSI a2zinc sessions for a track.")
    parser.add_argument("--base-url", default=DEFAULT_BASE, help="Base public URL ending in /public/")
    parser.add_argument("--track-id", default="22", help="TrackID number")
    parser.add_argument("--out", default="tmp/bicsi-track-sessions.md", help="Output Markdown path")
    parser.add_argument("--delay", type=float, default=0.8, help="Delay (seconds) between detail-page requests")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of sessions (0 = no limit)")
    args = parser.parse_args()

    base_url = args.base_url
    if not base_url.endswith("/"):
        base_url += "/"

    track_url = f"{base_url}Sessions.aspx?nav=true&TrackID={args.track_id}"

    try:
        track_html = _fetch(track_url)
    except urllib.error.URLError as e:
        raise SystemExit(f"Failed to fetch track page: {e}")

    refs = parse_track_sessions(track_html, base_url=base_url)
    refs.sort(key=lambda r: (r.datetime, r.title))

    if args.limit and args.limit > 0:
        refs = refs[: args.limit]

    details_list: list[SessionDetails] = []
    for i, ref in enumerate(refs, start=1):
        try:
            details_html = _fetch(ref.url)
        except urllib.error.URLError as e:
            desc = ""
        else:
            desc = parse_session_description(details_html)

        details_list.append(
            SessionDetails(
                title=ref.title,
                datetime=ref.datetime,
                room=ref.room,
                url=ref.url,
                description=desc,
            )
        )

        if args.delay:
            time.sleep(args.delay)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(export_markdown(details_list, track_url=track_url), encoding="utf-8")

    print(f"Wrote {out_path} ({len(details_list)} sessions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
