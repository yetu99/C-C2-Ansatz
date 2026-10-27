# Matthiesen 2002: Basisdefinition des Elementmodells „Wirkflächenpaare & Leitstützstrukturen“

| Feld | Wert |
|---|---|
| Autoren | Sven Matthiesen (Dipl.-Ing.) |
| Titel | Ein Beitrag zur Basisdefinition des Elementmodells “Wirkflächenpaare & Leitstützstrukturen” zum Zusammenhang von Funktion und Gestalt technischer Systeme |
| Quelle/Reihe | Dissertation, Fakultät für Maschinenbau, Universität Karlsruhe (TH); erschienen als Forschungsberichte des Instituts für Maschinenkonstruktionslehre und Kraftfahrzeugbau, Band 6, Hrsg. A. Albers; Hauptreferent A. Albers, Korreferent H. Birkhofer; mündliche Prüfung 21.10.2002 |
| Jahr | 2002 |
| ISSN | 1615-8113 (Reihe) |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben (Vermerk „Copyright: Institut für Maschinenkonstruktionslehre und Kraftfahrzeugbau, Universität Karlsruhe (TH), 2002, Alle Rechte vorbehalten“) |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Matthiesen2002), nicht im Repo (Lizenz) (184 S.) |
| Status | gelesen, Kernkapitel ausgewertet (Kap. 1, 2.2 bis 2.8, 3, 4, 5, 6 vollständig; Kap. 2.1 und Anhang 8.1 überblicksartig) |

## Kernaussage

Die Arbeit definiert erstmals geschlossen das **Elementmodell „Wirkflächenpaare & Leitstützstrukturen“** (WFP & LSS), den Vorläufer des C&C²-Ansatzes. Jede technische Funktion wird auf die Interaktion in **Wirkflächenpaaren (WFP)** und den sie verbindenden **Leitstützstrukturen (LSS)** zurückgeführt, festgelegt in **drei Grundhypothesen**, mengentheoretisch formalisiert und auf **Festkörper, Fluide und Felder** übertragen. Ein **Connector** kommt noch nicht vor. Neben der Analyse (Zahnradpaare) wird eine erste **Synthesemethode** mit **Projektionswürfeln** und **Kraftflussregel** vorgestellt.

## Inhalte nach Abschnitt

### 0. Vorwort, Kurzfassung (PDF-S. 5 bis 15)
- Vorwort Albers: Forschungsgruppe arbeitet seit ca. 5 Jahren an der Frage nach dem kleinsten funktionalen Element (Reuleaux 1874). Kern sei die Rückführung der Funktion auf WFP, wichtig ist die **Multi-Skaligkeit** (Anlagen bis Werkstoffstruktur).
- Albers listet als Grundelemente Wirkfläche, Wirkflächenpaar, Funktionskontakt, Leitstützstruktur, Tragstruktur, Reststruktur und Wirkstrukturen (PDF-S. 8).
- Englischer Titel „Working Surface Pairs & Channel and Support Structures“ (PDF-S. 1), im Abstract „Channel Support Structures“ (PDF-S. 15).
- Kurzfassung: Elementmodell entstand aus „umfangreichen Untersuchungen realer konstruktiver Gestaltungsprozesse und systematischer Abstraktion“; Anwendung auf mechanische, fluidmechanische und feldbasierte Wirkprinzipien (PDF-S. 13). Keine Zahlen zu Stichproben.

### 1. Einleitung (S. 1 bis 4)
- Problem ist der Schritt vom Lösungsprinzip zur Gestalt methodisch unzureichend unterstützt. Gestaltung als Wechsel zwischen Synthese und Analyse, deshalb muss ein Denkmodell beides unterstützen.
- Anforderungen an das Modell: auf möglichst alle technischen Systeme übertragbar, dem Denken des Ingenieurs nahe, pragmatisch, umsetzungsorientiert, **fraktal** (S. 1 bis 2).
- Fundament ist die **Kausalität** (Ursache und Wirkung), Newtons drittes Axiom actio = reactio und die Reuleaux-Frage nach dem kleinsten Element, verstanden auf funktionaler Ebene (S. 2 bis 3).
- Modell soll als **„Leitfaden beim Denken“** dienen, ausdrücklich kein „Kochrezept“ (S. 2, S. 4).
- Praxisbezug: Patentanmeldungen und Neuprodukte in Industrieprojekten, Einsatz in der Lehre (S. 2), ohne Zahlenangaben.

