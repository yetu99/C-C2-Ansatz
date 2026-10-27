# Albers, Wintergerst 2014: The Contact and Channel Approach (C&C²-A)

| Feld | Wert |
|---|---|
| Autoren | Albert Albers, Eike Wintergerst |
| Titel | The Contact and Channel Approach (C&C²-A): Relating a System's Physical Structure to Its Functionality |
| Quelle/Reihe | Chakrabarti, A.; Blessing, L. T. M. (Hrsg.): An Anthology of Theories and Models of Design, Springer-Verlag London 2014, Kap. 8, S. 151 bis 171 |
| Jahr | 2014 |
| DOI | 10.1007/978-1-4471-6338-1_8 |
| Lizenz | im PDF nicht angegeben (Springer-Verlag London) |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2014, ganzes Buch), nicht im Repo (Lizenz) (Kapitel 21 S., Buch PDF-S. 157 bis 177) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Kanonische englische Darstellung: Funktionen entstehen nur aus **Wechselwirkungen** zwischen Komponenten bzw. mit der Umgebung, und ihre **Qualität** hängt von den **Gestaltmerkmalen** der beteiligten Schnittstellen (WSP) und Strukturen (CSS) ab. Elemente werden als **Wirk-Net** je Funktion und Betriebsmodus und als **Wirk-Structure** über alle Wirk-Nets organisiert, **Connectoren** bilden die relevante Umgebung samt "Wirkung" ab. Das Kapitel liefert **Praxisleitlinien (Tab. 8.1)**, nennt die **drei Grundoperationen** der Synthese und benennt fehlende **Werkzeugunterstützung** und **Quantifizierung** als Hauptgrenzen.

## Inhalte nach Abschnitt

### 8.1 Einleitung (S. 151)
- Herausforderung: erklären und effizient beschreiben, wie die Qualität technischer Funktionen von der Gestaltung physischer Merkmale abhängt.

### 8.2 Analyse und Synthese (S. 152 bis 153)
- Mehrheit der Projekte ist **Produktgenerationsentwicklung** (Optimierung bestehender Produkte).
- Konstrukteure arbeiten auch früh mit Bauteilgeometrie; bei Analysen sind sie mit realitätsnahen Darstellungen sicherer.
- Produktmodelle dienen Analyse (Information zugänglich machen) und Synthese (Konzepte und Entscheidungen ausdrücken).

### 8.3 Funktionen in Forschung und Praxis (S. 153 bis 157)
- Praxis: Teilfunktionen bleiben meist mental, nicht dokumentiert, ohne Bezug zur Gestalt (Matthiesen 2011: keine eindeutige Funktionsstruktur in den untersuchten Firmen).
- Bezug zu CPM (Weber), Axiomatic Design, DSM (Lindemann), lösungsneutralen Funktionsstrukturen.
- Viele Funktionsbegriffe (Erden: 18); Funktionen sollen sich auf zweckgerichtete Wechselwirkungen von Systemen und Umgebung beziehen.
- Abstrakte Modelle passen schlecht zum intuitiven Denken; meist wird auf bestehenden Lösungen aufgebaut. Forderung nach integrierter qualitativer und quantitativer Beschreibung.

### 8.4 Integrierter Ansatz (S. 157 bis 165)
- Grundlage: Systemtheorie, Rodenacker, Roth, Hubka (Wirkflächen, Wirkvolumen).
- **Anwendungsbereich (S. 158):** Analyse (Funktionen und ihre physischen Strukturen erkennen, relevante Gestaltmerkmale identifizieren), Synthese (Merkmale optimieren, Wirk-Structure erweitern oder reduzieren), **Dokumentation und Kommunikation** (Funktionswissen speichern und abrufen).
- Forschungshypothese: Austausch von Ein- und Ausgangsgrößen findet in Schnittstellen und verbindenden Strukturen statt; deren Gestaltmerkmale bestimmen die Funktionsqualität.
- C&C-Modelle bauen auf **konkreten Darstellungen** auf: Zeichnungen, Skizzen, **Screenshots aus 2D- oder 3D-Modellen** (S. 158).
- Eine Komponente allein erfüllt keine Funktion; Merkmalsänderungen durch Verschleiß, Fertigungsabweichungen, Einflüsse im Einsatz.
- **Elemente des Wirk-Net (S. 160):**
  - CSS: "permanently or occasionally interacting physical structures of solid bodies, liquids, gases or fields" (keine Anzahl verbundener WSP in dieser Definition).
  - WSP: Schnittstellen zwischen diesen Strukturen.
  - Connector: repräsentiert die "Wirkung" und die Zustandseigenschaften der für die Funktion relevanten Umgebung; Fußnote verweist auf XiL-Framework (Straße, Umwelt, Fahrer, Restantriebsstrang).
