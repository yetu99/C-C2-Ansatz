# Albers et al. 2008: Systemanalyse in der Industrie mit dem Contact & Channel Model

| Feld | Wert |
|---|---|
| Autoren | A. Albers, T. Alink, S. Matthiesen, S. Thau (Kontakt Prof. Dr.-Ing. Dr. h.c. Albert Albers, IPEK, University of Karlsruhe (TH)) |
| Titel | Support of system analyses and improvement in industrial design trough the Contact & Channel Model (Schreibweise "TROUGH" so im Original) |
| Quelle/Reihe | International Design Conference DESIGN 2008, Dubrovnik, Croatia, May 19-22, 2008; Rubrik "Design Methods"; S. 245 bis 252; DS-Nummer im PDF nicht angegeben |
| Jahr | 2008 |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2008a), nicht im Repo (Lizenz) (8 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag überführt das **C&CM** vom Modell in eine Methode und stellt ein aus Industrieprojekten (Hilti AG) gewonnenes **C&CM-Kompendium** mit **vier Regeln** zur zielgerichteten Analyse vor: **Systemgrenze** festlegen, **Orte besonderen Interesses** bestimmen, **Kammansatz** (comb approach, angepasster Zoom) und **Sequenzmodell** für dynamische Systeme ("Sequenced Product Model"). Erstmals in dieser Quellenreihe werden **drei Basic Hypotheses** (I bis III) nummeriert benannt, ohne Connector. Ein Fallbeispiel (Schraubenmagazin) zeigt, dass ein **fehlendes WSP** die Fehlerursache war.

## Inhalte nach Abschnitt

### 1. Introduction (S. 245)
- Kürzere Test- und Validierungszeiten führen zu Rückrufen. Ziel ist konsequentere Analyse technischer Systeme vor Änderungen.
- C&CM als Basis einer Methode, Fokus auf Analyse von Produktversagen in industriellem Umfeld.

### 2. Contact and Channel Model C&CM (S. 245 bis 246)
- Vorgehen ist am Problemlöseprozess **SPALTEN** ausgerichtet (Albers 2007). Modellbildung intern (mental) und extern (CAD, Skizze), Bezug Eckert 2004.
- C&CM als "language to argue systematically about design problems" (S. 246).

### 2.1 Basis Principles (S. 246)
- Funktionen werden in **mindestens zwei WSP und einer verbindenden CSS** lokalisiert.
- Kern ist ein systematisches **function-component mapping** (Matthiesen 2002).
- **Basic Hypothesis I**: Funktion nur durch Wechselwirkung mit angrenzenden Systemen, action = reaction. **Basic Hypothesis II**: Funktion braucht ein weiteres WSP und eine CSS, die beide WSP verbindet. **Basic Hypothesis III**: Gesamtsystem vollständig durch Struktur aus WSP und CSS beschreibbar, auf jeder Detailebene mit denselben Elementen.
- Funktion definiert als Input-Output-Relation von Energie, Stoff, Information (Matthiesen 2002). Funktionen bestimmt durch Eigenschaften von WSP und CSS.

### 2.2 Target orientated analysis, C&CM Compendium (S. 246 bis 247)
- Modelle sind immer problembezogen und subjektiv (Stachowiak 1973). Vollständige Abbildung ist unmöglich, daher zielgerichtete Methode.
- Kompendium aus systematisch beobachteten Fallstudien, für Personen mit wenig Methodenerfahrung. "up to now four rules", keine feste Reihenfolge.

### 2.2.1 Systemgrenze und relevanter Systemteil (S. 247 bis 248)
- Top-down oder bottom-up. Schnitt möglichst **durch CSS** (Materialvolumen), damit an den WSP keine Information verloren geht, analog zum Freischnitt in der Technischen Mechanik.
- An den WSP der Schnittstelle werden alle Umgebungseinflüsse erfasst, Unwichtiges bewusst vernachlässigt.
- Indikatoren: unerklärliche Phänomene → höhere Detaillierung; Problem innerhalb der Grenze unlösbar → Grenze erweitern. Systemgrenzen auf allen Ebenen, auch überlappend.
- In jedem Zustand mindestens 2 WSP und eine CSS (Basic Hypothesis II).
- Fig. 1 Hilti Schnellbauschraube (Trockenbau, Gipskarton auf Metallprofil): Gesamtsystem WSP A bis G (Matrix-Schraube, Schraube-Bit, Bit-Schrauber, Schrauber-Nutzer, Grundträger-Boden, Boden-Nutzer, Matrix-Grundträger). Relevanter Teil mit WSP A und B und drei CSS (Matrix, Schraube, Bit). Legende "CSS ≡ components".

### 2.2.2 Orte besonderen Interesses (S. 248)
- Start an der vermutlich wichtigsten Stelle, meist einem WSP (Spitze, WSP A). Verbundenes WSP B bleibt angebunden, aber zunächst unbeachtet.
- Zoom-In: jedes Makro-WSP besteht aus vielen Mikro-WSP (A1, A2 ...), bezogen auf Basic Hypothesis III.
- **Zwei Strategien** (Fig. 2): von der Form ausgehend (alle WSP bestimmen, dann Funktionen erklären) oder von bekannten Funktionen ausgehend (Funktionsstruktur, dann Orte der Erfüllung suchen). Keine Priorisierung.

### 2.2.3 Comb Approach, adapted zoom (S. 248 bis 249)
- Basic Hypothesis II erinnert, dass es mindestens einen weiteren Ort der Funktionserfüllung gibt. Im Beispiel verhalten sich Schrauben trotz geklärter Spitze unerwartet, Antwort am WSP B Antrieb-Bit.
- Zoom in einen Ort, Zoom out, Wechsel zum nächsten Ort = **"Comb Approach"** (Fig. 3, Orte 1 bis 4). Hilft gegen Fixierung auf Details. Notfalls Systemgrenze erweitern (z. B. auf das Schraubgerät).

### 2.2.4 Sequence model for dynamic operating systems (S. 249 bis 250)
- Teil des Kompendiums für dynamische Vorgänge, **"Sequenced Product Model"**, zeitliche Dekomposition zusätzlich zur Dekomposition in Funktion und Gestalt.
- Zustandsfolgen ergeben sich aus der Betriebsart. Neuer Zustand, wenn eine Funktion durch Auflösen eines WSP endet oder durch Bilden eines WSP hinzukommt. Sequenz = mindestens zwei Zustände in stets gleicher Abfolge.
- Neue Zustände durch Hinzufügen, Wegnehmen oder Variation mindestens eines WSP. Sequenzen sind an eine Systemgrenze gebunden, können sich gegenseitig beeinflussen (Pause, Stopp, Neustart). Fig. 4 mit Sequenz A (Kupplung getrennt, Einkuppeln) und B.
- Im Schraubenfall wurde das Versagen stumpfen Spitzen zugeschrieben, die zeitliche Dekomposition zeigt Versagen zu einem Zeitpunkt, an dem die Spitze schon durch das Blech war. **6 Zustände** für WSP A, danach Sequenz für WSP B.
- Empfehlung, für jedes dynamische System eine Sequenz aufzubauen und Sequenzen aller relevanten Orte zu kombinieren.

### 3. Conclusion (S. 250 bis 251)
- Zeitliche Dekomposition ist der letzte Teil des Kompendiums. C&CM trennt Quelle und Wirkung von Problemen, liefert Basis für Ideen und Entscheidungen.

### 4. Industrial Examples, Hilti Stand-up-Tool (S. 251 bis 252)
- Dachschrauben für Profilbleche, Stand-up-Tool mit Magazin und Transportrohr (Fig. 5). Etwa jede 10. neue Schraube lag verkehrt herum. Fünf Tage Zeit bis zur Präsentation.
- Erste Analyse (Beobachten, Zerlegen) vermutete verschobenen Schwerpunkt und Trennklinge. Geänderte Klinge (neue Werkzeuge) scheiterte am 3. von 5 Tagen.
- Analyse nach den vier Kompendiumsregeln zeigt ein **fehlendes führendes WSP A** zwischen Schraubenkopf-Oberseite und Magazin beim Übergang Magazin → Transportrohr. Schwerpunkt begünstigte, verursachte aber nicht.
- Als Lösung wurden Schraubenhalter und Magazinführung enger zusammengeführt, Führung über WSP A bis F, Kosten "a small metal ring".

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Systemgrenze durch CSS schneiden, Umgebungseinflüsse an Schnitt-WSP sammeln | Werkzeug "Freischnitt": Grenze nur durch LSS zulassen, an Schnitt-WFP Umgebungsattribute (später Connector) erfassen |
| Indikatoren für Zoom-In vs. Grenze erweitern | Hinweisregel im Analyse-Workflow (unerklärliches Phänomen → verfeinern; ungelöst → Grenze erweitern) |
| Zwei Einstiegsstrategien (form-first, function-first) | Wahlschalter beim Modellstart mit passender Eingabereihenfolge |
| Comb Approach (Orte 1 bis n) | Liste "Orte der Funktionserfüllung" mit Status je Ort (offen, gezoomt, erklärt) |
| Zustandswechsel bei Bilden/Auflösen eines WSP, Sequenz ≥ 2 Zustände | Zeitachsen-Editor, automatischer Zustandsvorschlag bei Änderung der WSP-Menge, Sequenzen mit Einflusskanten (Pause, Stopp, Neustart) |
| Fehlendes WSP als Ursache (Hilti) | Vergleichsfunktion zweier Modellvarianten (alt/neu) mit Diff der WSP-Mengen je Zustand |
| Basic Hypotheses I bis III | Prüfregeln und Lerninhalte mit historischer Fassung (ohne Connector) |
| Ausrichtung an SPALTEN | Verknüpfung der Modellierung mit Problemlöseschritten (Situationsanalyse, Problemeingrenzung) |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Basisdefinition, function-component mapping), Albers und Meboldt 2007 (SPALTEN-Matrix), Eckert, Albers und Ohmer 2004 (kognitive Perspektive auf C&CM), Stachowiak 1973 (Modelltheorie), Pahl und Beitz 2003, Bender 2004 und Lossack 2004.
