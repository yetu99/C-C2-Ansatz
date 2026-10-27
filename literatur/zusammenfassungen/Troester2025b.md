# Tröster, Dieck, Albers 2025: Prozessmodell für den Extended C&C²-Approach

| Feld | Wert |
|---|---|
| Autoren | Peter M. Tröster, Tobias Dieck, Albert Albers |
| Titel | Development of a Process Model for the Extended C&C²-Approach for Analyzing and Synthesis of Embodiment Function Relations |
| Quelle/Reihe | Procedia CIRP 136 (2025), S. 618 bis 623, 35th CIRP Design 2025 |
| Jahr | 2025 |
| DOI | 10.1016/j.procir.2025.08.106 |
| Lizenz | CC BY 4.0 |
| Volltext | [`../volltexte/Troester2025b.pdf`](../volltexte/Troester2025b.pdf) (6 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der klassische C&C²-Ansatz liefert zu wenig **Vorgehensführung**, um Gestalt-Funktion-Zusammenhänge (Embodiment Function Relations, EFR) systematisch zu **dokumentieren**. Das Paper schlägt ein **Prozessmodell mit fünf Schritten** vor (Pre-Analysis, Analysis, Documentation, Synthesis, Evaluation and Adjustment), das **Designation Guide**, **Functional Delimitation** und **strukturierte Templates** einbindet. Leitmotiv ist **Wissenssicherung** gegen den Verlust impliziten Wissens durch ausscheidende Ingenieure.

## Inhalte nach Abschnitt

### 1. Einleitung (S. 618)
- Demografischer Wandel: implizites Wissen zu EFR geht mit erfahrenen Ingenieuren verloren.
- Der klassische Ansatz bietet "not sufficient procedural detail", besonders für unerfahrene Anwender.

### 2. Stand der Technik (S. 618 bis 619)
- Klassischer C&C²-Ansatz: Kernelemente WSP, CSS, Connector (Verweis auf Matthiesen 2021).
- Zusätzliche Formalisierung nötig, um EFR konsistent über Anwendungen und Projektphasen zu erfassen, ausdrücklich auch "for later use to teach artificial intelligence about EFR" (S. 619).
- **Designation Guide** (Tröster et al. 2023): standardisierte Benennung.
- **Functional Delimitation** (Quelle: Tröster, Prager, Schmid, Albers, SSP 2023): Zerlegung komplexer Systeme in funktionale Abschnitte, besonders bei Bauteilen mit mehreren Funktionen.

### 3. Forschungsfragen und Methodik (S. 619)
- RQ1: Schlüsselelemente und Schritte eines Prozessmodells. RQ2: Herausforderungen bei der Umsetzung.
- Design Research Methodology (DRM): Descriptive Study I mit Literatur und Empirie, Referenzmodell, Wirkmodell (Impact Model). Erste Anwendung in Live Lab (KIT) und Industrie (Details in Troester2025a).

### 4. Das Prozessmodell (S. 619 bis 621, Abb. 1 bis 5)
Jeder Schritt hat ein Ziel und Unterschritte. Beispielsystem in den Abbildungen ist eine **nachgiebige Zange (compliant mechanism plier)**.

| Schritt | Ziel | Unterschritte |
|---|---|---|
| 1 Pre-Analysis | Grundlage schaffen, Umfang und Ziele festlegen | 1 vorhandene Informationen sammeln (Spezifikationen, frühere Analysen, Experten, Use Cases; FMEA oder Persona-Methode möglich); 2 Umfang und Zweck festlegen (Systemgrenzen, Ziele); 3 **Bauteilbaum (component tree)** und Benennung nach Designation Guide; 4 Analyseaufwand und Ressourcen schätzen |
| 2 Analysis | EFR systematisch untersuchen | 1 Systemzustände und Einbindungspunkte mit einem **System State-Function Diagram (SFD)** identifizieren (Connectoren); 2 EFR analysieren (WSP, CSS zu Funktionen zuordnen); 3 **Konfidenzniveaus (confidence levels)** je Zusammenhang dokumentieren; 4 **funktionale Parameter** (z. B. Kräfte, Maße) je Funktion festlegen |
| 3 Documentation | Ergebnisse strukturiert ablegen | 1 Daten in **Templates** (Gestaltparameter, Funktionen, Konfidenz); 2 Dokumentation per **Hyperlink** mit C&C²-Modellen verknüpfen; 3 Vollständigkeit und Richtigkeit periodisch prüfen |
| 4 Synthesis | Optimierungen entwickeln und testen | 1 Optimierungspotenziale filtern; 2 **Referenzsystemelemente** suchen (Benchmarks aus anderen Systemen); 3 **Hypothesen** formulieren und per Simulation oder Prototyp testen; 4 Modifikationen dokumentieren |
| 5 Evaluation and Adjustment | Syntheseergebnis bewerten und nachsteuern | 1 Ergebnis gegen Ziele und Spezifikation testen; 2 offene Punkte identifizieren; 3 Anpassen; 4 **Abschlussdokumentation** (Ergebnisse, Anpassungen, finale Parameter) |

- Abb. 3 zeigt **Dokumentations-Arbeitsblätter** (documentation worksheets).

### 5. Diskussion (S. 621 bis 623)
- Unterschied zum klassischen Prozess (nach Matthiesen 2021): Schwerpunkt verschiebt sich von Problemanalyse und Lösungsgenerierung zur **systematischen Wissensdokumentation**; eigene Dokumentationsphase.
- Stärken: Konsistenz über Projekte, weniger Missverständnisse durch einheitliche Benennung, fokussierte Analyse durch Functional Delimitation.
- Schwächen: deutlich **mehr Zeitaufwand** mit den Templates; **20 Minuten Einführung** wurden von Studierenden und Ingenieuren als zu kurz bewertet.
- Zielkonflikt Analysetiefe gegen Effizienz bei zeitkritischen Projekten.

### 6. Fazit und Ausblick (S. 623)
- Schulungsprogramm entwickeln, Übertragbarkeit auf andere Branchen prüfen.
- **Digitale Werkzeuge** und automatisierte Analysehilfen sollen Aufwand senken und Konsistenz erhöhen.
- Glossar (Tab. 1) mit Kurzdefinitionen; Connector dort als "Interfaces linking external or internal elements to the system, that are not part of the design space".

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Fünf Schritte mit je 3 bis 4 Unterschritten | Geführter Wizard mit Fortschrittsanzeige; Unterschritte als Checkliste, Pflicht und optional markiert |
| Bauteilbaum plus Designation Guide in Schritt 1 | Strukturbaum-Editor, aus dem Bezeichner automatisch nach Designation Guide erzeugt werden |
| System State-Function Diagram | Matrixansicht Zustände × Funktionen als Navigationsebene über den Einzelmodellen |
| Konfidenzniveau je EFR | Pflichtattribut `konfidenz` an jedem Gestalt-Funktion-Zusammenhang; Filter "unsicher" für Folgeuntersuchungen |
| Funktionale Parameter je Funktion | Parameterliste mit Größe, Wert, Einheit, Quelle; Grundlage für spätere Berechnungen |
| Templates und Hyperlinks zur Dokumentation | Jede Dokumentationszeile verweist per ID auf Modellelement und Bildausschnitt |
| Synthese über Hypothesen und Referenzsystemelemente | Hypothesenregister plus Bibliothek von Referenzlösungen (PGE-Bezug) |
| Abschlussdokumentation mit finalen Parametern | Export als Entscheidungs- und Wissensbericht (PDF/Markdown) |
| Zeitaufwand und kurze Schulung als Hauptbarrieren | Vorlagen vorbefüllen, Lernhilfen kontextbezogen im Schritt einblenden |

## Im Paper zitierte Schlüsselquellen
Grauberger et al. 2020 (JED, 20 Jahre), Matthiesen 2021 (Pahl/Beitz Kap. 13, klassisches Vorgehen), Tröster, Schmidt, Albers 2023 (Designation Guide), Tröster, Prager, Schmid, Albers 2023 (SSP, Functional Delimitation, abschnittsweise GFZ), Tröster, Dieck, Albers 2025 (Evaluation), Grauberger et al. 2022 (Procedia CIRP 109, Hypothesen aus Industrieprojekten).
