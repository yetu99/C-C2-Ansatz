# Prager et al. 2024: Der C&C²-Ansatz als Denkwerkzeug in mechatronischen Systemen

| Feld | Wert |
|---|---|
| Autoren | Felix Prager, Peter M. Tröster, Albert Albers (KIT) |
| Titel | The C&C² Approach as a Thinking Tool in Mechatronic Systems |
| Quelle/Reihe | Procedia CIRP 128 (2024), S. 704 bis 709; 34th CIRP Design Conference |
| Jahr | 2024 |
| DOI | 10.1016/j.procir.2024.04.020 |
| Lizenz | CC BY-NC-ND 4.0 |
| Volltext | [`../volltexte/Prager2024.pdf`](../volltexte/Prager2024.pdf) (6 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Das Paper überträgt Prinzipien der **Bondgraphentheorie (bond graph theory)** auf den C&C²-Ansatz, um ihn domänenübergreifend (mechatronisch) nutzbar zu machen. Dafür werden nur zwei Erweiterungen der Kernelemente eingeführt: der **Quellen-Connector (source Connector)** zur Kennzeichnung des Ursprungs und damit der Richtung des **Energieflusses** sowie die Unterscheidung **statischer und dynamischer Leitstützstrukturen (static/dynamic CSS)**. Daraus folgen **Zuordnungsregeln** von C&C²-Elementen zu Bondgraph-Elementen (WSP → Junction oder Wandler, dynamische CSS → R, I oder C, Quellen-Connector → Quelle), sodass aus einem C&C²-Modell ein simulierbares mathematisches Modell abgeleitet werden kann (Beispiel Tiefpass 2. Ordnung).

## Inhalte nach Abschnitt

### 1. Introduction (S. 704)
- Zunehmende Elektrifizierung und Digitalisierung rein mechanischer Produkte erfordert angepasste Methoden.
- C&C²-Ansatz als Werkzeug zur Visualisierung von **Gestalt-Funktion-Zusammenhängen (embodiment function relations, EFR)**; bisher fast ausschließlich auf mechanische Probleme angewendet (nach Grauberger et al. 2020).
- C&C² ist rein grafisch-beschreibend, Bondgraphen sind eine mathematische Modellierungsmethode. Ziel: Simulation möglichst früh durch Ableitung eines Bondgraphen aus dem C&C²-Modell.

### 2. Methodology and Research Questions (S. 704 bis 705)
- Vergleich mit Referenzmodellen: gleichungsbasierte Methoden (z. B. Blockschaltbild der Regelungstechnik) bilden Gleichungen ab, keine physikalischen Effekte, daher inkompatibel mit C&C².
- Multipolbasierte Modelle (Bondgraphen, Kirchhoff-Netzwerke) passen; Wahl fiel auf die domänenneutrale Bondgraphentheorie, da Kirchhoff-Netzwerke nur für Elektrotechniker attraktiv seien.
- RQ1: Wie lässt sich der C&C²-Ansatz auf mechatronische Domänen anwenden? RQ2: Wie lässt sich ein mathematisches Modell aus einem C&C²-Modell für die Simulation ableiten?

### 3. State of the Art (S. 705 bis 706)
- **3.1 C&C²-Ansatz:** Kernelemente WSP, CSS, Connector (Fig. 1 nach Matthiesen et al. 2018, Procedia CIRP 70); Regelwerk über die drei Grundhypothesen (nur in Fig. 1 genannt, nicht im Text ausformuliert).
- Definitionen (nach Matthiesen 2002 bzw. Alink 2010, Albers & Wintergerst 2014) mit Flächen- und Volumenelement, CSS verbindet "exactly two" WSP (wörtlich im Befund).
- Connector: integriert Einflüsse außerhalb des Gestaltungsbereichs, hat eine repräsentative Wirkfläche, liegt im Betrachtungsbereich, nicht im Gestaltungsbereich.
- Weitere Grundlagen aus Matthiesen 2002: C&C² beruht auf Kausalität, die Schnittstelle zwischen Ursache und Wirkung bildet das WSP; CSS sind die **energiespeichernden Elemente**; bei ausreichend weiter Systemgrenze ergibt sich ein geschlossener Wirkungskreis, wodurch der physikalische Zustandsbegriff integrierbar wird.
- **3.2 Bondgraphen:** 1959 veröffentlicht; Leistungsbindung (power bond) als gerichteter Halbpfeil, Leistung P = e · f aus Effort- und Flow-Variable (Fig. 2); Standardelemente R, I, C; zusätzlich Quellen (Effort- oder Flow-Quelle) und Wandler (Zweitor); 1-Junction (Reihe, gleicher Flow) und 0-Junction (parallel, gleicher Effort) (Fig. 3); Bondgraph muss kausalisiert werden (20-sim, Dymola erledigen das automatisch).
- **3.3 Fallstudie Tiefpass 2. Ordnung:** zusätzliche Induktivität in Reihe zum Widerstand, steilere Dämpfung oberhalb der Grenzfrequenz (Fig. 4, intuitiver Bondgraph).

### 4.1 Thinking Tool for Mechatronic Systems (S. 706 bis 707)
- Ziel: Unterscheidung zwischen Leistungsübertragung, die eine Funktion erfüllt, und Datenübertragung, die eine Funktion nur vorgibt.
- Illustrationsbeispiel **Schraubverbindung** nach Matthiesen (Pahl/Beitz 2021), Fig. 5 (a) Eindrehen, (b) Zugbelastung.
- **Erweiterung 1, Quellen-Connector:** C&C²-Modell ist ungerichtet (actio = reactio), Bondgraph gerichtet. Pfeile an jeder CSS wären unübersichtlich und teils willkürlich (Beispiel CSS2-3 ohne eindeutige Richtung). Daher Kennzeichnung des Energieursprungs durch einen **doppelt umrandeten Connector (double-edged Connector)**; mehrere Quellen-Connectoren pro Modell möglich; die eingespeiste Energie kann negativ sein (Fig. 5 b, Zugkraft von C1).
- **Erweiterung 2, statische und dynamische CSS:** Energiefluss existiert nur, wenn Effort und Flow gleichzeitig ungleich null sind. Dynamische CSS = durchgezogene geschwungene Linie (wie bisher), statische CSS = gestrichelte geschwungene Linie. Beispiel: CSS2-3 an der Schraubenspitze statisch (Kraft ohne nennenswerte Bewegung); in Fig. 5 (b) sind alle CSS statisch, da die Schraube verankert ist (im Text steht "involves only CSSs", Einschätzung: gemeint sind statische CSS).
- **Table 1** (Kernelemente der domänenübergreifenden Definition):
  - Wirkflächenpaar: Knoten (Abgrenzung von Systemkomponenten)
  - statische CSS: kein Energiefluss (statische Sicht)
  - dynamische CSS: Energiefluss (dynamische Sicht)
  - Quellen-Connector: Ursprung des Energieflusses und Systemumgebung
  - Connector: Systemumgebung

### 4.2 Deriving a Bond Graph from a C&C²-Model (S. 707 bis 708)
- **Dynamische CSS → R-, I- oder C-Standardelement** (speichert oder dissipiert Energie); nur dynamische CSS gehen in den Bondgraphen ein. Der fraktale Charakter von C&C² setzt sich im Bondgraphen fort.
- **WSP → Junction oder Wandler:** WSP ist Verbindungspunkt zwischen "two or more CSSs"; je WSP ist zu bestimmen, ob die angeschlossenen CSS den Flow (Reihe, 1-Junction) oder den Effort (parallel, 0-Junction) teilen. Wandelt das WSP generalisierte Variablen (zwischen Domänen oder innerhalb einer Domäne), entspricht es einem Wandlerelement; welches der zwei Wandlerelemente gilt, hängt vom Umwandlungsverhältnis ab.
- **Quellen-Connector → Quellenelement;** zu bestimmen ist, ob er Effort oder Flow vorgibt. Einfacher Connector nur relevant, wenn an der dynamischen EFR beteiligt; meist am Ende eliminierbar.
- **Table 2:** WSP → Junction or converter; dynamic CSS → R, I or C standard element; source Connector → source element.
- **Voraussetzung:** Systemgrenze so wählen, dass ein geschlossener Kreis ("closed loop of cause and effect", nach Matthiesen 2002) entsteht; mit bekannten Gestalt- und Systemparametern (z. B. Trägheit einer Welle) ist ein vollständiger Bondgraph erstellbar.

### 4.3 Practical Example Low-Pass Filter (S. 708 bis 709)
- C&C²-Modell des Tiefpasses auf einer Platine (Fig. 6, Bildquelle Onlinehändler); zwei Farben für statische und dynamische Vorgänge (Farbwerte im Text nicht genannt).
- Ausgangsklemmen offen, kein Strom, daher nur Effort vorhanden, statische CSS an den Klemmen; Rückwirkung nachgeschalteter Komponenten ausgeklammert, abhängig vom Modellzweck.
- Signalweg: C1 (Quellen-Connector) → Leiterplatte → Spule (CSS1/2) → Leiterplatte → Kondensator (CSS3/4) → Minuspol; Ausgang parallel zum Kondensator abgegriffen.
- Ableitung nach der formalen Methode von Roddeck (akausale Bondgraphen, elektrische Domäne), Fig. 7 (a) bis (d):
  1. Schritte 1 bis 3: WSP als Orte von Potentialdifferenzen → 0-Junctions; jede CSS als Komponente über 1-Junctions an die WSP; Bondrichtung = Signalrichtung
  2. ohmsche Widerstände (Leiterplatte) als unwesentlich entfernt
  3. Schritt 4: Nullpotential (Minuspol, C2 und C4) entfernt
  4. Schritt 5: überflüssige Junctions nach Vereinfachungsregeln entfernt, finaler Bondgraph

### 5. Discussion (S. 709)
- Vorgehen sei intuitiv und nachvollziehbar, laut Autoren auch in weiteren, nicht berichteten Untersuchungen außerhalb der Elektrotechnik bestätigt.
- Kernelemente bleiben unverändert und erhalten nur zusätzliche Eigenschaften; der Quellen-Connector behält alle Connector-Eigenschaften.
- Erstmals mathematische Interpretation der Modellelemente; nach jeder Analyse-Synthese-Iteration kann ein Bondgraph abgeleitet werden.

### 6. Outlook (S. 709)
- weitere Domänen untersuchen (hydraulische, thermische, optische Systeme)
- Validierungsstudie zum Verständnisgewinn
- **Software**, in der C&C²-Modelle erstellt und Elementbeziehungen gespeichert werden, für automatische Bondgraph-Ableitung oder Export in Simulationsprogramme
- Simulation einer realen Fallstudie mit echten Parametern

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Quellen-Connector (doppelt umrandet) | Connector-Attribut `ist_quelle` (bool) plus `quellentyp` (Effort oder Flow), eigene Darstellung mit Doppelrand |
| Statische vs. dynamische CSS | LSS-Attribut `energiefluss` (statisch/dynamisch), Darstellung gestrichelt bzw. durchgezogen |
| Effort und Flow je Domäne | Domänenkatalog mit Effort/Flow-Paaren (Einschätzung, z. B. Kraft/Geschwindigkeit, Spannung/Strom, Druck/Volumenstrom; das Paper verweist für die Tabelle auf Schmitt und Andres) als Lerninhalt und Auswahlliste |
| WSP als Junction (0 oder 1) oder Wandler | WFP-Attribut `kopplung` (gleicher Effort, gleicher Flow, Wandler) plus Wandlerverhältnis |
| Dynamische CSS → R, I oder C | LSS-Attribut `bondgraph_element` (R/I/C) mit Parameterwert |
| Nur dynamische CSS gehen in den Bondgraphen | Exportregel: statische LSS werden beim Export ausgefiltert |
| Geschlossener Wirkungskreis als Voraussetzung | Prüfregel vor Export: Graph geschlossen, mindestens eine Quelle |
| Formale Methode nach Roddeck (5 Schritte) | Exportassistent mit schrittweiser Vereinfachung und Vorschau |
| Ausblick Software und Export | Export als Bondgraph bzw. Modelica-Gerüst (Einschätzung: Modelica nennt das Paper nicht, nur 20-sim und Dymola) |
| Leistungs- vs. Datenübertragung | Flusstyp-Attribut je LSS (Leistung/Information) zur Trennung von Funktionserfüllung und Funktionsvorgabe |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Diss., Basisdefinition WFP und LSS, Quelle der Definitionen und der Kausalitäts- und Zustandsargumente), Alink 2010 (Diss., Funktion mit dem C&C-Ansatz), Albers & Wintergerst 2014 (Anthology), Matthiesen et al. 2018 (SWP 58), Matthiesen, Grauberger, Sturm & Steck 2018 (Procedia CIRP 70, From Reality to Simulation, Quelle von Fig. 1), Grauberger et al. 2020 (JED, 20 Jahre Anwendungserfahrung), Matthiesen 2021 (Pahl/Beitz, Schraubenbeispiel). Bondgraphen: Roddeck 2019, Schmitt & Andres 2019, Das 2009.
