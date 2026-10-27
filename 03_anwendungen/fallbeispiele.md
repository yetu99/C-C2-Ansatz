# Anwendungen und Fallbeispiele

Gesammelte Anwendungsfälle des C&C²-Ansatzes, geordnet nach Domäne. Beste Gesamtübersicht ist `Grauberger2020a` (39 Anwendungen, Tab. 2). Stand 27.10.2026; (Abstract) = noch nicht im Volltext geprüft.

## Übersicht nach Domäne

| Domäne | System | Zweck der Modellierung | Methodik | Quelle |
|---|---|---|---|---|
| Power-Tools | Bolzensetzgerät (Schiebernase, Nageldetektion); 219 Komponenten, 520 Teilfunktionen | Bauteilversagen verstehen, neue Generation | Analyse Kraftfluss, Hypothesen | `Matthiesen2018a`, `Matthiesen2021` S. 404 |
| Power-Tools | Schlagwerk Schlagschrauber | Dynamisches Verhalten, Simulationsmodell ableiten | Sequenzmodell → Simulation | `Matthiesen2018c` (Abstract) |
| Power-Tools | Sicherheitsschalter | Logische Zustände | Logisches Sequenzmodell | `Matthiesen2019b` Abb. 3, `Matthiesen2012` |
| Power-Tools | Winkelschleifer | Konstruktive Details beeinflussen Systemverhalten | Vergleich Varianten | `Matthiesen2018a` |
| Power-Tools / Ergonomie | Hand-Arm-System | Einfluss Anwender, Prüfstand mit Roboter | Prüfstand, WFP Hand/Griff | `Matthiesen2014` (Abstract), `Matthiesen2018a` |
| Befestigungstechnik | Selbstbohrende Trockenbauschraube, Bit/Recess (Hilti) | Untergrunddicke von 0,75 auf 2,50 mm gesteigert; Bit- und Kupplungsspringen entdeckt | Heuristiken, Sequenzen, Statistik über 2500 Datensätze | `Thau2013`, `Matthiesen2018a` |
| Befestigungstechnik | Schraubenmagazin Standsetzgerät (Hilti) | Schraube fällt kopfüber ins Transportrohr (etwa jede 10.) | C&CM-Kompendium, fehlendes führendes WSP | `Albers2008a`, `Thau2013` |
| Befestigungstechnik | Spreizdübel, Kunststoffdübel | Krafteinleitung in Untergrund | Spannungsoptik | `Thau2013`, `Matthiesen2018a` |
| Haushalt | Handkehrmaschine | Analysemethodik, Perspektivenwechsel | analyseKIT | `Matthiesen2017b` (Abstract), `Matthiesen2021` |
| Fahrzeug | Schiebedach | Ursache unerwünschten Verhaltens, 131 Modelle, 12 Orte | Sequenzmodell mit vier Dimensionen, Verschleißspuren | `Matthiesen2019b` |
| Antriebstechnik | Doppelt sperrender Klemmrollenfreilauf | Prototyp aus Laserschnittteilen, Reibverluste | Logische Zustände, 6 Konstruktionshypothesen | `Matthiesen2019b` |
| Antriebstechnik | Einscheibentrockenkupplung | Kupplungsrupfen, kritische GFZ | Systemebenenmodell, Kritikalitätsbewertung, XiL-Prüfstand | `Troester2021a`, `Troester2021b` (Abstract) |
| Antriebstechnik | Nasse Lamellenkupplung | Thermische Last, Keramik statt Stahl, Reibleistung über 100 % verbessert | C&C² + Simulation + DSM | `Albers2014` S. 165 |
| Antriebstechnik | Hybridantrieb | Betriebsmodi als Wirknetze; modellbasierte Entwicklung | Wirk-Structure, SysML + C&C²-A | `Albers2014` Abb. 8.2, `Zingel2012` (Abstract) |
| Antriebstechnik | 2-Gang-Getriebe | Dynamische Struktur in SysML | SysML-Profil | `Albers2013` |
| Antriebstechnik | Pneumatische Getriebeschaltung (Schaltaktuator) | Fehleranalyse | C&C²-Fehleranalyse vs. konventionell | `Gladysz2018a` |
| Antriebstechnik | Getriebemotor, Rührmaschinenwelle | Analyse und Synthese (Projektionswürfel) | Elementmodell 2002 | `Matthiesen2002` |
| Antriebstechnik | CVT-Reibkontakt, Keramik | Zusätzliches WFP als Synthese | Heuristiken | `Albers2003a`, `Albers2005a` |
| Fahrzeugtechnik | Elektromechanische Bremse | Domänenübergreifende Traceability | UML-Profil, Mapping-Sprache | `Urbano2025` |
| Fahrzeugtechnik | Automotive-Front (Fallstudie) | Konsistente Benennung | Designation Guide | `Troester2023` |
| Fahrzeugtechnik | Stoßdämpfer Einrohr zu Zweirohr | Variationsart über Generationen | C&C² + PGE | `Troester2024b` |
| Elektrische Maschinen | Transversalflussmaschine, additiv gefertigter Stator | Mechanik und Elektromagnetik gemeinsam | Multi-Domain | `Noeller2023` |
| Mechatronik | Elektrischer Tiefpass 2. Ordnung | Ableitung Bondgraph | C&C² → Bondgraph | `Prager2024` |
| Mechatronik | Hydraulische Bremse, Getriebe, Sensorik | Ersatzgrößen für Messung | Lastpfad- und Knotenmodell | `Vogel2021` |
| Robotik | Humanoider Roboterarm ARMAR IIIb | Systemarchitektur, Änderungsauswirkung (Motortausch, Kühlung) | Software-Tool C&C-A | `Albers2011c`, `Albers2010` (Abstract) |
| Prägetechnik | Münzprägemaschine | Robustheit, zustandsabhängige GFZ | C&C² + Toleranzgraph | `Grauberger2020c` (Abstract) |
| Konsumgüter | Flasche (einteilig) | Variationsanteile über Generationen | C&C² + PGE, Functional Delimitation | `Troester2024a` |
| Werkzeuge | Nachgiebige Zange (compliant mechanism) | Evaluation Extended C&C² | Templates, Functional Delimitation | `Troester2025a`, `Troester2025b` |
| Sicherheitstechnik | Fangvorrichtung hydraulischer Hebebühnen, Wippe | Quantitative Synthese | WFP-Flächenvektor | `Troester2026` |
| Tribologie | Systemtribometer | Tribosysteme mit WFP/LSS/BF | Tribosystem-Begriff | `Behrendt_FB36` (Abstract) |
| Mikromechanik | Bauteile mit streuenden LSS | Rechnergestützter Entwurf | LSS-Modellierung | `Enkler2010` (Abstract) |
| Bremsen / Sensorik | Scheibenbremse (Axialkraftmessung) | Sensorposition priorisieren | C&C²-Analysemodell | `Vogel2019` (Abstract) |

