# Vogel 2021: Das Lastpfad- und Knotenmodell

| Feld | Wert |
|---|---|
| Autoren | Sven Vogel, M.Sc. (Berichterstatter Prof. Dr.-Ing. E. Kirchner, Mitberichterstatter Prof. Dr.-Ing. S. Matthiesen) |
| Titel | Das Lastpfad und Knotenmodell. Eine Erweiterung des C&C²-Ansatzes zur Bewertung von Ersatzgrößen in der Produktentwicklung mechatronischer Systeme (Titelblatt ohne Ergänzungsstrich nach "Lastpfad"; im Fließtext durchgehend "Lastpfad- und Knotenmodell") |
| Quelle/Reihe | Dissertation (Dr.-Ing.), Fachbereich Maschinenbau, Technische Universität Darmstadt, D17; veröffentlicht auf TUprints, URN urn:nbn:de:tuda-tuprints-178841, URI https://tuprints.ulb.tu-darmstadt.de/id/eprint/17884; eingereicht 10.11.2020, mündliche Prüfung 23.02.2021 |
| Jahr | 2021 |
| DOI | im PDF nicht angegeben (nur URN und URI) |
| Lizenz | CC BY-NC-SA 4.0 (Namensnennung, Nicht kommerziell, Share Alike 4.0 International) |
| Volltext | [`../volltexte/Vogel2021.pdf`](../volltexte/Vogel2021.pdf) (130 S.) |
| Status | gelesen, vollständig ausgewertet (Kap. 1 bis 8 und Anhang A1; Rohdatentabellen Anhang A2/A3 nur gesichtet) |

Seitenangaben unten sind Druckseiten (arabische Zählung, Druckseite = PDF-Seite minus 12). Vorspann und Anhang tragen römische Seitenzahlen.

## Kernaussage

Der **C&C²-Ansatz** findet Messmöglichkeiten nur an Gestaltelementen, die direkt die geleitete Größe führen. Vogel erweitert ihn um die Elemente **Umformung** (Form der Flussgröße ändert sich, Art bleibt) und **Wandlung** (Art bzw. physikalische Domäne ändert sich) sowie **Knoten** (Aufteilung und Überlagerung), **Speicher** und **Ein- und Ausleitung**. Daraus entsteht das **Lastpfad- und Knotenmodell** als Metamodell, mit dem sich **Ersatzgrößen** für eine **Zielgröße** auch in sekundären Lastpfaden (Reaktionen) finden und früh nach Anzahl signalmanipulierender Elemente und Parametertoleranzen bewerten lassen. Eine Crossover-Probandenstudie (N = 28) zeigt eine signifikante Verbesserung der Ersatzgrößenauswahl nach Schulung mit mittlerer Effektstärke (r = 0,33).

## Inhalte nach Abschnitt

### 1. Einleitung (S. 1 bis 3)
- Motivation Digitalisierung und Smart Products. Hemmnis ist das Verhältnis von Kosten zu zeitnahem Nutzen der Sensorintegration (Bauernhansl 2017).
- Entwickler wissen oft nicht, welche Größen im System messbar sind. Kataloge (VDMA-Leitfaden Sensorik für Industrie 4.0, Fleischer et al. 2018) helfen bei der Sensorwahl, nicht bei der Wahl der tatsächlich gemessenen Größe.
- Konflikt zwischen kalibrierten Standardsensoren (Systemanpassung nötig, mechanische Funktion gefährdet) und Spezialsensorik (Entwicklungs- und Kalibrieraufwand).
- Ziel der Arbeit ist es, bestehende Analysemodelle zu erweitern, um Größen für indirekte Messung systematisch zu identifizieren und den Lösungsraum früh zu reduzieren.

