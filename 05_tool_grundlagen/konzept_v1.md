# Tool-Konzept C&C²: v1 (Entscheidungen festgehalten)

Stand: 27.10.2026. Status: **Konzept mit getroffenen Entscheidungen, Grundlage für die Spezifikation v0.1.** Diskussionsgrundlage war [`konzept_diskussion_v0.md`](konzept_diskussion_v0.md), Anforderungen A1 bis A19 und Module M1 bis M10 gelten unverändert, soweit hier nichts anderes steht.

## 1. Entscheidungen

| Nr | Frage | Entscheidung | Begründung |
|---|---|---|---|
| E1 | Primärer Nutzer v1 | Nur Seti (eigene Projekte, Wasser/Energie). Später teamfähig für das Arbeitsumfeld | einfachste Umsetzung und Erprobung |
| E2 | Einbettung | Eigenständiger Prototyp, Daten und Tabellen von Anfang an kompatibel zu MeinIngenieur | schneller Start, Merge bleibt einfach |
| E3 | Standard-Führung | Klassisches Vorgehen (Schritte a bis g, `Matthiesen2021`) voreingestellt, Extended (fünf Schritte) umschaltbar | Annahme: "Standard" meint den klassischen Ansatz |
| E4 | Entscheidungsdokumentation | **Eigenständige Entscheidungsobjekte** (ähnlich Architecture Decision Records), n:m verknüpft mit Hypothesen, Evidenz und Elementen | siehe Abschnitt 4 |
| E5 | Darstellung | Tröster-Farbcode, kombiniert mit Linienstil | siehe Abschnitt 2 |
| E6 | Fluide | Fluidräume als **LSS in Kontrollvolumina** (`Noeller2023`), zusammengefasst im Bauteilbaum als Teilsystem "Fluid" | passt zu Pumpen, Ventilen, Leitungen; siehe Abschnitt 5 |
| E7 | IPEK-Kontakt | Gespräch mit P. M. Tröster erst mit laufendem Prototyp | Prototyp als Gesprächsgrundlage |
| T1 bis T9 | Trade-offs | Empfehlungen aus v0 übernommen | |
| S1 | Supabase | Projekt "Kompendium", Tabellen mit Präfix `cc_`, Bucket `cc-bilder`; lokal zuerst (IndexedDB), Abgleich ab v0.2 | siehe Abschnitt 6 |

## 2. Darstellungskonvention

Farben nach `Troester2025c` (Abb. 1) bzw. `Troester2026`, Linienstil nach `Thau2013` und `Grauberger2022b`. Farbe und Form sind beide gesetzt, damit die Elemente auch auf farbigen Fotos und im Schwarzweißdruck unterscheidbar bleiben. Hexwerte sind eigener Vorschlag.

| Element | Farbe | Form | Token |
|---|---|---|---|
| Wirkflächenpaar (WFP) | Rot | Doppellinie entlang der Kontaktfläche | `--cc-wfp` #D62828 |
| Leitstützstruktur (LSS) | Gelb | halbtransparente Fläche mit Wellenlinie als Achse | `--cc-lss` #F2B705 |
| Connector (C) | Grün | Polygon mit hervorgehobener Wirkfläche, Quellen-Connector doppelt umrandet (`Prager2024`) | `--cc-c` #2A9D4B |
| Functional Delimitation (FD) | Blau | zwei gekrümmte Parallelen (`Troester2024b`) | `--cc-fd` #1F6FD1 |
| Systemgrenze (räumlich) | Schwarz | gestrichelte geschlossene Linie | `--cc-grenze` #1A1A1A |
| Begrenzungsfläche, Reststruktur | Grau | dünne Linie bzw. Schraffur, standardmäßig ausgeblendet | `--cc-neben` #8A8A8A |

## 3. Systemgrenzen und fraktale Detailansicht

