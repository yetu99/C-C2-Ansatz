# Matthiesen et al. 2018: Modellbildung mit dem C&C²-Ansatz in der Gestaltung

| Feld | Wert |
|---|---|
| Autoren | S. Matthiesen, P. Grauberger, K. Hölz, T. Nelius, F. Bremer, A. Wettstein, A. Gessinger, B. Pflegler, K. Nowoseltschenko, K. Voß |
| Titel | Modellbildung mit dem C&C²-Ansatz in der Gestaltung: Techniken zur Analyse und Synthese |
| Reihe | KIT Scientific Working Papers, Band 58, IPEK, Karlsruhe |
| Jahr | 2018 |
| ISSN | 2194-1629 |
| Lizenz | CC BY-SA 4.0 |
| Volltext | [`../volltexte/Matthiesen2018_KIT-SWP58_Modellbildung-CC2.pdf`](../volltexte/Matthiesen2018_KIT-SWP58_Modellbildung-CC2.pdf) (22 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Gestaltung ist ein iteratives Wechselspiel aus **Analyse** und **Synthese**. Zentral ist ein (meist implizites) **Modell des Gestalt-Funktion-Zusammenhangs**. Der C&C²-Ansatz macht dieses Modell explizit, prüfbar und nutzbar.

## Inhalte nach Abschnitt

### 1. Einordnung der Gestaltung (S. 1 bis 3)
- Gestaltung nach VDI 2221-1:2018 als iterativer Prozess: Ziele (Entwicklungsauftrag, Anforderungen) → Aktivitäten → Ergebnisse (Gestaltdokumentation des herstellbaren Produkts).
- Zentrale Eingangsgrößen: Erfahrung mit verwandten Produkten, Gestaltdokumentation von Vorgänger- und Referenzprodukten (Bezug zur Produktgenerationsentwicklung PGE).
- **Risikomatrix (Abb. 2)** mit zwei Achsen:
  - Gestaltdokumentation: dokumentiert / nicht dokumentiert
  - Bekanntheit Gestalt-Funktion-Zusammenhang: unbekannt / implizit bekannt / explizit dokumentiert
  - Ohne Gestaltdokumentation ist das Risiko immer hoch (Cluster 4). Mit Dokumentation sinkt das Risiko, je expliziter der Gestalt-Funktion-Zusammenhang bekannt ist.
- Funktionserfüllung hängt von **konstruktiven Details** ab (Beispiel Winkelschleifer, Abb. 3).

### 2. Fallbeispiel Bolzensetzgerät (S. 4 bis 6)
- Neue Produktgeneration, Teilsystem "Schiebernase" der Repetiereinheit bricht.
- Analyse: Beobachtung des Systemverhaltens, Kräfte erzeugen ungünstigen Kraftfluss.
- Synthese: Optimierung des Kraftflusses in der neuen Gestalt, danach erneute Analyse.

### 3. Modellbildung mit dem C&C²-Ansatz (S. 7 bis 9)
- **Kernelemente:** Wirkflächenpaar (WFP), Leitstützstruktur (LSS), Connector (C).
- **Nebenelemente:** Wirkfläche (WF), Reststruktur (RS), Begrenzungsfläche (BF).
- **Strukturelemente:** Tragstruktur (TS), Wirknetz, Wirkstruktur.
- **Wirknetz** = Summe der Elemente eines C&C²-Modells, gültig für **einen** Systemzustand.
- **Wirkstruktur** = Summe der Wirknetze über alle betrachteten Zustände.
- Grundhypothesen beschreiben die Anwendung (Details siehe [`01_grundlagen/elemente_und_grundhypothesen.md`](../../01_grundlagen/elemente_und_grundhypothesen.md)).
- **Bestandteile eines C&C²-Modells (Abb. 13):** Modellzweck, Systemabbild, Systemgrenzen, Gestaltfunktionselemente, funktionsrelevante Gestaltparameter.
- **Vorgehen Modellbildung in der Analyse (Abb. 14), Schritte a bis g:**
  1. Modellzweck festlegen und dokumentieren
  2. geeignete Visualisierung (Systemabbild) für den Zweck finden
  3. Systemgrenzen definieren: zeitlich (Systemzustände) und räumlich (Teilsysteme)
  4. Fluss der Systemgrößen (Energie, Stoff, Information) verfolgen
  5. Gestaltfunktionselemente (WFP, LSS, C) im Systemabbild darstellen
  6. funktionsrelevante Gestaltparameter identifizieren
  7. Modell verifizieren
- Anschließend Synthese auf Basis des Modells (Abb. 15).

### 4. Analyse technischer Systeme (S. 10 bis 14)
- Gestaltparameter von **Produkt und Umwelt** erfassen.
- **Qualitative Analysemethoden** (Beobachtung realen Verhaltens) plus **Quantifizierung im Versuch**.
- **Ideal vs. real (Abb. 17, nach Lemburg 2009):** WFP im Idealzustand, verkleinert durch Fertigungsabweichung, verschoben durch Verschleiß. Modellbildung nur am Idealzustand verpasst reales Systemverhalten.
- Fallbeispiel Schnellbauschraube → spanlose Blechbohrschraube:
  - Initiales Modell: WFP1 (Werkstück-Schraube), WFP2 (Schraube-Bit), LSS1-2, C1 (Einspannung, Wandsteifigkeit), C2 (Axialkraft Benutzer, Drehmoment Schrauber).
  - **Technik Zoom-In:** Detaillierungsgrad an einem WFP erhöhen (Schraubenspitze-Blech).
  - **Technik Shift:** Fokus entlang des Wirknetzes verschieben (WFP1 → WFP2 Schraubenkopf-Bit), räumliche Systemgrenze dabei erweitert.
  - **C&C²-Sequenzmodell:** verknüpft Zustände während der Funktionserfüllung (nach Thau 2013).
- Beobachtbarkeit ist eingeschränkt: Hilfsmittel wie **Spannungsoptik** (Beispiel Kunststoffdübel).
- **Entwicklungsprüfstände** als Analyseumgebung, z. B. Roboter mit wirkungsäquivalentem Hand-Arm-System für Power-Tools.

### 5. Modellverifikation (S. 15 bis 16)
- Beispiel Nageldetektion: Hypothese "Kräfte aus Hauptfunktion" falsifiziert, Verschleißspuren stützen Hypothese "Trägheit aus Rückstoß".
- **Konstruktionshypothesen** (KIT SWP 61): einstellbarer Gestaltparameter ↔ messbare Funktion, im Experiment prüfbar.
- Beispiel: Gewindehöhe vs. Eindrehzeit bei der Schnellbauschraube.

### 6. Synthese (S. 16)
- **Drei Syntheseprinzipien** (nach Ohmer 2008, Albers et al. 2005):
  1. WFP und/oder LSS hinzufügen
  2. WFP und/oder LSS entfernen
  3. Eigenschaften von WFP/LSS ändern
- Ergebnis im Beispiel: Patent US 8,342,788 "Chipless thread-forming screw".

### 7. Ausblick Lehre (S. 17)
- Einsatz in KIT-Lehrveranstaltungen "Mechatronische Systeme und Produkte" und "Maschinenkonstruktionslehre" mit Bereitstellung von Produktdokumentation.
- Vermittlung an Lehramtsstudierende NwT ("Technik erleben und vermitteln").

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Modellzweck als Pflichtangabe | Pflichtfeld beim Anlegen eines Modells |
| Schritte a bis g | geführter Wizard / Checkliste |
| Zeitliche und räumliche Systemgrenze | Zustandsliste + Teilsystemauswahl |
| Wirknetz pro Zustand, Wirkstruktur über Zustände | Datenmodell: Modell → Zustände → Elemente |
| Zoom-In, Shift | Navigation: Detailebene je WFP, Fokuswechsel entlang Verbindungen |
| Ideal vs. real (Fertigung, Verschleiß) | Variantenattribut je WFP (ideal / gefertigt / verschlissen) |
| Konstruktionshypothesen | Hypothesen-Objekt: Gestaltparameter, Funktionsgröße, Messmethode, Ergebnis |
| Syntheseprinzipien | Ideengenerator: hinzufügen / entfernen / ändern je Element |

## Im Paper zitierte Schlüsselquellen (für Literaturliste)
Matthiesen 2002 (Diss., Basisdefinition), Albers & Wintergerst 2014 (Anthology), Matthiesen/Hölz/Grauberger 2017 (DfX, Analysemethoden), Lemburg 2009 (Diss. RWTH), Albers et al. 2008 (KT2008, Sequenzmodell), Thau 2013 (Diss., Heuristiken), Matthiesen et al. 2017 (SWP 61, Konstruktionshypothesen), Ohmer 2008 (Diss., Synthese), Albers et al. 2005 (Ilmenau, Denkmodell), Matthiesen 2011 (ICED, thinking tools).