### 2. Stand der Forschung (S. 4 bis 25)
- **Modelle und Methoden (S. 4 bis 6).** Modelltheorie nach Stachowiak (Abbildungs-, Verkürzungs-, pragmatisches Merkmal). Metamodell nach Matthiesen (2020) als "Modell mit Regeln und Elementen, das zur Modellbildung genutzt wird". Methoden liefern das Regelwerk für Arbeitsschritte, Vorgehensmodelle beschreiben die Schritte.
- **Systemtheorie (S. 6 bis 8).** Funktionales, strukturales, hierarchisches Konzept nach Ropohl (Abb. 2.1). Technisches System mit Energie-, Stoff-, Signalumsatz; Beispiele Getriebe (Energie leiten und umformen), Ventil (Stoffumsatz), Dehnungssensor (Signal wandeln und leiten).
- **Merkmal und Eigenschaft (S. 8 bis 11).** Eigenschaft = Merkmal + Wert (Abb. 2.3, z. B. Wellendurchmesser 30 mm). Hubka (innere, äußere, elementare Konstruktionseigenschaften), Wäldele (unabhängige/abhängige Eigenschaften, Eigenschaftsnetzwerk). Vogel übernimmt Weber, wonach Merkmale die Gestalt und Eigenschaften das Verhalten abbilden.
- **Produktmodelle (S. 11 bis 14).** Produktmodellpyramide nach Sauer (Funktion, Effekte, Wirkprinzip, Gestalt; Abb. 2.5). Product model framework nach Matthiesen et al. 2019b mit vier Aufgabenclustern (Abb. 2.6).
- **C&C²-Modell (S. 14 bis 15).**
  - Grafisches Modell, das Funktion, Verhalten und qualitative Gestalt beschreibt. Im product model framework Cluster III ("Einsicht erhalten"). Verknüpft Funktions- und Gestaltebene der Pyramide.
  - C&C²-Ansatz = Metamodell mit Regeln und Elementen zur Bildung von C&C²-Modellen.
  - Drei **Grundelemente** WFP, LSS, Connector (Abb. 2.7); Definitionen siehe Befunde.
  - Drei **Grundhypothesen** nach Matthiesen 2002 (ohne Connector formuliert), danach Hinweis, dass Connectoren bei Bedarf durch WFP und LSS abgebildet werden können.
  - Beispiel Schnellbauschraube (Abb. 2.7, Bildquelle Matthiesen 2020), Zweck Identifikation funktionsrelevanter Gestaltparameter an WFP1 und WFP2.
- **Prozessmodelle, Sequenzmodell (S. 15 bis 16).**
  - Sequenzmodell zerlegt dynamische Prozesse in zeitliche Sequenzen (Albers et al. 2008). "Mindestens zwei Zustände ergeben eine Sequenz."
  - Neuer Zustand, wenn ein WFP entsteht oder aufgelöst wird, sich die Funktion ändert oder eine zusätzliche Funktion entsteht (Matthiesen, Ruckpaul 2012); zusätzlich bei starker Änderung der Werte funktionsrelevanter Parameter (Matthiesen et al. 2018a).
  - Zustände können logisch statt chronologisch geordnet sein und wiederholt auftreten (Matthiesen et al. 2019a).
  - Beispiel Schraubenmontage, Zustände Körnen und Verdrängen, WFP A-1 bleibt, WFP B-2 entsteht (Abb. 2.8, Bildquelle Thau 2013).
- **Produktentwicklungsprozess (S. 16 bis 19).** VDI 2221 (sieben Arbeitsschritte), VDI 2222, VDI 2223 (strategisches und operatives Vorgehen). Prozess des Gestaltens nach Matthiesen et al. 2018b (Abb. 2.11).
- **Sensorintegrierende Maschinenelemente (S. 19 bis 21).** Stücheli und Meboldt (mechatronische Maschinenelemente). Unterscheidung sensorintegriert (überwacht eigene Funktion, z. B. Schraubenvorspannung) und sensorintegrierend (misst Prozessgrößen des Übersystems, z. B. Sensorschraube im Walzprozess). Vorwerk-Handing et al. 2020 unterscheiden sensortragend, sensorintegrierend, sensorisch nutzbar (Abb. 2.12). Vogel unterscheidet sensorintegrierend und sensorisch nutzbar nicht.
- **Messsysteme (S. 22 bis 24).** GUM (JCGM 100). Modell der Messung X_IND = g(Y, X1 ... Xn) und Modell der Auswertung Y = f(X_IND, X1 ... Xn) nach Heidenblut et al. 2007. **Übertragungsfunktion** X_IND / Y = f(X1 ... Xn) (Gl. 2.3) als Vergleichsbasis (Betrag für Auflösung, Parameteranzahl, Toleranzen). Unsicherheit = Daten-, Kontext-, Modellunsicherheit (Würtenberger 2018).
- **Interpretation (S. 24 bis 25).** Sensorintegration = Weiterentwicklung mit Zusatzfunktion ohne Änderung der bestehenden Funktion. GUM setzt bekannte Gestalt inkl. Sensor voraus.