### 2. Grundlagen und Stand der Technik (S. 5 bis 47)
- 2.1 Historie (S. 5 bis 25, überblicksartig): Reuleaux, Franke, Rodenacker, Roth, Ersoy, Koller, Jung, Hubka.
  - Rodenacker: Wirkflächen als „Grenzflächen, die zwei Medien voneinander trennen“, Beispiele Lager/Welle, Elektrode im Elektrolyt, Phasengrenze Wasser/Wasserdampf im Dampfkessel (S. 13). Wirkflächenpaare auch ohne Berührung (Keilspalt, S. 14).
  - Roth: WFP als zwei sich berührende Wirkflächen (Getriebelehre, Elementenpaare), dazu „Kraftleitungsstruktur“ (S. 19).
  - Ersoy (Schüler Roths): Wirkraum, Wirkfläche, Restkonturflächen; Wirkflächen treten paarweise auf (S. 19 bis 20).
  - Hubka: Kopplung von Systemen (seriell, parallel, Rückkopplung), „Wirkstelle“ als Raum, Fläche, Linie oder Punkt (S. 23 bis 24).
- 2.2 Einordnung (S. 26 bis 30): Nutzen immer dann, wenn Gestalt beachtet werden muss; Schwerpunkt Entwurfsphase, besonders Arbeitsabschnitte 5.1, 5.2 und 6.1 bis 6.5 nach VDI 2223 (S. 28; Abb. 10 VDI 2221, Abb. 11 VDI 2223).
- 2.3 Abgrenzung (S. 31 bis 34): Roths Modelle nur für mechanische Energiefunktionen und schwer ohne EDV nutzbar; Jung bleibt abstrakt. Begriffe Wirkort, Wirkstelle, Wirkfläche, WFP, Kraftleitungsstruktur werden „exakt definiert, erweitert, auf Fluide und Felder übertragen“ und um Leitstützstruktur, Reststruktur, Begrenzungsfläche ergänzt (S. 33). Methode soll ohne Kataloge auskommen (S. 32).
- 2.4 Modellbildung (S. 34 bis 35): Modellzweck steht im Vordergrund. Fazit in fünf Punkten, u. a. sind Modelle nur „brauchbar oder unbrauchbar“ (S. 35).
- 2.6 Synthese (S. 36): kleinste beim Konstruieren zusammengesetzte Einheiten sind WFP und die damit verbundene LSS.
- 2.7 Funktion (S. 36 bis 47): Funktionsbegriffe verschiedener Autoren (Tabelle S. 37). Festlegung nach VDI 2221 als lösungsneutrale Beziehung zwischen Eingangs- und Ausgangsgröße; Verhalten ist im Funktionsbegriff integriert; Formulierung darf „weicher“ sein, da jede Funktion auf WFP und LSS zurückführbar ist (S. 46 bis 47).

