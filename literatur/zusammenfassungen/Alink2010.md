# Alink 2010: Funktion im C&C-Ansatz

| Feld | Wert |
|---|---|
| Autoren | Thomas Alink (Dipl.-Ing., aus Freiburg) |
| Titel | Bedeutung, Darstellung und Formulierung von Funktion für das Lösen von Gestaltungsproblemen mit dem C&C-Ansatz (engl. Nebentitel im PDF "Meaning and notation of function for solving design problems with the C&C-Approach") |
| Quelle/Reihe | Dissertation, Fakultät für Maschinenbau, Karlsruher Institut für Technologie (KIT); Forschungsberichte IPEK, Band 48, Hrsg. A. Albers. Hauptreferent A. Albers, Korreferentin Dr. Claudia Eckert (Open University), Prüfungsvorsitz Prof. Frank Henning |
| Jahr | 2010 (mündliche Prüfung 3. Dezember 2010) |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Alink2010), nicht im Repo (Lizenz) (240 S.) |
| Status | gelesen, Kernkapitel ausgewertet (Kap. 1, 2.4, 3 bis 9, Begriffe und Anhang vollständig; Kap. 2.1 bis 2.3 überflogen) |

Seitenangaben unten sind Druckseiten (Druckseite = PDF-Seite minus 22). Begriffe und Anhang liegen auf S. 208 bis 216.

## Kernaussage

Ingenieure haben Schwierigkeiten, Funktionen zu formulieren und auf die Gestalt zu beziehen, weil sie ihre **Auffassung von Funktion** an eine einzelne Bedeutung oder an eine Konvention der Darstellung oder Formulierung knüpfen. Alink schlägt vor, **Funktion als Interaktion des betrachteten Systems mit Nachbarsystemen** aufzufassen und Funktion als **Konzept aus Bedeutung, Darstellung und Formulierung** zu behandeln, das je nach **Aktivität** im Problemlöseprozess unterschiedlich ausgeprägt ist. Für den C&C-Ansatz leitet er daraus Grundsätze ab, darunter die erstmalige Einführung des **Connectors** (Leitstützstrukturen der Umgebung, S. 182) und den Begriff **"Mittel zum Zweck"** für lokal geschlossene WFP-LSS-Anordnungen. Die Arbeit benennt zudem das bisherige Contact and Channel Modell (C&C-M) in **C&C-Ansatz** um (S. 3).

## Inhalte nach Abschnitt

### 1. Einleitung (S. 1 bis 7)
- Ausgangsthese zehn Ingenieure liefern zehn Lösungen mit zehn Herangehensweisen. Gestaltung ist heuristisch, kein algorithmischer Vorgang.
- Klassische Konstruktionsmethodik **diskretisiert** den Übergang Funktion zu Gestalt in Abstraktionsstufen, reale Prozesse verlaufen nicht kontinuierlich ("Henne-Ei-Problem" von Funktion und Gestalt, S. 2).
- **Namenswechsel (Fn. 11, S. 3)**. Die Benennung "C&C-Ansatz" für das bisher als "Contact and Channel Modell (C&C-M)" bezeichnete Vorgehen ist laut Alink "auch Ergebnis dieser Arbeit". Ein mit dem Ansatz gebildetes Modell heißt **C&C-Modell**. Kurzform im Text auch "C&C-A".
- Abb. 1 (S. 4) zeigt C&C-Modell einer Stirnradstufe auf mehreren Abstraktionsebenen (Text, Flüsse von Energie, Material, Information, WFP und LSS auf der Gestalt).
- Autor seit Januar 2006 in der Forschergruppe Albers. Forschungsfragen (S. 4) "Warum haben Ingenieure und Studierende Schwierigkeiten Funktionen zu formulieren und auf die Gestalt zu beziehen?" und "Warum sind die Darstellungen von Funktion immer unterschiedlich?".
- Gestalt nach Hansen 1968 als Gemeinschaft von Form und Stoffeigenschaft (S. 6), später erweitert um Quellcode (S. 187, S. 208).

