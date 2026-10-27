# Tröster et al. 2024b: Implikationen der Verknüpfung von C&C²-Ansatz und PGE-Modell

| Feld | Wert |
|---|---|
| Autoren | Peter Michael Tröster, Tobias Dieck, Giorgi Tsutskiridze, Albert Albers (Karlsruhe Institute of Technology, IPEK) |
| Titel | Implications of linking the C&C² approach and the model of PGE: Product Generation Engineering (im PDF steht statt des Doppelpunkts ein Halbgeviertstrich) |
| Quelle | NordDesign Conference, Reykjavik, Island, 12. bis 14. August 2024 (Seitenzahlen, Band und Reihe DS 130 im PDF nicht angegeben) |
| Jahr | 2024 |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Troester2024b), nicht im Repo (Lizenz) (9 S.) |
| Status | gelesen, vollständig ausgewertet |

Seitenangaben beziehen sich auf PDF-Seiten (PDF-S.), da das PDF keine Druckseiten enthält.

## Kernaussage

Der Beitrag baut auf Tröster et al. 2024a auf und schlägt vor, die **Prinzipvariation** (Principle Variation, PV) selbst in Anteile von **Attribut-/Gestaltvariation** (AV/EV) und **Übernahmevariation** (CV) zu zerlegen sowie die Übernahmevariation in einen **angepassten** und einen **unveränderten** Anteil zu teilen. Ein auf C&C²-Modellen basierender **Prozess zur Bestimmung der Variationsart** wird vorgeschlagen und am Generationswechsel **Einrohr- zu Zweirohr-Stoßdämpfer** erprobt. Motivation ist Wissenssicherung angesichts des demografischen Wandels.

## Inhalte nach Abschnitt

### 1. Introduction (PDF-S. 1)
- Demografischer Wandel führt zu Abfluss impliziten Wissens über Gestalt-Funktion-Zusammenhänge (Embodiment Function Relations, EFR).
- C&C² als **Metamodell** nach Stachowiak "which ... has model elements and basic rules", speziell für EFR entwickelt (nach Matthiesen 2021).
- Detailliertere Modellierung innerhalb eines Einzelteils ist möglich und nützlich (Verweis auf Tröster et al. 2024a).

### 2. State of the art (PDF-S. 1 bis 4)
- **2.1 C&C²-Ansatz (PDF-S. 1 bis 2):** Produktmodelle der Gestaltung nach Matthiesen et al. 2019 (Produktstruktur, He's Models, Gero's Models, Skizzen, SysML, Working Space Model, C&C²). Wahl von C&C² wegen einfacher Nutzbarkeit und breiter Anwendbarkeit (Grauberger et al. 2022).
  - Wirkflächenpaar (Working Surface Pair, WSP): Kontakt zweier Oberflächen fester Körper oder verallgemeinerter Grenzflächen von Flüssigkeiten, Gasen, Feldern.
  - Leitstützstruktur (Channel and Support Structure, CSS): Volumenelement, verbindet "precisely two Working Surface Pairs".
  - Connector (C): mit repräsentativer Wirkfläche (Working Surface, WS) als "parameterized model" der relevanten Umgebung, im Betrachtungsbereich, aber außerhalb des Gestaltungsraums.
  - **Funktionale Abgrenzung (Functional Delimitation, FD)** als "new virtual model element" (Abb. 2, Schraubenfeder): Analysewerkzeug, das LSS in Segmente teilt, ohne die Grundhypothesen zu verletzen. Keine Teilung der LSS in WFP (das wäre erst auf atomarer Ebene der Fall). **Symbol: zwei gekrümmte parallele Linien.** Die Linien teilen die LSS in Bereiche zwischen den Connectoren.
- **2.2 PGE (PDF-S. 2 bis 3):** PGE als Teil von SGE (Systemgenerationsentwicklung). Variationsarten:
  - CV Übernahmevariation (Adoption Variation): Übertragung von Teilsystemen, Anpassungen minimieren
  - PV Prinzipvariation: neues Lösungsprinzip gegenüber dem Referenzsystem
  - AV/EV Attributvariation/Gestaltvariation: Anpassung der Gestalt auf bekanntem Lösungsprinzip; "Attribute Variation" wenn Attribute variiert werden (Albers et al. 2015, 2023)
  - PV birgt Risiken durch fehlendes Wissen über neue Lösungsprinzipien. PGE auch für Produktportfolios (Schlegel et al. 2023).
- **2.3 Kombination (PDF-S. 3 bis 4, Abb. 3 Flaschen):** Ablauf zur Bestimmung von Variationsanteilen:
  1. Funktionale Abgrenzung (Identifikation von WSP, CSS, Connectoren)
  2. Segmentierung in handhabbare Abschnitte
  3. Einordnung in CV, PV, EV nach PGE
  4. Ableitung der Variationsanteile nach Anzahl der Abschnitte, Länge, Fläche oder Volumen

### 3. Methodology (PDF-S. 4)
- Idee: Variationsanteile zwischen Entwicklungs- und Produktgenerationen auf der Gestalt sichtbar machen.
- Drei Forschungsfragen, davon RQ1 und RQ3 fast wortgleich (Wissenserfassung und Wissenstransfer im demografischen Wandel); RQ2: Setzt sich PV aus AV- und CV-Anteilen zusammen und wie sind diese zu identifizieren?
- Qualitatives Forschungsparadigma, iterative Verfeinerung auf Basis der Erfahrung der Autoren, abschließende Fallstudie Stoßdämpfer. Keine Stichprobe, keine Probanden.

