# Erkenntnisse aus der Literatur für ein späteres Ingenieur-Tool

Status: **Anforderungssammlung, keine Spezifikation.** Stand 27.10.2026, nach Auswertung von 33 Volltexten (Zusammenfassungen je Quelle mit Abschnitt "Relevanz für ein Ingenieur-Tool"). Das Tool-Konzept selbst wird in Phase 3 im Dialog erarbeitet.

## 1. Was die Literatur fordert

| Befund | Quelle | Mögliche Tool-Anforderung |
|---|---|---|
| Kein verfügbarer, gepflegter C&C²-Editor; bisherige Software nur Prototypen (CAM 2011, SysML-Profil 2013, UML-Editor 2025) | `Albers2011c`, `Albers2013`, `Urbano2025`, `Albers2014` S. 168 | Marktlücke |
| IPEK (Tröster-Gruppe) entwickelt ein Tool für die Extended-Templates | `Troester2025a` S. 581 | Abgrenzung oder Kooperation klären |
| Papiermodelle: keine Konsistenz, kein Zoom, keine Ablage, keine Sequenzen in einem Datensatz | `Albers2011c`, `Albers2014` | Kernnutzen: Konsistenzprüfung, Detailebenen, Suche, Teamarbeit |
| C&C²-Modelle haben keine Datenstruktur | `Grauberger2020a` S. 261 | Offenes, versioniertes Datenformat (JSON-Schema) |
| Modelle entstehen auf Skizzen, Zeichnungen, CAD-Screenshots, Fotos | `Albers2014` S. 158, `Thau2013` S. 99 | Bild-Upload als Systemabbild, Elemente direkt einzeichnen |
| Novizen brauchen Prozessführung; Kurzschulung reicht nicht | `Troester2025b`, `Troester2025a`, `Troester2025c`, `Grauberger2022b`, `Thau2013` | Geführter Modus nach Prozessmodell (fünf Schritte) bzw. Schritten a bis g |
| Benennung und Functional Delimitation schwer vermittelbar | `Troester2023`, `Troester2025c` | Automatische Bezeichner nach Designation Guide, FD als Zeichenwerkzeug |
| Modellzweck ist Pflichtbestandteil | `Matthiesen2021`, `Albers2011c` S. 101006-5 | Pflichtfeld beim Anlegen |
| Parameter am wertvollsten, aber nicht formal verankert | `Grauberger2020b` | Parameter als Objekte mit Größe, Wert, Einheit, Quelle je WFP/LSS/C |
| Hypothesen und Konfidenz zentral | `Matthiesen2017a`, `Troester2025b`, `Thau2013` S. 100 | Hypothesenregister (Wenn-Dann-Weil, Prüfung, Ergebnis), Konfidenz je EFR |
| Dynamische Systeme brauchen Zustände in vier Dimensionen | `Matthiesen2019b` | Modell-Metadaten logischer Zustand, Systemzustand, Detailstufe, Ort; Matrixnavigation |
| Synthesis Gap | `Troester2026` | Berechnungsschicht je WFP (Flächenvektor, Pressung, Gleichgewicht) |
| Fehleranalyse ist bester Use Case | `Gladysz2018a`, `Albers2014` S. 166 | Modus Fehler- und Ursachenanalyse |
| Ideal vs. real (Fertigung, Verschleiß); Verschleißspuren als Indiz für WFP | `Matthiesen2018a`, `Matthiesen2021` S. 441 | Varianten je WFP; Foto-Evidenz je Element |
| Generationsvergleich, Variationsart je Abschnitt | `Troester2024a`, `Troester2024b` | Diff zwischen Modellversionen, Variationsart je Abschnitt |
| C&C² wird stets mit anderen Modellen kombiniert (CAD am häufigsten) | `Grauberger2020b`, `Paehler2024` | Verknüpfungen zu CAD, Messdaten, Simulation, FMEA |
| Bibliotheken und automatische Ergänzung fehlender Flüsse | `Albers2011c` | Komponentenbibliothek mit WFP-LSS-Vorlagen und Prüfregeln |
| Formale Taxonomie schränkt ein | `Albers2011c` | Freitext immer erlaubt, Taxonomie optional |
| KI nur mit manueller Freigabe je Schritt | `Schleifer2026` | KI-Vorschläge je Prozessschritt, Nutzer bestätigt |
| Einheitliche Benennung als Grundlage einer Modelldatenbank für KI | `Troester2023`, `Troester2025b` | Durchsuchbare Modellbibliothek |

## 2. Datenmodell-Skizze (aus Definitionen und Formalisierungen abgeleitet)

Grundlage: Formalisierung `Albers2011c` (Ports, Module, Part, Flow, Function), Definitionen `Matthiesen2021`, Sequenzstruktur `Matthiesen2019b`, Extended-Elemente `Troester2023`, `Troester2025b`, Quantifizierung `Troester2026`, Profile `Albers2013`, `Urbano2025`.