### 3. Das Elementmodell technischer Systeme (S. 48 bis 103), Kernkapitel
- **3.1 Definitionen (S. 48 bis 52)**, jeweils mit Kürzel:
  - **Wirkfläche WF** (S. 49): feste Oberflächen von Körpern oder „generalisierte“ Grenzflächen von Flüssigkeiten, Gasen oder Feldern, dauernd oder zeitweise in Kontakt zu einer weiteren WF, beteiligt am Energie-, Stoff- und Informationsaustausch. Jeder Austausch geschieht über WF; WF sind bei höherer Auflösung in kleinere WF zerlegbar.
  - **Begrenzungsfläche BF** (S. 50): Oberflächen oder Grenzflächen, die nie WF sind, damit funktionslos. Fußnote 158: BF ist nur „aus einer Willensbildung heraus“ definierbar, der Entwickler entscheidet.
  - **Wirkflächenpaar WFP** (S. 50): aus **genau zwei** WF gebildet, zeitweise ganz oder teilweise in Kontakt, Übertragung von Energie, Stoff und Information; kann temporär existieren.
  - **Funktionskontakt FK** (S. 50): Teil des WFP, in dem aktuell die Wechselwirkung stattfindet (kann das ganze WFP sein).
  - **Leitstützstruktur LSS** (S. 51): Volumina von Körpern, Flüssigkeiten, Gasen oder felddurchsetzte Räume, die **genau zwei** WFP verbinden und Leitung von Energie, Stoff oder Information ermöglichen. Tritt nur zusammen mit WFP auf. Fußnote 159: Bereich der LSS nur aus Willensbildung festlegbar.
  - **Tragstruktur TS** (S. 51): Menge aller möglichen LSS; definiert das funktionsrelevante Volumen.
  - **Reststruktur RS** (S. 51): Volumina, die nie Tragstruktur werden; funktionslos, oft aus Fertigungs- oder Kostengründen belassen (Bezug Topologieoptimierung).
  - **Wirkstruktur** (S. 51): Menge aller WF und LSS eines Systems, Teilsystems oder Bauteils; definiert alle Elemente, die das funktionale Verhalten beeinflussen.
  - **Einordnung (Abb. 16, S. 52)**: Matrix Flächen-/Körperelemente × Bauteil-/Systemebene. Bauteilebene (WF, BF, TS, RS) existiert „zu jeder Zeit“ und legt Gestalt fest; Systemebene (WFP, FK, LSS) nur im Zusammenspiel mit einem Obersystem identifizierbar, „temporäres Auftreten möglich“, legt Funktion fest.
- **3.2 Wirkung und Funktion (S. 52 bis 53)**: Funktion ist wirkungsauslösend; Wirkung nur zwischen wechselwirkenden Partnern; die Schnittstelle dazwischen „ist das Wirkflächenpaar!“ (S. 53).
- **3.3 Grundhypothesen (S. 53 bis 55)**: genau drei.
  - GH I: Grundelement erfüllt Funktion durch Wechselwirkung mit mindestens einem anderen Grundelement; eigentliche Funktion erst durch Kontakt zweier Flächen (WF bilden WFP). Fußnote 163: mehrere Grundelemente können ein Bauteil bilden (zwei verschweißte Bleche).
  - GH II: Funktion über **mindestens zwei WFP und eine sie verbindende LSS**; funktionsbestimmend allein deren Eigenschaften und Wechselwirkungen; bei Feldern zusätzlich Wechselwirkung der Feld-LSS mit mindestens zwei weiteren LSS; WFP und LSS sind einzige Ursache der Wirkung auf die Umgebung.
  - GH III: Jedes funktionserfüllende System besteht aus WFP und LSS in beliebiger Anzahl, Anordnung und Form; WFP aus genau zwei WF. Beantwortet laut Autor die Reuleaux-Frage, das kleinste Element liegt **zwischen** den Körpern (S. 55).
- **3.4 Systembetrachtung (S. 55 bis 56)**: Bauteil besteht aus Wirkstruktur, Reststruktur, Begrenzungsfläche; Wirkstruktur enthält WF und Tragstruktur. Systeme werden über mindestens zwei WFP gekoppelt; gekoppelte Systeme der Ebene n bilden ein System der Ebene n+1 (Abb. 17, Mengendarstellung, Hierarchiestufen 2 bis 5).
  - **Fraktaler Charakter (S. 56)**: beim Getriebe als Black-Box liegen WF an Wellen, Flanschen, Füßen, der „Rest“ gilt als LSS; weitere WF erst nach Öffnen der Black-Box sichtbar.
- **3.5 Mengentheorie (S. 57 bis 58)**:
  - Gl. (1) TF = f{WFP_i; LSS_j} mit n ≥ 2 WFP und m ≥ 1 LSS.
  - Gl. (2) {WF_k1; WF_l2} ∈ WFP_i; eine WF kann Element mehrerer WFP sein (Gl. 3 bis 6).
  - Gl. (7) Wirkung des WFP ist allein Funktion der Wirkungen der beiden WF.
