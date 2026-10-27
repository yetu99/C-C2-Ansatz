# Erweiterungen und Kopplungen des C&C²-Ansatzes

Übersicht über Arbeiten, die C&C² um Quantifizierung, weitere Domänen oder andere Modelle erweitern. Für ein Tool besonders relevant, weil sie berechenbare Attribute, Prüfregeln und Schnittstellen definieren. Stand 27.10.2026; Einträge mit (Abstract) sind noch nicht im Volltext geprüft.

## Übersicht

| Erweiterung | Kernidee | Neue Elemente / Attribute | Quelle | Prüfstand |
|---|---|---|---|---|
| Technische Mechanik im C&C² | Synthesis Gap schließen; Wirkfläche in projizierte Komponenten zerlegen | Flächenvektor A_WSP = (A_x, A_y, A_z) für Orientierung und Fläche, LSS-Längen, p = F/A, Momentengleichgewicht | `Troester2026` | Volltext |
| Bondgraphen | C&C²-Modell in Bondgraph übersetzen und simulieren | Quellen-Connector (Energieflussrichtung), statische/dynamische LSS | `Prager2024` | Volltext |
| Lastpfad- und Knotenmodell | Ersatzgrößen für Messung finden, auch in Reaktionspfaden | Lastpfad, Knoten (Bilanz), Umformung, Wandlung, Ein- und Ausleitung, Quellen, Speicher | `Vogel2021` | Volltext |
| Multi-Domain | Mechanik und Elektromagnetik in einem Modell | Feldvolumen als LSS, Materialübergänge als WFP, Kontrollvolumina für Luft, getrennte Flussfarben | `Noeller2023` | Volltext |
| Erweitertes Sequenzmodell | Zustandsfolgen strukturiert ablegen | Vier Dimensionen als Metadaten je Modell | `Matthiesen2019b` | Volltext |
| Designation Guide | Konsistente Benennung über Systemebenen | Hauptsystem (Buchstabe), Subsystem (Nummer), `//`, `~`, `(S[1; 6])` | `Troester2023` | Volltext |
| Functional Delimitation | Funktionsabschnitte in einteiligen Bauteilen | Virtuelles Modellelement (Symbol: zwei gekrümmte Parallelen, Farbe blau) | `Troester2023b`, `Troester2024b`, `Troester2025a` | Primärquelle fehlt |
| Extended C&C²-Prozessmodell | Wissensdokumentation in fünf Schritten | Templates, SFD, Konfidenzniveau, Bauteilbaum | `Troester2025b` | Volltext |
| PGE-Variationsanteile | Übernahme-, Gestalt-, Prinzipvariation je abgegrenztem Gestaltabschnitt | Variationsart je Abschnitt, Anteile nach Zählung oder Länge | `Troester2024a`, `Troester2024b` | Volltext |
| Konstruktionshypothesen | Prüfbare Verknüpfung Gestaltparameter / Funktion | Wenn-Dann-Weil, Referenz, Prüfung, Ergebnis | `Matthiesen2017a` | Volltext |
| Formalisierung für Software | C&C-A als Graph mit Bibliotheken | WS mit Ports, Module, Part, Flow, Function, Prüfregeln | `Albers2011c` | Volltext |
| SysML-Profil | Stereotypen für WS, WSP, CSS in SysML | Flow Ports, Connectoren mit Systemzuständen, Vererbungsmatrix | `Albers2013`, `Albers2011b`, `Zingel2012`, `Zingel2013` | `Albers2013` Volltext |
| Traceability CPS | C&C² als semantische Zwischenschicht CAD ↔ E/E ↔ Software | UML-Profil, WSP als binäre Assoziation, Mapping-Sprache, Berichte | `Urbano2025` | Volltext |
| EFRT-Modell | C&C² + Toleranzgraph für Robust Design | Toleranzattribute je WFP und Zustand | `Grauberger2020c`, `Li2023`, `Li2024a`, `Li2024b` | Abstract |
| C&C²-basierte Fehleranalyse | Fehlermechanismen über Wirknetze beschreiben | Fehlermodus je WFP/LSS, Zonen um den Fehlerort | `Gladysz2017`, `Gladysz2018a`, `Gladysz2018b` | `Gladysz2018a` Volltext |
| Sensorintegration | Priorisierung von Sensorpositionen | Sensoreignung je WFP/LSS | `Vogel2019` | Abstract |
| Simulationskopplung | Zustände parametrieren Simulationsmodelle | Zustandsparameter | `Matthiesen2018b`, `Matthiesen2018c`, `Albers2011d`, `Albers2005c` | Abstract |

