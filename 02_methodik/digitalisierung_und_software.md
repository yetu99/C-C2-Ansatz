# Digitalisierung, MBSE und Software-Unterstützung

Stand der Recherche: Oktober 2026. Ziel ist der Überblick, welche digitalen Umsetzungen von C&C² existieren und wo Lücken für ein eigenes Tool liegen.

## Bisherige Software-Umsetzungen

| Jahr | Umsetzung | Beschreibung | Verfügbarkeit | Quelle |
|---|---|---|---|---|
| 2005 | Behavioural Mock-Up (BMU) | C&CM + Modelica-Simulationsmodelle in einem CAD-Programm, Getriebebeispiele | nicht verfügbar | `Albers2005c` |
| 2009 | C&CM-Tool KIT / Cambridge | Verknüpft Funktionen mit Bauteilen, Flächen und physikalischen Effekten in früher Gestaltung | nicht verfügbar | `Albers2009` |
| 2010 | Teile- und Funktionsbibliotheken | Software mit Teiledatenbank zur Wiederverwendung, Humanoider Roboter | nicht verfügbar | `Albers2010` |
| 2011 | Software-Tool zur Systemarchitekturmodellierung | Formalisierung von C&C-A, Änderungsauswirkungen über das Modell | nicht verfügbar, wahrscheinlich Cambridge Advanced Modeller | `Albers2011c`, `Tool_CAM` |
| 2011 | Generalisiertes C&CM für Simulationsprozesse | Erste Umsetzung in standardisierter PE-Software (Name unbekannt) | nicht verfügbar | `Albers2011d` |
| 2011 bis 2013 | SysML-Profil C&C²-A | Stereotypen für WFP, LSS, C, eingebettet in iPeM | Konzept, kein Download gefunden | `Albers2011b`, `Albers2013`, `Zingel2012`, `Zingel2013` |
| 2025 | Traceability-Ansatz CPS | C&C² verknüpft Mechanik, Elektrik, Software, erzeugt Trace-Berichte | Forschungsprototyp | `Urbano2025` |

**Ergebnis der GitHub-Suche:** kein Repository mit C&C²-Editor, Bibliothek oder Datenformat gefunden.

## Kopplungsmöglichkeiten nach Zielsystem

| Zielsystem | Stand der Forschung | Quellen | Reifegrad |
|---|---|---|---|
| CAD (Creo, CATIA, NX) | Nur BMU 2005. Keine automatische WFP-Erkennung aus Baugruppen | `Albers2005c` | niedrig |
| SysML v1 | Profil mit Stereotypen beschrieben | `Albers2013` | mittel |
| SysML v2 / KerML | keine Arbeiten gefunden | | nicht vorhanden |
| Simulation FEM / MKS | Zustände parametrieren Simulation, Ergebnisse fließen zurück | `Matthiesen2018b`, `Matthiesen2018c` | mittel |
| Bondgraph / Modelica | Ableitung Bondgraph aus C&C² | `Prager2024` | mittel |
| Tolerierung | EFRT: Toleranzgraph + C&C² | `Li2023`, `Li2024a` | mittel |
| FMEA / FTA | C&C²-basierte Fehleranalyse, Vergleich mit FTA | `Gladysz2018a`, `Gladysz2018b` | mittel |
| Digital Thread / Traceability | semantische Verknüpfung über C&C² | `Urbano2025` | niedrig |
| KI / LLM | keine C&C²-Arbeit. Analogie: RAG-Tool für SAPPhIRE-Modelle | `Tool_SAPPhIRE_RAG` | nicht vorhanden |

## Empirische Anforderungen an Modellierungsunterstützung

Aus `Grauberger2022c` (Grounded Theory, 10 Industrieprojekte) und `Grauberger2020b` (23 Projekte):
- **Einfachheit und Klarheit:** Skizzenniveau statt CAD-Präzision
- **Mentale Modelle explizit machen**
- **Show rather than tell:** Modell direkt auf Systemabbild
- **Modelle verknüpfen:** C&C² wird fast immer zusammen mit anderen Modellen genutzt
- **Parameter verifizieren:** Hypothesen und Evidenz dokumentieren

Aus `Paehler2022` und `Troester2025c`: Kurzschulung reicht nicht. Benennung von Funktionen und Systemabgrenzung brauchen Führung direkt im Werkzeug.

## Produktmodell-Landschaft

`Matthiesen2019a` (Review Produktmodelle in der Gestaltung) und `Paehler2024` (Netzwerkanalyse von 52 Produktmodellen) beschreiben, welche Modelle Ein- und Ausgaben von C&C² sein können. Diese beiden Quellen sind die Grundlage für Import/Export-Schnittstellen.
