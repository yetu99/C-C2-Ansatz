# C&C²-Ansatz: Wissensbasis

Strukturierte Sammlung zum **Contact and Channel Approach (C&C²-A, C&C²-Ansatz)** des IPEK am KIT (Albers, Matthiesen). Ziel ist die Informationsbasis für ein späteres anwendungsbezogenes Tool, mit dem Ingenieurinnen und Ingenieure Gestalt-Funktion-Zusammenhänge schnell modellieren können.

**Stand:** 27.10.2026 · **Quellen:** 86 erfasst · **Volltexte:** 12 im Repo (offene Lizenz), 21 lokal in `Wissen/C&C2-Ansatz`

## Der Ansatz in 60 Sekunden

- **Zweck:** Zusammenhang zwischen Gestalt und Funktion technischer Systeme explizit machen (Denkzeug für Analyse und Synthese).
- **Kernelemente:** Wirkflächenpaar (WFP), Leitstützstruktur (LSS), Connector (C).
- **Grundhypothesen:**
  1. Wechselwirkung nur an Wirkflächenpaaren.
  2. Funktion braucht ≥ 2 WFP, verbunden durch eine LSS, eingebunden über Connectoren.
  3. Fraktal: jedes Teilsystem auf jeder Detailstufe mit denselben Elementen beschreibbar.
- **Dynamik:** Zustände und Sequenzmodelle.
- **Bester Nachweis:** Fehler- und Ursachenanalyse an bestehenden Systemen, Systemverständnis auf Systemebene.
- **Bekannte Schwächen:** Synthese wenig quantitativ (Synthesis Gap), keine Datenstruktur, Benennung und Systemabgrenzung für Novizen schwierig, kein verfügbares Software-Tool, Fluid- und Energiesysteme kaum ausgearbeitet.
- **Weiterentwicklung (Extended C&C², ab 2023):** Designation Guide, Functional Delimitation, Fünf-Schritte-Prozessmodell mit Templates.

## Struktur

| Ordner / Datei | Inhalt |
|---|---|
| [`01_grundlagen/elemente_und_grundhypothesen.md`](01_grundlagen/elemente_und_grundhypothesen.md) | Definitionen DE/EN, Grundhypothesen, Begriffsentwicklung |
| [`01_grundlagen/historie_und_akteure.md`](01_grundlagen/historie_und_akteure.md) | Zeitachse 1999 bis 2026, Forschungsgruppen, verwandte KIT-Modelle |
| [`02_methodik/modellbildung_analyse_synthese.md`](02_methodik/modellbildung_analyse_synthese.md) | Vorgehen, Analysetechniken, Konstruktionshypothesen, Syntheseprinzipien |
| [`02_methodik/erweiterungen.md`](02_methodik/erweiterungen.md) | Quantifizierung, Bondgraph, EFRT, PGE, Multi-Domain, Lücken |
| [`02_methodik/digitalisierung_und_software.md`](02_methodik/digitalisierung_und_software.md) | Bisherige Software, SysML, CAD, Simulation, KI |
| [`03_anwendungen/fallbeispiele.md`](03_anwendungen/fallbeispiele.md) | Anwendungsfälle nach Domäne, Fokus Wasser/Fluide/Energie |
| [`03_anwendungen/evidenz_und_lehre.md`](03_anwendungen/evidenz_und_lehre.md) | Empirische Studien, Gegenbefunde, Lehre |
| [`04_einordnung/vergleich_ansaetze.md`](04_einordnung/vergleich_ansaetze.md) | Vergleich mit Pahl/Beitz, FBS, SAPPhIRE, CPM u. a. |
| [`05_tool_grundlagen/erkenntnisse_fuer_tool.md`](05_tool_grundlagen/erkenntnisse_fuer_tool.md) | Abgeleitete Anforderungen, Datenmodell-Skizze, Leseliste |
| [`05_tool_grundlagen/konzept_diskussion_v0.md`](05_tool_grundlagen/konzept_diskussion_v0.md) | Tool-Konzept v0 als Diskussionsgrundlage (Module, Datenmodell, Abläufe, Trade-offs, Entscheidungspunkte) |
| [`05_tool_grundlagen/konzept_v1.md`](05_tool_grundlagen/konzept_v1.md) | Tool-Konzept v1 mit Entscheidungen E1 bis E7, Farbcode, Systemgrenze, fraktale Detail-Tabs, Supabase, Ausbaustufen |
| [`literatur/quellen.csv`](literatur/quellen.csv) | **Quellendatenbank** (Single Source of Truth, `;`-getrennt, Excel-tauglich) |
| [`literatur/literaturverzeichnis.md`](literatur/literaturverzeichnis.md) | Literaturverzeichnis nach Thema (generiert) |
| [`literatur/beschaffungsliste.md`](literatur/beschaffungsliste.md) | **To-do-Liste Volltexte:** KIT-Zugang und Open Access (generiert) |
| [`literatur/literatur.bib`](literatur/literatur.bib) | BibTeX für Zotero/LaTeX (generiert) |
| [`literatur/zusammenfassungen/`](literatur/zusammenfassungen/) | Ausgewertete Volltexte |
| [`literatur/volltexte/`](literatur/volltexte/) | PDFs, Dateiname = Zitierschlüssel |
| [`tools/build_literatur.py`](tools/build_literatur.py) | Generator für Verzeichnis, Beschaffungsliste, BibTeX |

