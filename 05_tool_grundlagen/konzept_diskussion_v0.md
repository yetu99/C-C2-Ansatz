# Tool-Konzept C&C²: Diskussionsgrundlage v0

Stand: 27.10.2026. Status: **Entwurf für Phase 3 (Dialog), keine Spezifikation, kein Code.** Grundlage sind die 33 ausgewerteten Volltexte, [`erkenntnisse_fuer_tool.md`](erkenntnisse_fuer_tool.md) und das Zielbild der Tool-Zusammenführung (MeinIngenieur, modularer Monolith, Supabase "Kompendium" mit Tabellenpräfix). Entscheidungspunkte sind mit **⚑ E1 bis E7** markiert.

## 1. Leitidee

Ein Werkzeug, mit dem man **auf einem Bild des echten Systems** (Foto, Skizze, CAD-Screenshot) Gestalt-Funktion-Zusammenhänge einzeichnet und daran **Wissen, Hypothesen und Designentscheidungen** festhält. Die Zeichnung ist nur die Oberfläche, darunter liegt ein prüfbares Datenmodell. Zielnutzen nach der Literatur: weniger Aufwand pro Modell, Führung für Unerfahrene, Konsistenz, Wiederfinden.

Abgrenzung v1: kein CAD-Plugin, keine Simulation, keine automatische Modellerzeugung.

## 2. Anforderungen aus der Literatur

| Nr | Anforderung | Begründung | Quelle |
|---|---|---|---|
| A1 | Systemabbild zuerst: Foto, Skizze, CAD-Screenshot, Video-Frame hochladen, Elemente als Overlay zeichnen | C&C²-Modelle entstehen auf konkreten Darstellungen | `Albers2014` S. 158, `Thau2013` S. 99 |
| A2 | Standardelemente WF, WFP, LSS, Connector, Systemgrenze, Functional Delimitation, optional BF und RS | Kern-, Neben- und Extended-Elemente | `Matthiesen2021`, `Troester2025b` |
| A3 | Graph unter der Zeichnung (WF mit Ports, WFP und LSS als Verbindungen) | einzige publizierte Formalisierung, ermöglicht Prüfregeln | `Albers2011c` |
| A4 | Prüfregeln aus GH 1 bis 3 (LSS genau zwei WFP, Funktion ≥ 2 WFP, ≥ 1 LSS, Connectoren) als Hinweise | Modelle verschiedener Personen weichen stark ab | `Albers2011c`, `Matthiesen2021` |
| A5 | Zustände und Sequenzen mit vier Dimensionen, Matrixnavigation, Zustandsvorschlag bei Elementänderung | dynamische Systeme, 131 Modelle in einem Projekt | `Matthiesen2019b`, `Albers2008a` |
| A6 | Operationen Zoom-In/Out und Shift (Connector in WFP und LSS auflösen) | Kernaktivitäten der Analyse | `Matthiesen2021` S. 435 bis 436 |
| A7 | Automatische Bezeichner nach Designation Guide, stabile interne IDs | Benennung schwer vermittelbar | `Troester2023`, `Troester2025c` |
| A8 | Modellzweck und Systemgrenze als Pflicht | Pflichtbestandteile | `Matthiesen2021`, `Thau2013` |
| A9 | Parameter als Objekte (Größe, Wert, SI-Einheit, Quelle) an WFP, LSS, C | wertvollstes Element, bisher nicht formalisiert | `Grauberger2020b` |
| A10 | Hypothesen Wenn-Dann-Weil mit Prüfung und Ergebnis, Konfidenz je Zusammenhang | Modellverifikation | `Matthiesen2017a`, `Troester2025b` |
| A11 | **Entscheidungsdokumentation**: jede Gestaltänderung als Syntheseoperation (hinzufügen, entfernen, ändern) mit Begründung, Alternativen, Bezug zu Hypothese und Evidenz | drei Grundoperationen; Wissensverlust durch ausscheidende Ingenieure | `Albers2014` S. 167, `Troester2025b` |
| A12 | Evidenz am Element (Verschleißfoto, Messdatei, Simulationsbild) | Verschleißspuren sind Indizien für WFP | `Matthiesen2021` S. 441, `Matthiesen2019b` |
| A13 | Geführte Abläufe für Analyse/Retrofit, Neuentwicklung, Fehleranalyse | Novizen brauchen Führung | `Troester2025b`, `Gladysz2018a` |
| A14 | Lernbereich in drei Stufen mit Beispielen und Quiz, kontextbezogene Hilfe im Editor | 20 min Schulung reichen nicht | `Troester2025c`, `Troester2025a` |
| A15 | Basisrechnungen je WFP (Flächenvektor, p = F/A, Gleichgewicht) über eng-core | Synthesis Gap | `Troester2026` |
| A16 | Export PDF-Bericht und JSON, später Bondgraph | Kommunikation, keine Datenstruktur bisher | `Grauberger2020a` S. 261, `Prager2024` |
| A17 | Versionen und Generationen mit Diff, Variationsart je Abschnitt | PGE | `Troester2024a`, `Troester2024b` |
| A18 | Minimalpfad: ein brauchbares Modell in etwa 10 Minuten | Zeitaufwand ist Hauptbarriere | `Troester2025b`, `Troester2025c` |
| A19 | Fluid und Energie: Medium je Element, Fluid als Teilsystem bzw. Kontrollvolumen, Wandler-Kennzeichnung, Betriebspunkte als Zustände | in der Literatur unausgearbeitet | `Matthiesen2002`, `Alink2010`, `Noeller2023`, `Vogel2021` |