### 3. Forschungsdesign (S. 26 bis 29)
- Drei Defizite: Hilfsmittel unterstützen nur Sensorauswahl; messtechnische Hilfsmittel setzen bekannten Sensor bzw. vollständige Messkette voraus; es fehlt eine Modellbasis zur Identifikation und Auswahl von Ersatzgrößen.
- Mit dem C&C²-Ansatz lassen sich keine Reaktionseffekte infolge von **Umformen** und **Wandeln** (Begriffe nach Roth 2000) darstellen. Auch das auf C&C² aufbauende **Wirkraummodell** kann das nicht (S. 28, ohne Quellenangabe an dieser Stelle).
- Fünf Forschungsfragen (S. 28): FF1 C&C² zur systematischen Ersatzgrößensuche, FF2 Störgrößen erkennen, FF3 Erweiterung für sekundäre Reaktionen, FF4 Anwendung zur Bewertung, FF5 Steigerung der Analysefähigkeit.

### 4.1 Ziel-, Ersatz- und Messgröße (S. 30 bis 34)
- Anforderungen an das neue Analysemodell (S. 30): Reaktionsgrößen infolge der gewünschten Größe, mögliche Messstellen und Ersatzgrößen, zu berücksichtigende Parameter darstellen.
- Hierarchie der Entwicklungsziele am Beispiel Fabrik, Maschine, Baugruppe (Abb. 4.1).
- Drei Begriffsdefinitionen **Zielgröße**, **Ersatzgröße**, **Messgröße** (Wortlaut siehe Befunde). Abgrenzung zu DIN 1319-1, deren "Messgröße" je nach Kontext der Ziel- oder Ersatzgröße entspricht.
- Zuordnung Ersatzgröße zu Zielgröße muss nicht eindeutig sein; Eindeutigkeit oft durch mehrere Ersatzgrößen.
- **Lösungsraum** = Überschneidung der durch die Gestalt gegebenen Ersatzgrößen mit den Messgrößen verfügbarer Sensoren (Abb. 4.2). Ersatzgröße ohne Sensor oder Sensor ohne Ersatzgröße fällt heraus, außer bei Sensorentwicklung bzw. konstruktiver Anpassung.
- Kaskadierung (Abb. 4.3). Die Ersatzgröße eines Systems wird Zielgröße des Subsystems bzw. Lieferanten (Auslastung, Durchsatz, Last, Dehnung, Spannung).

### 4.2 Erweiterung des C&C²-Ansatzes (S. 34 bis 55)
- Ausgangspunkt Getriebemotor (Abb. 4.5). Funktionsstruktur nach Roth (Verknüpfen, Wandeln, Umformen), C&C²-Modell der Funktion Umformen. Lastpfad des Drehmoments rot, weitere Lastpfade blau.
- Versuch am pmd (Abb. 4.4). Die elektrische Impedanz eines Wälzlagers im Industriegetriebe hängt vom Drehmoment ab (T = 50 °C, n = 1350 min⁻¹). Messort Lager liegt außerhalb des Lastpfades des Drehmoments.
- **4.2.1 Messstellen und Ersatzgrößen (S. 38 bis 40).**
  - Beteiligt sind WFP1 bis WFP4 und LSS L1 bis L3. Prinzip ist, dass jede Aktion eine Reaktion hat.
  - **Veränderliche Oberflächeneigenschaften** von WFP (Abb. 4.6): Größe des WFP (A0 → A1, Hertzsche Fläche), Kontaktwiderstand, Dicke funktionaler Schicht.
  - **Veränderliche Volumeneigenschaften** von LSS (Abb. 4.8): lokale Verformung, globale Verschiebung (Δγ), elektrische Permittivität (z. B. Schmierstoff im Wälzlager), Eigenfrequenzen.
  - Funktionsrelevante und veränderliche Eigenschaften bilden jeweils eigene, unabhängige, nicht exklusive Mengen.
  - Sensor zwischen zwei Wirkflächen (Abb. 4.7) ändert das Modell. WFP1 entfällt, WFP2, WFP3 und LSS1 kommen hinzu. Komponententausch gegen Sensorkomponente (Abb. 4.9) ersetzt LSS1 durch LSS2. Beides ändert die **Primärfunktionsgestalt**, die Funktionserfüllung ist erneut zu prüfen (Belege Brecher et al. 2016, Tlusty, Andrews 1983).