### 2.1 bis 2.3 Stand der Forschung, allgemein (S. 8 bis 45, knapp)
- Konstruktionsmethodik (Pahl/Beitz, Roth, Rodenacker, Koller, Hubka, VDI 2221), Systemtechnik (Ropohl), Methodeneinführung (Geis et al. 2008, Birkhofer).
- Heuristisches Vorgehen, Problemlösen, **SPALTEN** (Albers et al. 2005) als Grundlage des Vorgehens in allen Studien (S. 17 f.).
- Funktionsauffassungen und **5- bzw. 6-Kern-Konzepte-Beschreibung nach Vermaas** (Ziele, Aktionen, Funktion als Zweck, Funktion als idealisiertes Verhalten, tatsächliches Verhalten, Struktur/Gestalt), am Beispiel Betonanker (Abb. 7, S. 30). Drei archetypische Bedeutungen nach Vermaas (S. 32).
- Diskretisierende Ansätze (VDI 2221, Roth, Hubka, Lindemann, Functional Basis nach Stone/Wood, Axiomatic Design nach Suh, FBS nach Gero) und deren Kritik (S. 33 bis 45). Im Zwischenfazit gilt die Konvention "abstrakt, lösungsneutral, zwei Worte" wurde für die Suche nach Lösungsprinzipien erstellt und behindert andere Aktivitäten (S. 45).

### 2.4.1 Systematik des C&C-Ansatzes (S. 46 bis 48)
- **Drei Grundhypothesen** in der in dieser Arbeit verwendeten Form (S. 46):
  - GH1 ein Effekt (Reibung, Keileffekt, Kraftübertragung, Informationsübertragung) findet nur statt, wenn eine Wirkfläche (WF) mit einer weiteren WF ein Wirkflächenpaar (WFP) bildet.
  - GH2 (Fassung nach Albers 2010) Funktion wird durch mindestens 2 WFP und sie verbindende Leitstützstrukturen erfüllt.
  - GH3 ein technisches System ist beschreibbar durch eine Struktur von WFP und LSS.
- Fn. 169 zitiert die **Erstfassung nach Matthiesen 2002** (GH I bis III, u. a. "Ein Wirkflächenpaar setzt sich aus genau zwei Wirkflächen zusammen"). Laut Fn. 170 erfolgte 2008 eine Präzisierung durch Albers, Matthiesen und Alink (Albers et al. 2008b), weil Matthiesen 2002 den Effekt ebenfalls als Funktion bezeichnete.
- Beispiel **Kugelschreiber** (Abb. 18, S. 47): WFP0.1 Papier/Kugelschreiber, WFP0.2 Hand/Kugelschreiber, LSS0.1/0.2. Auf Glas findet in WFP0.1 kein Effekt statt.
- **Benennungskonvention** (Fn. 172, S. 47, nach Albers et al. 2007c): Nummer stets zweistellig, erste Ziffer Hierarchieebene der Identifikation, zweite Ziffer laufende Nummer. Beim Ebenenwechsel wird ein WFP nicht umbenannt.
- Zeitliche Einordnung (S. 48). Studien Anfang 2006 bis Mitte 2009. 2009 präzisierte Albers GH2 (Plural "Leitstützstrukturen", explizite Umgebung). Die Studien beruhen auf der älteren Fassung (Albers et al. 2007, Fn. 175), die Präzisierung wird erst in Kap. 7 aufgegriffen.

### 2.4.2 C&C-M und C&C-Ansatz (S. 48 bis 51)
- Fn. 167 definiert den **C&C-Ansatz** als allgemein gültiger Teil, aus dem **C&C-Modelle** gebildet werden. C&C-Modelle sind immer spezifisch.
- Verwandte Elemente bei Rodenacker, Roth, Ersoy (Wirkfläche, Wirkflächenpaar, Wirkraum). C&C-Ansatz setzt Konstruktion als heuristisches Verfahren voraus.
- Historie: erste Nennung Albers et al. 1999/2002, Lehre Maschinenkonstruktionslehre und Karlsruher Lehrmodell, Evaluation in der Lehre (Albers et al. 2003, 2003b), Syntheseprinzipien (Albers et al. 2003c, 2004b, 2005), kognitive Studien Albers/Eckert 2004, Änderungsfortpflanzung (Keller et al. 2007), Vorgehen zum Lösen von Gestaltungsproblemen auf SPALTEN-Basis (Albers et al. 2008, 2008b).
- **Erweiterter C&C-Ansatz** (Albers/Schyr) für Validierungsumgebungen, **generalisierter C&C-Ansatz** (Albers, Enkler, Ottnad) für Kopplung von Simulationswerkzeugen über WFP als Schnittstellen (S. 50).
- Gestalt umfasst bei Albers auch Software/Quellcode (S. 51).

