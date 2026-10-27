# Paehler und Matthiesen 2024: Landkarte der Produktmodelle in der Gestaltung

| Feld | Wert |
|---|---|
| Autoren | Lukas Paehler, Sven Matthiesen (KIT, IPEK) |
| Titel | Mapping the landscape of product models in embodiment design |
| Quelle | Research in Engineering Design 35 (2024), S. 289 bis 310, Original Paper; eingereicht 02.03.2023, überarbeitet 18.01.2024, angenommen 20.01.2024, online 09.03.2024 |
| Jahr | 2024 |
| DOI | 10.1007/s00163-024-00433-x |
| Lizenz | CC BY 4.0 (Open Access, Projekt DEAL) |
| Volltext | [`../volltexte/Paehler2024.pdf`](../volltexte/Paehler2024.pdf) (22 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Die Autoren erstellen per Literaturreview mit **Grounded-Theory-Analyse** eine **Landkarte von 52 Produktmodellen** der Gestaltung (embodiment design). Zwei Modelle sind **verknüpfbar** (linkable), wenn Ausgaben des einen als Eingaben des anderen nutzbar sind. Das Netzwerk (69 Knoten, 183 Kanten) zeigt ein dichtes **Zentrum** um das **2D/3D-CAD-Modell** (Grad 23), einen locker verknüpften **Rand** und **Satelliten** mit wenigen oder keinen Verknüpfungen. Das **C&C²-Modell** erscheint als Produktmodell mit Wirknetz und Wirkstruktur als Ausgabe.

## Inhalte nach Abschnitt

### 1. Introduction (S. 289 bis 291)
- Konstrukteure erzeugen Folgen von Produktmodellen und wechseln zwischen ihnen. Schnelles und genaues Wechseln beschleunigt den Prozess (nach Jones et al. 2020).
- **Definition Produktmodell** (S. 289): von Menschen erstellte, pragmatische, reduzierte Repräsentation eines technischen Produkts mit Attributen ähnlich dem Original, zur Darstellung von Funktion, Verhalten oder Struktur oder zur Verhaltensanalyse (nach Andreasen et al. 2015, Stachowiak 1973, Eckert und Hillerbrand 2018).
- **Definition verknüpfbar** (S. 290): Ausgaben eines Modells können als Eingaben des Folgemodells genutzt werden, per technischer Schnittstelle oder durch den Konstrukteur. Unterschiede im Abstraktionsniveau bleiben ausgeklammert.
- Vorarbeiten: Matthiesen et al. 2019b (Produktmodelle der Gestaltung, Auswahlrahmen) und Weidmann et al. 2017 (mechatronisch), zusammen 79 Modelle; der Wechselaufwand wurde dort nicht betrachtet.
- **1.1 Beitrag (S. 290 bis 291):** Fokus auf Gestaltung nach Pahl/Beitz 1996 (vom Konzept zur Gestalt, Wechsel von Analyse und Synthese). RQ1: Welche Kategorien ähnlicher Ein- und Ausgaben gibt es? RQ2: Welche Verknüpfungen lassen sich bilden?

### 2. Methodology (S. 291 bis 293, Abb. 1)
- **2.1 Literatursammlung (S. 292):** Aktualisierung von Matthiesen et al. 2019b (2009 bis 2018) bis August 2022, Vorgehen nach Dresch et al. 2015. Suchbegriffe u. a. "embodiment function relation", "product model", "function model*". Datenbanken ASME, Google Scholar, IEEE, ResearchGate, Scopus, Web of Science (TEMA entfallen). Drei Stufen von Einschlusskriterien (ab 2018, Engineering Design, Englisch; Produktmodell in Titel/Abstract, Gestaltungskontext; Modell beschrieben, Darstellungs- und Informationsart angegeben, peer reviewed).
- **2.2 Analyse (S. 292 bis 293):** Schritt "Analyze" nach Wolfswinkel et al. 2013; offenes, axiales, selektives Kodieren der Ein- und Ausgaben, auch Abbildungen ausgewertet.
- **2.3 Konsolidierung und Visualisierung (S. 293):** Modellpaare aus Übereinstimmung von Ausgabe und Eingabe. Gephi, Kategorien als ungerichtet verbundene Knoten, Modelle gerichtet verknüpft, Layout Yifan Hu (kraftbasiert). Ein- oder Ausgaben ohne Gegenstück werden nicht visualisiert.

### 3. Results and discussion (S. 293 bis 298)
- **3.1 Literatur (S. 293 bis 294, Tab. 1):** 2853 Treffer nach Stufe 1, 1636 nach Duplikatentfernung, 79 nach Stufe 2, 26 nach Stufe 3 (0,9 %). Zusammen mit 48 Publikationen aus Matthiesen et al. 2019b: **74 Publikationen**. 6,5 statt 4,8 Publikationen pro Jahr; 26 neue Publikationen aus 13 Institutionen (vorher 48 aus 36).
- **3.2 Kategorien (S. 294 bis 295, Abb. 2, 5, 6):**
  - **52 Produktmodelle** (34 bei Matthiesen et al. 2019b, also 18 mehr, teils durch Aufteilung von Frameworks wie He et al. 2013). Zwei frühere Quellen ausgeschlossen.
  - 11 Eingabe- und 14 Ausgabekategorien, zusammengeführt 17 Kategorien (u. a. Graph Representation 16, Relations 21, Function Model 16, Virtual Representation 14, Physical System 13, 2D/3D CAD Model 13, Matrix Representation 10).
  - Fünf Modelle ohne Kategorie (vier merkmalsbasierte Modelle nach He et al. 2013, SAPPhIRE).
  - Technische Zeichnung fehlt als Produktmodell (nicht hinreichend beschrieben), erscheint aber als Kategorie.
  - Kategorien reichen von ausgetauschter Information über konkrete Modelle bis zu Darstellungsarten.
- **3.3 Landkarte (S. 295 bis 298, Abb. 3, 4):**
  - 69 Knoten, 183 Kanten, mittlerer Grad 5,3, maximaler Grad 23 beim 2D/3D-CAD-Modell.
  - Darstellung: Modelle als leere schwarze Kreise, Kategorien als gefüllte grüne Quadrate, Kanten ab Modell grau durchgezogen, Kanten ab Kategorie grün gestrichelt, Knotengröße nach Grad.
  - Sektoren: Zentrum (z. B. Design Structure Matrix, um Graph Representation und CAD), Rand (z. B. Function Means Tree; z. B. NVH Model, Pseudo Rigid Body Model ohne Rückweg ins Zentrum), Satelliten (He-et-al.-Cluster, unverknüpftes SAPPhIRE/-lite).
  - Position einzelner Modelle ist nicht aussagekräftig, nur Strukturen mit bestimmenden Kanten.
  - CAD-Modell als Verbindungspunkt, Grenzen bei Zusatzinformationen; formale Übergabe z. B. über Kategorientheorie.
  - Modelle ohne Rückweg fließen vermutlich über mentale Modelle zurück, mit Fehlerrisiko.
  - In Abb. 3 ist "C&C²-A Model" in einem der vergrößerten Ausschnitte beschriftet (Ausschnittszuordnung im Textextrakt nicht eindeutig).

### 4. Conclusion and outlook (S. 298 bis 299)
- Beispiel Kette: Integrated Function Model → Design Graph → 2D/3D-CAD → Mehrkörpersystem und FEM.
- Beispiel Auswahl: Aus Bond Graph lassen sich Behavioral Matrix und Causal Graph bilden, nur von der Behavioral Matrix ist ein Weg zum Function Means Tree bekannt.
- Landkarte zeigt Verknüpfbarkeit, aber keinen Modellzweck. Zweck soll künftig integriert werden. Gephi-Daten als erweiterbare Wissensbasis (Zusatzmaterial).

### 5. Limitations (S. 299)
- Nur Literatur ab 2009. Analyse über textuelle Beschreibungen, abweichende Benennungen gleicher Dinge evtl. nicht erkannt.

### Anhang: Tabelle 2 und Abb. 5, 6 (S. 300 bis 306)
- **C&C²-Modell in Tab. 2 (S. 300):** Quellen Albers et al. 2009, 2019; Boersting et al. 2008; Freund et al. 2015; Gladysz et al. 2018; Gladysz und Albers 2018a, 2018b; Grauberger et al. 2020a bis d, 2021, 2022; Matthiesen et al. 2019a; Wettstein et al. 2021; Zingel et al. 2012.
  - Ausgaben: "Wirk-structure (multiple C&C2-Models)" und "Wirk-net (= C&C2-Model)" mit Working surface pairs, Channel and support structures, Connectors.
  - Eingaben (Einschätzung aus der Zeilenfolge des zerlegten Tabellenlayouts): Physical System, Sketch, Technical Drawing, 2D/3D CAD Model.
- **C&C²-Modell als Eingabe (S. 302, Einschätzung aus Zeilenfolge):** für die Function-Effort-Matrix (Albers et al. 2019), zusammen mit CAD-Modell, Zeichnung und physischem Referenzelement.
- **Abb. 6 (S. 306):** Ausgabebeschreibung "Wirk-nets (C&C²-Models)" erscheint in der Nähe der Kategorie Schematic Representation (Zuordnung im Textextrakt nicht eindeutig).

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Verknüpfbarkeit = Ausgabe A ist Eingabe B | Import-/Exportschnittstellen als Kernanforderung, explizit dokumentierte Ein- und Ausgaben je Modelltyp |
| C&C²-Eingaben: physisches System, Skizze, technische Zeichnung, 2D/3D-CAD | Modellanlage aus Foto, Skizze, Zeichnungs-PDF oder CAD-Datei als Hintergrund-Systemabbild |
| C&C²-Ausgabe: Wirknetz (ein Modell), Wirkstruktur (mehrere Modelle) | Datenmodell: Projekt enthält Wirkstruktur, diese enthält Wirknetze; Export beider Ebenen |
| C&C² als Eingabe der Function-Effort-Matrix | Exportfunktion: Matrix Funktion × Teilsystem aus WFP/LSS-Zuordnungen vorbefüllen |
| CAD-Modell als zentraler Verbindungspunkt (Grad 23) | CAD-Anbindung priorisieren (Geometrie-IDs mit WFP/LSS verknüpfen) |
| Rückweg aus Randmodellen fehlt, Rückfluss über mentale Modelle fehleranfällig | Ergebnisse externer Analysen (FEM, Versuch) als Anhang an Modellelemente zurückführen |
| Kategorie "Relations between components" | Graph-Export (z. B. GraphML/Gephi) des Wirknetzes zur Weiterverarbeitung |
| Grenze: Landkarte ohne Modellzweck | Pflichtfeld Modellzweck, damit Exporte für Folgemodelle eingeordnet werden können |

## Im Paper zitierte Schlüsselquellen
Matthiesen et al. 2019b (Product models in embodiment design, Vorgängerreview), Albers et al. 2009 (ICED09, Contact and Channel Modelling früher Phase), Albers et al. 2019 (ICED19, Agile Lightweight Design mit C&C²), Gladysz und Albers 2018a (C&C²-AFM), Gladysz et al. 2018 (C&C²-Modelle in der Fehleranalyse), Grauberger et al. 2020a (Modellkombination Gestaltung und Tolerierung), 2020b (Leitfaden agile Entwicklung), 2020c (Projektanalyse qualitativer Modellierung), 2020d (20 Jahre Anwendungserfahrung, JED), 2021 (Methodentraining), 2022 (Hypothesen aus Industrieprojekten, Procedia CIRP), Matthiesen, Grauberger, Schrempp 2019a (Extended sequence modelling, ICED19), Wettstein, Grauberger, Matthiesen 2021 (Sequenzmodellierung dynamischen Verhaltens, Schlagwerk), Zingel et al. 2012 (C&C²-A in SysML), Freund et al. 2015 (Schnittstellenunsicherheit mit dem Contact and Channel Model, ICED15), Boersting et al. 2008 (Funktionen und Anforderungen, DESIGN 2008).