## Details zu den wichtigsten Erweiterungen

### Tröster, Pfaff, Albers 2026: Integration technischer Mechanik
- **Synthesis Gap:** C&C²-Modelle helfen bei Analyse und Kommunikation, für Syntheseentscheidungen fehlt quantitative Präzision.
- WFP erhalten **Orientierung (WSPO)** und **Fläche (WSPA)**, beide im Flächenvektor A_WSP = (A_x, A_y, A_z) (Gl. 1); das Komponentenverhältnis gibt die Orientierung, z. B. Keilwinkel. Ein separater Normalenvektor wird nicht eingeführt.
- Zwei erweiterte Syntheseprinzipien konkretisieren das dritte Grundprinzip "Eigenschaften ändern": WFP-Orientierung und -Fläche variieren, LSS-Geometrie variieren.
- Dreistufiges Vorgehen: Analyse, Übersetzung in mechanische Parameter, hypothesengetriebene Synthese. Beispiele Wippe und Fangvorrichtung hydraulischer Hebebühnen (Zustände S1 bis S4). Keine empirische Validierung.
- Tool: direkte Grundlage für eine Berechnungsschicht je WFP (Flächenpressung, Gleichgewicht, Hebelarme).

### Prager, Tröster, Albers 2024: Bondgraphen
- Nur zwei Erweiterungen der Kernelemente: **Quellen-Connector** (doppelt umrandet, Ursprung des Energieflusses) und Unterscheidung **statische LSS** (gestrichelt) und **dynamische LSS** (durchgezogen).
- **Zuordnungsregeln (Tab. 2):** WFP → 0- oder 1-Junction bzw. Wandlerelement; dynamische LSS → R, I oder C; Quellen-Connector → Quelle (Effort oder Flow). Statische LSS entfallen. Voraussetzung ist ein geschlossener Wirkungskreis.
- Beispiel elektrischer Tiefpass 2. Ordnung. Werkzeuge 20-sim und Dymola (Modelica nicht explizit genannt). Hydraulik und Thermik nur als Ausblick.
- Tool: Exportpfad C&C² → Bondgraph → Simulation; für Hydraulik (Druck als Effort, Volumenstrom als Flow) noch nicht erprobt.

### Vogel 2021: Lastpfad- und Knotenmodell (TU Darmstadt)
- Ausgangspunkt: C&C² findet Messorte nur an Elementen, die die Zielgröße direkt führen.
- Neue Elemente (S. 55 bis 65): **Lastpfad** (Flussgröße unverändert zwischen Lasten oder Knoten), **Knoten** (Aufteilung und Überlagerung, bilanzierbar 0 = ΣF mit Vorzeichenregel, wirkt additiv), **Umformung** (Form ändert sich, Art bleibt, multiplikativ, z. B. Getriebeübersetzung), **Wandlung** (Domäne ändert sich, multiplikativ, z. B. Strom zu Drehmoment, Druck zu Kraft), **Ein- und Ausleitung** mit **Quellen**, **Speicher** (F = m·v̇ bzw. C·u̇).
- Jede Umformung und Wandlung erzeugt Reaktionsgrößen mit eigenem Lastpfad (sekundäre Funktion "Gleichgewicht herstellen").
- Arbeitet mit **Flussgrößen statt Energie**; Stoffströme werden nicht als eigene Lastpfade modelliert.
- Studie N = 28, p = 0,044, r = 0,33; Reaktionsermittlung bei Wandlung noch Einzelfallbeurteilung (S. 95).
- Für Wasser- und Energiesysteme zentral: Pumpen, Turbinen, Generatoren sind Wandler, Rohrverzweigungen Knoten (eigene Einschätzung, im Text nicht gezeigt).