- **4.2.2 Zu berücksichtigende Parameter (S. 40 bis 43).**
  - Ersatz/Zi = f(Einflussparameter) (Gl. 4.1), konkretisiert als f(WFP_i; L_i) (Gl. 4.2).
  - Messen einer Eigenschaft erzeugt eine **zweite Funktion "mechanisches Signal leiten"** mit eigenem C&C²-Modell (Informationspfad, Abb. 4.10). Deren funktionsrelevante Parameter bestimmen die Übertragungsfunktion, z. B. f(WFP1; L1; WFP2) (Gl. 4.3).
  - Beispiel Torsionsdehnung an Welle, T_A = (π/2)·r³·G·ε (Gl. 4.5). Hohlwelle statt Vollwelle erzeugt neuen Parameter d_Innen, das Auswertemodell wird ungültig.
  - Abb. 4.11 ordnet Messkette (SRC, TRANS, IND nach Sommer, Siebert 2004), Teilfunktionen (Einleitung der Zielgröße, Signal leiten, Signal wandeln, Signal leiten, Auswertung), C&C²-Modell und Bauteile einander zu. Bestehendes System leitet das mechanische Signal, der integrierte Sensor wandelt es. Sensor und Anbindung werden als ideal angenommen.
- **4.2.3 Störgrößen (S. 43 bis 45).**
  - Nicht berücksichtigter Parameter wird zur Störgröße.
  - Nach Rossi et al. 2019 bewirken **additive** Störgrößen eine Nullpunktverschiebung und **multiplikative** Störgrößen eine Steigungsänderung.
  - Strategien nach Matthias 2015: Unsicherheit eliminieren, Einfluss unterdrücken, Wirkung reduzieren (Beispiel DMS-Temperaturkompensation).
  - Sensitivität = lokale Steigung der Übertragungsfunktion am Betriebspunkt (Abb. 4.12, Toleranzfeld Schubmodul → Messunsicherheit). Bestehende Toleranzen reichen für Sensorik oft nicht aus.
- **4.2.4 Parallele Lastpfade (S. 45 bis 51).**
  - Reihenschaltung (eindeutiger Lastpfad, Abb. 4.13). Lokal H1 = 1/c1, unabhängig von c2; global H2 = (c1 + c2)/(c1·c2), sensitiv auf beide. Lokale Messung ist robuster.
  - Parallelschaltung (Abb. 4.14). Lokal = global, H3 = 1/(c1 + c2), sensitiv auf beide Pfade. Globale Messung paralleler Pfade ist robuster als globale Messung eindeutiger Pfade.
  - Folglich muss die Übertragungsfunktion auch **Connectoren** enthalten, also Ersatz/Zi = f{WFP_i; L_i; C_i} (Gl. 4.15).
  - Beispiel elastische Klauenkupplung (Abb. 4.15) und berührungslose Kantendetektion aller Einfederungen (Abb. 4.16; belastete und entlastete Pfade im Wechsel, nach acht Kantenpassagen wiederholt). Symmetrische Lastaufteilung mit Traganteil reicht für Auslegung, für Sensorik oft nicht (Schork et al. 2016).
