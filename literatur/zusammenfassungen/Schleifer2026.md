# Schleifer et al. 2026: KI-basiertes, modulares Assistenzsystem für funktionale Systemarchitekturen

| Feld | Wert |
|---|---|
| Autoren | Simon Schleifer, Adriana Lungu, Benjamin Kruse, Lea Schwarz, Stefan Goetz, Sandro Wartzack (FAU Erlangen-Nürnberg, Lehrstuhl für Konstruktionstechnik KTmfk; Audi AG, Ingolstadt) |
| Titel | KI-basiertes, modulares Assistenzsystem für funktionale Systemarchitekturen |
| Quelle | Konstruktion 78 (2026) Nr. 10, Rubrik Fachaufsatz, S. 44 bis 49 (Literatur und Lizenz auf S. 49) |
| Jahr | 2026 |
| DOI | 10.37544/0720-5953-2026-10-44 |
| Lizenz | CC BY 4.0 (Open Access) |
| Volltext | [`../volltexte/Schleifer2026.pdf`](../volltexte/Schleifer2026.pdf) (8 S., davon 6 S. Fachaufsatz, Rest Heftvorschau und Rubrikseite) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag stellt ein **modulares Assistenzsystem** vor, das **NLP** und **Large Language Models (LLMs)** in die manuelle **Verhaltensmodellierung** mit SysML (Use-Case-, Aktivitäts-, Sequenzdiagramm, Zustandsautomat) einbindet. Die Module folgen **Schritt für Schritt der Modellierungsmethode**, sind als **Plugin im Modellierungswerkzeug** integriert und verlangen nach jedem Aufruf eine **manuelle Prüfung** durch den Entwickler. Ein Bezug zum C&C²-Ansatz besteht nicht; der Beitrag dient als Kontext für KI-Unterstützung in einem Modellierungstool.

## Inhalte nach Abschnitt

### 1. Einleitung und Motivation (S. 44)
- Steigende Systemkomplexität in der Automobilindustrie, MBSE als Antwort. Manuelle Modellierung ist besonders zu Beginn zeitintensiv, KI soll natürlichsprachliche Anforderungen in formale Modelle überführen.

### 2. Stand der Technik (S. 44 bis 45)
- MBSE-Dreiklang Sprache, Methode, Werkzeug. SysML-Verhaltensdiagramme (Use Case, Aktivität, Sequenz, Zustandsautomat).
- V-Modell nach VDI/VDE 2206, Systemebenen, **RFLP-Ansatz** (Requirements, Functional, Logical, Physical) mit Referenzarchitektur. Übergang R zu F erfordert Formalisierung natürlichsprachlicher Anforderungen.
- NLP-Methoden: POS-Tagging, Named-Entity Recognition, Embeddings. LLM-Techniken: One-/Few-Shot Prompting, **Prompt Chaining** (Aufgabe in mehrere Prompts zerlegt).
- Vorarbeiten: Use Cases aus User Stories per Clustering, Aktivitätsdiagramme per Deep Learning, Zustandsautomaten per NLP; für Sequenz- und Use-Case-Diagramme liefern LLMs bessere Qualität als NLP.

### 3. Forschungsproblem (S. 45, Bild 1)
- Bestehende Ansätze betrachten Einzelaspekte isoliert, Ein- und Ausgänge aufeinanderfolgender Ansätze sind nicht abgestimmt, die Einbindung des Menschen fehlt, homogene Anforderungen werden vorausgesetzt.
- Anforderungen an Unterstützung:
  - Verarbeitung unstrukturierter Anforderungsspezifikationen
  - Erstellung initialer sowie Ergänzung bestehender Systemmodelle
  - Anpassbarkeit an geänderte Methode oder Domäne
- Forschungsfrage: Aufbau eines Assistenzsystems zur automatisierten Erstellung funktionaler Systemarchitekturen. Beispiel-User-Journey: Navigation, fahrerloses Parken, kabelloses Laden eines batterieelektrischen Fahrzeugs.

### 4. Assistenzsystem (S. 45 bis 48, Bild 2 bis 4)
- **Architektur:** Plugin in Cameo Systems Modeler, KI über RestAPI, Sprachmodell "gpt-4o" in privater Instanz. Jedem Modul liegen Schritte der unternehmensspezifischen Methode **FAME** zugrunde, die ins Prompt Engineering einfließen (Meta-Modell Bild 4). Nach jedem Modulaufruf manuelle Prüfung (Bild 3).
- Nutzen laut Autoren: Zeitersparnis, höhere Modellkonsistenz durch weniger subjektive Einflüsse und Wiederverwendung bestehender Modellinhalte.
- **4.1 Kontextmodellierung (S. 46 bis 47):**
  - M1.1 Use-Case-Identifikation: Anforderungen als Embeddings, gewichtete Kanten aus funktionaler Ähnlichkeit und expliziten Beziehungen, **überlappendes graphbasiertes Clustering**, Keyphrases zur Prüfung. Beispiel "Navigation": fünf Use Cases.
  - M1.2 Use-Case-Detaillierung: One-Shot Prompts für Name und Dokumentation, **kuratierte Auswahllisten** für Vor-/Nachbedingungen und Auslöser, Akteure gemäß Referenzarchitektur, Beziehungen per Prompt Chaining, Import des Diagramms, Freigabe durch Nutzer.