### Nöller et al. 2023: Mechanik und Elektromagnetik (Transversalflussmaschine)
- Feldbeflutete Volumina (Luftspalt, Vakuum) als LSS, Materialübergänge als WFP; "a CSS always connects two WSP" (S. 13).
- Fluidvolumina in **Kontrollvolumina** unterteilt (nach Brezger 2013), angewendet auf Luft im Luftspalt.
- Kraftfluss und magnetischer Fluss parallel in verschiedenen Farben.
- Offen: Darstellung der **Energiewandlung zwischen Domänen** und der Kraftentstehung im Volumen.

### PGE-Verknüpfung (Tröster et al. 2024a, 2024b)
- Variationsarten: Übernahmevariation (CV), Gestalt- bzw. Attributvariation (EV/AV), Prinzipvariation (PV). Nach Albers et al. 2017: PV ändert Anzahl von WFP und LSS, EV ändert Gestalt ohne neue Elemente, CV betrifft vor allem Connectoren.
- Variationsanteile werden je **abgegrenztem Gestaltabschnitt** (Functional Delimitation) bestimmt, nicht getrennt je WFP oder LSS. Flasche: 75/25 % (Zählung) bzw. 65/35 % (Länge) Übernahme- zu Gestaltvariation.
- 2024b relativiert: Hinzufügen oder Entfernen von WFP ist nicht universell Prinzipvariation; Beispiel Einrohr- zu Zweirohr-Stoßdämpfer.

### Formalisierung im Software-Tool (Albers et al. 2011)
Siehe [Digitalisierung und Software](digitalisierung_und_software.md#formalisierung-albers-et-al-2011).

### EFRT-Modell (KIT Matthiesen + FAU Wartzack)
- Kombination aus C&C²-Modell und Toleranzgraph, 9 adaptierte Robust-Design-Prinzipien (`Li2023`), adaptive Methode mit 5 Stufen und Gates (`Li2024a`). Noch nicht im Volltext geprüft.

## Lücken (aus der Literatur abgeleitet)

- Keine C&C²-Arbeit zu Wasserpumpen, Turbinen, Rohrnetzen oder Wärmeübertragern. `Grauberger2020a` (S. 260) bestätigt: keine der 39 dokumentierten Anwendungen betrifft Fluid-, Gas- oder Feldsysteme als Schwerpunkt. Nächste Bezüge: Axialkolbenpumpe (`Alink2010`), Hochdruck-Benzinpumpe (`Gladysz2018a`), hydrodynamisches Gleitlager (`Matthiesen2002`), Transversalflussmaschine (`Noeller2023`), Wandlung Druck zu Kraft (`Vogel2021`).
- Sequenzmodell: Dimensionen für hydraulische und elektrische Systeme nicht untersucht (`Matthiesen2019b`).
- Keine SysML-v2-Abbildung (letzte SysML-Arbeiten 2011 bis 2013; `Urbano2025` nutzt ein UML-Profil).
- Kein standardisiertes Austauschformat (JSON/XML-Schema). `Grauberger2020a` (S. 261): C&C²-Modelle sind "two-dimensional conceptual models without an underlying data structure".
- Parameter gelten als wertvollstes Element, haben aber keine formale Modellierungsweise (`Grauberger2020b`).
- Domänenwandlung (mechanisch, elektrisch, hydraulisch, thermisch) im C&C²-Modell methodisch offen (`Noeller2023`, `Vogel2021` S. 95).
