# Matthiesen, Grauberger, Schrempp 2019: Erweitertes C&C²-Sequenzmodell

| Feld | Wert |
|---|---|
| Autoren | Sven Matthiesen, Patric Grauberger, Lukas Schrempp |
| Titel | Extended Sequence Modelling in Design Engineering: Gaining and Documenting Knowledge about Embodiment Function Relations with the C&C²-Approach |
| Quelle/Reihe | Proceedings of the 22nd International Conference on Engineering Design (ICED19), Delft, 5. bis 8.08.2019, S. 1483 bis 1492 (Cambridge University Press) |
| Jahr | 2019 |
| DOI | 10.1017/dsi.2019.154 |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Matthiesen2019b), nicht im Repo (Lizenz) (10 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Das klassische C&C²-Sequenzmodell wird unübersichtlich, sobald Gestalt-Funktion-Zusammenhänge (EFR) in verschiedenen Zuständen **und** Detailstufen **und** Orten betrachtet werden. Das Paper gibt dem Sequenzmodell eine **Struktur mit vier Dimensionen**: **logischer Zustand** (übergeordnet) sowie innerhalb eines logischen Zustands ein **3D-Koordinatensystem** aus **Systemzustand**, **Detaillierungsgrad** und **Ort der Funktionserfüllung**. Jedes Einzelmodell erhält **Metadaten** zu seiner Position, aus denen sich **Ansichten** filtern lassen. Angewandt an einem Schiebedach (131 Modelle) und einem Klemmrollenfreilauf.

## Inhalte nach Abschnitt

### 1. Einleitung (S. 1483 bis 1485)
- Explizite Modelle: ausführbar-analytisch (FEM, MKS) und nicht ausführbar (CPM, FBS, Organ Domain, C&C²-M). Analytische Modelle erst ab parametrisierter Gestalt verfügbar.
- Zustandswechsel während der Funktionserfüllung erzeugen entstehende und verschwindende EFR. SysML-Sequenzdiagramme bilden Zustände ab, aber ohne Gestalt.
- Das bestehende **C&C²-Sequenzmodell (Albers et al. 2008)** stößt an strukturelle Grenzen, wenn EFR auf verschiedenen Detailstufen in verschiedenen Zuständen nötig sind.
- Forschungsfrage: Welche Struktur braucht ein EFR-Modell, um Erkenntnisgewinn in komplizierten Systemen zu unterstützen?

### 2. Grundlagen (S. 1485 bis 1487)
- **C&C²-Ansatz** als Denkzeug und Metamodell mit **drei Kernelementen** (WSP, CSS, C) und **drei Grundhypothesen** (S. 1485, nach Matthiesen 2002 und Matthiesen et al. 2018):
  - GH1: Funktion braucht Wechselwirkung über WSP.
  - GH2: Funktion über mindestens zwei WSP, verbunden durch eine CSS und durch Connectoren in die Umgebung eingebunden.
  - GH3: fraktaler Charakter, Modelle unterscheiden sich nach Sichtweise und Zweck.
- WSP = Schnittstelle, an der Systemteile während der Funktionserfüllung in Kontakt sind; CSS verläuft durch Systemteile und verbindet die WSP, kann Bauteilteile oder ganze Teilsysteme umfassen; Connector setzt die **Systemgrenze** und überträgt Einflüsse von außen (nach Albers und Wintergerst 2014).
- Parameter: z. B. **Reibwert als Parameter eines WSP**, **Steifigkeit als Parameter einer CSS** (S. 1485).
- **Zustand** (S. 1486): "an arbitrarily long time span in which the amount and properties of the key elements of the C&C²-Approach can be seen as constant". **Sequenz** = Verknüpfung von mindestens zwei Zuständen. Beispiel Schrauber und Schraube mit vier Zuständen, Zustand 3 mit vier Unterzuständen (Abb. 2 nach Thau 2013).
- **Kammstruktur (comb-approach)** von Thau 2013 für Sequenzen an verschiedenen Orten: schwer anwendbar, in der Literatur nicht weiter genutzt.
- **Logische Zustände** (S. 1486 bis 1487, Abb. 3 nach Matthiesen und Ruckpaul 2012): für Systeme ohne feste Chronologie (Auslöser, Trigger), Beispiel Sicherheitsschalter eines Power-Tools; Übersichtsebene ohne Gestalt, Detailebene mit Kernelementen.

### 3. Struktur des Sequenzmodells (S. 1487 bis 1489, Abb. 4 bis 6)
- **Vier Dimensionen:**
  1. **Logischer Zustand (logical state):** übergeordnete Dimension; mögliches Systemverhalten abhängig von internen oder externen Auslösern. Verbindet die Koordinatensysteme.
  2. **Systemzustand (state of the system):** Achse im 3D-Koordinatensystem eines logischen Zustands; zentrale Dimension des bisherigen Sequenzmodells.
  3. **Detaillierungsgrad (level of detail):** Achse, abgeleitet aus GH3 (fraktaler Charakter).
  4. **Ort der Funktionserfüllung (location of function fulfilment):** dritte Achse, für die Anpassung der Systemgrenze.
- Jedes C&C²-Modell erhält **Metadaten** zu seiner Position; Quadrate im Koordinatensystem stehen für Einzelmodelle; Icons zeigen die Metadaten.
- **Abgeleitete Ansichten:** Schnitt an einem Ort über mehrere Zustände (Zahnradpaar, Kraftfluss wechselt von WSP1.1 zu WSP1.2 beim nächsten Zahneingriff, Abb. 5) oder Schnitt in einem Zustand über mehrere Orte (Zahnrad und zwei Lager, Abb. 6).

### 4. Anwendung (S. 1489 bis 1491)
- **Schiebedach (Industrie):** Ursachen unerwünschten Verhaltens; **131 C&C²-Modelle**, **12 Orte der Funktionserfüllung**; am ersten Ort spaltet sich Detailstufe 0 in sechs Zustände auf Detailstufe 1, einer davon in vier auf Detailstufe 2. Weitere **vier logische Zustände** bei abgeschaltetem Motor und äußeren Lasten. Befund über **Verschleißspuren**: Kraft geht zeitweise in den Antriebsschlitten (Abb. 8). Ergebnisvorstellung im Meilensteintermin, Experten bewerteten in **etwa 2 h**.
- **Doppelt sperrender Klemmrollenfreilauf (Hochschulprojekt):** Prototyp aus lasergeschnittenen Platten; unbestimmte Rollenlage als Trigger; WSP3 (Rolle schleift am Außenring) als vermutete Ursache für Reibverluste; **Konstruktionshypothese** (Matthiesen et al. 2017) getestet, durch Parameteränderung an WSP1 tritt WSP3 nicht mehr auf; insgesamt **sechs Konstruktionshypothesen** getestet.

### 5. Diskussion und Ausblick (S. 1491 bis 1492)
- Die vier Dimensionen erlauben, alle erstellten EFR-Modelle einzuordnen; Kommunikation wird unterstützt.
- Grenzen: nur mechanische Aspekte; **Dimensionen für elektrische oder hydraulische Systeme nicht untersucht**; nur erfahrene Modellierer; Nutzbarkeit für Unerfahrene offen.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Vier Dimensionen als Metadaten jedes Einzelmodells | Datenmodell: `Modell { logischer_zustand, systemzustand, detailstufe, ort }` als Pflichtkoordinaten |
| Logischer Zustand mit Trigger | Zustandsautomat-Ansicht (Übersichtsebene ohne Gestalt) mit Triggerbedingungen |
| 3D-Koordinatensystem je logischem Zustand | Navigationsmatrix: Zeilen Orte, Spalten Zustände, Ebenen Detailstufen; Klick öffnet Einzelmodell |
| Abgeleitete Ansichten (Schnitt nach Ort oder Zustand) | Filter- und Vergleichsansichten, nebeneinander gestellte Einzelmodelle |
| Zustand = Zeitspanne mit konstanten Elementen | Automatischer Vorschlag eines neuen Zustands, wenn sich Elementmenge oder Attribut ändert |
| 131 Modelle im Industrieprojekt | Skalierung: Modelle müssen gruppierbar, priorisierbar und durchsuchbar sein |
| Verschleißspuren als Evidenz | Fotoevidenz je Befund, verknüpft mit Element und Zustand |
| Konstruktionshypothesen im Freilaufprojekt | Hypothesenobjekt verknüpft mit Element, Zustand und Prüfergebnis |
| Hydraulische Systeme nicht untersucht | Offene Forschungsfrage für Wasser/Energie: eigene Dimensionen prüfen (z. B. Betriebspunkt) |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002, Albers und Wintergerst 2014, Matthiesen et al. 2018 (SWP 58), Albers et al. 2008 (Sequenzmodell), Thau 2013 (Kammstruktur), Matthiesen und Ruckpaul 2012 (logische Zustände), Matthiesen et al. 2017 (Konstruktionshypothesen), Matthiesen 2011 (ICED, mentale Modelle).