- **3.6 Eigenschaften und Wechselwirkungen (S. 59 bis 66)**:
  - Geschlossener **Wirkungskreis** bei ausreichend weiter Systemgrenze (Abb. 18, S. 61; erweitert Abb. 19, S. 65).
  - Gleichungsübersicht für ein Datenmodell:
    - (7) W_WFP = f{W_WF1, W_WF2}
    - (8), (9) W_WF = f{GEO_WF, STO_WF, W_LSS}
    - (10), (11) W_LSS = f{GEO_LSS, STO_LSS, W_WF, W_LSS,ki}
  - Physikalischer **Zustand** (Zustandsgrößen, Thermodynamik) wird aufgenommen; empfohlen ist, die resultierende Eigenschaft zu modellieren (Temperatur der WF → momentane Härte), S. 59 bis 60.
  - Kräfte im WFP senkrecht zur WF oder parallel über Reibung (S. 60).
  - Zu WF. Punkt- und Linienkontakt sind nur Modellvorstellung; Begründung „genau zwei WF“ geometrisch (keine Durchdringung von drei Flächen), S. 62. Gl. (8) W_WF = f{E_WF; W_LSS}, Gl. (9) mit GEO_WF und STO_WF.
  - Zu LSS. Sie verbindet zwei WFP, leitet Energie/Stoff/Information, definiert geometrische Lage der WFP, kann **speichern** (kinetische Energie, elastische Energie, chemische Energie, Wärme) und wird so **Effektträger**; Reststruktur nie Effektträger (S. 63). Gl. (10) und (11) W_LSS = f{GEO_LSS; STO_LSS; W_WF; W_LSS,ki}, Wechselwirkung benachbarter LSS bei Feldern oder im selben Körper (S. 64, 66).
- **3.7 Beispiele (S. 66 bis 83)**:
  - Portal stationär (Abb. 20, 21): linke Säule, WFP1 (Säulenauflage/Traverse), WFP2 (Säulenunterfläche/Fundament), LSS1, BF1, TS1, RS1 (S. 67 bis 68). Ist die Optik funktionsrelevant, wird die Oberfläche WF (S. 68).
  - **Veränderung von Randbedingungen** (S. 68 bis 71): Windlast macht BF zur WF und verändert LSS1; Konstrukteur dimensioniert die Tragstruktur. **Korrosion** im Meerwasser (Ölbohrinsel) als unerwünschte Funktion mit WFP1 (Salzwasser/Säule), WFP2 (LSS/reaktives Molekül), LSS1 (Abb. 22). Abhilfen: WFP1 aufheben, WFP2 aufheben, LSS entfernen oder Eigenschaften ändern; konstruktiv Lackschicht (zwei neue WFP plus neue LSS), rostfreier Werkstoff, kathodischer Schutz bzw. Opferanode.
  - **Veränderung der Auflösung** (S. 71 bis 75): Flächenpressung σ = F/A (Gl. 12 bis 14); bei höherer Auflösung zerfällt WFP1 in WFP1 bis WFP3 mit A* < A (Abb. 23); Schraubenverbindung VDI 2230 (Setzen); ZrO2-Mikrozahn mit ca. 11 Körnern, Anisotropie verändert LSS (Abb. 24).
  - Getriebemotor quasistationär (S. 75 bis 79): Hauptfunktion „Wandeln von elektrischer Energie in mechanische Energie“; Teilfunktionen TF1 bis TF4, Elementarfunktionen; Drehmomentübertragung braucht mindestens ein zweites WFP mit parallelversetzter Gegenkraft (S. 77; Abb. 27, 28).
  - Schwungrad dynamisch (S. 80 bis 83), Randbedingungen Reibung vernachlässigbar, Kupplung dauernd geschlossen, konstante Fahrgeschwindigkeit (S. 81). WFP2 ist die Flanschverbindung zur Kurbelwelle, WFP1 die Reibbelagsoberfläche zur Kupplung.
  - Am Schwungrad werden drei Betriebszustände unterschieden (Energieaufnahme, konstant, Energieabgabe), die LSS wirkt als Energiespeicher (Abb. 30). Abgeleitete Grundsätze: Teile, die Energie speichern, sind LSS; verbundene WFP können zeitlich nacheinander auftreten; zeitversetzte WFP können in **einem** WFP zusammenfallen (S. 83).