- **4.2.5 Umformung und Wandlung im Wirknetz (S. 51 bis 55).**
  - Gleichgewichte m·ẍ = ΣF, Θ·φ̈ = ΣM (Gl. 4.16, 4.17). Umformung F_Aus = U·F_Ein mit U ≠ 1 (Gl. 4.18, 4.19).
  - Ein unbeschleunigter Körper braucht dann eine weitere Größe F_Kopp = −F_Ein·(U + 1) (Gl. 4.20, 4.21). Deren Leitung erfordert ein **weiteres Wirknetz für die sekundäre Funktion "Gleichgewicht herstellen"** (Abb. 4.17).
  - Zahnradwelle (Abb. 4.18) mit Lastpfad des Drehmoments und Lastpfade der Reaktionskräfte F2, F3 über L1 bis L4, WFP1 bis WFP5. Lagerkraft F2 als Ersatzgröße für T1 (Abb. 4.19, Gl. 4.24). Überlagerung durch Axialkraft (Schrägverzahnung, in C2) und Wellengewicht.
  - Wandlung am Getriebemotor (Abb. 4.20). Strom I wird zu Drehmoment gewandelt, im Getriebe mehrfach umgeformt.
  - Betrachtung von **Flussgrößen statt Energie** erlaubt Beschreibung auch bei blockierter Welle (keine Energieübertragung). Erhaltungsgleichungen (Energie, Masse, Ladung, Impuls) bleiben gültig. I/T1 = f(C_i, L_i; WFP_i) (Gl. 4.25).
  - Vergleich und Priorisierung über Anzahl und Schwankungsbreite der funktionsrelevanten Parameter der Funktion Signal leiten.

### 4.3 Das Lastpfad- und Knotenmodell (S. 55 bis 66)
- Metamodell, das Regeln und Elemente zum Bilden von Lastpfad- und Knotenmodellen liefert. Ergänzt den erweiterten C&C²-Ansatz um **Knoten, Wandeln, Umformen** (S. 55). In 4.3.1 kommen **Ein- und Ausleitung** (inkl. Quellen) und **Speicher** hinzu.
- **Lastpfad (S. 56).**
  - Weg einer Flussgröße durch das System, Teil des Wirknetzes der Funktion Energie leiten.
  - Wirkt zwischen mindestens zwei Lasten oder Knoten. Flussgröße wird darin weder gewandelt noch umgeformt. Braucht Eingang und Ausgang.
  - Vergleich C&C²-Modell und Lastpfad an Welle, Passfeder, Nabe (Abb. 4.21).
- **Knoten (S. 57 bis 59).**
  - Aufteilung und Überlagerung von Lastpfaden. Kann nichts speichern, daher bilanzierbar.
  - Vorzeichenregel zum Knoten zeigend positiv, weg zeigend negativ, 0 = F1 − F2 − F3 + F4 (Abb. 4.22, Gl. 4.26).
  - Ein Knoten zwischen Ziel- und Ersatzgröße wirkt **additiv** auf die Signalübertragung.
  - Beispiel Radialkraft Zahnrad mit Aufteilung auf zwei Lager, F_R2/F_R3 = l3/l2 (Gl. 4.27), Auswertemodell mit Gewichtskraft (Gl. 4.28). Bereiche "Aufteilung muss/muss nicht berücksichtigt werden" farbig (grün Nabe, gelb Welle; Abb. 4.23).
  - Aufteilung kann von Betriebsparametern, Verschleiß, Reibung abhängen. Anzahl und Komplexität der Aufteilungen dienen dem frühen Konzeptvergleich (Vogel et al. 2019).
- **Umformung (S. 59 bis 60).**
  - Ändert die Form der Flussgröße, die Art bleibt. Wirkt **multiplikativ** auf das Signal.
  - Erzeugt Reaktionsgröße F_R, die einen eigenen Lastpfad braucht und aus dem System geleitet werden muss (Abb. 4.24).
  - Beispiel Getriebeausgangswelle M_A = F_T·U mit U = R_Z (Teilkreisradius) (Gl. 4.29, 4.30). F_R teilt sich im Knoten auf zwei Lager (Abb. 4.25).
- **Wandlung (S. 60 bis 62).**
  - Ändert die Art der Flussgröße, d. h. die physikalische Domäne. Ebenfalls multiplikativ.
  - Je Domäne eigene Erhaltungsbedingungen (mechanisch Impuls, Drehimpuls; elektrisch Ladung). Daraus folgen Reaktionsgrößen in beiden Domänen (Abb. 4.26).
  - Verluste meist als Wärmestrom ausgeleitet; Effizienz geht in den Zusammenhang der Flussgrößen ein.
  - Beispiel Elektromotor T = I·W, Gleichstrommotor W = c(η_W)·Φ (Gl. 4.31, 4.32; Abb. 4.27). Zielgröße messbar über Strom in einem Kabel oder über mechanische Reaktion (Fundamentkräfte).