## 3. Module

| Modul | Inhalt | v1 |
|---|---|---|
| M1 Projekt und Systemabbild | Projekt, Produkt/Generation, Bauteilbaum, Bilder hochladen, Ausschnitte, Maßstab optional | ja |
| M2 Editor | Zeichenwerkzeuge für Standardelemente auf dem Bild, Ebenen (Zustände), Ein- und Ausblenden, Farbschema umschaltbar (klassisch Linienstil oder Tröster-Farbcode) | ja |
| M3 Struktur und Benennung | Systembaum, automatische Bezeichner, Funktionsliste je Modell | ja (Bezeichner einfach) |
| M4 Zustände und Sequenzen | Zustandsliste, Sequenzmatrix (Ort × Zustand × Detailstufe, logische Zustände als Reiter), Vergleichsansicht | einfach (Liste + Vergleich) |
| M5 Wissen und Entscheidungen | Parameter, Hypothesen, Evidenz, Entscheidungen, Konfidenz, offene Fragen | ja |
| M6 Assistent und Prüfregeln | Ampel je Modell (Regeln A4, A8), geführte Schritte je Ablauf, Hinweis "neuer Zustand?" | ja (Regeln), Führung einfach |
| M7 Berechnung | Flächenvektor, Pressung, Gleichgewicht; später Knotenbilanz und Wandler | v2 |
| M8 Lernbereich | Stufe 1 Grundlagen, Stufe 2 Notation und Zustände, Stufe 3 Functional Delimitation und Synthese; Beispielmodelle (Schraube, Zange, Pumpe) | Stufe 1 |
| M9 Export und Verknüpfung | PDF-Bericht, JSON, WikiLinks ins Kompendium, Werkstoff aus Werkstoffatlas an LSS, Link zur Prozesswerkbank (SPALTEN) | PDF, JSON |
| M10 KI-Assistenz | Vorschläge je Schritt mit Freigabe (Muster `Schleifer2026`) | später |

## 4. Datenmodell (Entwurf, Supabase-Präfix `cc_`)

```
cc_project        id, titel, zweck, typ: analyse|neuentwicklung|fehleranalyse, generation_von?
cc_part           id, project, parent, name, bezeichner (Designation Guide), werkstoff_ref? (wa_*)
cc_image          id, project, datei (Storage), art: foto|skizze|cad|ct|video, quelle, maßstab?
cc_model          id, project, image, zweck, logischer_zustand, systemzustand, detailstufe, ort,
                  systemgrenze (Polygon), parent_model? (Zoom), version
cc_element        id, model, typ: WF|WFP|LSS|C|FD|BF|RS|Grenze, bezeichner, geometrie (im Bild),
                  medium: fest|fluid|gas|feld, part?, attrs (JSON: statisch/dynamisch, quelle?, variante)
cc_link           id, model, typ: wfp_wf|lss_wfp|c_wf|zoom|shift, von, nach
cc_function       id, model, text, elemente[] (≥2 WFP, ≥1 LSS, Connectoren), flows[]
cc_parameter      id, element, name, wert, einheit (SI), quelle, art: gemessen|angenommen|berechnet
cc_hypothesis     id, project, wenn, referenz, dann, weil, pruefung, ergebnis, status, konfidenz
cc_evidence       id, ziel (element|hypothesis), datei, beschreibung, datum
cc_decision       id, project, operation: hinzufuegen|entfernen|aendern, elemente[], begruendung,
                  alternativen, hypothese?, status: offen|entschieden|verworfen, datum, autor
cc_state          id, project, name, art: zeitlich|logisch|betriebspunkt, trigger?, reihenfolge
```