### 2.4.3 C&C-M beim Lösen von Gestaltungsproblemen (S. 51 bis 55)
- Vorgehen nach Albers und Alink 2007, Analyse vor Synthese, Detaillierungstiefe frei wählbar (Blackbox bis Detail).
- Lehrbeispiel **Hochentaster** (Abb. 19 bis 21) mit Hauptfunktion "Äste in großen Höhen absägen" (WFP0.1, WFP0.2, LSS0.1/0.2). Problem Ermüdung wird WFP0.2 und LSS0.1/0.2 zugeordnet, Trennung der Funktionen "Hochentaster halten" (Hüfte, Tragesystem) und "Hochentaster führen" (Arme). Neues SOLL sind vier Stunden Arbeit ohne Pause.
- Laut Fn. 206 existiert die LSS nur, wenn das Gerät angewendet wird.
- WFP und LSS referenzieren unterschiedliche Abstraktionen (Foto, Funktionsbeschreibung, FE-Modell) aufeinander (S. 55).

### 2.4.4 Konzept von Funktion im C&C-Ansatz (S. 55 bis 57)
- Matthiesen 2002 definiert Funktion als "lösungsneutrale Beschreibung zwischen Eingangs- und Ausgangsgrößen eines Systems" (nach VDI 2221). Damit wird die Unterscheidung Zweck versus Verhalten umgangen.
- Kerngedanke der Weiterentwicklung (Albers, Matthiesen, Alink) "Funktion beschreibt keinen potenziellen Zustand, sie findet statt" (S. 56).
- Matthiesen empfahl bereits pragmatische Formulierung über die Nomen-Verb-Kombination hinaus (nach VDI 2803).
- In älteren C&C-Modellen wird Funktion kaum explizit formuliert (Abb. 22, S. 57).

### 3. Zielsetzung und Forschungshypothesen (S. 60 bis 65)
- **HP1** Funktionen sind wichtig, ihre Verwendung geschieht aber nur intuitiv.
- **HP2** unterschiedliche Vorgehensweisen müssen zugelassen werden und erfordern unterschiedliche Bedeutungen von Funktion.
- **HP3** die aktuellen Grundhypothesen sind in Bezug auf Funktion zu allgemein formuliert.
- **HP4** bei der Anwendung treten C&C-unspezifische Barrieren auf.
- Je Hypothese drei bis vier Forschungsfragen, u. a. "Was sind die Elemente eines C&C-Modells eines technischen Systems?" (S. 64).

### 4. Forschungsmethode (S. 66 bis 73)
- Vorrangig qualitativ. Zwei Bereiche: Studien unter Realbedingungen (Projekte) und ein Laborexperiment mit 20 isolierten Teilnehmern.
- **Methodenchronologie (Abb. 23, S. 70)**: Januar 2006 bis Januar 2009 Projekte (9 Diplomarbeiten, 4 Forschungsworkshops, 6 Schulungen, 2 Entwicklungsprojekte), Identifikation von fünf Handlungsfeldern (Notationen, Leitfaden, Funktionen, Analyse/Synthese, Vorgehensweisen), Fokus auf Handlungsfeld 3 Funktionen.
- Mai und Juni 2009 **11 Interviews** mit Entwicklungsingenieuren (gemeinsam mit Eckert). Juli und August 2009 Experiment mit 20 IPEK-Mitarbeitern. Auswertung September 2009 bis März 2010 mit Diplomandin Anne Ruckpaul.
- Tabelle 1 (S. 72 f.) Datenmengen (z. B. Experiment je ca. 4000 Worte Transkript, ca. 5 h Transkription je aufgezeichneter Stunde). Detailanalyse nur bei 8 von 20 Probanden aus Ressourcengründen.