- **Ein- und Ausleitung (S. 62 bis 63).**
  - Schnittstellen = Wirkflächen von Wirkkörpern oder Wirkräumen an der Systemgrenze. Pfeile zum System hin (Einleitung) bzw. vom System weg (Ausleitung, direkte Reaktion).
  - **Quellen** (Vorspannung, systeminterne Stromquelle, Batterie Abb. 4.28) haben Ein- und Ausleitung an derselben Stelle, auch innerhalb der Systemgrenze. Platzierung an der tatsächlichen Ursache empfohlen.
- **Speicher (S. 63 bis 65).**
  - Eingeleitete, nicht ausgeleitete Flussgröße wird gespeichert, mechanisch F_Ein = m·v̇, elektrisch analog F_Ein = C·u̇ (Gl. 4.33, 4.34; Abb. 4.29).
  - Nötig für schwingende Systeme (Effekt **Isolation**). Einmassenschwinger mit Impulsspeicher (Abb. 4.30). Oberhalb des Zweifachen der Eigenfrequenz ω0 gelangt nur ein geringer Anteil in den statischen Lastpfad (Abb. 4.31). Hochfrequente Größen am statischen Lastpfad oft nicht messbar.
- **Eigenschaften eines Lastpfad- und Knotenmodells (S. 65 bis 66).**
  - Basis der mathematischen Modellbildung der Messkette.
  - Für Alternativen gezielt Umformungen und Wandlungen modellieren und in sekundären Lastpfaden suchen.
  - Frühe Kriterien: **Anzahl signalmanipulierender Elemente** (Knoten, Wandlungen, Umformungen) und **bekannte Toleranzen** (Messorte mit großen Toleranzfeldern ausschließen).
  - Modelle werden über den Prozess präzisiert. Endbewertung mit vollständiger Messkette inkl. Sensor und Auswerteeinheit. Modell dient auch zur Entscheidungsdokumentation.

### 5. Evaluation an bekannten Produkten (S. 67 bis 80)
- **5.1 Hydraulische Industriescheibenbremse (S. 67 bis 72), Referenz Richter et al. 2010.**
  - Die Zielgröße Axial-/Bremskraft wird bisher über die Ersatzgröße Druck in der Druckkammer bestimmt. Bei Belagverschleiß ändern sich Federweg und Vorspannung der Tellerfedern (nichtlineare Kennlinie), das Modell verliert Gültigkeit.
  - Drei **Zustände** werden modelliert. Drucklos (Tellerfedervorspannung als Quelle, Umformungen U1 bis U3, Biegemoment im Steg, Abb. 5.3). Geöffnet (Druck → Kraft an Wandlung W1, Rückwandlung W2, radiale Reaktionen R1, R2 im Gehäuse, Abb. 5.4). Geregelt als Überlagerung (Abb. 5.5).
  - Farbcodierung schwarz primärer Lastpfad, rot Reaktionen, blau Elemente im Lastpfad der Messung.
  - Im geregelten Zustand teilt sich die Zielgröße F_Zi im Knoten K1 auf LP1 (Zugstange, Wandlungen W1, W2) und LP2 (Tellerfedern), Vereinigung in K2. Auswertemodell F_Zi = K1·W1·p mit K1 = c1/(c1 + c2), W1 = A_Kolben (Gl. 5.1).
  - Größte Unsicherheit ist die Tellerfedersteifigkeit c2 (Knoten K1). Alternative ohne Knoten K1 ist die Dehnung in der Gehäusegrundstruktur hinter K2, F_Zi = π(ra² − ri²)·E·ε (Gl. 5.2; Symbol des Moduls im extrahierten Text unvollständig). Geringere Streuung, Primärfunktionsgestalt bleibt unverändert.
  - Reibung in Dichtungen und Führungen erzeugt weitere Knoten, wird vernachlässigt. Granularität über Matthiesens Techniken (Matthiesen 2020) wählen.
