#!/usr/bin/env python3
"""Erzeugt Literaturverzeichnis, Beschaffungsliste und BibTeX aus literatur/quellen.csv.

Aufruf (aus dem Repo-Root):  python3 tools/build_literatur.py
Die CSV ist die einzige Quelle der Wahrheit. Generierte Dateien nicht von Hand editieren.
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT = ROOT / "literatur"
CSV = LIT / "quellen.csv"

THEMEN = {
    "grundlagen": "Grundlagen und Theorie",
    "methodik": "Methodik, Modellbildung, Erweiterungen",
    "digital": "Digitalisierung, MBSE, Software",
    "anwendung": "Anwendungen und Fallstudien",
    "evaluation": "Empirische Evaluation",
    "lehre": "Lehre",
    "einordnung": "Einordnung und Kontext",
}
STATUS = {
    "vorhanden": "PDF im Repo",
    "oa_download": "frei verfügbar",
    "kit_zugang": "KIT-Zugang nötig",
    "pruefen": "Angaben prüfen",
    "web": "Webquelle",
}
BIBTYPE = {
    "journal": "article",
    "conference": "inproceedings",
    "chapter": "incollection",
    "dissertation": "phdthesis",
    "thesis": "mastersthesis",
    "working_paper": "techreport",
    "preprint": "misc",
    "web": "misc",
    "software": "misc",
}


def load():
    with CSV.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def short_authors(a):
    names = [n.strip() for n in a.split(";") if n.strip()]
    if len(names) > 3:
        return f"{names[0]} et al."
    return "; ".join(names)


def link(r):
    if r["doi"]:
        return f"[DOI](https://doi.org/{r['doi']})" if not r["doi"].startswith("http") else f"[Link]({r['doi']})"
    if r["url"]:
        return f"[Link]({r['url']})"
    return "keine"


def access(r):
    parts = []
    if r["url"]:
        parts.append(f"[Volltext/Seite]({r['url']})")
    if r["doi"] and not r["doi"].startswith("http"):
        parts.append(f"[DOI](https://doi.org/{r['doi']})")
    return ", ".join(parts) or "über Katalog suchen"


def md_escape(s):
    return s.replace("|", "\\|")


def build_verzeichnis(rows):
    by = defaultdict(list)
    for r in rows:
        by[r["thema"]].append(r)
    out = [
        "# Literaturverzeichnis C&C²-Ansatz",
        "",
        "> Generiert aus [`quellen.csv`](quellen.csv) mit `python3 tools/build_literatur.py`. Nicht von Hand editieren.",
        "",
        f"**{len(rows)} Quellen.** Priorität: **A** = Pflichtlektüre, **B** = vertiefend, **C** = Kontext.",
        "Konfidenz: **hoch** = bibliografische Angaben über Verlags- oder Repository-Eintrag bestätigt, "
        "**mittel** = teilweise bestätigt, **niedrig** = nur sekundär zitiert.",
        "",
        "| Thema | Anzahl |",
        "|---|---|",
    ]
    for k, v in THEMEN.items():
        out.append(f"| [{v}](#{re.sub(r'[^a-z0-9 -]', '', v.lower()).replace(' ', '-')}) | {len(by.get(k, []))} |")
    out.append("")
    for k, v in THEMEN.items():
        items = sorted(by.get(k, []), key=lambda r: (r["prio"], r["jahr"], r["id"]))
        if not items:
            continue
        out += [f"## {v}", "", "| Prio | ID | Jahr | Autoren | Titel | Quelle | Zugang | Status | Konfidenz |",
                "|---|---|---|---|---|---|---|---|---|"]
        for r in items:
            out.append(
                f"| {r['prio']} | `{r['id']}` | {r['jahr']} | {md_escape(short_authors(r['autoren']))} | "
                f"{md_escape(r['titel'])} | {md_escape(r['quelle'])} | {link(r)} | {STATUS[r['status']]} | {r['konfidenz']} |"
            )
        out.append("")
    return "\n".join(out)


def build_beschaffung(rows):
    kit = sorted([r for r in rows if r["status"] in ("kit_zugang", "pruefen")], key=lambda r: (r["prio"], r["jahr"]))
    oa = sorted([r for r in rows if r["status"] == "oa_download"], key=lambda r: (r["prio"], r["jahr"]))
    out = [
        "# Beschaffungsliste Volltexte",
        "",
        "> Generiert aus [`quellen.csv`](quellen.csv). Nach dem Download: PDF unter dem Zieldateinamen in "
        "[`volltexte/`](volltexte/) ablegen und in `quellen.csv` den Status auf `vorhanden` setzen.",
        "",
        "**Warum diese Liste:** Die Cloud-Umgebung dieser Session blockiert direkte Downloads (Netzwerk-Policy, "
        "HTTP 403 auf designsociety.org, cambridge.org, KITopen u. a.). Deshalb liegen die PDFs noch nicht im Repo.",
        "",
        "## Teil 1: Über KIT-Account beschaffen",
        "",
        "Zugangswege: [KIT-Bibliothek Katalog](https://www.bibliothek.kit.edu), Springer/Elsevier/T&F über KIT-VPN oder "
        "Shibboleth (\"Access through your institution\"), Design-Society-Proceedings ggf. über Fernleihe oder Anfrage "
        "beim IPEK. Status `pruefen` = bibliografische Angaben vor Bestellung im Katalog verifizieren.",
        "",
        "| ✓ | Prio | ID | Zitat | DOI / Link | Status | Hinweis | Zieldatei |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in kit:
        cit = f"{short_authors(r['autoren'])} ({r['jahr']}): {r['titel']}. {r['quelle']}"
        out.append(
            f"| ☐ | {r['prio']} | `{r['id']}` | {md_escape(cit)} | {access(r)} | {STATUS[r['status']]} | "
            f"{md_escape(r['notiz'])} | `{r['id']}.pdf` |"
        )
    out += [
        "",
        "## Teil 2: Frei verfügbar (Open Access), nur herunterladen",
        "",
        "| ✓ | Prio | ID | Zitat | Download | Zieldatei |",
        "|---|---|---|---|---|---|",
    ]
    for r in oa:
        cit = f"{short_authors(r['autoren'])} ({r['jahr']}): {r['titel']}"
        out.append(f"| ☐ | {r['prio']} | `{r['id']}` | {md_escape(cit)} | {access(r)} | `{r['id']}.pdf` |")
    out += ["", f"Summe: {len(kit)} über KIT, {len(oa)} frei verfügbar.", ""]
    return "\n".join(out)


def bib_escape(s):
    return s.replace("&", r"\&").replace("²", "{\\texttwosuperior}").replace("%", r"\%")


def build_bib(rows):
    out = ["% Generiert aus literatur/quellen.csv. Nicht von Hand editieren.", ""]
    for r in rows:
        t = BIBTYPE.get(r["typ"], "misc")
        authors = " and ".join(n.strip() for n in r["autoren"].split(";") if n.strip())
        fields = {
            "author": authors,
            "title": "{" + r["titel"] + "}",
            "year": r["jahr"],
            "language": r["sprache"],
        }
        if t == "misc":
            fields["note"] = r["quelle"]
        if t == "article":
            fields["journal"] = r["quelle"]
        elif t in ("inproceedings", "incollection"):
            fields["booktitle"] = r["quelle"]
        elif t in ("phdthesis", "mastersthesis", "techreport"):
            fields["institution" if t == "techreport" else "school"] = r["quelle"]
        if r["doi"] and not r["doi"].startswith("http"):
            fields["doi"] = r["doi"]
        if r["url"]:
            fields["url"] = r["url"]
        out.append(f"@{t}{{{r['id']},")
        for k, v in fields.items():
            if v:
                out.append(f"  {k} = {{{bib_escape(v) if k not in ('url', 'doi') else v}}},")
        out.append("}")
        out.append("")
    return "\n".join(out)


def main():
    rows = load()
    (LIT / "literaturverzeichnis.md").write_text(build_verzeichnis(rows), encoding="utf-8")
    (LIT / "beschaffungsliste.md").write_text(build_beschaffung(rows), encoding="utf-8")
    (LIT / "literatur.bib").write_text(build_bib(rows), encoding="utf-8")
    print(f"{len(rows)} Quellen verarbeitet.")


if __name__ == "__main__":
    main()