### 5.1 Projekte als Datengrundlage (S. 74 bis 83)
- Auswertung per einfacher Protokollanalyse (Ericsson) mit Codierungsschema (Tabelle 3, S. 76).
- **9 Diplomarbeiten** (Tabelle 4, S. 77), 2006 bis 2009, je sechs Monate in Industrieunternehmen, u. a. Trockenbauschrauben (DA1, DA2, DA8), Bogenoffsetdruckmaschine (DA3, DA4, DA5), Innenraumentlüftung Transporter (DA6), Kettenbremse Elektrokettensäge (DA7), Beschichtung Piezoaktor Dieselinjektor (DA9). Noten 1,0 bis 2,0.
- **6 Schulungen** S1 bis S6 (Tabelle 5, S. 79), Juli 2008 bis Januar 2010, 4 bis 16 h, 7 bis 42 Teilnehmende, Aufgabe jeweils **Betonanker** mit großer Streuung der maximalen Haltekraft (teils über das Zweifache des Zertifizierungswerts). Evaluation von S2 per Fragebogen und 11 Interviews (Juni 2009).
- **2 Entwicklungsprojekte** (Tabelle 6, S. 81): E1 blockierende Motorwellen bei Gleitlagern (Juli 2006, 1 Monat), E2 Verschleiß von Gleitführungen in einer Betonherstellungsanlage (März 2009, 6 Monate).
- **4 Forschungsworkshops** F1 bis F4 (Okt. 2006 bis Mai 2008). F2 Erweiterung der GH II, F3 Sequenzmodell, F4 Begriffe um Funktion (S. 82).

### 5.2 Unterschiedliche Auffassungen von Funktion in Projekten (S. 84 bis 97)
- **Transformation von Flussgrößen** (häufigste Auffassung). Blackbox wird mit einer durch WFP lokalisierten Systemgrenze gleichgesetzt, Papierbögen "fließen" durch WFP (DA1, Abb. 25). Fehler tritt nur bei Materialflüssen auf (DA3 bis DA6, DA9).
- Fn. 279 (S. 85) gibt GH1 in einer Variante mit Wirkfläche "des betrachteten Systems" und "eines benachbarten System".
- **Funktion als Zustandsänderung** (entspricht Zielen bei Vermaas). Beispiel Entformen, kein C&C-Modell möglich, weil sich Zustände auf verschiedene Zeitpunkte beziehen (S. 88 f.).
- **Passive Reaktion und Bauteilbeschreibung** ("Schlitten wird eingefahren", "Hubsauger") verschleiern Zusammenhänge (S. 89 bis 91).
- **Substantiviertes Verb ohne Zuordnung** ("Klemmung", "Körnen") beschreibt eher Effekte in einem WFP (S. 91 bis 93).
- **Aktionen des Nachbarsystems** und **C&C-Sequenzmodell** des Betonankers mit vier Zuständen (Loch bohren, Einführen, Anziehen, Betriebszustand), Problemhypothese schräg gebohrtes Loch (Abb. 31, S. 93 f.). Sequenzmodell nach Albers et al. 2008.
- **Zweck** ("wofür das System benötigt wird", Kettenbremse DA7, Bremsung innerhalb 100 ms), **Lösungsprinzipien**, **Alltagssprache** (S. 95 bis 97).

### 5.3 Einfluss der Vorgehensweise (S. 98 bis 103)
- Explizites Ziel der Modellbildung zu Beginn verhindert spätere Konflikte.
- Durchgängige C&C-Nutzung von Analyse bis Synthese (positiv DA7, Abb. 35 "Jedes WFP trägt zu mindestens zwei Funktionen bei", negativ DA4).
- Offene Frage "Wie tief muss man analysieren?" blieb in allen Projekten unbeantwortet (S. 101).
- Top-down-Aufbau statt Sammeln aller WFP/LSS (Abb. 31 vs. Abb. 36). **Regel 3 bis 5 Teilfunktionen** je Funktion, mehr als fünf ist Hinweis auf nötige Fokussierung (S. 103).

### 5.4 Funktion und Gestalt zuordnen (S. 104 bis 112)
- Funktion ohne Bezug zu WFP/LSS (Dieselinjektor DA9), **Vernachlässigung der LSS**, Funktion an einem einzelnen WFP.
- **Künstliche WFP** aus der technischen Mechanik (Schwerpunkt, Fliehkraft) sind falsch. Schwerkraft dagegen als WFP zum Gravitationsfeld modellierbar (Abb. 38, 39, S. 106 f.).
- **Funktionslogische Fehler**: System führt sich selbst ("Kolben führen" durch den Kolben), Funktion ohne erfüllendes Teilsystem ("Welle mit Nabe verbinden" beim zylindrischen Pressverband), geschlossenes System (Abb. 42) (S. 107 bis 110).
- **Mehrdeutigkeit** der Zuordnung in Teams (Betonanker mit oder ohne Messdose, Abb. 43). Konkrete Formulierung "Hülse im Beton festklemmen" führte schneller zu Konsens als "Axialkraft erzeugen und in Reibkraft umwandeln" (Tabelle 8, S. 112).