### 4. Results (PDF-S. 4 bis 7)
- Vier Bezugsgrößen für Anteile: Zählung, Fläche, Volumen, Länge (PDF-S. 4). Mit FD lässt sich auch die Kritikalität der Variationsabschnitte besser einschätzen.
- **Definition Komponente** (PDF-S. 5): einzeln identifizierbares Element, das sich nicht weiter vom vorgesehenen Ausgangszustand trennen lässt.
- Albers et al. 2017 (ZMS): PV ging stets mit Änderung der Anzahl von WFP und LSS einher. Die These, dass Hinzufügen oder Entfernen von WFP immer eine Prinzipvariation bedeutet, lasse sich laut Autoren nicht allgemein anwenden, weil Wirk- und Lösungsprinzipien oft teilweise übernommen werden.
- **Vorgeschlagene PV-Definition** (PDF-S. 5, siehe Befunde).
- Bezug immer auf die Generation im Markt Gn−1 gegenüber Gn.
- **Feinere Gliederung der Variationsanteile (Abb. 5, PDF-S. 6):** PV umfasst AV- und CV-Anteile; CV wird in "adapted" und "unchanged" geteilt.
- **Prozess zur Bestimmung der Variationsart (Abb. 6, PDF-S. 6 bis 7):**
  1. Referenzsystemelement als Ganzes betrachten, auch wenn es eine Baugruppe ist
  2. PV prüfen: Änderung von Wirk- oder Lösungsprinzip gegenüber Gn−1 (Energie-, Stoff-, Informationsflüsse, neue physikalische oder chemische Größen); Änderung der Anzahl von Komponenten und Wirkflächen (andere Wirkstruktur, "effective structure")
  3. Variationsanteile abschnittsweise bestimmen: Änderung von Anzahl oder Anordnung der WFP oder der Volumengestalt deutet auf Gestaltvariation; keine Änderung bedeutet CV; geänderte Wirkflächen oder Begrenzungsflächen (z. B. Rauheit, Härte) ohne Volumenänderung bedeutet **angepasste CV**
  4. Komponenten umranden, die gemeinsam das Wirk- oder Lösungsprinzip der PV darstellen
- **Fallstudie Stoßdämpfer (Abb. 4, 7, PDF-S. 5 und 7):** Einrohr- zu Zweirohrdämpfer als Prinzipwechsel (z. B. Gasblase beim Einrohrdämpfer, andere Komponentenzahl). Alle Komponenten liegen innerhalb der PV-Umrandung. Die meisten Bauteile sind CV-Anteile innerhalb der PV. Ventilplatten (Wirkflächen und Volumen geändert) und Dämpferaufhängung sind AV-Anteile. Farben je Variationsart nach Abb. 5 (Farbwerte im Text nicht genannt).

### 5. Discussion (PDF-S. 8)
- Aufschlüsselung in PV, CV, AV erhöht Transparenz der EFR und dient als Argumentationsbasis für Änderungsentscheidungen (Änderungsmanagement).
- FD erlaubt Identifikation kritischer Funktionsbereiche.
- Teilung der CV in angepasst und unverändert erfasst von außen nicht sichtbare Gestaltunterschiede.

### 6. und 7. Summary und Outlook (PDF-S. 8)
- Anwendung auf komplexere Baugruppen, prozentuale Erfassung je Gestaltabschnitt, Kritikalität der PV für die zu entwickelnde Generation.
- Förderung DFG 509078026.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| FD als virtuelles Modellelement mit Symbol (zwei gekrümmte Parallelen) | Zeichenwerkzeug "Abgrenzung" auf LSS, erzeugt Segmente, eigenes Symbol |
| FD teilt LSS nicht in WFP | Validierungsregel: Abgrenzung erzeugt keine neuen WFP und keine neuen Connectoren |
| Prozess Abb. 6 (vier Schritte) | Geführter Entscheidungsbaum zur Variationsart je Referenzsystemelement und Segment |
| Variationsarten PV, AV/EV, CV angepasst, CV unverändert | Enum `variationsart` mit fünf Werten, PV als Container über mehrere Komponenten |
| Kriterien: Anzahl/Anordnung WFP, Volumengestalt, Oberflächeneigenschaften (Rauheit, Härte) | Diff-Regeln beim Generationenvergleich: Elementanzahl, Anordnung, Volumen, Oberflächenattribute |
| Bezug Gn−1 zu Gn | Datenmodell: Modellgenerationen mit Vorgängerreferenz |
| Anteile nach Zählung, Länge, Fläche, Volumen | Kennzahl-Panel mit umschaltbarer Bezugsgröße |
| Wissenssicherung im demografischen Wandel | Export der Modelle samt Variationshistorie als Wissensdokument je Produktgeneration |
| Stoßdämpfer Einrohr/Zweirohr | Fallbeispiel Fluidtechnik in der Lernbibliothek |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Basisdefinition), Matthiesen 2021 (Pahl/Beitz), Albers und Wintergerst 2014 (Anthology), Matthiesen et al. 2018 (SWP 58), Matthiesen et al. 2019 (Product Models Embodiment Design), Grauberger et al. 2022 (Procedia CIRP 109, qualitative Modellierung und Hypothesen), Tröster, Prager, Schmid, Albers 2023 (SSP 2023, Functional Delimitation), Tröster et al. 2024 (DESIGN 2024), Albers, Bursac, Rapp 2017 (ZMS), Stachowiak 1973.