### 3.1 Systemgrenze einzeichnen
- Werkzeuge: Polygon, Rechteck, Freihand-Lasso; Eckpunkte nachträglich verschiebbar.
- Je Modell genau eine räumliche Grenze. Die zeitliche Grenze ist die Zuordnung des Modells zu Zuständen (`Matthiesen2021` S. 427).
- Schneidet die Grenze ein Bauteil oder eine LSS, schlägt das Tool an dieser Stelle einen Connector vor (Schnitt durch die LSS, `Albers2008a` S. 247; Connectoren an der Grenze, `Thau2013` S. 72 bis 80).
- Prüfregeln (Ampel): Grenze geschlossen; mindestens eine Funktion innerhalb (`Thau2013`); jedes WFP an der Grenze hat einen Connector.

### 3.2 Fraktale Detailansicht (Zoom-In) in eigenem Tab
Grundlage GH 3 und Zoom-In/Shift (`Matthiesen2021` S. 435 bis 436). Das übergeordnete Modell bleibt gültig, das Detailmodell ist eine feinere Darstellung desselben Elements.

1. Rechtsklick auf WFP, LSS oder Connector → "Detail öffnen". Es entsteht ein **Detailmodell in neuem Tab**, Detailstufe = übergeordnete Stufe + 1.
2. Systemabbild des Details: Ausschnitt des übergeordneten Bildes oder neues Bild (Makrofoto, Schliff, CAD-Schnitt).
3. Die Systemgrenze des Details entspricht dem gewählten Element. Angrenzende Elemente der Ebene darüber werden im Detail **automatisch als Connectoren** angelegt (Shift-Logik: Umgebung wird Connector).
4. Bezeichner im Detail in Punktnotation vom Elternelement: aus WFP1 werden WFP1.1, WFP1.2, Connectoren C1.1 usw. (`Matthiesen2021` Abb. 13.20, `Alink2010` S. 47).
5. Im übergeordneten Modell trägt das Element ein Symbol "Detail vorhanden"; Klick öffnet den Tab. Brotkrumen zeigen die Ebenen (Gesamtsystem › Pumpe › Dichtung › Gleitring).
6. Konsistenz: Ändert sich im Detail ein Connector, der auf ein Element der Ebene darüber zeigt, wird das Elternmodell markiert ("Schnittstelle prüfen").
7. Zoom-Out: mehrere Elemente zu einem zusammenfassen; die zusammengefassten Elemente wandern in ein neues Detailmodell.

## 4. Entscheidungsdokumentation (E4)

**Begründung für eigenständige Objekte:**
- In der Neuentwicklung gibt es Entscheidungen ohne Hypothese (Gestalt festgelegt aus Erfahrung, Norm, Kosten).
- Eine Entscheidung stützt sich oft auf mehrere Hypothesen und Evidenzen, eine Hypothese kann mehrere Entscheidungen beeinflussen.
- Entscheidungen haben einen eigenen Lebenszyklus und werden später ersetzt; genau diese Historie ist das gesicherte Wissen (`Troester2025b`, Wissensverlust).

**Felder:** Titel, Kontext (Problem, Ziel), Syntheseoperation (hinzufügen, entfernen, Eigenschaften ändern; `Albers2014` S. 167), betroffene Elemente, betrachtete Alternativen, Begründung, gestützt auf (Hypothesen, Evidenz, Parameter, Norm), Konfidenz, Status (vorgeschlagen, entschieden, umgesetzt, verworfen, ersetzt durch), Datum, Autor.

## 5. Fluid- und Energiesysteme (E6)

- Fluidraum = **LSS**, unterteilt in **Kontrollvolumina** (z. B. Saugstutzen, Laufradkanal, Spirale, Druckstutzen). Eigenschaften: Medium, Dichte, Viskosität, Temperatur (`Matthiesen2002` S. 84: Viskosität ist LSS-Eigenschaft).
- WFP an Fluidgrenzen: Fluid/Wand, Fluid/Schaufel, Fluid/Luftpolster; Eigenschaften Benetzung, Rauheit, Druck (Haftung ist WFP-Eigenschaft, `Matthiesen2002` S. 84).
- Bauteilbaum: Teilsystem "Fluid" gruppiert die Kontrollvolumina. Damit ist auch die Sicht von `Alink2010` (Fluid als Teilsystem) abgebildet.
- Connectoren an Leitungsenden tragen den **Betriebspunkt** (Druck, Volumenstrom, Temperatur).
- Betriebspunkte (Anfahren, Nennlast, Teillast, Stillstand, Störfall) sind Zustände der Art "Betriebspunkt".
- Wandler kennzeichnen (hydraulisch, mechanisch, elektrisch, thermisch) nach `Vogel2021`; Bilanzen erst ab v0.3.