- **4.2 Verhaltensmodellierung (S. 47 bis 48):**
  - M2.1 Aktivitätsdiagramm-Grundstruktur per Prompt Chain und Few-Shot über **textuelle Diagrammbeschreibung**; Syntaxfehler über Funktionsaufrufe des LLM aufgelöst. Beispiel "Perform auto park".
  - M2.2 Zuweisung zu Subsystemen/Funktionen über **Vektordatenbank** der Operationen aller Funktionen plus Prompt Chaining; Kandidatenlisten; Restfälle über nachgelagerte Prompts.
  - M2.3 Informationsfluss: LLM schlägt Signal vor, Abgleich mit Vektordatenbank; bei Treffer Wiederverwendung, sonst Vorschlag zur manuellen Prüfung.
  - M3.1 Sequenzdiagramm, übernimmt Lifelines und Nachrichten aus bestehendem Aktivitätsdiagramm. Beispiel Authentifizierung an Ladesäule.
  - M3.2 zeitliche Zusicherungen aus Anforderungen (Beispiel 3 s bis Ladebeginn).
  - M3.3 Nachricht als Signal oder Operation, Wiederverwendung über Vektordatenbank und Entscheidungsprompt mit Kandidaten.
  - M4.1 Zustandsautomat aus Use Cases; **Simulation** prüft Ausführbarkeit, Fehlermeldungen fließen in den Prompt zurück. Beispiel "Charging": Idle, Charging, Connected, Error.
  - M4.2 Zuordnung von Verhaltensdiagrammen zu Zuständen, Detaillierung von Transitionen.
  - M4.3 Ergänzung des Gesamtsystem-Zustandsautomaten aus Vor- und Nachbedingungen.

### 5. Zusammenfassung und Ausblick (S. 48 bis 49)
- Module aufeinander abgestimmt (z. B. Use-Case-Beschreibung als Eingabe für Aktivitäts- und Sequenzdiagramm). Modularer Aufbau erleichtert Anpassung und manuelle Prüfung durch schrittweisen Modellaufbau.
- Erste Nutzerstudie nur für das Use-Case-Diagramm (Verweis auf [16], INCOSE 2025); im Beitrag selbst keine Zahlen. Industrielle Anwendbarkeit und Übertragbarkeit noch zu untersuchen.
- Finanzierung durch Audi AG.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Module folgen den Methodenschritten | KI-Funktionen je Schritt des C&C²-Vorgehens (Modellzweck, Systemgrenze, WFP/LSS/C, Gestaltparameter), keine Gesamtgenerierung |
| Manuelle Prüfung nach jedem Modulaufruf | Vorschläge erscheinen als Entwurf mit "Übernehmen/Verwerfen", Status `ki_vorschlag` bis zur Freigabe |
| Kuratierte Auswahllisten statt Freitext | KI wählt aus festen Enums (Elementtyp, Flussart Energie/Stoff/Information, Variationsart) |
| Vektordatenbank zur Wiederverwendung bestehender Elemente | Ähnlichkeitssuche über vorhandene WFP, LSS, Connectoren und Hypothesen vor Neuanlage, Duplikatwarnung |
| Textuelle Diagrammbeschreibung als Zwischenformat | Internes JSON-Schema des C&C²-Modells als Austauschformat zwischen LLM und Editor |
| Syntaxprüfung und Simulationsfeedback an das LLM | Validierungsregeln (z. B. LSS mit genau zwei WFP) prüfen KI-Ausgaben, Fehlermeldungen gehen in einen zweiten Prompt |
| Clustering unstrukturierter Anforderungen | Import einer Anforderungsliste, Gruppierung nach Funktionen als Startpunkt für Modellzweck und Zustände |
| Private Modellinstanz, Plugin im Werkzeug | Konfigurierbare Modellanbindung (eigener Schlüssel oder lokales Modell), keine Pflicht zum Cloud-Upload |

## Im Paper zitierte Schlüsselquellen
Keine C&C²-Quellen. Für KI-Unterstützung relevant: Schleifer et al. 2024 (DFX2024, Use-Case-Diagramme aus Anforderungen), Schleifer et al. 2025 (INCOSE IS, LLM-basierte Use-Case-Diagramme, Nutzerstudie), Schleifer et al. 2025 (Design Science, Use-Case-Identifikation per Graph-Clustering), Schleifer et al. (eingereicht, Aktivitätsdiagramme per LLM), Hovemann et al. 2025 (Prompt Engineering im Systems Engineering, ZWF), Wu et al. 2022 (AI Chains), VDI/VDE 2206:2021-11.
