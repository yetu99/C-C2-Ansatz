# Albers et al. 2003: Neues Basismodell für Analyse und Synthese (C&CM)

| Feld | Wert |
|---|---|
| Autoren | A. Albers (o. Prof. Dr.-Ing. Dr. h. c.), S. Matthiesen (Dr.-Ing.), M. Ohmer (Dipl.-Ing.); Corresponding author Manfred Ohmer, University of Karlsruhe (TH), Institute of Machine Design and Automotive Engineering (mkl) |
| Titel | An innovative new basic model in design methodology for analysis and synthesis of technical systems |
| Quelle/Reihe | International Conference on Engineering Design, ICED 03, Stockholm, August 19-21, 2003; Seiten im Tagungsband und DS-Nummer im PDF nicht angegeben (Beitrag intern S. 1 bis 10) |
| Jahr | 2003 |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2003a), nicht im Repo (Lizenz) (10 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag stellt das **Elementmodell C&CM** (Contact & Channel Model, "Working Surface Pairs & Channel and Support Structures", deutsch **Wirkflächenpaare (WFP) & Leitstützstrukturen (LSS)**) als neues Modell für **Analyse und Synthese** vor. Jede technische Funktion wird WFP und den sie verbindenden LSS zugeordnet, und zwar **Wirkflächenpaaren** und keinen einzelnen Wirkflächen. Eine "basic proposition" lautet, dass jede Funktion **mindestens zwei WFP und eine LSS** braucht. Zwei Beispiele (Nietverbindung bis Schraubverbindung, Keramik-Pin im CVT) zeigen regelbasierte Synthese auf abstrakter Ebene.

## Inhalte nach Abschnitt

Seitenangaben = interne Seitenzahlen des Beitrags (identisch mit PDF-S.).

### 1. Objectives (S. 1 bis 2)
- Produktentwicklung als Wechsel von Synthese und Analyse (Bezug Lindemann und Pulm 2001).
- Forschung am mkl (Institute of Machine Design and Automotive Engineering, Universität Karlsruhe) "Since 1997".
- Anspruch ist die Übertragbarkeit auf Systeme mit Fluiden und Gasen sowie auf Feldeffekte, das Modell sei "obvious, pragmatical, easy to realise and fractal".

### 2. The Element Model C&CM (S. 2 bis 4)
- Analysen realer Konstruktionsprozesse ergaben, dass ein allgemeiner Zusammenhang von Funktion und Gestalt nur über die kleinsten funktionalen Elemente auffindbar ist. Modell hat **fraktalen Charakter**.
- Bezeichnung "Element Model", weil WFP und LSS allen technischen Systemen gemeinsam sind. Grundlagen vollständig in [1] Albers und Matthiesen 2002 und [2] Matthiesen 2002.
- Regeln sind in "basic hypotheses" gefasst (S. 2). Genannt wird nur eine "basic proposition" (S. 3).
- WFP = generalisierte Oberflächen, die durch Wechselwirkung die Funktion erzeugen. LSS = "the volumes linking them". Beides für Festkörper, Fluide, Gase und Felder definiert.
- Funktion wird in WFP und LSS durch Austausch und Speicherung der Systemgrößen Stoff, Energie, Information erfüllt.
- Idee des WFP aus der Konstruktionsmethodik übernommen und von Festkörpern auf Fluide und Felder erweitert (S. 3).
- Fig. 1 Stirnradstufe: WFP1 zwischen Zahnflanken (aus WF1 und WF2), WFP2 an der Passfederflanke, LSS = Radkörper. Entfernt man ein WFP, entfällt die Funktion.
- Funktion ist WFP zugeordnet und keinen einzelnen Wirkflächen, "a technical function only exists as long as the associated Working Surface Pairs are existing" (S. 3).

### 3.1 Anwendung: Herleitung einer Schraubverbindung (S. 4 bis 6)
- Zwei überlappende Platten, Kraft F parallel, WFP1 zwischen den Platten. Reibkraft nach Coulomb FR = µ · FN (Gl. 1) erfordert Normalkraft.
- Normalkraft nur über zwei WFP und eine verbindende LSS erzeugbar. Lösung Niet mit WFP2 (oben) und WFP3 (unten), Nietkörper als LSS (Fig. 3).
- Zusatzfunktion "lösbar" durch neues WFP4 im Winkel, das den Niet teilt, Verschieben von LSS3,4 stellt die Normalkraft ein (Fig. 4). Aufrollen des WFP um die Nietachse ergibt die Schraubverbindung.
- Weitere Anforderungen erfüllbar durch Ändern von Anordnung oder Eigenschaften von WFP und LSS oder durch zusätzliche WFP und LSS (S. 5).

### 3.2 Anwendung: Reibkontakt Pin-Scheibe im CVT (S. 6 bis 8)
- Umschlingungs-CVT mit Wiegedruckstücken (Pins) und Kegelscheiben (Fig. 5, 6). SFB 483 "High performance sliding and friction systems based on advanced ceramics".
- Hybridlösung Keramikscheibe und Metallpin verschleißt am Pin. Keramikpin scheitert an Biegung in der LSS "Pin".
- Widerspruch WFP-Anforderung (Keramik) vs. LSS-Anforderung (Metall). Regel auf C&CM-Ebene "For solving a conflict that is due to different requirements in the used material, an additional WFP can be introduced." (S. 7)
- Klebung erzeugt zwei neue WFP (Keramik-Kleber, Kleber-Metall). Wegen Schub zusätzlich Formschluss durch Keramik-Inlays mit WFP4 parallel zur Pinachse (Fig. 7).

### 4. Key Conclusions (S. 9)
- Anwendbar in Analyse bestehender und Synthese neuer Systeme, leicht erlernbar, unterstützt Black-Box-Konstruktion.
- In Industrieprojekten validiert, mehrere Patentanmeldungen und neue Produkte (ohne Zahlen).
- Grundlage des Karlsruher Lehrmodells KaLeP.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Funktion ist an WFP gebunden und existiert nur, solange das WFP existiert | Datenmodell Funktion → Liste von WFP; Löschen eines WFP markiert abhängige Funktionen als gefährdet |
| Mindestens zwei WFP und eine LSS je Funktion | Prüfregel bei Funktionszuordnung |
| Fig. 1 Zahnrad (WF1, WF2 → WFP1) | Lernbeispiel und Vorlage "Zahnradstufe" |
| Coulomb-Bedingung im WFP (Kraft parallel braucht Normalkraft) | Attribut Kraftrichtung je WFP (parallel = Reibschluss, orthogonal = Formschluss) mit Hinweis auf benötigte Normalkraft |
| Regel "Materialkonflikt → zusätzliches WFP" | Heuristik-Katalog mit Auslöser (Konflikt in Werkstoffanforderung) und Vorschlag |
| Benennung LSS3,4 nach verbundenen WFP | automatische Benennung von LSS aus den Indizes der verbundenen WFP |
| Fluide, Gase, Felder als WFP-Partner | Medium-Attribut je Wirkfläche (fest, flüssig, gasförmig, Feld) |

## Im Paper zitierte Schlüsselquellen
Albers und Matthiesen 2002 (Konstruktion 54, Grundmodell WFP und LSS), Matthiesen 2002 (Diss., Basisdefinition), Pahl und Beitz 1997, Roth 1994, Albers/Burkardt/Matthiesen 2001 und Albers/Matthiesen 1999, 2000 (KaLeP), Lindemann und Pulm 2001 (ICED, funktionale Produktstrukturierung).
