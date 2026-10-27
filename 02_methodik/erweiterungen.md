# Erweiterungen und Kopplungen des C&C²-Ansatzes

Übersicht über Arbeiten, die C&C² um Quantifizierung, weitere Domänen oder andere Modelle erweitern. Besonders relevant für ein späteres Tool, weil sie berechenbare Attribute und Schnittstellen definieren.

## Übersicht

| Erweiterung | Kernidee | Neue Elemente / Attribute | Quelle | Status |
|---|---|---|---|---|
| Technische Mechanik im C&C² | WFP-Orientierung und WFP-Fläche als Vektorattribute, Zerlegung in projizierte Komponenten | Normalenvektor, Flächenvektor, Reibwert, Lastvektoren, Flächenpressung | `Troester2026` | OA, 2026 |
| Bondgraphen | Aus C&C²-Modell einen Bondgraphen ableiten, Elemente erhalten mathematische Bedeutung | Energiedomäne, Effort/Flow-Variablen | `Prager2024` | OA |
| Lastpfad- und Knotenmodell | C&C² um Wandlung und Umformung ergänzt, Bewertung von Ersatzgrößen in der Mechatronik | Wandlungselement, Umformungselement, Knoten | `Vogel2021` | OA |
| Multi-Domain | Mechanische und elektromagnetische Domäne gleichzeitig modelliert (Transversalflussmaschine) | Feld-Wirkflächen, Domänenebenen | `Noeller2023` | OA |
| EFRT-Modell | C&C² + Toleranzgraph für Robust Design | Toleranzattribute je WFP und Zustand | `Grauberger2020c`, `Li2023`, `Li2024a`, `Li2024b` | OA |
| PGE-Variationsanteile | Übernahme-, Gestalt-, Prinzipvariation je WFP/LSS | Variationstyp je Element | `Troester2024a`, `Troester2024b` | OA |
| Designation Guide | Konsistente Benennung über Systemebenen | Hierarchische Bezeichner | `Troester2023` | OA |
| Erweitertes Sequenzmodell | Struktur in vier Dimensionen für Zustandsfolgen | Zustand, Übergang, Detailstufe | `Matthiesen2019b` | OA |
| Konstruktionshypothesen | Prüfbare Verknüpfung Gestaltparameter / Funktion | Hypothese, Evidenz, Status | `Matthiesen2017a` | OA |
| C&C²-basierte Fehleranalyse | C&C² + CAD + Ursache-Wirkungs-Modelle | Fehlermodus je WFP/LSS | `Gladysz2017`, `Gladysz2018a`, `Gladysz2018b` | KIT |
| Sensorintegration | C&C²-basierte Priorisierung von Sensorpositionen | Sensoreignung je WFP/LSS | `Vogel2019` | KIT |
| SysML-Profil | Stereotypen für WFP, LSS, C in SysML | Blöcke, Ports, Konnektoren | `Albers2011b`, `Albers2013`, `Zingel2012`, `Zingel2013` | teils OA |
| Traceability CPS | C&C² als semantischer Anker zwischen Mechanik-, Elektrik- und Softwaremodellen | Trace-Links, Berichte | `Urbano2025` | OA |
| Simulationskopplung | Zustände des Sequenzmodells parametrieren Simulationsmodelle | Zustandsparameter | `Matthiesen2018b`, `Matthiesen2018c`, `Albers2011d`, `Albers2005c` | teils OA |

## Details zu den wichtigsten Erweiterungen

### Tröster, Pfaff, Albers 2026: Integration technischer Mechanik
- Benennt den **Synthesis Gap**: C&C²-Modelle helfen bei Analyse und Kommunikation, liefern für Syntheseentscheidungen aber wenig quantitative Präzision.
- WFP erhalten **Orientierung** und **Fläche** als Vektoren. Dadurch lassen sich Reibung, Kräftegleichgewicht, Hebelarme und Flächenpressung direkt am Modell anwenden.
- Demonstriert an einer Wippe und einem dynamischen Fangsystem.
- Für ein Tool: direkte Grundlage für eine Berechnungsschicht (z. B. p = F/A je WFP, Gleichgewichtsprüfung).

### Prager, Tröster, Albers 2024: Bondgraphen
- C&C² als Denkzeug in mechatronischen Systemen. Bondgraphen machen GFZ auch in nichtmechanischen Domänen darstellbar.
- Für ein Tool: Exportpfad C&C² → Bondgraph → Modelica / 20-sim.

### Vogel 2021: Lastpfad- und Knotenmodell (TU Darmstadt)
- Erweiterung um **Wandlung** (Energieform ändert sich) und **Umformung** (Größe ändert sich bei gleicher Energieform).
- Für Wasser- und Energiesysteme zentral, weil Pumpen, Turbinen und Generatoren Energiewandler sind.

### EFRT-Modell (KIT Matthiesen + FAU Wartzack)
- Kombination aus C&C²-Modell und Toleranzgraph. 9 adaptierte Robust-Design-Prinzipien (`Li2023`).
- Adaptive Methode mit 5 Stufen und Gates, abhängig vom verfügbaren spezifischen Gestaltungswissen (`Li2024a`).

## Lücken (aus der Literatur abgeleitet)

- Keine C&C²-Arbeit speziell zu Wasserpumpen, Turbinen oder Hydraulikkreisläufen gefunden. Nächste Bezüge sind Hydraulikpumpe (`Eckert2011`), Hochdruck-Einspritzpumpe (`Gladysz2018a`), Transversalflussmaschine (`Noeller2023`) und Wandlungselemente (`Vogel2021`).
- Keine SysML-v2-Abbildung (letzte SysML-Arbeiten 2011 bis 2013).
- Kein standardisiertes Austauschformat (JSON/XML-Schema) für C&C²-Modelle.
- Fluide Wirkflächen sind definitorisch abgedeckt (generalisierte Grenzflächen), aber kaum ausgearbeitet.