### 5.5 Unspezifische Faktoren (S. 112 bis 114)
- Vorbehalte gegen Methoden, Bedarf an Anleitung, Abbruch der Systematik bei Komplexität (nach Visser). Nach drei Diplomarbeiten Umstellung auf direkten Einstieg am realen Problem.

### 6.1 Experiment Axialkolbenpumpe (S. 115 bis 132)
- Untersuchtes System ist eine ölhydraulische **Axialkolbenmaschine** (als Motor oder Pumpe in geschlossenen Kreisläufen), Abb. 44.
- **Vergleichsmodell** (Alink und Ruckpaul, ohne Zeitlimit) auf Ebene der Hauptfunktion mit vier WFP zur Umgebung (WFP0.1 Keilwelle/Motor, WFP0.4 Montage, WFP0.2 und WFP0.3 Öl/Abtrieb bzw. Reservoir). **Das Öl ist Teil des betrachteten Systems**. Acht Teilfunktionen, insgesamt **47 Funktionen** (S. 116 f.).
- **Stichprobe** 20 Probanden (18 m, 2 w), Maschinenbauingenieure (19 KIT, 1 Hannover), 17 am KIT tätig, Berufserfahrung unter 1 bis 30 Jahre, meist 2 bis 5 Jahre. Zwei Hochschullehrer unterrichteten alle anderen in MKL und C&C-Ansatz (S. 117).
- **Ablauf** mit Leitung durch Eckert, Alink stiller Beobachter. Lautes Denken, Zeitlimit 1 h, DIN-A1-Papier, zwei Videokameras plus Ton. Gruppe 1 **physisches Modell (n = 11)**, Gruppe 2 **Wartungszeichnung (n = 9)**. Auftrag Funktionen mit C&C-M bestimmen und als Funktionenbaum ordnen (S. 118 bis 121).
- Auswertung zweistufig: quantitativ alle 20 (Tabelle 9), detailliert 8 Probanden mit vier Betrachtungsebenen (Überblick, Teilsystem, Teil-Teilsystem, Element) über der Zeit (Tabellen 10 bis 12, Abb. 51, 52).

### 6.2 Auffassungen von Funktion im Experiment (S. 132 bis 143)
- Selbstdefinitionen der Probanden in sechs Gruppen (Zweck, Flussgrößen, syntaktisch, Transformation, Eigenschaft, Andere) (Tabelle 13, S. 133). Wechsel der Auffassung erfolgte unbewusst.
- Flüsse von Material, Energie, Information wurden in keinem Datensatz als Funktionsbeschreibung angewandt (S. 134).
- Formulierung der Hauptfunktion 12-mal konkret, 6-mal abstrakt, 1-mal gemischt, 1-mal fehlend (Tabelle 14). 2 von 20 erkannten Nutzung als Motor.
- Zwei Formulierungstypen beim Sprechen: umgebungsgerichtete **Um-zu-Formulierungen** und systeminnere **Muss-Formulierungen** (S. 136 f.).
- **Quantität** Mittelwert 11,3 Funktionen (7,3 aufgeschrieben, 4 ausgesprochen), Median 6 bzw. 4, Spannweite aufgeschrieben 1 bis 17, ausgesprochen 0 bis 13 (S. 138). Berufserfahrung unter 2 J. (n = 5) sprechen mehr aus als sie schreiben, 2 bis 5 J. (n = 12) umgekehrt, über 5 J. (n = 3) schreiben fast alles auf (Abb. 56).
- Meist zwei bis drei Hierarchieebenen mit drei bis fünf Funktionen, nur ein Proband mit vier Ebenen (S. 140 f.).
- Im Abgleich mit dem Vergleichsmodell (Abb. 58) erscheint der Pumpmechanismus fast immer, Lagerung und Mittelzapfen oft vernachlässigt. Schmierung und Dichtung von 7 Probanden als Nebenfunktionen eingestuft. 4 Probanden nutzten ein Sequenzmodell (ansaugen, weiterfördern, ausstoßen) (S. 141 bis 143).

