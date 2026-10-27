# Anwendungen und Fallbeispiele

Gesammelte Anwendungsfälle des C&C²-Ansatzes, geordnet nach Domäne. Die beste Gesamtübersicht ist `Grauberger2020a` (Review 20 Jahre, KIT-Zugang nötig).

## Übersicht nach Domäne

| Domäne | System | Zweck der Modellierung | Methodik | Quelle |
|---|---|---|---|---|
| Power-Tools | Bolzensetzgerät (Schiebernase, Nageldetektion) | Bauteilversagen verstehen, neue Generation | Analyse Kraftfluss, Hypothesen | `Matthiesen2018a` |
| Power-Tools | Schlagwerk Schlagschrauber | Dynamisches Verhalten, Simulationsmodell ableiten | Sequenzmodell → Simulation | `Matthiesen2018c` |
| Power-Tools | Winkelschleifer | Konstruktive Details beeinflussen Systemverhalten | Vergleich Varianten | `Matthiesen2018a` |
| Power-Tools / Ergonomie | Mensch als Teilsystem, Hand-Arm-System | Einfluss Anwender, Prüfstand mit Roboter | Prüfstand, WFP Hand/Griff | `Matthiesen2014`, `Matthiesen2018a` |
| Befestigungstechnik | Schnellbauschraube → spanlose Blechbohrschraube | Gestaltmerkmale für spanloses Einschrauben | Zoom-In, Shift, Sequenzmodell, Hypothese | `Matthiesen2018a` (Patent US 8,342,788) |
| Befestigungstechnik | Kunststoffdübel | Krafteinleitung in Untergrund | Spannungsoptik | `Matthiesen2018a`, `Matthiesen2017b` |
| Haushalt | Handkehrmaschine | Analysemethodik entwickeln | analyseKIT | `Matthiesen2017b` |
| Antriebstechnik | Einscheibentrockenkupplung | Kupplungsrupfen, kritische GFZ | C&C² + Sequenzmodell, Geometrieabweichungen | `Troester2021a`, `Troester2021b` |
| Antriebstechnik | Pneumatische Getriebeschaltung | Fehleranalyse | C&C²-Fehleranalyse vs. Fehlerbaum | `Gladysz2018a` |
| Antriebstechnik | Hybridantrieb | Modellbasierte Entwicklung | SysML + C&C²-A | `Zingel2012` |
| Antriebstechnik | Stirnradstufe, automatisiertes Schaltgetriebe | Verhaltensmodell in CAD | C&CM + Modelica | `Albers2005c` |
| Fahrzeugtechnik | Elektromechanische Bremse | Domänenübergreifende Traceability | C&C² als semantischer Anker | `Urbano2025` |
| Fahrzeugtechnik | Automotive-Fallstudie | Konsistente Benennung | Designation Guide | `Troester2023` |
| Prägetechnik | Münzprägemaschine | Robustheit, zustandsabhängige GFZ | C&C² + Toleranzgraph | `Grauberger2020c` |
| Konsumgüter | Flaschen (Einteiler) | Variationsanteile über Generationen | C&C² + PGE | `Troester2024a` |
| Robotik | Humanoider Roboterarm | Änderungsauswirkungen, Architektur | Software-Tool C&C-A | `Albers2010`, `Albers2011c` |
| Sicherheitstechnik | Dynamisches Fangsystem, Wippe | Quantitative Synthese | WFP-Vektoren | `Troester2026` |
| Tribologie | Systemtribometer | Tribosysteme mit WFP/LSS/BF | Tribosystem-Begriff | `Behrendt_FB36` |
| Mikromechanik | Bauteile mit streuenden LSS | Rechnergestützter Entwurf | LSS-Modellierung | `Enkler2010` |
| Bremsen / Sensorik | Scheibenbremse (Axialkraftmessung) | Sensorposition priorisieren | C&C²-Analysemodell | `Vogel2019` |

## Wasser, Fluide, Energie (Interessenschwerpunkt)

Keine C&C²-Publikation speziell zu Wasserpumpen, Turbinen, Rohrnetzen oder Wasseraufbereitung gefunden. Die nächstgelegenen Arbeiten:

| System | Bezug | Erkenntnis | Quelle |
|---|---|---|---|
| Hydraulikpumpe | Experiment zur Funktionsanalyse mit 38 Ingenieuren | Funktionsbegriff wird uneinheitlich verwendet (Ziel vs. Verhalten), Benennung braucht Führung | `Eckert2011`, `Eckert2012` |
| Hochdruck-Benzin-Einspritzpumpe | Realer Fehlerfall in Live-Lab | C&C²-Modelle finden mehr Fehlerursachen als Fehlerbäume | `Gladysz2018a` |
| Transversalflussmaschine (additiv gefertigter Stator) | Elektrische Maschine, Energiewandler | C&C² funktioniert als Multi-Domain-Sprache (mechanisch + elektromagnetisch) | `Noeller2023` |
| Mechatronische Systeme allgemein | Wandlung und Umformung von Energie | Elemente für Energiewandlung ergänzt | `Vogel2021` |
| Nichtmechanische Domänen | Bondgraphen (hydraulisch, elektrisch, thermisch abbildbar) | Brücke zu Simulation | `Prager2024` |

**Bewertung:** Die Definition der Wirkfläche umfasst ausdrücklich Grenzflächen von **Flüssigkeiten, Gasen und Feldern**. Der Ansatz ist damit auf Pumpen, Ventile, Dichtungen, Wärmeübertrager und Turbinen übertragbar. Ausgearbeitete Fallbeispiele fehlen. Für ein Tool im Wasser- und Energiebereich ist das eine echte Lücke und zugleich ein Differenzierungsmerkmal.

### Naheliegende Fluid-Anwendungsfälle zum späteren Ausarbeiten

| System | Typische WFP | Typische LSS | Typische Connectoren |
|---|---|---|---|
| Kreiselpumpe | Laufrad / Fluid, Gleitringdichtung, Lager | Welle, Laufradschaufeln, Fluidvolumen im Spiralgehäuse | Motor (Drehmoment), Saug- und Druckleitung (Druck, Volumenstrom) |
| Kolbenpumpe (z. B. Handpumpe Grundwasser) | Kolben / Zylinder, Ventilsitz / Ventilkörper, Fluid / Kolbenfläche | Kolbenstange, Wassersäule | Bediener (Hebelkraft), Brunnen (Förderhöhe) |
| Rückschlagventil | Ventilkugel / Sitz, Fluid / Kugel | Feder, Fluidvolumen | Leitungsdruck vor und nach dem Ventil |
| Wärmeübertrager | Fluid / Wand (beidseitig) | Wandmaterial, Fluidströme | Ein- und Austrittszustände |

Diese Tabelle ist eine eigene Ableitung (nicht aus der Literatur) und dient als Startpunkt.