- **3.8 Fluide (S. 83 bis 86)**: Fluid nach Dubbel (Flüssigkeiten, Dämpfe, Gase). Hydrodynamisches Radialgleitlager (Abb. 31) in drei Fällen (n = 0, groß, unendlich). Mit steigender Drehzahl löst sich der Festkörperkontakt WFP1 auf, die Radialkraft läuft dann über WFP2, LSS1 (Schmierfilm) und WFP3. **Viskosität η ist Eigenschaft der LSS**, Haftung (Adhäsion) ist Eigenschaft des WFP bzw. der Fluid-WF im Bezug zum Kontaktpartner. Im Fazit passen Fluid-WF ihre Gestalt dem Kontaktpartner an; dasselbe Fluidvolumen kann zu verschiedenen Zeitpunkten WF oder LSS sein (S. 86).
- **3.9 Felder (S. 86 bis 103)**: Gravitationsfeld, elektrostatisches Feld, magnetisches Feld.
  - Der die Fernwirkung übertragende Raum wird als **Tragstruktur** definiert, Feldgröße (g, E, B) ist Stoffeigenschaft der LSS (S. 90, 95).
  - Bezeichnung (Abb. 33, S. 92): Körperoberfläche WF1, „generalisierte Oberfläche“ des Feldes WF2 bzw. WF3, zweiter Körper WF4, felddurchsetzter Raum LSS2. Ein Körper mit eigenem Feld allein hat keine Funktion.
  - Fernwirkung geht von LSS aus und wirkt direkt auf eine andere LSS, setzt aber zwei WFP voraus (S. 95). „Die Existenz einer Leitstützstruktur ist nicht an Materie gebunden“ (S. 95).
  - Magnetfeld als „Grundlage aller elektrischen Energiemaschinen“ (S. 100); Spannungsinduktion als Größenänderung der LSS (S. 101). Übertragbar auf elektromagnetische Strahlung (S. 103).

### 4. Funktionsanalyse mit dem Elementmodell (S. 104 bis 119)
- Zwecke der Funktionsanalyse: Fehlererkennung, Schwachstellenanalyse, Weiterentwicklung, Produktdokumentation, Wettbewerbsanalyse, Funktionskosten (S. 104).
- **Zahnradpaar εα = 1,0** (Z1 = 16, Z2 = 25, Eingriffswinkel 20°, Passfederverbindung; Abb. 34 bis 36):
  - Quasistationär n = 2 WFP und eine LSS, TF = f{WFP1; WFP2; LSS1}, Nebenbedingung 0 ≤ m ≤ n − 1 (S. 106).
  - Systemgrenze kann WFP „wegschneiden“ (Ersatz durch Schnittgrößen), S. 106.
  - Dynamisch: theoretisch 25 × 16 = 400 mögliche Zahnflanken-WFP, daher **Benennungskonvention** WF_a1, WF_b2, WFP_{k1;l2}, LSS_{b2;c3} (S. 107 bis 109).
  - Funktionskontakt wandert auf der Evolvente; LSS-Geometrie und Steifigkeit ändern sich (S. 110). Nie kontaktierte Flankenanteile heißen „Restfläche“ (S. 110).
  - **Problemspezifische Vereinfachung**: wirkungsgleiche WFP dürfen gleich benannt werden; alle über eine Umdrehung entstehenden LSS ergeben die Tragstruktur (S. 112). Ist kinetische Energie funktionsrelevant, ist der ganze Körper LSS (Fußnote 217, S. 113).