### 6.3 Vorgehensweisen (S. 144 bis 152)
- Vier Vorgehensweisen: Top-down (n = 4), Wichtigstes zuerst (n = 2), Opportunistisch, entlang Kraftfluss (n = 7). Für opportunistisch ergibt sich rechnerisch n = 7 (Einschätzung aus Abb. 62, Beschriftung im Textextrakt verschoben).
- Top-down erzeugte die meisten Funktionen und tiefsten Bäume (Abb. 62, 63).
- Funktions- versus komponentenorientierte Strukturierung. Wer Funktionen zuerst listet und später zuordnet, findet weniger Funktionen als wer den Baum direkt auf die Gestalt bezieht (S. 151).
- Zeitpunkt "System verstanden" ist subjektiv (S. 152).

### 6.4 Funktion und Gestalt zuordnen im Experiment (S. 152 bis 156)
- Mit physischem Modell zeichneten 10 von 11 Skizzen, mit Zeichnung nur 1 von 9 (S. 130 f.). Zuordnung meist über WFP ohne LSS.
- **Boxdarstellung** als Lehrdarstellung der MKL (Proband Nr. 2, Abb. 69): große Box Hauptfunktion, innere Boxen Teilfunktionen, Zeile für LSS mit Bauteilen in Klammern, WFP in Skizze rot eingezeichnet.
- 8 Probanden nummerierten WFP/LSS, 5 benannten WFP nach angrenzenden Bauteilen (S. 154).
- Von 8 Detailprobanden wendeten 3 den C&C-Ansatz wie in der Literatur an, 3 nur verbal. Proband Nr. 13 nutzte LSS als Schlangenlinien und WFP als Doppellinien, also ein schematisches Bauteilmodell, was Alink als falsches Verständnis wertet (S. 154 f.).

### 6.5 Unspezifische Faktoren (S. 156 f.)
- Prägung durch klassische Konstruktionsmethodik (abstrakt, lösungsneutral) und Vorfixierung.

### 7.1 Konzept von Funktion (S. 158 bis 167)
- Bestätigung von HP1 bis HP4 (S. 158 bis 160).
- **Konzept von Funktion** = Bedeutung, Darstellung, Formulierung (S. 161).
- **Bedeutungen** (S. 162 f.) sind Funktion als aktives Geschehen (Abgrenzung zum Ziel), Aktionen des Anwenders, Zweck (Wirkung auf die Umgebung), erwartetes Verhalten, tatsächliches Verhalten, physikalisch/chemische Effekte. Abgleich tatsächlich versus erwartet ist Motivation aller Entwicklung.
- **Darstellung** (S. 163 f.) als hierarchischer Funktionenbaum mit eingetragenen WFP und LSS (Abb. 71), prozedurale Darstellung als Flussgrößen, textuell mit Verweisen auf WFP/LSS. **Materialflüsse als eigenes Teilsystem** modellieren.
- **Formulierung** (S. 164 bis 166) richtet sich nach der Bedeutung. Zweck mit Um-zu, erwartetes Verhalten mit "mittels", Effekte als substantiviertes Verb ("Reibung"), Analyse konkret in Sätzen, Synthese abstrahiert (z. B. Verb-Nomen nach VDI 2223).
- **Funktion als Interaktion mit Nachbarsystemen (7.1.5, S. 167)** mit Beispiel Hydrauliköl der Axialkolbenpumpe "Die Vorwärtsbewegung des Kolbens zum Abtrieb leiten". Der Name des betrachteten Systems darf nicht Operand sein.

### 7.2 Verlauf der Problemlösung (S. 168 bis 178)
- Aktivitäten Übersicht behalten, Tiefe des Systemverständnisses (Abb. 72, 73 Aufwand versus Sicherheit), gemeinsames Verständnis, Aufgeben der Systematik, Lösungssuche.
- Lösungssuche beginnen, wenn gut begründete Hypothesen vorliegen und weitere Verifikation mehr kostet als die Implementierung (S. 172).
- Teamregeln (S. 173) sind Ziel gemeinsam klären, Betrachtungsraum über Hauptfunktion mit WFP/LSS festlegen, Hypothesen zu Abweichungen tatsächlich/erwartet den WFP/LSS zuordnen.
- **Tabelle 15 (S. 176 bis 178)** ordnet 12 Aktivitäten je Bedeutung, Darstellung und Formulierung zu (u. a. 1 Ziel klären, 2 Betrachtungsraum eingrenzen, 3 Funktion herausarbeiten, 4 Problem beschreiben, 5 Lösungen suchen, 6 Lösung darstellen, 7 Lösung bewerten, 8 Aktionen des Nachbarsystems, 9 lokales Geschehen, 10 keine Funktion erfüllt, 11 formales Modell, 12 Technik erklären). Spaltenzuordnung der Zeilen 6 bis 11 im Textextrakt teils unsicher.

