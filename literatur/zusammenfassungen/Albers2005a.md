# Albers et al. 2005: Syntheseansätze im Contact and Channel Model

| Feld | Wert |
|---|---|
| Autoren | A. Albers, N. Burkardt, M. Ohmer (Kontakt o. Prof. Dr.-Ing. Dr. h.c. Albert Albers, University of Karlsruhe (TH), IPEK Institute of Product Development) |
| Titel | Approaches for the synthesis of technical systems within the Contact and Channel Model C&CM |
| Quelle/Reihe | International Conference on Engineering Design, ICED 05, Melbourne, August 15-18, 2005; Seiten im Tagungsband und DS-Nummer im PDF nicht angegeben (Beitrag intern S. 1 bis 11) |
| Jahr | 2005 |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2005a), nicht im Repo (Lizenz) (11 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag beschreibt, wie Konstruktionsprinzipien, Richtlinien und Regeln aus der Literatur (u. a. Pahl/Beitz, Roth, TRIZ) auf die Abstraktionsebene des C&CM übertragen und zu einem konsistenten Satz von **Heuristiken** zusammengeführt wurden. Diese Heuristiken sind nach **vier Anwendungsmustern** (patterns of application) geordnet: **Hinzufügen** und **Entfernen** von WSP und CSS sowie **Eigenschaften von WSP** bzw. **von CSS ändern**. Zusätzlich wird eine **Zeichnungssymbolik** für Eigenschaften von WSP und CSS nach dem Vorbild der DIN ISO 1101 vorgestellt. Die Definitionen legen fest, dass eine **CSS genau zwei WSP verbindet** ("connect only two").

## Inhalte nach Abschnitt

Seitenangaben = interne Seitenzahlen des Beitrags (identisch mit PDF-S.).

### 1. Introduction (S. 1)
- "Elementary Design Model C&CM (Contact and Channel Model)" beschreibt den Zusammenhang von Funktion und Gestalt über **Working Surface Pairs (WSP)** und **Channel and Support Structures (CSS)**. Entwicklung am IPEK "since 1999".
- Prinzipien existieren teils auf Funktionsebene (Aufgabenteilung), teils auf Gestaltebene (Kraftleitung). Das C&CM soll beide verbinden.

### 2. C&CM (S. 1 bis 3)
- C&CM als "thinking model", gleichzeitiger Blick auf Funktion und Gestalt.
- **2.1 Basics**: Idee ursprünglich aus [3] Albers und Matthiesen 2002, aufbauend auf Reuleaux (im Original "Releaux"), Rodenacker, Roth, Koller, Hubka.
- Vier Definitionen (S. 2): WSP (paarweise Schnittstellen zwischen Komponenten bzw. Komponente und Umgebung, Festkörper, Flüssigkeiten, Gase, Felder, permanenter oder gelegentlicher Kontakt), CSS (Komponenten oder Volumina, "which connect only two Working Surface Pairs", leiten und speichern Systemgrößen, Beispiel Massenträgheit), Limiting Surfaces LS (potenzielle Wirkflächen, Beispiel Seite der Kransäule bei Wind), Remaining Structures RS (funktionslos, Beispiel fertigungsbedingte Teile eines Gussgehäuses).
- Fig. 1 abstrakte Produktbeschreibung (Kran).
- Funktion ausschließlich durch Eigenschaften der WSP und CSS bestimmt. Eigenschaften umfassen Werkstoff, Fläche/Volumen, Relationen zu anderen Elementen, physikalische und chemische Eigenschaften (S. 3).
- Anwendbar auf Ölfilm eines Gleitlagers und Magnetfeld eines Elektromotors (S. 3).
- Neben "basic hypotheses and definitions" enthält das Modell Werkzeuge und Methoden (Wortlaut der Hypothesen nicht wiedergegeben).

### 2.2 C&CM Heuristics (S. 4 bis 5)
- Prinzipien aus Pahl/Beitz [9], TRIZ nach Terninko et al. [13], Roth [12] analysiert, verglichen, klassifiziert, teils kombiniert, viele neue gefunden.
- Table 1 Beispielheuristik "Create a Detachable Connection" mit den Lösungen "Frictional Working Surface Pair is to be added" oder "elasticity" einer CSS erhöhen; Beispiele Klemm- bzw. Schraubverbindungen und Schnappdeckel.
- Neue Richtlinien aus neuen Technologien, z. B. "micro-oriented" für Mikrotechnik [2].
- Kopplung zwischen Originalprinzip und C&CM-Heuristik wird dokumentiert, Wechsel zwischen Abstraktionsebenen möglich.
- **Vier Anwendungsmuster** (S. 4 bis 5): 1. Adding WSP and CSS, 2. Removing WSP and CSS, 3. Changing the properties of WSP, 4. Changing the properties of CSS. Weitere Klassifikation nach gleicher Absicht oder gleichen Handlungen möglich.

### 2.3 C&CM Drawings (S. 5 bis 6)
- Symbolsatz zur Dokumentation von WSP- und CSS-Eigenschaften, Aufbau ähnlich DIN ISO 1101: jede Eigenschaft in einem Kästchen, links Art der Eigenschaft, rechts zunehmend detaillierte Angaben. **Abgerundete Ecken** zur Unterscheidung von DIN ISO 1101.
- Fig. 2 Beispiel WSP zwischen **Kolben eines Hydraulikzylinders und Fluid** in der Kolbenkammer. Erste Zeile Elementtyp (WSP vs. CSS) und Aggregatzustand der beiden Wirkflächen (fest, flüssig).
- Fig. 3 erweiterte Angaben: zweite Zeile hauptsächlich übertragene Systemgröße (Energie, mechanisch, Kraft orthogonal zum WSP, also Formschluss), dritte Zeile Relativbewegung (keine), unterste Zeile Kontaktart (permanent; Ventile hätten Kontakt zu diskreten Zeitpunkten). Weitere vordefinierte oder selbst definierte Symbole möglich.

### 3. Example of application (S. 7 bis 9)
- Rührwerk, Welle 2 soll während des Betriebs auf und ab bewegt werden (Fig. 4).
- Table 2 Heuristik "Add an additional function to an existing system": mindestens ein zusätzliches WSP einfügen oder Eigenschaften eines bestehenden WSP ändern.
- Vorgehen (Fig. 5, 6): zuerst Funktion des neuen WSP festlegen ("Move the rotating shaft in vertical direction and fix it on definite positions"), dann übertragene Größen (Kraft, Positionsinformation), Relativbewegung, Aggregatzustand (beide fest), Formschluss, daraus geometrische Orientierung. Gleitkontakt überträgt nur Druck, daher zweites, entgegengesetzt orientiertes WSP. Ergebnis ähnelt Schaltgabel eines Handschaltgetriebes.
- Jede Lösungsidee ist direkt dokumentiert und jede funktionale Spezifikation hat ein geometrisches Gegenstück (S. 9).

### 4. Conclusions and Future Research (S. 10)
- Heuristik "Add a new Working Surface Pair" war zentral für Keramik im CVT (Sonderforschungsbereich).
- Nächste Schritte: Strategie zur Auswahl der passenden Heuristik, Symbole für komplexe Effekte mit mehreren WSP (z. B. Keilwellen-Effekt, "spline effect").

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| CSS verbindet "only two" WSP | Kardinalitätsregel im Datenmodell (CSS genau zwei WSP) |
| WSP auch zwischen Komponente und Umgebung | Element "Umgebung" als Partner eines WSP (Vorstufe Connector) |
| LS als potenzielle Wirkfläche, RS als funktionslose Masse | Elementtypen mit Statuswechsel (LS → WF bei neuem Lastfall, RS als Leichtbaupotenzial) |
| Eigenschaftsliste (Material, Fläche/Volumen, Relationen, physikalisch-chemische Eigenschaften) | Attributschema je WSP und CSS |
| Symbolkästchen nach DIN ISO 1101 (Elementtyp, Aggregatzustand, Systemgröße, Kraftrichtung, Relativbewegung, Kontaktdauer) | Eigenschafts-Badge je Element im Diagramm, strukturierte Felder mit Enum-Werten |
| Vier Anwendungsmuster | Synthese-Assistent mit vier Aktionen und verknüpftem Heuristik-Katalog |
| Heuristik-Tabellen (Problem, Lösungen, Beispiel) | Heuristik-Datenbank mit Rückverweis auf Originalprinzip (Pahl/Beitz, TRIZ, Roth) |
| Hydraulikzylinder Kolben-Fluid, Ölfilm Gleitlager, Magnetfeld Motor | Lernbeispiele für Wasser- und Energietechnik (fest-flüssig-WSP, Feld-WSP) |

## Im Paper zitierte Schlüsselquellen
Albers und Matthiesen 2002 (Konstruktion 54, Ursprung der Idee), Matthiesen 2002 (Diss., Basisdefinition), Albers, Matthiesen und Ohmer 2003 (ICED 03), Albers, Marz und Burkardt 2003 (Mikrotechnik), Pahl und Beitz 1995, Roth 1994, Terninko et al. 1998 (TRIZ), Hubka 1984, Koller 1998, Rodenacker 1991, Reuleaux und Moll 1854, DIN ISO 1101.
