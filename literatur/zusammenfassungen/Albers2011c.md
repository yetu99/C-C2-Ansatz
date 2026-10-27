# Albers et al. 2011: Systemarchitekturmodellierung in einem Software-Tool auf Basis des C&C-A

| Feld | Wert |
|---|---|
| Autoren | Albert Albers, Andreas Braun, Eike Sadowski, David C. Wynn, David F. Wyatt, P. John Clarkson |
| Titel | System Architecture Modeling in a Software Tool Based on the Contact and Channel Approach (C&C-A) |
| Quelle/Reihe | Journal of Mechanical Design 133 (10), Oktober 2011, Artikel 101006, S. 101006-1 bis 101006-8 |
| Jahr | 2011 (eingereicht 14.01.2011, online 18.10.2011) |
| DOI | 10.1115/1.4004971 |
| Lizenz | im PDF nicht angegeben (© 2011 ASME) |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2011c), nicht im Repo (Lizenz) (8 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

KIT (IPEK) und Cambridge (EDC) **formalisieren** den C&C-A und implementieren ihn als Software auf Basis des **Cambridge Advanced Modeller (CAM)**. Das Metamodell besteht aus **Working Surface (mit äußerem und innerem Port), WSP, CSS, Module, Part, Flow und Function**, ergänzt um **Modellierungsregeln** (Komplementarität, Mehrfachfunktionen) und **Bibliotheken** für Flüsse, Funktionen (Functional Basis nach Hirtz et al.) und Normteile. Am Roboterarm ARMAR IIIb zeigen die Autoren Änderungsfolgen (Motortausch erzeugt Kühlbedarf). Der Connector kommt in dieser Formalisierung **nicht** vor.

## Inhalte nach Abschnitt

### 1. Einleitung (S. 101006-1)
- Funktion und Form entstehen gemeinsam und sollen gemeinsam repräsentiert werden.
- Software-Ansatz: Formalisierung, Bibliotheken für Funktionsbegriffe, Suche nach generischen Teilen, Algorithmen für **fehlende Hilfsfunktionen** (Beispiel Wärmeabfuhr eines E-Motors).

### 2. Hintergrund (S. 101006-1 bis -2)
- Funktionsbegriffe (Vermaas, Erden mit 18 Bedeutungen, Pahl/Beitz, FBS). MBSE, Axiomatic Design, Function-Means-Tree, FuncSION, Schemebuilder, Bondgraphen, SysML.
- Kritik: rechnergestützte Syntheseansätze erzeugen viele Lösungen, unterstützen aber kaum die **Analyse** und die Auswahlentscheidung.

### 3. Der C&C-A (S. 101006-2 bis -3)
- Funktion ist **formabhängig**; die C&C-Elemente dienen als Platzhalter bzw. Zeiger auf die Form. Kein festgelegter Funktionsbegriff, Abstraktionsebenen frei wählbar. Modellnotation heißt **C&C-M**.
- Elementdefinitionen (S. 101006-3):
  - WSP: geometrische Schnittstellen zwischen Artefakten oder Artefakt und Umgebung, auch Grenzflächen von Flüssigkeiten, Gasen, Feldern; je eine Working Surface auf jedem der zwei Bauteile.
  - CSS: "physical components or volumes of liquids, gases or fields which connect exactly two WSPs".
  - Wirk Structure: Menge der WSP und CSS, die für eine gegebene Funktion relevant ist.
- Probleme der Papierpraxis: viele Skizzen, keine Konsistenzprüfung, kein Zoomen, keine Ablage und Suche.

### 4. Formalisierung und Implementierung (S. 101006-3 bis -5)
- Motivation: Modelle verschiedener Personen zum selben System weichen stark ab (Begriffe, Darstellung, Detailgrad).
- **Formalisierte Elemente:**
  - **Working Surface** mit zwei bidirektionalen Ports: "outer" zu einer WS eines anderen Teils, "inner" zur angrenzenden CSS im selben Teil.
  - **WSP** = Verbindung der äußeren Ports zweier WS; trägt einen oder mehrere **Flows**.
  - **CSS** = Verbindung der inneren Ports zweier WS (interne Struktur). WSP und CSS sind in tiefere Ebenen zerlegbar.
  - **Module** = logische Untergliederung, enthält Module oder Parts (Hierarchie).
  - **Part** = unterste Ebene; nur Parts enthalten WS und CSS.
  - **Flow** = Energie, Stoff oder Signal (Taxonomie nach Hirtz et al. 2002, drei Ebenen).
  - **Function** = mit mindestens zwei WSP und einer CSS verknüpft; Input- und/oder Output-Flow; Funktionsbegriff aus Taxonomie, z. B. "Transform: Electrical Energy to Mechanical Rotational Energy".
- **Modellierungsregeln:** Komplementarität (keine Funktion an einem Teil allein, Software prüft ≥ 2 WSP mit Flows und verbindende CSS); Mehrfachfunktionen und Formabhängigkeit; Parameter wie Reibwert und Last können an WSP und CSS notiert werden.
- **Implementierung in CAM:** Metamodell mit grafischen Repräsentationen (Abb. 1), Hervorheben, **Auf- und Zuklappen** von Modulen, Plug-ins für Bibliotheken; Taxonomien und Teilebibliothek als **CSV-Dateien**.
- **Arbeitsweise:** grobes Layout aus Modulen, dann schrittweise Verfeinerung; Parts aus Bibliothek bringen Funktionen und WSP-CSS-Struktur mit; **fehlende Flows oder Funktionen werden automatisch ergänzt und markiert**; inkonsistente Definitionen werden bei Änderungen automatisch gelöscht.
- **Filter der Teilebibliothek:** passend zu allen geforderten Output-Flows oder zu mindestens einem Input- und einem Output-Flow.

### 5. Anwendung ARMAR IIIb (S. 101006-5 bis -7)
- Erster Schritt: **Modellzweck definieren** und Fokusbereich festlegen.
- Ziel: kompakte, leichte Arme. Modell von ARMAR IIIa als Basis, humanoides Layout zur Navigation.
- Bibliotheksmotor (DC-Torquemotor) erzeugt Wärmeabfuhr-Bedarf; Gehäuse ohne Belüftung passt nicht; Wechsel auf rahmenlosen Motor mit Kühlung über den Rahmen; neue, nicht passende WSP und CSS werden markiert.
- Modell mit zwei Freiheitsgraden: **über 100 Funktionsbeziehungen, 150 WSP, etwa 280 CSS**.
- Grenzen: feste Input-Function-Output-Terminologie kann Absichten nicht immer ausdrücken (Beispiel Lager "Freiheitsgrad begrenzen"); Vorschlag: erklärende Notizen neben formaler Beschreibung. Qualitative Beschreibung; quantitative Parameter und Prüfalgorithmen als Ausblick; WSP-CSS-Struktur könnte CAD-Geometrie und CAE unterstützen. Software ist **erster Prototyp**.

### 6. Fazit (S. 101006-7)
- Formalisierung soll Modellbau unterstützen, Design nicht vollständig berechenbar machen.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| WS mit äußerem und innerem Port | Graph-Datenmodell: WSP = Kante zwischen WS verschiedener Bauteile, CSS = Kante zwischen WS desselben Bauteils |
| Module und Parts als Hierarchie | Systembaum (deckt sich mit Bauteilbaum aus Troester2025b), Auf- und Zuklappen |
| Flow-Taxonomie nach Hirtz | Auswahlliste Energie/Stoff/Signal mit Unterklassen; für Wasser/Energie um Hydraulik und Wärme konkretisieren |
| Function mit ≥ 2 WSP und 1 CSS | Validierungsregel beim Speichern einer Funktion |
| Automatische Ergänzung fehlender Flows (Wärme beim Motor) | Regelbasierte Hinweise "Nebenfunktion fehlt" aus Bauteilbibliothek |
| Teilebibliothek als CSV | Erweiterbare Bibliothek typischer Komponenten (Pumpe, Ventil, Lager, Dichtung) mit WSP-CSS-Vorlagen |
| Starre Terminologie schränkt ein | Freitext plus optionale Taxonomie, nie nur Taxonomie |
| Papiermodelle ohne Konsistenz und Zoom | Kernnutzen digital: Konsistenzprüfung, Detailstufen, Suche |
| Connector fehlt in der Formalisierung | Eigenes Element Connector ergänzen (Systemgrenze, Umgebungsmodell) |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Basisdefinition, dort als Ref. [2] mit englischem Titel), Hirtz et al. 2002 (Functional Basis), Albers et al. 2008 (Industrieanwendung, Ref. [29]), Albers et al. 2010 (ASME IDETC, Bibliotheken), Wynn et al. (CAM, Ref. [31]), Albers, Braun, Muschik 2010 (Fraktalität von Prozessen).
