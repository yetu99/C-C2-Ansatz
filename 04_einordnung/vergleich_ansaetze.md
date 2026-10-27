# Einordnung: C&C² im Vergleich zu anderen Konstruktionsmodellen

> **Quellenlage (Stand 27.10.2026):** Direkt belegte Vergleiche gibt es gegen Fehlerbaum, SysML IBD und CAD (`Gladysz2018b`, Abstract) sowie gegen intuitives Vorgehen (`Grauberger2022b`, `Paehler2022`). Aus den Volltexten belegt ist außerdem die Einordnung durch die Autoren selbst: `Albers2014` (Kap. 8.3) gegenüber CPM, Axiomatic Design, DSM und lösungsneutralen Funktionsstrukturen; `Albers2011c` gegenüber MBSE, Function-Means-Tree, FuncSION, Schemebuilder und Bondgraphen; `Matthiesen2019b` mit der Unterscheidung ausführbarer und nicht ausführbarer Modelle. Die übrigen Zeilen beruhen auf Allgemeinwissen und sind noch mit Primärquellen zu belegen. Die Anthologie (Chakrabarti und Blessing 2014) liegt lokal vor (Datei `Albers2014`), ihre Kapitel zu den anderen Ansätzen sind noch nicht ausgewertet.

## Vergleichstabelle

| Ansatz | Fokus | Kernelemente | Stärken | Schwächen | Verhältnis zu C&C² |
|---|---|---|---|---|---|
| **C&C²-A** (Albers, Matthiesen) | GFZ auf Ebene der konkreten Gestalt | WFP, LSS, C, Zustände, Sequenzmodell | Funktion an Geometrie verortet, gut für Analyse bestehender Systeme und Fehleranalyse, wenige Elemente, domänenübergreifend definiert | Synthesis Gap, keine Datenstruktur, Benennung und Systemgrenzen schwierig für Novizen, stets mit anderen Modellen kombiniert | |
| **Pahl/Beitz** (Funktionsstruktur, Wirkprinzip) | Abstrakte Flüsse → Wirkprinzip → Gestalt | Funktionsstruktur (Energie, Stoff, Signal), Wirkprinzipien | Standard in der Lehre, systematisch in der Konzeptphase | Schwache Verbindung zur konkreten Gestalt; Funktionsstrukturen in der Praxis kaum eindeutig dokumentiert (`Albers2014` S. 154 nach Matthiesen 2011) | C&C² ergänzt die Gestaltungsphase, im Pahl/Beitz 9. Aufl. enthalten (`Matthiesen2021`) |
| **Rodenacker / Roth / Koller / Hubka** (Wirkflächen, Wirkstelle) | Effekt → Wirkfläche / Wirkbewegung → Gestalt | Wirkflächen, Wirkstellen, Kraftleitungsstruktur | Direkte Vorläufer der WFP-Idee | Roths Modelle nur für mechanische Energiefunktionen; LSS, RS, BF fehlen | Ideengeschichtliche Grundlage, ausdrücklich genannt (`Matthiesen2002` S. 13 bis 33, `Albers2014` S. 157) |
| **Hubka/Eder** (Theory of Technical Systems) | Allgemeine Theorie technischer Systeme | Transformationssystem, Organe | Umfassend | Für rechnergestützte Ansätze teils überpräskriptiv (`Albers2011c` S. 101006-2) | Organ ≈ Funktionsträger, C&C² konkreter |
| **FBS** (Gero) | Kognitives Modell des Konstruierens | Function, Behaviour, Structure | Domänenneutral | Struktur ohne Gestaltvisualisierung | Nicht ausführbares Modell wie C&C², aber ohne Gestaltbild (`Matthiesen2019b` S. 1484) |
| **SAPPhIRE** (Chakrabarti) | Kausalkette, Analogien | State change, Action, Parts, Phenomenon, Input, oRgan, Effect | Detaillierte Kausalität, LLM-Tool vorhanden | Viele Konstrukte | "Organ" nahe an WFP + LSS (Einschätzung) |
| **CPM/PDD** (Weber) | Merkmale vs. Eigenschaften | Characteristics, Properties, Relations | Berechenbar, an Analysewerkzeuge koppelbar | Kaum räumliche Verortung | Gestaltparameter ≈ Characteristics; `Grauberger2020a` (S. 261) schlägt eine CPM-ähnliche Datenstruktur für C&C² vor |
| **Domain Theory / Organ Domain** (Andreasen) | Domänen Transformation, Organ, Teil | Organe, Teile | Gut für Produktarchitektur, enthält Gestaltvisualisierung | Nicht für Gestaltanalyse operationalisiert | Neben C&C² das einzige nicht ausführbare Modell mit Gestaltbild (`Matthiesen2019b` S. 1484) |
| **Axiomatic Design** (Suh) | Unabhängigkeit, Zig-Zagging | FR, DP, Design-Matrix | Formale Entkopplungsprüfung | Wenig Bezug zu konkreter Geometrie | Komplementär (`Albers2014` S. 154) |
| **DSM** (Lindemann) | Abhängigkeiten Funktionen ↔ Komponenten | Matrizen | Architekturoptimierung | Keine Gestaltdarstellung | Mit C&C² kombiniert (Lamellenkupplung, `Albers2014` S. 165) |
| **SysML / MBSE** | Systemmodellierung, Anforderungen, Verhalten | Blöcke, Ports, Aktivitäten, Zustände | Industriestandard | Funktion-Gestalt-Abhängigkeiten nicht im Detail modellierbar (`Albers2011c` S. 101006-2); Sequenzdiagramme ohne Gestalt (`Matthiesen2019b`) | Profile existieren (`Albers2013`, `Urbano2025`) |
| **Bondgraphen** | Energiefluss, Simulation | Junctions, R, I, C, Quellen, Wandler | Domänenübergreifend, simulierbar | Keine Gestalt | Ableitbar aus C&C² (`Prager2024`) |
| **Fehlerbaum / FMEA** | Ursache-Wirkung | Ereignisse, Gatter | Industriestandard | FMEA erfahrungsbasiert, ohne Ursache-Wirkungs-Modell (`Gladysz2018a`) | C&C²-Fehleranalyse erweitert Umfang (`Gladysz2018a`) |
| **Funktionsbäume (Verb-Substantiv)** | Hierarchische Funktionszerlegung | Funktionen | Einfach | Große Streuung der Zerlegungen (`Alink2010`: im Mittel 11,3 von 47 Funktionen) | C&C² verortet Funktion physisch |