### 7.3 Grundsätze für den C&C-Ansatz (S. 179 bis 189)
- **7.3.1** In jedem WFP findet wechselseitige Interaktion statt. Energie und Information werden ausgetauscht, Material ist gegenständlich und geht meist nicht durch ein WFP. Zwei Prüffragen zur Einordnung von Materialfluss (S. 179 f.). **Künstliche WFP** (Volumenstrom "hindurch", Schnitt durch LSS) vermeiden.
- **7.3.2** Studien beruhten auf GH2 "mindestens 2 WFP und eine sie verbindende LSS" (Albers et al. 2007), die keine Umgebung enthält (Abb. 74). Albers 2010 modifizierte zu "sie verbindende Leitstützstrukturen". Leitstützstrukturen der Umgebung werden **Connectoren** genannt, Symbol kreisförmig mit Verbindung zur Wirkfläche (Abb. 75, 76, S. 182). Connectoren liegen außerhalb des Gestaltungsraums, begrenzen das Modell und können bei Erweiterung zu LSS werden (S. 183). Beispiele Betonfestigkeit beim Betonanker, Einsatzort und Umgebungstemperatur der Pumpe.
- **7.3.3** Geschlossene Anordnungen ohne Umgebungsbezug (Pressverband, Betonanker, Energiespeicher, lokaler Kraftausgleich) heißen **"Mittel zum Zweck"** (Abb. 77, S. 184 f.). Ketten und Netze von Teilsystemen (Abb. 78). LSS ist nie mit Bauteil gleichzusetzen. **Systemgrenze** = Grenze des Gestaltungsraums, entspricht nicht zwingend einem WFP (S. 186 f.).
- **7.3.4** Synthese = Gestalt ändern bei gleichen Effekten oder neue Effekte mit gleicher Wirkung auf die Umgebung (S. 187).
- **7.3.5 Zusammenfassung der Grundsätze (S. 188 f.)**. Funktion = Interaktion mit Nachbarsystemen, Zweck und Verhalten unterscheiden, Funktion findet statt. Funktion nur erfüllt mit mindestens 2 WFP, mindestens einer verbindenden LSS und **mindestens zwei Connectoren** an die Umgebung. "Eine Leitstützstruktur verbindet genau zwei WFP." In einem WFP finden physikalische oder chemische Effekte statt. C&C-Ansatz ist **fraktal**, Anzahl der Betrachtungsebenen unbegrenzt. WFP und LSS können in mehrere WFP und LSS aufgeteilt werden.

### 8. Handlungsempfehlungen (S. 191 bis 197)
- Für Anwender die Bedeutungen nicht explizit unterscheiden. Stattdessen **konkrete Fragen je Aktivität** (Tabelle 16, S. 194 f.), z. B. "Wofür ist dieses System gemacht und durch welche WFP interagiert es mit seiner Umgebung?", "Welche 3-5 Teilfunktionen tragen zur Erfüllung der Hauptfunktion bei?", "Wann entsteht eine WFP und wann fällt eines weg?", "Was passiert in diesem WFP?".
- **Hypothesen, Maßnahmen, Fakten** (Abb. 80, S. 196 f., in Anlehnung an SPALTEN). Hypothesen, Maßnahmen und Fakten werden je WFP, LSS und "Anbindungen" abgelegt. Verifizierte Hypothesen werden Fakten. Nicht mehr als 5 Teilfunktionen je Betrachtungsebene.

### 9. Zusammenfassung (S. 198 bis 200)
- Wiederholung der Kernergebnisse. Studien betrafen vorrangig mechanische Systeme, Übertragung auf andere Bereiche ist offen.

