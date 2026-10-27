# Matthiesen et al. 2017: Methodische Unterstützung des Erkenntnisgewinns durch Konstruktionshypothesen

| Feld | Wert |
|---|---|
| Autoren | Sven Matthiesen, Patric Grauberger, Thomas Nelius, Kevin Hölz |
| Titel | Methodische Unterstützung des Erkenntnisgewinns in der Produktentwicklung durch Konstruktionshypothesen |
| Quelle/Reihe | KIT Scientific Working Papers 61, IPEK Institut für Produktentwicklung, Karlsruher Institut für Technologie (KIT), Karlsruhe; ISSN 2194-1629 |
| Jahr | 2017 |
| DOI | im PDF nicht angegeben |
| Lizenz | CC BY-SA 4.0 |
| Volltext | [`../volltexte/Matthiesen2017a.pdf`](../volltexte/Matthiesen2017a.pdf) (17 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Die **Konstruktionshypothese** ist eine Methode zur **Verifikation von Modellvorstellungen des Gestalt-Funktion-Zusammenhangs**. Ihr Kern ist ein **Leitsatz "Wenn [konkreter Gestaltparameter], dann [messbare Funktion], weil [Modellvorstellung der Ursache]"**, ergänzt um **Prüfung** (Experiment) und **Ergebnis**. Eine erste Fassung (nur Wenn-Dann) wurde in einem **Live-Lab mit 70 Studierenden** erprobt; sie wurde oft zur Modellbildung auf Konzeptebene missbraucht, daher kam der **Weil-Teil** hinzu und die Methode wird klar auf **Modellverifikation in konstruktiven Details** begrenzt.

## Inhalte nach Abschnitt

### Abstract (PDF-S. 3)
- Zweisprachig (EN/DE). Live-Lab mit 70 Studierenden ("70 undergraduate students" in der englischen Fassung); Methode zeigte Potenzial, wurde aber häufig zur Modellbildung genutzt, wo sie nicht hilft; Optimierung durch Aufnahme der Modellvorstellung der Ursache in das Formblatt.

### 1. Einleitung (PDF-S. 4)
- Kunde will einen **Zweck**; Konstrukteur erfüllt ihn über (Teil-)Funktionen und kann Funktionen nur über **Gestalt** (funktionsrelevante Bauteile und ihre Eigenschaften) ändern.
- Beispiel **Winkelschleifer**: Zweck "gutes Arbeitsgefühl", Vibration als unerwünschte Funktion, Vermutung Elastizität der Lagersitze beeinflusst Schwingung der Motorwelle.

### 2. Stand der Forschung, vier Anforderungen (PDF-S. 4 bis 8)
- 2.1 Gestalt-Funktion-Zusammenhang; **synthesegetriebene Analyse**; C&C²-Ansatz als **Denkzeug** (Fußnote: Werkzeug zur Unterstützung der Denkvorgänge in Analyse und Synthese) zur expliziten Modellbildung mit Fotos oder CAD-Modellen. Anforderung 1 explizite Modellbildung des Gestalt-Funktion-Zusammenhangs als Basis.
- 2.2 Früher Markteintritt, Iterationen früh provozieren, **gezieltes Testing** mit erkenntnisorientierten Prototypen. Anforderung 2 Nutzung des gezielten Testing.
- 2.3 Konstruieren als Wechsel zwischen Gestalt und Funktion, oft opportunistisch (Hacker 2002); Erkenntnis nur in Modellen (Stachowiak); Fehlerquellen **Scheinkorrelationen** und kognitive Verzerrungen (Arnott 2006); Reflexion verbessert Lösungsgüte. Anforderung 3 Verifikation der Modellvorstellung zur Erkennung kausaler Zusammenhänge.
- 2.4 Wissenschaftliche Hypothesen mit unabhängiger, abhängiger und Störvariable; Anforderungen widerspruchsfrei, widerlegbar, **operationalisierbar** (Hussy et al. 2013). Hypothesen mit begrenzter (räumlicher, zeitlicher, systembezogener) Gültigkeit aus der Psychologie. Bezüge zu **Schadenshypothesen nach VDI 3822** und Hypothesen nach Ehrlenspiel. Anforderung 4 Merkmale wissenschaftlicher Hypothesen als Rahmen, Anschluss an bestehende Methoden.

### 3.1 Erster Entwurf (PDF-S. 8)
- Leitsatz mit Gestalt (unabhängige Variable) und Funktion (abhängige Variable) in **Wenn-Dann-Beziehung**; dazu Prüfung über gezieltes Testing, die genau Gestalt und Funktion aus dem Leitsatz prüft.

### 3.2 Live-Lab "Mechatronische Systeme und Produkte" (PDF-S. 8 bis 9)
- Live-Lab nach Albers als Untersuchungsumgebung mit realitätsnahem Prozess und gestaltbaren Randbedingungen.
- **70 Studierende** entwickeln semesterbegleitend zwei kooperierende autonome mechatronische Systeme; Fertigung mit Lasercutter und Baukastenteilen; Mikrocontroller und Sensoren (Infrarot, Ultraschall, Helligkeit, Farbe); Aufgabe Würfel und Zylinder einsammeln und an Positionen stapeln.

### 3.3 Anwendung im Live-Lab (PDF-S. 9 bis 11)
- Methode in einer Übung vermittelt, Template in der Projektdokumentation.
- **Erfolgsbeispiel Sortierrad** (Team 3, MSuP 2016/17, Abb. 1): Paper-Prototype, dann HDF-Bauteile (Lasercutter). Würfel klemmen.
  - Hypothese 1 "Dicke der Seitenwand" 5 mm auf 3 mm, falsifiziert
  - Hypothese 1.1 "Breite der Öffnung" in der Rückwand vergrößert, falsifiziert
  - Hypothese 1.3 "Seitenwinkel der Bodenfläche", verifiziert mit schräg gestelltem Sortierrad
  - Hypothese 2 Reibung im **Wirkflächenpaar Welle-Lagerhülse**, Nylonfaden als reibungsarme Hülse
  - Prüfanforderung mindestens 10 Würfel fehlerfrei sortieren und fördern; Funktion nach **4 Iterationen** erfüllt
- **Misserfolgsbeispiel**: "Wenn eine Getriebeübersetzung von X (...) vorliegt, dann ist das Greiferfahrzeug trotzdem schnell genug"; keine Prüfung formuliert, Funktion nicht quantifiziert, nur Entscheidung "Konzept beibehalten/verwerfen" möglich.
- Methode hilft vor allem bei Schwierigkeiten in **konstruktiven Details**; dort aufwändiger als bei Konzeptbewertung.

### 4.1 Erkenntnisse aus der Studie (PDF-S. 11 bis 12)
- Online-Umfrage, **25 vollständige Datensätze**.
- Etwa **75 % (119 von 160)** der gebildeten Hypothesen wurden als weniger oder nicht hilfreich empfunden. Wer so urteilte, bildete im Mittel **13,2 Hypothesen**; wer sie hilfreich fand, im Mittel **6,8**.
- Als Ursache zeigte die Dokumentenanalyse, dass viele Hypothesen Ausformulierungen von **Konzeptideen** mit mehreren Gestaltparametern waren ("Wenn ein drehbares Rad verwendet wird, dann können die Würfel damit sortiert werden"). Sie dienten der Modellbildung und kaum der Verifikation.
- Als Konsequenz wurde der Leitsatz um die **Modellvorstellung der Ursache** erweitert. Klare Trennung **Modellbildung** (Zusammenhang unbekannt, Analysemethoden helfen, Konstruktionshypothese ungeeignet) und **Modellverifikation** (identifizierter Zusammenhang wird an der Realität geprüft, Konstruktionshypothese geeignet).

### 4.2 Die Konstruktionshypothese (PDF-S. 12 bis 15)
- **Formblatt (Abb. 2)**:
  - Hypothesentitel mit Nummer und Beschreibung des Gestaltparameters
  - Wenn: konkreter Gestaltparameter mit Angabe der Referenz
  - Dann: erwartete messbare Funktionsveränderung im Vergleich zur Referenz
  - Weil: Modellvorstellung der Ursache der Funktionsveränderung
  - Prüfung: Beschreibung des Experiments mit allen relevanten Randbedingungen
  - Ergebnis: Ergebnis der Hypothesenprüfung, daraus Handlungsempfehlung
- Bewusst auf die Verknüpfung **konkreter Gestaltparameter** mit **messbaren Funktionen** eingeschränkt.
- **Beispiel Winkelschleifer (Abb. 3)**, Hypothese "Steifigkeit des Lagersitzes": Wenn Lagersitz **75 Shore D** statt Referenz **50 Shore D**, dann sinkt die Bewegungsamplitude der Motorwelle im Leerlauf (Schwingungs-RMS-Wert fällt), weil höhere Zwangskräfte das Aufschaukeln begrenzen und geringere Amplituden ins Gehäuse übertragen werden. Prüfung mit Lagerringen auf dem Teilkomponentenprüfstand, Vergleich Prototyp und Referenz; Ergebnis verifiziert.
- Shore-Härte bündelt Steifigkeit und Dämpfung, daher erweitertes Experiment für Nichtlinearitäten; Literatur zur Versuchsplanung (Siebertz et al. 2010, Kleppmann 2011).
- Im Prüfaufbau unterscheiden sich Prototyp und Referenz nur im betrachteten Parameter.
- **Gültigkeit begrenzt** auf die geprüften Zusammenhänge; kein Extrapolieren (härter ist nicht automatisch besser); daher viele Hypothesen je Projekt nötig.
- Fokus auf besonders kritische konstruktive Details; die allgemeine Eignung von Konzepten ist ausdrücklich kein Gegenstand der Methode.

### 5. Zusammenfassung und Ausblick (PDF-S. 15)
- Prüfung der Wirksamkeit der Maßnahme im nächsten Live-Lab-Durchlauf, vertiefte Schulung, Beobachtung einzelner Konstruktionsprozesse, Anwendung in einem Unternehmensprojekt.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Formblatt Titel, Wenn, Dann, Weil, Prüfung, Ergebnis | Datenobjekt `Konstruktionshypothese` mit genau diesen Feldern, Nummerierung hierarchisch (1, 1.1, 1.3, 2) |
| Wenn = konkreter Gestaltparameter mit Referenz | Pflichtverknüpfung zu Parameter-Objekt (Element-ID WFP/LSS/C, Referenzwert, Prüfwert, Einheit) |
| Dann = messbare Funktionsveränderung | Pflichtfelder Messgröße, Einheit, erwartete Richtung (steigt/fällt) oder Zielwert |
| Weil = Modellvorstellung der Ursache | Pflichtfeld Freitext plus Verweis auf Wirknetz-Pfad im C&C²-Modell |
| Prüfung mit allen Randbedingungen, nur ein Parameter variiert | Prüfplan mit Feldern Prüfaufbau, Randbedingungen, Betriebszustand (z. B. Leerlauf), Prüfkriterium (z. B. 10 Würfel); Warnung bei mehreren variierten Parametern |
| Ergebnis mit Handlungsempfehlung | Statusfeld verifiziert/falsifiziert/offen und Folgehypothese als Kind-Objekt (Iterationskette) |
| Fehlanwendung auf Konzeptebene (75 % wenig hilfreich) | Prüfregel "nur ein Gestaltparameter je Hypothese", Warnung bei qualitativer Funktion ohne Messgröße |
| Begrenzte Gültigkeit | Gültigkeitsbereich-Feld (System, Zustand, Parameterbereich) |
| Trennung Modellbildung vs. Modellverifikation | Workflow, in dem Hypothesen erst nach Abschluss der Modellbildung freischalten |
| Schadenshypothesen VDI 3822 | Optionaler Hypothesentyp "Schadensursache" für Fehleranalyse und Retrofit |

## Im Paper zitierte Schlüsselquellen

Matthiesen 2011 (ICED, Thinking Tools, Denkzeug-Begriff); Albers und Wintergerst 2014 (Anthology, im Literaturverzeichnis als "The Contact and Channel Approach (C&C²-A)"); Ruckpaul, Kriltz und Matthiesen 2014 (synthesegetriebene Analyse); Meboldt, Matthiesen und Lohmeyer 2012 (Iterationen); Hacker 2002 (Denkpsychologie); VDI 3822 Blatt 1 (Schadenshypothesen); Walter et al. 2016 (Live-Lab); Matthiesen, Gwosch und Gittel (IGF 18196N, Winkelschleifer-Prüftechnik); Matthiesen et al. 2017 (Konstruktion, realitätsnahe Komponententests).