## Alleinstellungsmerkmale von C&C²

1. Funktion wird **an konkreten Flächen und Volumina** verortet; Modelle entstehen auf **konkreten Darstellungen** (Skizze, Zeichnung, CAD-Screenshot, Foto), nicht auf abstrakten Kästchen (`Albers2014` S. 158).
2. **Fraktale Modellierung** (GH 3): gleiche Elemente auf jeder Detailstufe.
3. **Zustände und Sequenzen** für dynamische Systeme, strukturiert in vier Dimensionen (`Matthiesen2019b`).
4. **Wenige Elemente** (WS, WSP, CSS, Connector) als gemeinsame Sprache (`Albers2014` S. 167).
5. **Connector** als expliziter Platz für Umgebung und Randbedingungen, anschlussfähig an XiL und Traceability (`Urbano2025`).

## Zu ergänzende Primärquellen für diese Seite

- [ ] Chakrabarti und Blessing (Hrsg.) 2014, Kapitel FBS, TTS, Domain Theory, SAPPhIRE, CPM (Buch liegt lokal vor, Datei `Albers2014`)
- [ ] Eisenbart, Gericke, Blessing 2013 (`Eisenbart2013`), Review Funktionsmodelle
- [ ] Koller, Konstruktionslehre für den Maschinenbau; Roth, Konstruieren mit Konstruktionskatalogen
- [ ] Erden et al. 2008, A review of function modeling (AI EDAM 22). Sekundär belegt: 18 Funktionsbegriffe, zitiert in `Albers2011c`, `Albers2014`, `Matthiesen2021`