### Anhang Vergleichsmodell der Pumpe (S. 211 bis 216)
- Englische Notation **WSP** (Working Surface Pair) und **CSS** (Channel and Support Structure). Umgebung als "CSS {Drive}", "CSS {Environment}", "CSS {Reservoir}", "CSS {Machine}".
- MF "Provide oil pressure", SF1 Drive pump, SF2 Sustain angularity, SF3 Pump oil, SF4 Separate suction and pressure side, SF5 Absorb operational forces, SF6 Lubrication of piston head, SF7 Lubrication of pump interior, dazu ein Sequenzmodell A/B mit State 1 bis 4.
- Flussgrößen an WSP annotiert (M, n; F{ax, rad}; Oil {V, p_low/p_high}; Info).
- CSS-Bezeichner verbinden teils vier WSP (z. B. CSS0.1/0.2/0.3/0.4).

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Funktion = Interaktion mit Nachbarsystemen, Operand darf nicht das System selbst sein (S. 167) | Prüfregel beim Formulieren: Warnung, wenn Funktionstext den Namen des eigenen Teilsystems als Objekt enthält ("Kolben führen" am Kolben) |
| Konzept von Funktion = Bedeutung, Darstellung, Formulierung (S. 161) | Datenmodell Funktion mit Attributen `bedeutung` (Zweck, erwartetes Verhalten, tatsächliches Verhalten, Aktion, Effekt, Mittel zum Zweck), `formulierung` (konkret/abstrakt), Freitext statt Verb-Nomen-Zwang |
| Grundsatz 2 WFP + mind. 1 LSS + mind. 2 Connectoren (S. 188) | Validierung je Funktion: Zähler WFP, LSS, Connectoren; Status "Mittel zum Zweck", wenn keine Umgebungsanbindung |
| Connector als eigenes Element außerhalb des Gestaltungsraums, kann zu LSS werden (S. 182 f.) | Elementtyp Connector mit Attributen Einflussgrößen, Randbedingungen (Streuung, Temperatur, Einsatzort); Aktion "in LSS umwandeln" bei Erweiterung der Systemgrenze |
| Benennung WFPx.y, LSSa/b nach verbundenen WFP (S. 47) | automatische ID-Vergabe nach Ebene und laufender Nummer, LSS-Name aus WFP-IDs, stabile IDs beim Ebenenwechsel |
| Materialfluss als eigenes Teilsystem, keine künstlichen WFP (S. 179 f.) | Assistent mit zwei Prüffragen; Fluid (Öl, Wasser) als Teilsystem anlegen statt als Fluss durch WFP |
| 3 bis 5 Teilfunktionen je Ebene (S. 103, 194) | Hinweis bei mehr als 5 Kindfunktionen, Zoom-Vorschlag |
| Fragenkatalog je Aktivität (Tabelle 16) | geführter Workflow mit Fragen statt Bedeutungsauswahl, Aktivitätsstatus pro Modell |
| Hypothesen, Maßnahmen, Fakten an WFP/LSS (S. 196 f.) | Objekt Hypothese mit Status (offen, Maßnahme, verifiziert = Fakt), Verknüpfung zu Elementen, Kennzeichnung schwer zuordenbarer Hypothesen |
| Sequenzmodell mit Zuständen und Frage "Wann entsteht ein WFP?" (S. 93, 194) | Zeitachse von Zuständen je Modell, WFP/LSS mit Gültigkeit pro Zustand, Aktionen des Nachbarsystems als Zustände |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Diss., Basisdefinition und Erstfassung der Grundhypothesen), Albers & Matthiesen 2002 (Konstruktion, Elementmodell), Albers, Matthiesen & Ohmer 2003, 2003b, 2003c (Evaluation, ICED03), Albers, Burkardt & Ohmer 2004, 2004b, 2005 (Paarcharakter der Wirkflächen, Prinzipien), Eckert, Albers & Ohmer 2004b (kognitive Perspektive), Albers & Meboldt 2005 (SPALTEN), Albers & Alink 2007 (CIRP Design Seminar), Albers, Alink & Oerding 2007c (Benennung WFP/LSS), Albers, Alink, Thau & Matthiesen 2008 (TMCE, temporal decomposition, Sequenzmodell) und 2008b (Design 2008, Leitfaden), Albers, Alink & Deigendesch 2008c (Design 2008, Problemlösen), Albers, Alink & Oerding 2010 (Ziele und C&CM), Albers 2010 (TMCE "Five Hypothesis about Product Engineering", modifizierte GH2), Albers, Enkler & Ottnad 2009b (generalisierter C&C-Ansatz), Keller et al. 2007 (Änderungsfortpflanzung), Ohmer 2008 (Diss., Synthese), Alink, Eckert, Ruckpaul & Albers 2010 (DCC, Pumpenexperiment), Eckert, Alink & Albers 2010 (Issue driven analysis), Vermaas 2009, 2010 (Funktionsbedeutungen).