Regeln im Kern (reine Funktionen, testbar wie eng-core): GH-Prüfungen, Zustandsvorschlag, Bezeichnergenerator, Export.

## 5. Abläufe

### 5.1 Analyse und Retrofit (bestehendes Produkt)

1. **Pre-Analysis**: Problem oder Ziel, Modellzweck, Unterlagen sammeln, Bauteilbaum anlegen.
2. **Systemabbild und Grenze**: Foto oder Schnitt hochladen, räumliche Grenze ziehen.
3. **Zustände**: Betriebszustände und Übergänge festlegen (System State-Function Diagram).
4. **Modell je Zustand**: Fluss der Systemgrößen verfolgen, WFP, LSS, Connectoren einzeichnen, Prüfregeln grün.
5. **Parameter und Indizien**: Werte, Verschleißspuren, Messungen am Element.
6. **Hypothesen und Prüfung**: Wenn-Dann-Weil, Versuch oder Rechnung, Ergebnis, Konfidenz.
7. **Maßnahmen**: Syntheseoperationen als Entscheidungen mit Alternativen und Begründung.
8. **Abschluss**: Bericht (PDF), Modell wird Referenzsystem für die nächste Generation.

### 5.2 Neuentwicklung

1. **Ziel und Funktionen**: Hauptfunktionen, Randbedingungen, Schnittstellen (spätere Connectoren).
2. **Referenzsysteme** (PGE): Vorgänger oder Wettbewerber mit Ablauf 5.1 in Kurzform analysieren.
3. **Konzeptskizze als Systemabbild**: Soll-Wirknetz je Hauptfunktion und Zustand zeichnen.
4. **Gestaltentscheidungen**: je WFP und LSS festlegen, begründen, Hypothese und Prüfplan anhängen.
5. **Reifen mit dem CAD**: Skizze durch CAD-Screenshots ersetzen, Modellversion erhöhen, Diff zeigt Änderungen.
6. **Validierung**: Hypothesen testen, Entscheidungen bestätigen oder verwerfen.

### 5.3 Fehleranalyse (Kurzweg von 5.1)

Symptom → betroffene Zustände → Wirknetz um den Fehlerort, Zonen nach außen über Connectoren → Ursachenhypothesen → Test → Maßnahme.

## 6. Trade-offs

| Nr | Frage | Option A | Option B | Empfehlung |
|---|---|---|---|---|
| T1 | Darstellung | Zeichnen auf dem Bild (nah an der Praxis) | abstrakter Graph-Editor (leichter prüfbar) | Overlay auf dem Bild, Graph darunter; Graphansicht als Zweitansicht. Mehr Aufwand, aber Kernnutzen |
| T2 | Bildbasis | 2D-Bilder und Screenshots | 3D-Viewer (glTF/STEP) | 2D in v1; 3D erst, wenn 2D trägt |
| T3 | Regelstrenge | Blockieren bei Regelverstoß | Hinweise (Ampel) | Hinweise; strenger Modus für Lehre optional |
| T4 | Vorgehen | klassisch a bis g | Extended fünf Schritte mit Templates | ein Datenmodell, zwei Führungsmodi (Light und Voll) |
| T5 | Einbettung | eigenständige App | Modul in MeinIngenieur (Bereich Entwickeln) | als Modul im Zielbild planen, Tabellen `cc_`, Begriffe als WikiLinks |
| T6 | Speicherung | online (Supabase) | Offline-first mit Abgleich (Muster SPALTEN light) | Offline-first, weil Fotos im Feld entstehen |
| T7 | KI | früh einbauen | später | später; Datenmodell und Benennung jetzt KI-tauglich halten |
| T8 | Quantifizierung | eigene Rechner im Tool | eng-core aufrufen | eng-core (eine Formel nur an einem Ort) |
| T9 | Aufwand je Modell | vollständige Dokumentation | Minimalpfad mit späterer Ergänzung | Minimalpfad als Standard, Vollständigkeit über Ampel sichtbar |