```
Projekt
 └─ Produkt / Produktgeneration (PGE-Bezug)
     ├─ bauteilbaum: [Modul → Teil]                 # Albers2011c, Troester2025b Schritt 1
     │    └─ bezeichner nach Designation Guide       # Hauptsystem (Buchstabe), Subsystem (Nummer)
     └─ C&C²-Modell (= genau ein Wirknetz)            # Matthiesen2021 S. 423
         ├─ zweck: Text (Pflicht)
         ├─ systemabbild: Foto | Skizze | CAD-Screenshot | CT | Video-Frame
         ├─ metadaten: { logischer_zustand, systemzustand, detailstufe, ort }   # Matthiesen2019b
         ├─ systemgrenze: { räumlich, zeitlich }
         ├─ wirkflaechen: [WF { teil, medium: fest|fluid|gas|feld, geometrie_im_bild }]
         ├─ wfp: [WFP { wf_a, wf_b, flows: [Energie|Stoff|Signal], flaechen_vektor?, reibwert?,
         │              variante: ideal|gefertigt|verschlissen, konfidenz }]
         ├─ lss: [LSS { wfp_a, wfp_b (genau zwei), medium, statisch|dynamisch, parameter }]   # Prager2024
         ├─ connectoren: [C { wf_repraesentativ, umgebungsmodell, quelle?: bool }]
         ├─ funktionsabgrenzungen: [FD { teil, abschnitt }]         # Troester2023b
         ├─ funktionen: [Funktion { text, wfp: [≥2], lss: [≥1], connectoren: [≥2] }]
         └─ parameter: [{ element, name, wert, einheit, quelle }]
 ├─ hypothesen: [{ wenn (parameter + referenz), dann (funktionsgröße), weil, pruefung, ergebnis }]
 ├─ entscheidungen / modifikationen: [{ syntheseprinzip: hinzufuegen|entfernen|aendern, begruendung, hypothese }]
 └─ verknuepfungen: [{ ziel: CAD|Messung|Simulation|SysML|FMEA|Bondgraph, referenz }]
```

**Prüfregeln direkt aus der Literatur:**
- GH 1: Jede Wechselwirkung braucht ein WFP aus genau zwei Wirkflächen (`Matthiesen2002` S. 50).
- GH 2: Eine Funktion braucht ≥ 2 WFP, ≥ 1 verbindende LSS und je einen Connector zur Umgebung (`Matthiesen2021`, `Albers2011c` Komplementarität).
- LSS verbindet genau zwei WFP (`Matthiesen2021` S. 421 bis 422); gröbere Darstellungen als Gruppierung zulassen (`Noeller2023`).
- GH 3: Jedes Element darf in ein Untermodell aufgelöst werden (Zoom); Shift löst Connector in WFP und LSS auf (`Matthiesen2021` S. 436).
- Zustand: Änderung von Anzahl oder Eigenschaften der Gestaltfunktionselemente erzeugt einen neuen Zustand (`Matthiesen2021` S. 423); jeder Zustand hat mindestens zwei Connectoren (`Thau2013` S. 82).
- Vogel-Elemente für Energiesysteme: Knotenbilanz, Reaktionspfad je Umformung und Wandlung (`Vogel2021`).

## 3. Offene Fragen aus der Erstrecherche, jetzt beantwortet

| Frage | Antwort | Quelle |
|---|---|---|
| Struktur des Sequenzmodells | Vier Dimensionen: logischer Zustand (übergeordnet), Systemzustand, Detaillierungsgrad, Ort der Funktionserfüllung; Metadaten je Modell, abgeleitete Ansichten | `Matthiesen2019b` |
| Formalisierung in `Albers2011c` | WS mit äußerem und innerem Port, WSP und CSS als Verbindungen, Module/Part-Hierarchie, Flow und Function aus Taxonomie, Komplementaritätsregel, Bibliotheken, automatische Ergänzung; kein Connector | `Albers2011c` |
| Fünf Schritte des Extended C&C² | Pre-Analysis, Analysis, Documentation, Synthesis, Evaluation and Adjustment, je 3 bis 4 Unterschritte | `Troester2025b` |
| Darstellungskonventionen | Doppellinie WFP, Wellenlinie LSS, Connector als Kreis bzw. Polygon; Farbcode nur Tröster-Gruppe (rot, gelb, grün, blau) | `Thau2013`, `Grauberger2022b`, `Alink2010`, `Troester2025c` |
| Zielgruppe | weiterhin offen, Gegenstand von Phase 3 | |

## 4. Weiterhin offen

- Primärquelle Functional Delimitation (`Troester2023b`) und Konstruktionswissen-Buch (`MatthiesenGrauberger2024`) beschaffen.
- Ohmer 2008 (Synthese-Dissertation) fehlt noch als Volltext.
- Modellierungsregeln für Fluide, Druck, Volumenstrom und Domänenwandlung sind in der Literatur nicht ausgearbeitet und müssen für Wasser/Energie selbst definiert und geprüft werden.
- Kontakt zur Tröster-Gruppe (IPEK) zum angekündigten Software-Tool.

## 5. Lesestand Pflichtlektüre

| Quelle | Status |
|---|---|
| `Grauberger2020a` Review 20 Jahre | gelesen |
| `Matthiesen2018a` SWP 58 | gelesen (Vorarbeit) |
| `Albers2014` Anthology-Kapitel | gelesen |
| `Matthiesen2021` Pahl/Beitz Kap. 13 | gelesen |
| `Troester2025b`, `Troester2023`, `Troester2025a`, `Troester2025c` | gelesen |
| `Matthiesen2019b` Sequenzmodell | gelesen |
| `Albers2011c` Formalisierung | gelesen |
| `Troester2026` WFP-Vektoren | gelesen |
| `Gladysz2018a` Fehleranalyse | gelesen |
| `Vogel2021` Wandlungselemente | gelesen |
| `Prager2024` Bondgraph | gelesen |
| `Ohmer2008` Synthese | fehlt (KIT-Zugang) |
| `Troester2023b` Functional Delimitation | fehlt (SSP 2023) |
