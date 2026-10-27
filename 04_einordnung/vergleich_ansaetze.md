# Einordnung: C&C² im Vergleich zu anderen Konstruktionsmodellen

> **Quellenlage:** Direkt belegte Vergleiche gibt es nur gegen Fehlerbaum, SysML IBD und CAD (`Gladysz2018b`) sowie gegen intuitives Vorgehen (`Grauberger2022b`, `Paehler2022`). Die übrigen Zeilen sind eine Einordnung auf Basis des Allgemeinwissens zu den jeweiligen Theorien und noch mit Primärquellen zu belegen. Die Anthologie `Albers2014` (Chakrabarti & Blessing 2014) enthält Kapitel zu mehreren dieser Ansätze und ist der beste Startpunkt.

## Vergleichstabelle

| Ansatz | Fokus | Kernelemente | Stärken | Schwächen | Verhältnis zu C&C² |
|---|---|---|---|---|---|
| **C&C²-A** (Albers, Matthiesen) | GFZ auf Ebene der konkreten Gestalt | WFP, LSS, C, Zustände, Sequenzmodell | Funktion an Geometrie verortet, gut für Analyse bestehender Systeme und Fehleranalyse, qualitativ, domänenübergreifend | Synthesis Gap, Benennung und Systemgrenzen schwierig für Novizen, wird stets mit anderen Modellen kombiniert | |
| **Pahl/Beitz** (Funktionsstruktur, Wirkprinzip) | Abstrakte Flüsse → Wirkprinzip → Gestalt | Funktionsstruktur (Energie, Stoff, Signal), Wirkprinzipien, morphologischer Kasten | Standard in der Lehre, systematisch in der Konzeptphase | Schwache Verbindung von Funktion zu konkreter Gestalt, wenig Unterstützung bei Analyse bestehender Produkte | C&C² ergänzt die Gestaltungsphase, im Pahl/Beitz 9. Aufl. enthalten (`Matthiesen2021`) |
| **Koller / Rodenacker / Roth** (Wirkflächen, physikalische Effekte) | Effekt → Wirkfläche / Wirkbewegung → Gestalt | Wirkflächen, Wirkbewegungen, physikalische Effekte | Nächster Vorläufer der WFP-Idee, gut für Synthese über Effekte | Kein Konzept für Leit- und Stützstrukturen, selten für Systemanalyse genutzt | Ideengeschichtlicher Vorläufer |
| **Hubka/Eder** (Theory of Technical Systems) | Allgemeine Theorie technischer Systeme | Transformationssystem, Operanden, Organe, Baustruktur | Umfassend, rigoros | Abstrakt, aufwändig in der Anwendung | Organ ≈ Funktionsträger, C&C² konkreter |
| **FBS** (Gero) | Kognitives Modell des Konstruierens | Function, Behaviour, Structure, 8 Prozesse | Domänenneutral, verbreitet in Protokollstudien | Eher beschreibend, Struktur ohne Geometriebezug | C&C² liefert konkrete Strukturebene |
| **SAPPhIRE** (Chakrabarti) | Kausalkette, Analogien | State change, Action, Parts, Phenomenon, Input, oRgan, Effect | Detaillierte Kausalität, Analogiesuche, LLM-Tool vorhanden | Viele Konstrukte, steile Lernkurve | "Organ" nahe an WFP + LSS |
| **CPM/PDD** (Weber) | Merkmale vs. Eigenschaften | Characteristics, Properties, Relations, External Conditions | Berechenbar, gut an Analysewerkzeuge koppelbar | Kaum räumliche Verortung der Funktion | Gestaltparameter in C&C² ≈ Characteristics |
| **Domain Theory** (Andreasen) | Domänen Transformation, Organ, Teil | Organe, Teile, Architektur | Gut für Produktarchitektur | Nicht für Gestaltanalyse operationalisiert | Organ-Domäne ≈ WFP + LSS |
| **Axiomatic Design** (Suh) | Unabhängigkeit, Informationsgehalt | FR, DP, Design-Matrix | Formale Entkopplungsprüfung | Wenig Bezug zu konkreter Geometrie | Komplementär (Bewertung) |
| **Fehlerbaum / SysML IBD** | Ursache-Wirkung, logische Schnittstellen | Ereignisse, Gatter, Blöcke, Ports | Industriestandard, MBSE-fähig | Allein genutzt weniger Fehlerursachen gefunden als mit C&C² (`Gladysz2018b`) | Kombinierbar, SysML-Profil existiert (`Albers2013`) |
| **Funktionsbäume (Verb-Substantiv)** | Hierarchische Funktionszerlegung | Funktionen | Einfach | Ziel und Verhalten vermischt, große Streuung der Zerlegungen (`Eckert2011`, `Eckert2012`) | C&C² verortet Funktion physisch |

## Alleinstellungsmerkmale von C&C²

1. Funktion wird **an konkreten Flächen und Volumina** verortet. Das erleichtert die Analyse existierender Produkte und reduziert Fixierung (`Albers2004b`).
2. **Fraktale Modellierung** (GH 3): gleiche Elemente auf jeder Detailstufe.
3. **Zustände und Sequenzen** für dynamische Systeme.
4. Modelle sind **auf beliebigen Abbildern** (Skizze, Foto, CT, CAD-Schnitt) zeichenbar.

## Zu ergänzende Primärquellen für diese Seite

- [ ] Chakrabarti & Blessing (Hrsg.) 2014, An Anthology of Theories and Models of Design (Kapitel FBS, TTS, Domain Theory, SAPPhIRE, CPM)
- [ ] Eisenbart, Gericke, Blessing 2013 (`Eisenbart2013`), Review Funktionsmodelle
- [ ] Koller, Konstruktionslehre für den Maschinenbau; Roth, Konstruieren mit Konstruktionskatalogen
- [ ] Erden et al. 2008, A review of function modeling (AI EDAM)