## 7. Anwendungsfall Wasser und Energie

**Beispiel Retrofit Kreiselpumpe (Leckage an der Gleitringdichtung):** Zustände Anfahren, Nennbetrieb, Teillast, Stillstand. WFP Gleitring/Gegenring (Fluidfilm als LSS mit Viskosität, nach `Matthiesen2002` S. 84), WFP Welle/Sekundärdichtung, Connectoren Motor (Drehzahl), Saug- und Druckseite (Druck, Temperatur des Mediums). Hypothese (illustrativ): Wenn Federvorspannung gegenüber Serie um x erhöht, dann Leckrate sinkt, weil Spaltdicke im WFP abnimmt. Entscheidung mit Alternativen (Werkstoffpaarung ändern, Spülung hinzufügen).

**Beispiel hydraulischer Widder (SubHydra):** Ausgeprägte Sequenz mit logischen Zuständen (Beschleunigung der Triebwassersäule, Schließen des Stoßventils, Druckstoß und Förderung über das Druckventil, Rückschlag, Öffnen). WFP Ventilteller/Sitz, Wasser/Luftpolster im Windkessel; LSS Wassersäule in der Triebleitung (Kontrollvolumina); Connectoren Zulauf (Gefälle) und Steigleitung (Förderhöhe). Genau hier fehlt Methodik in der Literatur.

**Nötige Erweiterungen gegenüber der Literatur:** Medium-Attribut je Element; Fluid als eigenes Teilsystem mit Kontrollvolumina; Druck und Volumenstrom als Standardparameter an Connectoren und WFP; Wandler-Kennzeichnung (hydraulisch, mechanisch, elektrisch, thermisch) nach `Vogel2021`; Betriebspunkte als logische Zustände; später Knotenbilanz (Volumenstrom) und Bondgraph-Export für Hydraulik.

## 8. Vorschlag Ausbaustufen

| Stufe | Umfang |
|---|---|
| v0.1 | M1, M2 (WFP, LSS, C, Grenze), Zustandsliste, Prüfregeln, Parameter, Hypothesen, Entscheidungen, PDF/JSON-Export, Lernbereich Stufe 1 |
| v0.2 | Sequenzmatrix mit vier Dimensionen, Zoom und Shift als Operationen, Designation Guide automatisch, Functional Delimitation, Versionen und Diff |
| v0.3 | Berechnung über eng-core, Fluid- und Wandler-Erweiterung, Komponentenbibliothek (Pumpe, Ventil, Lager, Dichtung), Bondgraph-Export |
| später | KI-Vorschläge je Schritt, 3D-Ansicht, Teamfunktionen |

## 9. Entscheidungspunkte

- **⚑ E1 Primärer Nutzer v1**: eigene Projekte (Retrofit und Analyse im Wasser- und Energiebereich), Lehre, oder Team im Job?
- **⚑ E2 Einbettung**: von Anfang an Modul in MeinIngenieur (`cc_`-Tabellen, gemeinsames Supabase) oder zuerst eigenständiger Prototyp?
- **⚑ E3 Standard-Führung**: klassisch (a bis g) oder Extended (fünf Schritte) als Voreinstellung?
- **⚑ E4 Entscheidungsdokumentation**: eigenständige Entscheidungsobjekte (wie Architecture Decision Records) oder an Hypothesen gekoppelt?
- **⚑ E5 Darstellungskonvention**: Linienstil klassisch (Doppellinie, Wellenlinie) oder Tröster-Farbcode als Standard?
- **⚑ E6 Fluid-Regeln**: Fluid grundsätzlich als Teilsystem modellieren (Alink) oder als LSS mit Kontrollvolumina (Nöller)?
- **⚑ E7 IPEK-Kontakt**: Tröster-Gruppe wegen des angekündigten Tools ansprechen (Kooperation, Abgrenzung) oder unabhängig bleiben?