- **Zahnradpaar εα > 1,0** (Abb. 37 bis 39): zeitweise n = 3 WFP und zwei LSS, parallelgeschaltete WFP, gegenseitige Beeinflussung der LSS im selben Körper (S. 115 bis 118). **Neues Zeitintervall bei Bildung oder Auflösung eines WFP** (S. 117). Wechsel zwischen zwei und drei WFP erklärt Schwingungen (S. 119).

### 5. Synthese mit dem Elementmodell (S. 120 bis 141)
- Von der Funktion ist keine eindeutige Gestalt ableitbar (Beispiel „Drehmoment wandeln“ mechanisch per Zahnradpaar oder hydraulisch per Föttingerwandler, S. 120), aber Gemeinsamkeiten im Bereich der WFP sind erkennbar.
- **Grundsätze**: orthogonale Parallelprojektion einer WF auf höchstens drei Bildebenen, Umkehrung nicht eindeutig (S. 121); **Kraftflussregel**: Kräfte im Funktionskontakt normal zum WFP oder parallel über Reibung, jede andere Richtung als Vektorsumme (S. 122).
- Konstrukteur legt zuerst WFP, dann verbindende LSS fest (S. 122). Einordnung in VDI 2223 Abschnitte 4 bis 5.3 (S. 123).
- **Vorgehen** (S. 123 bis 124): WF zunächst ohne geometrische Erstreckung; **Projektionswürfel** (6 Seiten = mögliche Projektionsebenen); zwei Würfel symbolisieren ein WFP; je Elementarfunktion anordnen, dann zum System zusammenfügen (Interaktionen schränken Lagen ein), dann auf reale WFP-Gestalt schließen. Erfahrungsschritte („scheinbar selbstverständliches Vorgehen“) kursiv markiert.
- **Beispiel Rührmaschine einer Großbäckerei, Welle 2** (Abb. 41 bis 56): Höhenverstellung 150 mm im Betrieb; Funktionsstruktur mit HF, NF, EF4 bis EF9 (Abb. 42), getrennt nach System- und Bauteilebene. Elementarfunktionen laut Abb. 42 (Zuordnung aus der Textextraktion, unsicher):
  - EF4 Aufnahme des Drehmomentes von Tellerrad Z2
  - EF5 Abgabe des Drehmomentes in die Welle-Nabe-Verbindung des Rührers
  - EF6 Rotation ermöglichen
  - EF7 Axialkraft von Höhenverstellung auf Welle 2 übertragen
  - EF8 Radialkraft über Lagerung aufnehmen bzw. abgeben
  - EF9 Axialkraft nicht über Lagerung aufnehmen
  - Hinweis: Im Fließtext sind die Bezeichnungen von EF6 und EF8 teils vertauscht (S. 130, 133).
  - Die systematische Prüfung der Würfelseiten kann fehlende Funktionen aufdecken (Beispiel EF9, S. 131). Je EF wird über Funktionsprinzip (mechanisch) und Schlussart (formschlüssig) entschieden. Schraffur markiert nötige Projektionsebenen, Linienkreuz ausgeschlossene. Zwei WFP für Kraft in zwei Richtungen (S. 128, 132). Für die Lagerstellen ergibt sich als einzig mögliche Gestalt ein Paar koaxialer Zylindermantelflächen (S. 137). Danach Iterationen aus Analyse und Synthese (Abb. 55, 56).
- Methode laut Fußnote 225 auch für hydraulische WFP nutzbar (S. 127).
- Im Fazit heißt es, die Methode werde kaum als Ganzes angewendet, hilft bei Blockaden; positive Lehrerfahrungen (S. 141), ohne Zahlen.
- Hinweis: S. 4 kündigt als Beispiel eine „schaltbare Kupplung“ an, im Text steht die Rührmaschinenwelle.

### 6. Zusammenfassung und Ausblick (S. 142 bis 144)
- Modell gilt für alle technischen Systeme, fraktal, ohne Rechner nutzbar, unterstützt Konstruktion mit Black-Boxes.
- Weiterentwicklungsbedarf vor allem bei der Synthese. Modell ist Grundlage des **Karlsruher Lehrmodells für Produktentwicklung (KaLeP)**; Arbeiten zu Konstruktionsregeln laufen an (S. 143).