## Wasser, Fluide, Energie (Interessenschwerpunkt)

**Befund aus den Volltexten:** Die Definitionen schließen Flüssigkeiten, Gase und Felder seit 2002 ausdrücklich ein. In der Anwendung bleibt das weitgehend uneingelöst: Keine der 39 Anwendungen im Review hat Fluid-, Gas- oder Feldsysteme als Schwerpunkt, die Autoren fragen selbst nach dem Grund (`Grauberger2020a` S. 260). Thau schließt Fluide und Gase für seine Heuristiken ausdrücklich aus (`Thau2013` S. 66). Das Sequenzmodell ist für hydraulische Systeme nicht untersucht (`Matthiesen2019b`).

### Was die Literatur zu Fluiden konkret sagt

| Aussage | Bedeutung für die Modellierung | Quelle |
|---|---|---|
| Hydrodynamisches Gleitlager: "Die Viskosität ist eine Eigenschaft der Leitstützstruktur LSS1. Das Haftverhalten des Öls an der Welle ist Eigenschaft des Wirkflächenpaares WFP2." | Fluidvolumen = LSS, Benetzung/Haftung = WFP-Eigenschaft | `Matthiesen2002` S. 84 |
| "Wirkflächen von Fluiden passen ihre Gestalt der in Kontakt stehenden festen Wirkfläche an." Derselbe Fluidanteil kann zeitweise Teil der Wirkfläche oder der LSS sein | Fluid-WF ohne feste Geometrie, zeitabhängige Zuordnung | `Matthiesen2002` S. 86 |
| Föttingerwandler als hydraulische Alternative für "Drehmoment wandeln"; Methode "prinzipiell genauso" für hydraulische WFP | Übertragbarkeit der Synthese auf Hydraulik behauptet | `Matthiesen2002` S. 120, 127 |
| WSP zwischen Hydraulikkolben und Fluid, Fluid an der Zylinderwand mit Relativbewegung, Ventile mit diskretem Kontakt | Kodierung von Aggregatzustand, Relativbewegung, Kontaktdauer je WSP | `Albers2005a` S. 5 bis 6 |
| Ölhydraulische Axialkolbenpumpe: Öl als Teilsystem der Pumpe ("Das Öl selbst erfüllt eine zentrale Funktion in der Pumpe"), keine künstlichen WFP, durch die ein Volumenstrom fließt; Einsatzort und Umgebungstemperatur als Connector-Eigenschaften | Fluid als eigenes Teilsystem mit WFP zu Kolben, Gehäuse, Leitung | `Alink2010` S. 116, 167, 180, 183 |
| Luftvolumina in Kontrollvolumina unterteilen (nach Brezger 2013) | Diskretisierung von Fluidräumen in mehrere LSS | `Noeller2023` |
| Wandlung Druck ↔ Kraft an der hydraulischen Bremse; Flussgrößen statt Energie; Wandlungsverluste als Wärmestrom | Wandler-Element zwischen Domänen, Verlust als zusätzlicher Pfad | `Vogel2021` S. 54, 69 bis 70 |
| Hochdruck-Benzinpumpe: Fehleranalyse an Dichtung, Druckventil, Kolben | Fehleranalyse an Fluidtechnik funktioniert, Fluid selbst nicht modelliert | `Gladysz2018a` |
| Lamellenkupplung: Wärmeübergang ins Öl als Connector C_Oil, Ölalterung als Nebenwirkung | Thermik über Connector | `Albers2014` S. 165 |
| Hydraulik und Thermik als Bondgraph-Domänen | nur Ausblick | `Prager2024` |
| Review Tab. 2 nennt Druckausgleich (#33), Vakuumpumpe (#35), Hygienic Design (#36) | nur Titel, Inhalte nicht beschrieben | `Grauberger2020a` |

**Bewertung:** Für Wasser- und Energiesysteme ist der Ansatz definitorisch vorbereitet, aber methodisch unausgearbeitet. Offene Fragen sind Fluid als Teilsystem oder LSS, Diskretisierung von Strömungsräumen, Abbildung von Druck und Volumenstrom, Domänenwandlung (Pumpe, Turbine, Generator) und Zustände über Betriebspunkte. Für ein Tool ist das eine Lücke und ein Differenzierungsmerkmal.

### Naheliegende Fluid-Anwendungsfälle zum späteren Ausarbeiten

Eigene Ableitung (nicht aus der Literatur), ergänzt um die Modellierungsregeln oben.

| System | Typische WFP | Typische LSS | Typische Connectoren | Hinweis aus Literatur |
|---|---|---|---|---|
| Kreiselpumpe | Laufrad/Fluid, Gleitringdichtung, Lager | Welle, Laufradschaufeln, Fluid im Spiralgehäuse (in Kontrollvolumina) | Motor (Drehmoment, Drehzahl), Saug- und Druckleitung (Druck, Volumenstrom) | Fluid als Teilsystem (`Alink2010`), Kontrollvolumina (`Noeller2023`), Wandlung (`Vogel2021`) |
| Kolbenpumpe (z. B. Handpumpe Grundwasser) | Kolben/Zylinder, Ventilsitz/Ventilkörper, Fluid/Kolbenfläche | Kolbenstange, Wassersäule | Bediener (Hebelkraft), Brunnen (Förderhöhe) | Ventile mit diskretem Kontakt (`Albers2005a`), Zustände Saug- und Druckhub |
| Hydraulischer Widder (Stoßheber) | Ventilteller/Sitz (Stoßventil, Druckventil), Wasser/Windkessel-Luftpolster | Triebleitung, Wassersäule, Luftpolster | Zulauf (Gefälle), Steigleitung (Förderhöhe) | Ausgeprägte Sequenz mit logischen Zuständen (`Matthiesen2019b`) |
| Rückschlagventil | Ventilkugel/Sitz, Fluid/Kugel | Feder, Fluidvolumen | Leitungsdruck vor und nach dem Ventil | Zustände offen, schließend, geschlossen |
| Wärmeübertrager | Fluid/Wand (beidseitig) | Wandmaterial, Fluidströme | Ein- und Austrittszustände | Wärmestrom als Flussgröße (`Vogel2021`) |
