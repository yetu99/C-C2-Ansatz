# Grauberger et al. 2020: The contact and channel approach, 20 years of application experience

| Feld | Wert |
|---|---|
| Autoren | Patric Grauberger, Holger Wessels, Bartosz Gladysz, Nikola Bursac, Sven Matthiesen, Albert Albers |
| Titel | The contact and channel approach - 20 years of application experience in product engineering (im PDF mit Halbgeviertstrich zwischen den Titelteilen) |
| Quelle/Reihe | Journal of Engineering Design, Vol. 31, No. 5, S. 241 bis 265 (Taylor & Francis), online veröffentlicht am 04.12.2019 |
| Jahr | 2020 (Heft), Online-Erstveröffentlichung 2019 |
| DOI | 10.1080/09544828.2019.1699035 |
| Lizenz | im PDF nicht angegeben (nur "© 2019 Informa UK Limited, trading as Taylor & Francis Group") |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Grauberger2020a), nicht im Repo (Lizenz) (26 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Das Review fasst **20 Jahre Anwendung des C&C²-Ansatzes** zusammen. Über Data Mining in rund 14.500 Publikationen werden **39 Anwendungsfälle** identifiziert und nach den **Modellzwecken nach Andreasen, Hansen und Cash (2015)** kategorisiert; Schwerpunkt ist **"obtain insight" (20 von 39)**. Zusätzlich liefert der Artikel eine kompakte **Historie** (Elementmodell vor 2002, C&CM ab 2004, C&C²-A mit **Connector ab 2010**), die Definitionen der Kern- und Strukturelemente sowie den Wortlaut der **drei Grundhypothesen**. Als zentrale Grenzen werden die fehlende Datenstruktur der zweidimensionalen Modelle, fehlende Wiederverwendung und das Fehlen von Anwendungen in Fluid-, Gas- und Feldsystemen genannt.

## Inhalte nach Abschnitt

### 1. Introduction (S. 241 bis 243)
- Ausgangspunkt Produktgenerationsentwicklung (PGE) mit Referenzsystem; Gestalt-Funktion-Zusammenhänge (embodiment function relations, EFRs) müssen verstanden werden, weil Funktionen aus Wechselwirkungen entstehen und ein Bauteil allein keine Funktion erfüllt (Albers, Matthiesen und Lechner 2002).
- Abgrenzung zu FEM, Axiomatic Design (Suh 1998), FBS (Gero und Kannengiesser 2004) und CPM (Weber 2005). C&C²-A nutzt beliebige Visualisierungen der Gestalt (Skizzen, CAD, Zeichnungen, reales Produkt) als Modellbasis.
- Drei Forschungsfragen (S. 242): In welchen Anwendungen wurde C&C²-A genutzt? Wie unterstützt er Designaktivitäten auf Basis von Referenzsystemen? Welche Grenzen bestehen?

### 2. The contact and channel approach (S. 243)
- Albers und Matthiesen griffen den nicht formalisierten Ansatz der Wirkflächenpaare (Hubka 1984, Rodenacker und Claussen 1973, Roth 1982) auf. Funktion wird unterschieden in gewünschte Funktion (Zweck) und Verhalten; Gestalt in Merkmale (characteristics, direkt beeinflussbar) und Eigenschaften (properties, nur indirekt) nach Weber.

### 3. Historical outline (S. 243)
- Erste Ideen bei Albers aus der Entwicklung eines **Zweimassenschwungrads** bei einem Automobilzulieferer (Albers 1994); 1996 Wechsel an die Universität Karlsruhe, gemeinsam mit Sven Matthiesen erste formale Beschreibung.
- Phase 1 (vor 2002) Ideenfindung und Theorie. Elementmodell "Working Surface Pairs & Channel and Support Structures", erstmals publiziert 2002 (Albers, Matthiesen und Lechner 2002; Matthiesen 2002). Enthielt WFP, LSS, die **drei Grundhypothesen**, Strukturelemente und Visualisierungen für WFP und LSS.
- 2004 Benennung **Contact & Channel Model (C&CM)** (vgl. Albers, Ohmer und Eckert 2004). Phase 2002 bis 2010 Entwicklung aus Praxiserfahrung.
- **Seit 2010 "Contact and Channel Approach (C&C²-Approach)"** zur Unterscheidung von Metamodell (Ansatz als Modellierungssprache mit Elementen und Anwendungsregeln) und konkretem Modell C&C²-M. Das "C²" kam mit dem Kernelement **Connector**, das die Systemumgebung integriert. Dies gilt als Reifepunkt des Ansatzes.
- Seit 1997 in Konstruktionslehre unterrichtet, rund **20.000 Ingenieure** kennen die Modellierungsweise.

### 4. C&C²-Approach und C&C²-Modelle (S. 244)
- Methodischer Ansatz zur Unterstützung von Denkprozessen (Matthiesen 2002) und gemeinsame Sprache im Team. Kern sind **drei Kernelemente und drei Grundhypothesen**.
- C&C²-Modell folgt den Modellmerkmalen nach Stachowiak (1973): Abbildung (Bezug zum Original, auch FEM oder CAD), Verkürzung (nur relevante EFRs, schlanke Modellierung), Pragmatismus (immer mit Zweck; Zwecke nach Andreasen et al. 2015).
- Kernelemente (auch "embodiment function elements", EF-Elemente) WSP, CSS, Connector mit Definitionen (Wortlaut siehe Befunddatei). Connector besitzt eine repräsentative Wirkfläche und ist ein parametrisiertes Modell der relevanten Umgebung, im Betrachtungsbereich, aber außerhalb des Gestaltungsbereichs (Albers und Wintergerst 2014; Alink 2010).

### 5. Grundhypothesen (S. 245)
- (1) Funktionsrelevante Elemente wirken über Wechselwirkung mit mindestens einem anderen Element; Wechselwirkung nur bei Kontakt von Wirkflächen (Matthiesen 2002).
- (2) Eine Funktion benötigt mindestens zwei WFP, verbunden durch eine LSS und beide über Connector in die Umgebung eingebunden (Albers und Wintergerst 2014).
- (3) Jedes Teilsystem ist mit WFP, LSS und C auf verschiedenen Abstraktions- und Detaillierungsebenen beschreibbar; dazu Variation von Anzahl, Anordnung und/oder Eigenschaften (Albers und Wintergerst 2014).

### 6. Vergleich mit CPM und Axiomatic Design (S. 245 bis 246)
- Beispiel **Schrägkugellager** unter Axiallast (Abb. 1), Darstellung der Kernelemente im Querschnitt; Vergleich mit CPM und Axiomatic Design (Abb. 2).
- Empfohlene Kombination: C&C²-A zum Finden funktionsrelevanter Gestaltparameter, CPM zum Strukturieren, Axiomatic Design zur Entkopplung. Detailvergleich AD und C&C²-A bei Marques et al. (2009). Durch Änderung von LSS- und WFP-Eigenschaften wäre auch ein Magnetlager denkbar.

### 7. Strukturelemente (S. 247 bis 248)
- **Wirknetz (Wirk-Net)** in einem Zustand t_x, **Wirkstruktur (Wirk-Structure)** über die untersuchten Zustände (Albers und Wintergerst 2014).
- Weitere Elemente: Wirkfläche (WF), Begrenzungsfläche (BF), **Tragstruktur (Support Structure, SST) = Summe der modellierten LSS**, Reststruktur (RS) = Volumen, das nie LSS wird (Matthiesen 2002).
- Abb. 3 zeigt eine **Ontologie der Elemente und Elementmengen nach Gladysz (2019)**.

### 8. Heuristiken zum Modellaufbau (S. 247 bis 248)
- Zuerst Systemgrenze festlegen; Wirkungen von außen über Connectoren. Neben der örtlichen gibt es eine **zeitliche Systemgrenze**.
- **Zustand** = Zeitraum, in dem WFP, LSS und C unverändert bleiben. Ändert sich der Lastfall, muss das Modell angepasst oder neu erstellt werden.
- Beispiel Kreuzschlitz-Verschraubung mit **Cam-out-Effekt** (Abb. 4, in Analogie zu Thau 2013).
- **C&C²-Sequenzmodell** (Albers et al. 2008a) verknüpft Zustandsmodelle; eine Sequenz hat **mindestens zwei Zustände**. Für logisch verknüpfte, nicht lineare Zustände das **erweiterte Sequenzmodell** (Matthiesen und Ruckpaul 2012).

### 9. Modellverifikation (S. 248 bis 249)
- Verifikation über **Konstruktionshypothesen (design hypotheses)** (Matthiesen et al. 2017): Gestaltparameter aus einem Kernelement wird in einer Wenn-Dann-Hypothese mit messbarer Funktion oder messbarem Systemverhalten verknüpft; **Testplan** ist wesentlicher Bestandteil und wird bei der Ableitung festgelegt.

### 10. Syntheseregeln (S. 249)
- Drei Grundoptionen hinzufügen, entfernen, Eigenschaften ändern, jeweils für WFP und LSS (Tab. 1, sechs Metaregeln). Tabellenunterschrift nennt Albers, Ohmer und Eckert (2004), der Fließtext Albers, Burkardt und Ohmer (2004). Connectoren sind in Tab. 1 nicht enthalten.

### 11. Forschungsmethodik (S. 249 bis 250)
- Literaturreview mit Data Mining, Suche Anfang 2018, Update Mitte 2019. Suchbegriffe DE/EN Wirkflächenpaar, Leitstützstruktur, Connector.
- Rund **14.500 Publikationen** gescreent, **220 relevant**, im Update **157 weitere**; daraus **39 Anwendungsfälle**. Kategorisierung nach Modellzweck (Andreasen et al. 2015) und Zeitachse (Abb. 5).

### 12. Anwendungen (S. 250 bis 259)
- Tab. 2 listet 39 Fälle mit System, Quelle, Zweck, Beteiligten (D = Entwickler des Ansatzes, I = unabhängige Forschende) und Nutzungsart (MP = Reifungsphase, O = Originalansatz, A = Adaption).
- Verteilung laut Tab. 2 (nachgezählt) **OI 20, DD 8, CU 5, COM 4, MG 2**; Beteiligte D 29, I 8, D,I 2; Nutzung O 22, MP 9, A 8.
- Systeme u. a. humanoider Roboter, Kupplungen, Hybridantriebe, Nockenwelle, Biegebalken, Rennwagenaktuator, Schiebedach, **Druckausgleich (#33)**, **Vakuumpumpe (#35)**, **Hygienic Design (#36)**, Schlagbohrer, Spannelement.
- **Capture the unknown (#20, Leichtbau)** nach Posner et al. Sicherheits-Schutztür (Abb. 6), Variation durch Hinzufügen, Entfernen, Eigenschaften ändern; **134 kg Ausgangsgewicht, 49 kg eingespart** bei nahezu keinen Mehrkosten.
- **Define the design (#23, Zingel et al. 2012)** Hybridantrieb, Integration von C&C²-Prinzipien in **SysML** (Aktivitäts-, Zustands-, Blockdiagramme; Connectoren als Blockdiagramm) gekoppelt mit **Simulink** (Abb. 7).
- **Obtain insight (#5)** Bolzensetzgerät, **600 J** freigesetzte Energie (Schlagbohrer etwa 5 bis 10 J). FMEA wurde wegen Funktionsintegration unbeherrschbar; **erweitertes Sequenzmodell für logische Zustände** machte FMEA handhabbar (Abb. 8, 9; Matthiesen und Ruckpaul 2012).
- **Obtain insight (#8)** Einscheiben-Trockenkupplung über Produktgenerationen. Erhöhung des Moments bei gleichem Bauraum; Anpressen führte zu thermischen Problemen, daher Optimierung über Reibwert µ. Zoom auf Teilfunktion, WFP1 Schwungrad-Kupplungsscheibe, WFP2 Kupplungsscheibe-Druckplatte. **Temperaturverteilung als Indikator** für reale Wirkfläche; ideale (gestrichelt) vs. effektive (durchgezogen) WFP-Umrisse (Abb. 10 bis 12).
- **Manage (#16)** Nockenwelle; C&C²-Modell der Kernkomponenten, Variation von Parametern klassifiziert (Nockendurchmesser = unkritische Übernahmevariation, Nockenbreite = Gestaltvariation mit neuer Validierung); **datenbankgestützte Auswertung** bestehender Produkte im Angebotsprozess (Abb. 13, 14).
- **Communicate (#24, Scherer 2016)** Hybridmodul Porsche 918 Spyder in **Cameo Systems Modeler 18.1** mit Stereotypen für Gestaltelemente, Funktionen, LSS und WFP. **31 technische Themen** dokumentiert, **rund 7000 Modellelemente**, **16 Produktentwickler** bestätigten zu **69 %** Verständlichkeit der Darstellung, **75 %** Bedienbarkeit, **81 %** Wissenstransfer; Modellierungsaufwand im Mittel **2,25 h** (Abb. 15 bis 17).

### 13. Discussion (S. 259 bis 261)
- FF1: Alle fünf Zwecke abgedeckt; meist industrielles Umfeld; Hemmschwelle für Alltagsnutzung; fast nur deutschsprachig und mit Beteiligung der Entwickler; Adaptionen sind gewollt.
- FF2: Alle Anwendungen nutzten Referenzsysteme; Modelle oft auch quantitativ (relevante Parameter mit Werten). **Keine Anwendung zeigte explizite Wiederverwendung** der Modelle.
- FF3: Alle Anwendungen betrafen **mechanische Teilsysteme** meist mechatronischer Systeme; **keine Anwendung in Flüssigkeits-, Gas- oder Feldsystemen**, obwohl die Definition dies beansprucht. C&C²-Modelle sind **zweidimensionale konzeptuelle Modelle ohne zugrundeliegende Datenstruktur**; Verbindung zwischen Betrachtungsebenen bleibt unklar. Vorschlag einer CPM-ähnlichen Struktur, integrierbar in CAx-Modelle.

### 14. Conclusion and outlook (S. 261)
- Forschungsbedarf Anwendbarkeit (außerhalb DACH, nicht-mechanische Probleme) und Nützlichkeit (Wiederverwendung, Quantifizierung von EFR-Wissen).

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Modelle sind 2D ohne Datenstruktur, Ebenenbezug unklar (S. 261) | Kernbegründung des Tools; Graph-Datenmodell (Elemente, Zustände, Ebenen) mit expliziten Eltern-Kind-Verknüpfungen zwischen Zoom-Ebenen |
| Metamodell vs. konkretes Modell C&C²-M (S. 243) | Trennung Schema (Elementtypen, Regeln) und Projektinstanzen |
| Zustand = Zeitraum ohne Änderung von WFP, LSS, C; Sequenz mindestens zwei Zustände; erweitertes Sequenzmodell mit logischen Zuständen | Zustandsobjekt mit Zeitintervall, Sequenz als gerichteter Graph mit Verzweigungen; Prüfregel "Sequenz hat mindestens 2 Zustände" |
| LSS verbindet genau zwei WFP; Funktion braucht mindestens zwei WFP, eine LSS, Connector | Validierungsregeln: LSS hat Kardinalität 2 zu WFP; Funktionswirknetz ohne Connector erzeugt Warnung |
| Connector mit repräsentativer Wirkfläche, im Betrachtungsbereich und außerhalb des Gestaltungsbereichs | Attribute je Element "im Gestaltungsbereich ja/nein", Systemgrenze als Polygon im Bild |
| Tragstruktur = Summe modellierter LSS, Reststruktur = nie LSS | Abgeleitete Sichten (automatisch berechnet), Reststruktur als Leichtbau-/Retrofit-Hinweis |
| Modellzwecke nach Andreasen et al. (CU, OI, DD, MG, COM) | Pflichtfeld Modellzweck mit diesen fünf Werten, Filter im Projektarchiv |
| Syntheseregeln hinzufügen, entfernen, ändern je WFP/LSS; Leichtbau 134 kg zu 85 kg | Variantengenerator mit Änderungslog je Element, Retrofit-Workflow |
| Ideal vs. effektive Wirkfläche über Temperaturverteilung (Kupplung) | Je WFP Geometrievarianten "ideal" und "gemessen" mit Messmethode und Beleg |
| SysML/Cameo-Stereotypen, Nockenwellen-Datenbank (Übernahme- vs. Gestaltvariation) | Export nach SysML; Variationsart je Parameter (Übernahme, Gestalt, Prinzip) für Wiederverwendung |
| Keine Anwendungen in Fluid-, Gas- und Feldsystemen | Lerninhalt und Pilotfälle Wasser/Energie (Pumpen, Ventile, Wärmeübertrager) als Alleinstellungsmerkmal; Einschätzung, im Paper nicht vorgeschlagen |

## Im Paper zitierte Schlüsselquellen

Albers, Matthiesen und Lechner 2002 (Grundmodell, Konstruktion 54); Matthiesen 2002 (Diss., Basisdefinition); Albers, Ohmer und Eckert 2004 (Benennung C&CM, kognitive Perspektive); Albers, Burkardt und Ohmer 2004 (TMCE, Syntheseprinzipien); Albers et al. 2005 (C&CM als Denkmodell); Albers et al. 2008a (DESIGN, Sequenzmodell); Albers et al. 2008b (TMCE, zeitliche Dekomposition); Ohmer 2008 (Diss., Synthese); Alink 2010 (Diss., Funktion, C&C-Ansatz); Matthiesen 2011 (ICED, Thinking Tools); Matthiesen und Ruckpaul 2012 (logische Zustände); Zingel et al. 2012 (SysML); Thau 2013 (Diss., Heuristiken); Albers und Wintergerst 2014 (Anthology); Posner et al. 2012 bis 2016 (Leichtbau); Scherer 2016 (Diss., MBSE Hybrid); Matthiesen et al. 2017 (SWP 61, Konstruktionshypothesen); Gladysz und Albers 2018a/b, Gladysz 2019 (Fehleranalyse, Ontologie); Matthiesen, Grauberger und Schrempp 2019 (erweitertes Sequenzmodell); Beetz und Kirchner 2019 (Wirkraummodell, Hygienic Design).