### 7. bis 8. Literatur und Anhang (S. 145 bis 158)
- Anhang 8.1: Begriffstabelle (Begriff, Quelle, Erklärung), eigene Einträge u. a. zu Fernwirkung, Funktion, technischer Funktion TF, WF, WFP.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Elementtypen WF, BF, WFP, FK, LSS, TS, RS, Wirkstruktur mit Kürzeln (S. 49 bis 51) | Datenmodell mit festen Elementklassen und Kürzel-Präfixen für automatische Benennung |
| Bauteilebene (permanent) vs. Systemebene (temporär möglich), Abb. 16 | Attribut „Ebene“ und „Existenz: dauernd/temporär“; getrennte Ansichten Bauteil und System |
| WFP besteht aus genau zwei WF; LSS verbindet genau zwei WFP (S. 50 bis 51) | Prüfregeln beim Speichern: Kardinalität WFP = 2 WF, LSS = 2 WFP; Warnung bei Verletzung |
| GH II, Gl. (1) n ≥ 2, m ≥ 1, 0 ≤ m ≤ n − 1 | Vollständigkeitscheck je Funktion: mindestens zwei WFP und eine LSS; Ausnahme „zeitversetzt zusammenfallende WFP“ als Flag |
| Eine WF kann mehreren WFP angehören (Gl. 3 bis 6) | WF als eigenständiges Objekt mit n:m-Zuordnung zu WFP |
| Eigenschaften GEO/STO, gespeicherte Energie/Stoff/Information (Gl. 9, 11) | Eigenschaftsfelder je WF und LSS (Geometrie, Stoff, Speicher), z. B. Viskosität, Steifigkeit, Härte |
| BF und LSS-Bereich „aus Willensbildung“; BF wird unter neuen Randbedingungen WF (S. 50, 69) | Lastfall/Randbedingungs-Varianten; Hinweis-Dialog „Kann diese BF unter Lastfall X zur WF werden?“ |
| Auflösung der Betrachtung, fraktaler Charakter, Black-Box (S. 56, 71 bis 75) | Zoom-Hierarchie: WFP verfeinern in Unter-WFP; Black-Box-Knoten mit WF an der Grenze |
| Neues Zeitintervall bei Bildung oder Auflösung eines WFP (S. 117); Benennungskonvention WFP_{k1;l2} | Zeitachse mit automatisch erzeugten Intervallen; Indexschema für wiederkehrende WFP (Zahneingriff) |
| Korrosionsbeispiel: WFP aufheben, LSS entfernen/ändern, WFP einfügen (S. 70 bis 71); Projektionswürfel, Kraftflussregel (S. 121 bis 137) | Synthese-Assistent mit Änderungsoperatoren je Element und Projektionswürfel-Skizze (Schraffur = erforderlich, Kreuz = ausgeschlossen) |

## Im Paper zitierte Schlüsselquellen
Albers & Matthiesen 2002 (Konstruktion 54, H. 7/8, Grundmodell WFP & LSS, im Text Alb02/1), Albers & Matthiesen 1999/2000 sowie Albers, Burkardt, Matthiesen, Schweinberger 2000 (KaLeP, Karlsruher Lehrmodell), Albers 2000 (Skriptum Maschinenkonstruktionslehre I, Portal-Beispiel), Albers et al. 2001/2002 (Mikrozahnräder ZrO2, Leitstützstruktur bei Anisotropie), Roth 1982 (Konstruieren mit Konstruktionskatalogen, WFP, Kraftleitungsstruktur), Ersoy 1975 (Diss., Wirkfläche, Wirkraum), Rodenacker 1970/1973 (Wirkflächen als Grenzflächen), Koller 1976 (Wirkfläche, Effektträger), Hubka 1973/1984 (Kopplung, Wirkstelle), Jung 1989 (Geometrie-Funktionsprinzip), Reuleaux 1875 (kleinste Elemente), VDI 2221, VDI 2223, VDI 2803.
