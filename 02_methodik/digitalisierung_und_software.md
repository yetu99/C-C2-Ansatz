# Digitalisierung, MBSE und Software-Unterstützung

Stand 27.10.2026, gegen Volltexte geprüft, soweit nicht (Abstract) vermerkt. Ziel: Überblick, welche digitalen Umsetzungen von C&C² existieren und wo Lücken für ein eigenes Tool liegen.

## Warum digital: Grenzen der Papiermodelle

Die Autoren selbst begründen den Bedarf so (`Albers2011c` S. 101006-3, `Albers2014` S. 167 bis 168):
- Komplexe Analysen erfordern sehr viele Skizzen; Modelle sind Momentaufnahmen, Sequenzen lassen sich nicht in einem Datensatz halten.
- Keine Konsistenzprüfung, kein Ein- und Ausblenden von Detailebenen ("zooming"), keine Ablage und Suche, schlechte Teamarbeit.
- C&C²-Modelle sind "two-dimensional conceptual models without an underlying data structure" (`Grauberger2020a` S. 261).
- Anwender fordern Software (`Thau2013` S. 159, 171; `Troester2025a` S. 580: Wunsch nach digitalen Templates; `Troester2025c` S. 460).

## Bisherige Software-Umsetzungen

| Jahr | Umsetzung | Beschreibung | Verfügbarkeit | Quelle |
|---|---|---|---|---|
| 2005 | Behavioural Mock-Up (BMU) | C&CM + Modelica-Simulationsmodelle in CAD, Getriebebeispiele | nicht verfügbar | `Albers2005c` (Abstract) |
| 2009 | C&CM-Tool / P3 Platform KIT / Cambridge | Linkage-Metamodelle, WF als Elemente und CSS als Verbindungen | nicht verfügbar | `Albers2009` (Abstract), `Thau2013` S. 41 |
| 2010 | Teile- und Funktionsbibliotheken | Software mit Teiledatenbank, humanoider Roboter | nicht verfügbar | `Albers2010` (Abstract) |
| 2011 | Systemarchitektur-Tool in Cambridge Advanced Modeller (CAM) | Formalisierung, Bibliotheken als CSV, automatische Ergänzung fehlender Flüsse, Auf- und Zuklappen | erster Prototyp, nicht verfügbar; CAM selbst ist frei erhältlich | `Albers2011c`, `Tool_CAM` |
| 2011 | Generalisiertes C&CM für Simulationsprozesse | Umsetzung in PE-Software (Name unbekannt) | nicht verfügbar | `Albers2011d` (Abstract) |
| 2011 bis 2013 | SysML-Profil C&C²-A | Stereotypen und Plugin, das aus Aktivitätspartitionen CSS und WS erzeugt | Konzept, kein Download | `Albers2013`, `Albers2011b`, `Zingel2012`, `Zingel2013` |
| 2025 | Traceability-Ansatz CPS mit Editor | UML-Profil, CAD-Ansicht, Baumansicht, C&C²-Ansicht, Mapping-Sprache, Berichte | Forschungsprototyp | `Urbano2025` |
| ab 2025 | Software für Extended-C&C²-Templates (Tröster-Gruppe) | "currently in development" | angekündigt | `Troester2025a` S. 581 |

**Ergebnis der GitHub-Suche (Erstrecherche):** kein Repository mit C&C²-Editor, Bibliothek oder Datenformat gefunden.

## Formalisierung Albers et al. 2011

Die einzige vollständig publizierte Formalisierung (`Albers2011c`, S. 101006-3 bis -5). Grundlage für jedes Datenmodell.

| Element | Formale Bedeutung |
|---|---|
| Working Surface (WS) | Fläche mit zwei bidirektionalen Ports: "outer" zu einer WS eines anderen Teils, "inner" zur angrenzenden CSS im selben Teil |
| Working Surface Pair (WSP) | Verbindung der äußeren Ports zweier WS; trägt einen oder mehrere Flows |
| Channel and Support Structure (CSS) | Verbindung der inneren Ports zweier WS (interne Struktur eines Teils); in tiefere Ebenen zerlegbar |
| Module | Logische Untergliederung, enthält Module oder Parts |
| Part | Unterste Ebene, nur Parts enthalten WS und CSS |
| Flow | Energie, Stoff oder Signal (Taxonomie Hirtz et al. 2002, drei Ebenen) |
| Function | Mit mindestens zwei WSP und einer CSS verknüpft, Input- und/oder Output-Flow, Begriff aus Funktionstaxonomie |

**Regeln:** Komplementarität (keine Funktion an einem Teil allein, Software prüft ≥ 2 WSP mit Flows und verbindende CSS); Mehrfachfunktionen; Parameter wie Reibwert und Last an WSP und CSS notierbar. Bibliotheksteile bringen Funktionen und WSP-CSS-Struktur mit, **fehlende Flüsse werden automatisch ergänzt und markiert** (E-Motor erzeugt Wärmeabfuhr-Bedarf), inkonsistente Definitionen werden bei Änderungen gelöscht. Teilebibliothek filterbar nach Flows.

**Grenzen laut Autoren:** starre Input-Function-Output-Terminologie kann Absichten nicht immer ausdrücken (Lager "Freiheitsgrad begrenzen"), daher erklärende Notizen neben der Formalisierung; nur qualitativ; **kein Connector** im Metamodell. Skalierung: Roboterarm mit 2 Freiheitsgraden ergab über 100 Funktionsbeziehungen, 150 WSP und etwa 280 CSS.

## SysML- und UML-Profile im Vergleich