- **5.2 Flachwalzprofiliermaschine (S. 72 bis 80), Referenz Oppel 2008.**
  - Ziel ist das Erkennen vertikaler Kräfte durch Walzfehler.
  - Drei Lastfälle als getrennte Modelle: Kippmoment aus und in die Schnittebene (Abb. 5.7, 5.8) und horizontale Walzkraft F_W (Abb. 5.9), Knoten K1 bis K7, form- und reibkraftschlüssige Parallelpfade.
  - Fehlerfreier Prozess = nur Walzkraftzustand. Fehler = Überlagerung.
  - Es gibt keine Stelle, an der beide Fehlerzustände ohne Überlagerung durch F_W reagieren. Außerhalb von Backe und Backenkorb mindestens zwei Sensoren nötig.
  - Kandidaten: Biegemoment Einstellschraube, Druck Backenkorbboden, Druck Backenkorblagerung, Druck oder Biegung (Abb. 5.10 bis 5.13).
  - Abgleich mit Oppel. Dessen Positionen wurden gefunden. Nicht gefunden wurde nur der zusätzliche vorgespannte Niederhalter (Abb. 5.14), weil er die Gestalt der Primärfunktion ändert.

### 6. Probandenstudie (S. 81 bis 92)
- **Design.** Crossover-Studie (Abb. 6.1). Gruppe A erst Bremse, Gruppe B erst Schieber; dann Fragebogen zu Kenntnis Kraftfluss und C&C²-Modell; Schulung Lastpfad- und Knotenmodell mit Übungen Presse 1 und 2; dann jeweils andere Aufgabe; Abschlussfragebogen.
- **Aufgaben.** Multiple Choice mit vier Optionen (0 bis 3 Punkte) plus Sensorrangfolge. Bremse mit Kriterium Anzahl Störgrößen (Bewertung a hydrostatischer Druck 1, b axiale Dehnung 2, c Biegung 3, d axiale Dehnung 0). Schieber mit Kriterium Signalstärke, Punkte aus FEM (a 1, b 2, c 3, d 0) (Anhang A1, S. XII bis XV).
- **Stichprobe (Abb. 6.2).** Durchgang 1 TU Darmstadt mit 2 WiMis und 2 HiWis pmd (Vorstudie) sowie 13 Tutoren pmd, also 17. Durchgang 2 mit 8 WiMis IPEK, 2 HiWis IPEK, 1 WiMi IDD, also 11. Gesamt N = 28, Gruppe A 16, Gruppe B 12.
- **Ergebnisse.**
  - Gesamt Median 2 → 3, T = 115 < T_crit = 116, p = 0,0440, r = 0,33 (mittel). 12 besser, 11 gleich, 5 schlechter (Tab. 6.1, Abb. 6.4).
  - Durchgang 1 mit N = 17, T = 34, p = 0,0443, r = 0,375.
  - Durchgang 2 mit N = 11, T = 24,5, p = 0,472, r = 0,241 (nicht signifikant).
  - Unterschied der Durchgänge U = 80,5, p = 0,271.
  - Aufgabe Bremse signifikant schwerer (T = 108, p = 0,0396, r = 0,367).
  - Gruppen unterschiedlich (U = 238,5, p = 0,0042), erklärt durch Deckeneffekt beim Schieber.
  - Auf der Bremsaufgabe allein Schulungseffekt r = 0,609.
- **Interpretation.** Schulungseffekt vorhanden, aber nicht uneingeschränkt. Erfahrene Teilnehmende (IPEK-WiMis mit C&C²-Kenntnis) profitieren weniger, Neuheit für sie geringer (Abb. 6.13).

### 7. und 8. Zusammenfassung, Fazit und Ausblick (S. 93 bis 95)
- Antworten auf FF1 bis FF5 (S. 93 bis 94). FF4 wird beantwortet mit Bewertung über Anzahl der Knoten, Wandlungen und Umformungen sowie Unsicherheit der Parameter. FF5 nur bedingt beantwortet.
- Offene Punkte (S. 95):
  - Für Reaktionen bei Wandlung und Umformung fehlen **konsistente Regeln für eine automatisierte Auswertung**. Jede Wandlung/Umformung braucht eine Einzelfallbeurteilung. Vorschlag ist ein **Katalog bekannter Reaktionen**.
  - Anbindung an Toleranzmodelle.
  - Regelbasierte Ersatzgrößenauswahl über physikalische Effektketten (Diss. Vorwerk-Handing, unveröffentlicht).
  - Auswahl der Ersatzgröße bleibt bislang intuitiv.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Elemente Lastpfad, Knoten, Umformung (U), Wandlung (W), Speicher, Ein-/Ausleitung, Quelle | Zusätzliche Elementtypen als Graph-Overlay auf dem C&C²-Modell. Knoten = Graphknoten mit Bilanz, Lastpfad = Kante mit Flussgrößentyp, U/W = Kantenattribut mit Faktor und Reaktionspflicht |