## 6. Supabase (S1)

| Kriterium | Eigenes Projekt | Projekt "Kompendium" mit `cc_` |
|---|---|---|
| Merge in MeinIngenieur | Daten und Storage müssen umziehen | entfällt, Zielbild sieht ein Projekt mit Präfixen vor |
| Verknüpfungen (Werkstoffe `wa_*`, Begriffe im Kompendium, `pw_*`) | nur über zweite Verbindung | direkt per Fremdschlüssel bzw. Entitätsschlüssel |
| Risiko für bestehende Tools | keines | gering, wenn Migrationen nur `cc_`-Objekte anlegen |
| Kontingent im kostenlosen Plan | zählt als weiteres Projekt; inaktive Projekte werden pausiert | kein weiteres Projekt; Speicher für Fotos teilen sich alle Tools |

**Empfehlung: Kompendium mit Präfix `cc_`.** Regeln: Migrationen als SQL-Dateien im Prototyp-Repo, ausschließlich `cc_`-Tabellen und Bucket `cc-bilder`; Fotos vor dem Upload clientseitig verkleinern; ohne Login wie die übrigen Tools, solange nur Seti nutzt (bei Teamnutzung neu bewerten). Im kostenlosen Plan sind Speicher und Projektanzahl begrenzt; aktuelle Grenzen vor Start in der Supabase-Übersicht prüfen.

## 7. Technische Architektur Prototyp (Vorschlag)

| Schicht | Inhalt | Technik |
|---|---|---|
| `cc-core` | Datenmodell, Prüfregeln, Bezeichnergenerator, Zoom/Shift-Operationen, Export; reine Funktionen | TypeScript, Vitest (Muster eng-core) |
| Speicher | lokal zuerst, später Abgleich mit Supabase | Dexie (IndexedDB), Outbox-Muster aus SPALTEN light |
| Editor | Bild mit Overlay, Werkzeuge, Ebenen, Tabs | React, react-konva (Canvas mit Hit-Test, Zoom, Transform) |
| UI-Rahmen | wie die übrigen Tools | TanStack Start, Tailwind, shadcn |
| Export | PDF-Bericht, JSON | Druckroute bzw. bestehender Exportweg |

Repo: eigenständig, App im Wurzelordner (Lovable-kompatibel, Umsetzung direkt im Code). Namensvorschlag `wirknetz`.

## 8. Ausbaustufen (angepasst)

| Stufe | Umfang | Abnahme |
|---|---|---|
| v0.1 | Projekt, Bauteilbaum, Bild-Upload, Editor mit Tröster-Farbcode (WFP, LSS, C, FD, Systemgrenze), fraktale Detail-Tabs mit Punktnotation, Zustandsliste, Prüfregeln, Parameter, Hypothesen, Entscheidungen, Export PDF/JSON, lokal gespeichert | Hydraulischer Widder mit 5 Zuständen und Kreiselpumpe mit Detail Gleitringdichtung vollständig modelliert |
| v0.2 | Abgleich Supabase, Sequenzmatrix (vier Dimensionen), Extended-Modus, Versionen und Diff, Lernbereich Stufe 1 | Retrofit-Fall mit zwei Modellversionen |
| v0.3 | Berechnung über eng-core, Wandler und Bilanzen, Komponentenbibliothek, Bondgraph-Export | Pumpenkennlinie am Connector, Pressung an WFP |
| später | KI-Vorschläge je Schritt, 3D, Teamfunktionen, Modul in MeinIngenieur | |

Lernbereich rückt wegen E1 nach v0.2; in v0.1 genügen kurze Erklärtexte je Werkzeug.