| Aspekt | `Albers2013` (SysML) | `Urbano2025` (UML-Profil) |
|---|---|---|
| WS | Stereotypisierter Flow Port | nicht als eigenes Element |
| WSP | Stereotypisierter SysML-Connector mit Eigenschaft "Systemzustände" | Erweiterung von Association, genau zwei Enden (CSS zu CSS oder CSS zu Connector) |
| CSS | aus Aktivitätspartitionen erzeugt, Mapping-Matrix CSS ↔ Komponente mit Vererbung | Stereotyp von Class, mit CAD-Part-Referenz und Mapping-Speicher |
| Connector | als Grundelement definiert ("carries properties of adjacent systems", S. 356), Umsetzung im Profil im Text nicht eindeutig | Stereotyp von Class; intern (zwischen Teilsystemen) oder extern (zu E/E, Software) mit External Connection ID |
| Zustände | WSP-Eigenschaft | nicht Schwerpunkt |
| Evaluation | Illustrationsbeispiel 2-Gang-Getriebe | Fallstudie elektromechanische Bremse, ca. 10 h Modellierung, über 70 % manuell |

## Kopplungsmöglichkeiten nach Zielsystem

| Zielsystem | Stand der Forschung | Quellen | Reifegrad |
|---|---|---|---|
| CAD (Creo, CATIA, NX) | BMU 2005; Editor mit CAD-Ansicht und Part-Referenz (2025). Keine automatische WFP-Erkennung. Modelle auf CAD-Screenshots ausdrücklich vorgesehen (`Albers2014` S. 158) | `Albers2005c`, `Urbano2025`, `Albers2014` | niedrig |
| SysML v1 / UML | Profile mit Stereotypen | `Albers2013`, `Urbano2025` | mittel |
| SysML v2 / KerML | keine Arbeiten gefunden | | nicht vorhanden |
| Simulation FEM / MKS | Zustände parametrieren Simulation | `Matthiesen2018b`, `Matthiesen2018c` (Abstract) | mittel |
| Bondgraph | Zuordnungsregeln, Export in 20-sim oder Dymola | `Prager2024` | mittel |
| Tolerierung | EFRT: Toleranzgraph + C&C² | `Li2023`, `Li2024a` (Abstract) | mittel |
| FMEA / FTA | C&C²-basierte Fehleranalyse, FMEA als Informationsquelle in der Pre-Analysis | `Gladysz2018a`, `Gladysz2018b`, `Troester2025b` | mittel |
| Digital Thread / Traceability | C&C² als semantische Zwischenschicht | `Urbano2025` | niedrig |
| Produktmodell-Landschaft | Eingaben (Skizze, Zeichnung, CAD, physisches System) und Ausgaben (Wirknetz, Wirkstruktur) des C&C²-Modells | `Paehler2024` Tab. 2 | Orientierung |

## KI-Unterstützung

| Ansatz | Kern | Übertragbarkeit auf ein C&C²-Tool | Quelle |
|---|---|---|---|
| Datenbank vieler Modelle als KI-Basis | Einheitliche Benennung ermöglicht Vergleich und Datenbank | Designation Guide als Schlüssel für eine Modellbibliothek | `Troester2023` S. 1227 |
| EFR "to teach artificial intelligence" | Formalisierung soll spätere KI-Nutzung erlauben | Strukturierte Templates als Trainings- und Retrieval-Daten | `Troester2025b` S. 619 |
| Modulares LLM-Assistenzsystem in SysML | Modul je Methodenschritt, Prompt Chaining, Vektordatenbank gegen Duplikate, manuelle Freigabe nach jedem Schritt | Muster direkt übertragbar: KI-Vorschläge je Schritt des Prozessmodells, Nutzer bestätigt | `Schleifer2026` |
| Semantische Überlappungen per KI | Mappings zwischen Domänenmodellen automatisch vorschlagen | Ausblick | `Urbano2025` |
| RAG-Tool für SAPPhIRE-Modelle | LLM erzeugt Funktionsmodelle aus Wissensbasis | Analogie | `Tool_SAPPhIRE_RAG` (Abstract) |
| Agentic AI in der Produktion (Fraunhofer IWU) | Kontext | Inhalt wegen Nutzungsvorbehalt im PDF nicht ausgewertet | `KonstruktionAgenticAI2026` |

## Empirische Anforderungen an Modellierungsunterstützung

- **Einfachheit, Skizzenniveau, "show rather than tell":** Modell direkt auf Systemabbild (`Grauberger2022c` (Abstract), `Albers2014` S. 158).
- **Parameter formal verankern:** Parameter gelten als wertvollstes Element, haben aber keine Modellierungsweise (`Grauberger2020b`).
- **Modelle verknüpfen:** In 23 Projekten wurden viele zusätzliche Modelle genutzt, CAD am häufigsten; quantitative Modelle selten mit C&C² verknüpft (`Grauberger2020b`).
- **Hypothesen und Konfidenz dokumentieren** (`Matthiesen2017a`, `Troester2025b`).
- **Führung im Prozess, automatische Benennung:** Kurzschulungen reichen nicht, Designation Guide und Functional Delimitation werden schlecht behalten (`Troester2025a`, `Troester2025c`, `Grauberger2022b`).
- **Skalierung:** 131 Modelle in einem Industrieprojekt (`Matthiesen2019b`), rund 7000 Modellelemente in Anwendung #24 (`Grauberger2020a` S. 258), 150 WSP und 280 CSS im Robotermodell (`Albers2011c`).
- **Nutzer nicht entmündigen:** Formale Taxonomien nur ergänzend, Freitext zulassen (`Albers2011c`); KI-Vorschläge mit manueller Freigabe (`Schleifer2026`).