| Knotenbilanz mit Vorzeichenregel (Gl. 4.26) | Automatische Bilanzprüfung je Knoten (Summe ein = Summe aus), Warnung bei offenem Knoten |
| Umformung und Wandlung erzwingen Reaktionsgrößen mit eigenem Lastpfad | Prüfregel, nach der jede U/W ohne zugeordneten Reaktionslastpfad markiert wird. Bei W je Domäne eigene Erhaltungsbilanz (Impuls, Ladung, ggf. Masse) plus optionaler Verlust-Wärmestrom |
| Ziel-, Ersatz-, Messgröße und Lösungsraum (Abb. 4.2) | Objekte Zielgröße, Ersatzgröße, Messgröße (Sensorkatalog). Lösungsraum als Schnittmenge berechnen; Kaskade Ersatzgröße → Zielgröße Subsystem |
| Veränderliche Oberflächen- (WFP) und Volumeneigenschaften (LSS), getrennt von funktionsrelevanten Eigenschaften | Zwei unabhängige Eigenschaftslisten je Element (funktionsrelevant / veränderlich) mit Vorschlagskatalog (Kontaktwiderstand, Schichtdicke, Permittivität, Eigenfrequenz ...) |
| Übertragungsfunktion Ersatz/Zi = f{WFP_i; L_i; C_i}, additive (Knoten) vs. multiplikative (U, W) Einflüsse | Pfadauswertung zwischen Zielgröße und Messort. Elemente entlang des Pfades sammeln, Typ additiv/multiplikativ anzeigen, Parameter mit Toleranz für Sensitivitätsrechnung (dH/dc) |
| Frühkriterien Anzahl signalmanipulierender Elemente und Toleranzfelder | Ranking-Tabelle möglicher Messorte (Score aus Anzahl K/U/W, Parameteranzahl, Toleranzbreite), Entscheidungsprotokoll |
| Sensor im WFP oder Komponententausch ändert Primärfunktionsgestalt (Abb. 4.7, 4.9) | Diff-Funktion: Wegfall/Neu von WFP und LSS anzeigen und Flag "Primärfunktion erneut prüfen" setzen |
| Mehrere Zustände (Bremse drucklos, geöffnet, geregelt) und Überlagerung von Lastfällen (Walzmaschine) | Zustands- bzw. Lastfallverwaltung mit Überlagerungsansicht; Suche nach Messorten, an denen nur ein Lastfall wirkt |
| Speicher und Isolation über 2·ω0 | Frequenzattribut je Flussgröße; Hinweis, wenn hochfrequente Zielgröße am statischen Lastpfad gemessen werden soll |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Diss., Grundelemente und Grundhypothesen), Matthiesen 2020 (Pahl/Beitz Kapitel, Metamodell, Connector, Techniken), Matthiesen et al. 2019b (Product Models in Embodiment Design, product model framework, Connector-Abbildung), Matthiesen et al. 2018b (KIT SWP, Modellbildung mit C&C²), Albers et al. 2008 (DESIGN 2008, Sequenzmodell), Thau 2013 (Diss., Heuristiken, Bildquelle Sequenz), Matthiesen, Ruckpaul 2012 (logische Zustände), Matthiesen et al. 2018a (NordDesign, Sequenzmodellierung), Matthiesen et al. 2019a (ICED, Extended Sequence Modelling), Grauberger 2021 (Diss., Auswertungsvorgehen der Studie), Vogel, Kirchner 2019 (ICED, Simple Integration of Sensory Functions), Vogel et al. 2019 (DfX, Priorisierung von Weiterentwicklungsoptionen), Vorwerk-Handing et al. 2020 (Klassifikation mechatronischer Maschinenelemente), Roth 2000 (allgemeine Funktionen Leiten, Umformen, Wandeln).
