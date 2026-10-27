# Tröster, Dieck, Albers 2025: Evaluation des Extended C&C²-Approach

| Feld | Wert |
|---|---|
| Autoren | Peter M. Tröster, Tobias Dieck, Albert Albers |
| Titel | Evaluating the Extended C&C²-Approach in a Live Lab and in Practice |
| Quelle/Reihe | Procedia CIRP 136 (2025), S. 576 bis 581, 35th CIRP Design 2025 |
| Jahr | 2025 |
| DOI | 10.1016/j.procir.2025.08.099 |
| Lizenz | CC BY 4.0 |
| Volltext | [`../volltexte/Troester2025a.pdf`](../volltexte/Troester2025a.pdf) (6 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Erste Evaluation des **Extended C&C²-Approach** (Templates, Designation Guide, Functional Delimitation, Prozessmodell) gegen den klassischen Ansatz mit **27 Studierenden** im Live Lab und **9 Ingenieuren** eines Automobilzulieferers. Die Gruppe mit Extended-Werkzeugen fand im Mittel **mehr Funktionen (8 statt 5)**, mehr Zustände inklusive Zwischenzustände, **rund 4 Abschnitte mehr** und **25 % mehr Optimierungsvorschläge**. Hauptbarriere ist die zu kurze Schulung; die Autoren kündigen ein **Software-Tool** an, das sich in Entwicklung befindet.

## Inhalte nach Abschnitt

### 1. Motivation (S. 576)
- Demografischer Wandel, Verlust impliziten EFR-Wissens. Prozessmodell auf Basis C&C² soll Wissen erfassen, dokumentieren und nutzbar machen.

### 2. Stand der Technik (S. 576 bis 577)
- Klassischer Ansatz mit WSP, CSS, C (Abb. 1 nach Matthiesen et al. 2018, Procedia CIRP 70).
- **Designation Guide:** Regeln für WSP ("//") und CSS ("~").
- **Functional Delimitation** (Abb. 2, Beispiel Schraubenfeder): Segmentierung einteiliger Bauteile in funktionale Abschnitte, z. B. bei nachgiebigen Mechanismen.
- Prozessmodell in fünf Hauptschritten mit Pflicht- und optionalen Unterschritten (Kurzfassung von Troester2025b): Pre-analysis, Analysis Phase (inkl. **confidence level**), Documentation (mit Designation Guide), Synthesis (Variation der EFR), Evaluation and Adjustment.

### 3. Forschungsfragen (S. 577 bis 578)
- Fünf Fragen: Verbesserung der Analysefähigkeit, Unterschied in Anzahl und Qualität gefundener EFR, Nutzerbewertung, Hindernisse in der Praxis, signifikanter Unterschied bei Optimierungspotenzialen.

### 4. Methodik (S. 578)
- **27 Studierende** (Master Maschinenbau und Wirtschaftsingenieurwesen, Live Lab IP) und **9 Ingenieure** eines Automobilzulieferers.
- Gruppe A klassischer Ansatz, Gruppe B Extended-Templates (System-State Function Diagram, Pre-Analysis-Template, Dokumentationsformulare). Firmengruppen AF und BF analog.
- Zufällige Zuteilung; **90 Minuten** Analysezeit; Gruppe B mit **20 Minuten** Schulung.
- Untersuchungsobjekt: segmentiertes 3D-Modell bzw. 3D-Druck einer **Zange** mit vorbeschrifteten Teilen. Firmenstudie mit realen Automotive-Bauteilen.
- Zwei Termine wegen Terminlage; am zweiten Tag nur eine Gruppe B (ein Betreuer). Gruppengrößen je Tag im Text nicht beziffert.
- Daten: Anzahl Funktionen, Zustände, Optimierungsvorschläge (Zählschema Abb. 4), Fragebogen mit Likert-Skala und offenen Fragen.

### 5. Ergebnisse (S. 579)
- Gruppe B im Mittel **8 Funktionen**, Gruppe A **5**.
- Gruppe B fand mehr Zustände, auch **Zwischenzustände** ("opening", "closing").
- Durch Functional Delimitation im Mittel **4 zusätzliche Abschnitte**.
- **25 % mehr Optimierungsvorschläge** (Ergonomie, Funktion, Materialeinsparung).
- Befragung: **75 %** in Gruppe B empfanden die Templates als erleichternd; **87 %** in Gruppe A hielten die vorhandenen Werkzeuge für unzureichend; **70 %** wünschten mehr Schulungszeit.
- Der Text spricht von "significantly outperformed", nennt aber **keine Teststatistik** (kein p-Wert, keine Effektstärke). Einschätzung: als Tendenz lesen.

### 6. Diskussion (S. 579 bis 580)
- Standardisierung erleichtert Kommunikation; Pre-Analysis hilft bei Systemgrenzen.
- Herausforderungen: Schulungsbedarf, knappe Analysezeit.
- Grenzen: kleine Stichprobe (besonders n = 9 in der Industrie), kurze Laufzeit, Selbstauskünfte mit möglichen Verzerrungen.
- Teilnehmende wünschten **digitale Versionen der Templates**.

### 7. Fazit und Ausblick (S. 580 bis 581)
- Breitere Expertenstudien, Längsschnittstudien zur Wissensweitergabe.
- "A software tool, which is currently in development, is intended to significantly streamline the application of our templates" (S. 581).
- Förderung: DFG, Projektnummer 509078026.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Messgrößen Funktionen, Zustände, Abschnitte, Optimierungsvorschläge | Eingebaute Kennzahlen je Modell (Zählung), nutzbar für eigene Evaluation und Qualitätsanzeige |
| Zwischenzustände werden mit Templates eher gefunden | Zustandsassistent fragt aktiv nach Übergangszuständen zwischen zwei Hauptzuständen |
| Functional Delimitation erhöht Detailtiefe | Werkzeug zum Einzeichnen von Funktionsabschnitten auf einem Bauteil (eigener Elementtyp) |
| Pre-Analysis-Template für Systemgrenzen | Startformular: Zweck, Systemgrenze räumlich/zeitlich, Bauteilliste |
| 20 Minuten Schulung reichen nicht | Lernmodus mit kurzen kontextbezogenen Erklärungen und Beispielen je Schritt |
| Wunsch nach digitalen Templates | Templates als Formulare im Tool, Export als PDF |
| IPEK entwickelt eigenes Software-Tool | Marktbeobachtung, mögliche Kooperation mit IPEK (Tröster) prüfen |

## Im Paper zitierte Schlüsselquellen
Matthiesen und Grauberger 2024 (Buch "Konstruktionswissen für Ingenieure", Springer), Matthiesen et al. 2018 (Procedia CIRP 70), Grauberger et al. 2020 (JED), Matthiesen 2021 (Pahl/Beitz), Tröster et al. 2023 (Designation Guide), Tröster, Prager, Schmid, Albers 2023 (SSP, Functional Delimitation), Tröster et al. 2025 (Prozessmodell), Walter et al. 2016 (Live-Lab).