- **Minimalkonfiguration (Abb. 8.1, Schraube in Wand):** mindestens zwei Wirkflächen, verbunden durch eine CSS, je an einen Connector gekoppelt; jeder Connector enthält ein Umgebungsmodell und eine Wirkfläche.
- **Wirk-Net** je Funktion und Betriebsmodus; **Wirk-Structure** = Zusammensetzung aller Wirk-Nets (S. 160 bis 161). Beispiel Hybridantrieb mit Betriebsmodi Rekuperation, elektrisch, Verbrenner, Boost (Abb. 8.2); Lamellenkupplung, Schraube, Software mit mehreren CPUs.
- Weitere Elemente **Limiting Surfaces (LS)** und **Remaining Structures (RS)** ohne Funktionsbeitrag, aber durch Randbedingungen nötig (S. 161).
- Alle Elemente **fraktal** (Abb. 8.3, Lamellenkupplung).
- **Leitlinien (S. 163, Tab. 8.1, S. 164):** Hauptfunktion mit mindestens zwei Connectoren beschreibbar; Top-down-Vorgehen; bei Unerklärtem Umgebung erweitern, abstrahieren oder zu anderem **Zeit- oder logischen Zustand** wechseln; unsichere Annahmen als **Hypothesen** mit Prüfmaßnahmen festhalten.
- **Tab. 8.1 Phasen:** Vorbereitung (Modellzweck, Darstellung), Problemklärung und Zielspezifikation (Fokus in Zeit und Raum, Funktionen und Eigenschaften, Wirk-Nets inkl. Connectoren, Verknüpfung über Zeit- und logische Zustände, Wechsel qualitativ zu quantitativ), Gestaltspezifikation (änderbare Merkmale wählen, neue WSP und CSS einführen, Wirkung von Variationen mit QFD, DSM, DoE, FMEA bestimmen, Maßnahmen ableiten und validieren mit Skizzen, CAD, Prototypen).
- Ziel: kleinste Menge an Gestaltmerkmalen mit größter Wirkung auf die Funktionsqualität.
- **Beispiel Lamellenkupplung (Abb. 8.4, S. 165):** WSP an Reibflächen, Wechsel Stahl zu Keramik, Wärmeübergang ins Öl (Connector C_Oil), Ölalterung als Nebenwirkung; spezifische Reibleistung um **über 100 %** verbessert (nach Ref. [32]).

### 8.5 Studien und Ergebnisse (S. 166 bis 168)
- **Über 20** veröffentlichte und unveröffentlichte empirische Studien in der Praxis; Hauptanwendung ist die **Analyse von Gestaltungsproblemen** an Produkten.
- Lehre: Fähigkeit, technische Systeme zu verstehen, "considerably increased" seit Einführung (ohne Zahlen).
- Anwendungen: Tribologie Lamellenkupplung, Mikrosysteme, Fehlermodi Power-Tool über logische Funktionszustände.
- **Stärken (S. 167):** wenige Elemente (WS, WSP, CSS, Connector); Hypothese, dass jede Gestalt über **drei Grundoperationen** angepasst werden kann: "integration or elimination of Working Surface Pairs or Channel and Support Structures as well as modification of their design characteristics".
- **Grenzen (S. 167 bis 168):** analoge Modelle sind Momentaufnahmen, nicht konsistent prüfbar, kein Ein- und Ausblenden, keine globale Ablage; digitale Medien könnten Konsistenz sichern und Sichten aus einem gemeinsamen Datensatz ableiten (z. B. parametrisches CAD). Bisher nur isolierte, wenig ausgereifte Software; künftig Integration in gängige Werkzeuge wie **CAD**. Forschungsbedarf **Quantifizierung**.

### 8.6 Zusammenfassung (S. 169)
- Integrierte Modellierung von Funktion und physischer Beschreibung als gemeinsame Sprache; Schwerpunkte künftig Werkzeugunterstützung und quantitative Modellierung.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Modelle auf Skizzen, Zeichnungen, CAD-Screenshots | Bild-Upload als Systemabbild, Elemente direkt einzeichnen |
| Wirk-Net je Funktion und Betriebsmodus, Wirk-Structure gesamt | Datenmodell: Funktion × Betriebsmodus → Wirknetz; Gesamtansicht als Überlagerung |
| Betriebsmodi (Hybridantrieb) | Für Wasser/Energie: Betriebspunkte (Teillast, Volllast, Anfahren, Störfall) als Zustände |
| Connector mit Umgebungsmodell und "Wirkung" | Connector-Objekt mit Feldern für Umgebungsgrößen (Druck, Drehzahl, Temperatur) |
| LS und RS | Optionale Elementtypen, z. B. für Leichtbau- oder Fertigungsentscheidungen |
| Tab. 8.1 Leitlinien | Phasenstruktur im Workflow mit Methodenhinweisen (QFD, DSM, DoE, FMEA) |
| Hypothesen bei unsicheren Ursache-Wirkungs-Annahmen | Hypothesenregister mit Prüfmaßnahme |
| Drei Grundoperationen der Synthese | Variantenassistent: hinzufügen, entfernen, Merkmal ändern, jeweils begründet dokumentiert |
| Grenzen analoger Modelle | Kernargumente für das Tool: Konsistenz, Sichten, Ablage, Teamarbeit |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2011 (ICED, thinking tools), Eckert, Alink, Albers 2010 (DESIGN, Analyse auf Abstraktionsebenen), Eckert et al. 2011 (JED, Funktionsbegriffe), Albers et al. 2011 (Ref. [25], Software-Tool, J Mech Des), Albers et al. 2008 (Ref. [26], DESIGN 2008, Industrieanwendung), Matthiesen und Ruckpaul 2012 (Ref. [34], DESIGN 2012, logische Zustände), Albers, Bernhardt, Ott 2011 (Ref. [32], Lamellenkupplung Keramik), Koller 1994, Roth 1994, Weber 2008 (CPM), Suh 1998, Lindemann und Deubzer 2009.