## Arbeitsablauf

```bash
# 1. Quelle ergänzen oder Status ändern: literatur/quellen.csv bearbeiten
# 2. Abgeleitete Dateien neu erzeugen
python3 tools/build_literatur.py
# 3. PDF mit offener Lizenz (CC) als literatur/volltexte/<ID>.pdf ablegen, Status "vorhanden"
#    Verlags-PDF nur lokal in Wissen/C&C2-Ansatz ("<ID> - Autor - Kurztitel (Quelle, Jahr).pdf"), Status "lokal"
```

**Spalten in `quellen.csv`:** `id`, `jahr`, `autoren` (mit `;` getrennt), `titel`, `quelle`, `typ`, `sprache`, `doi`, `url`, `oa` (ja/nein/unklar), `thema`, `prio` (A/B/C), `konfidenz` (hoch/mittel/niedrig), `status` (vorhanden = PDF im Repo / lokal = PDF nur lokal wegen Lizenz / oa_download / kit_zugang / pruefen / web), `notiz`.

## Methodik der Recherche

- Websuche über Verlags- und Repository-Einträge (KITopen, Design Society, Cambridge Core, Elsevier, Springer, T&F, Open Research Online, TUprints).
- Drei Recherchestränge: Grundlagen, Methoden/Digitalisierung, Anwendungen/Evaluation.
- Keine DOI erfunden. Unsichere Angaben sind mit Konfidenz `mittel`/`niedrig` oder Status `pruefen` markiert.
- **Volltexte:** Seit 27.10.2026 sind 33 Volltexte ausgewertet (Zusammenfassungen in `literatur/zusammenfassungen/`). Bibliografische Angaben wurden gegen die PDFs geprüft. Was im PDF fehlt, bleibt mit Konfidenz `mittel`/`niedrig` bzw. Status `pruefen` markiert.
- **Lizenz:** Das Repo ist öffentlich. Verlags-PDFs ohne offene Lizenz liegen deshalb nur lokal.

## Nächste Schritte

1. Fehlende Prio-A-Quellen beschaffen: `Ohmer2008` (Synthese), `Troester2023b` (Functional Delimitation). Danach Prio B laut [Beschaffungsliste](literatur/beschaffungsliste.md).
2. Restliche offene Punkte in den Themenseiten (Checkboxen) abarbeiten.
3. Prototyp v0.1 nach [`konzept_v1.md`](05_tool_grundlagen/konzept_v1.md) spezifizieren und bauen.
