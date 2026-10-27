# Gladysz und Albers 2018: How do C&C²-models improve efficiency, comprehensibility and scope in failure analysis

| Feld | Wert |
|---|---|
| Autoren | B. Gladysz, A. Albers (Albert Albers, Prof. Dr.-Ing. Dr. h. c., KIT, als Korrespondenzautor) |
| Titel | How do C&C²-models improve efficiency, comprehensibility and scope in failure analysis - an empirical study based on two live-labs |
| Quelle/Reihe | International Design Conference, DESIGN 2018, Rubrik "Design Methods", S. 1127 bis 1138 |
| Jahr | 2018 |
| DOI | 10.21278/idc.2018.0497 |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Gladysz2018a), nicht im Repo (Lizenz) (12 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Zwei **Laborstudien in Live-Labs mit insgesamt 80 Masterstudierenden** vergleichen eine **C&C²-basierte Fehleranalysemethode** (Wirknetz-basierte Beschreibung von **Fehlermechanismen**) mit konventionellen Modellen. Studie 1 (38 Personen, Schaltaktuator) zeigt **signifikant bessere Nachvollziehbarkeit (comprehensibility)** in allen drei Fehlerfällen und einen **Effizienzgewinn nur beim komplexesten Fehlerfall**. Studie 2 (42 Personen inkl. 7 Moderatoren, **Hochdruck-Kraftstoffpumpe**) zeigt einen **erweiterten Analyseumfang**, denn Testgruppen finden signifikant mehr Ursachen in der peripheren Zone (Fehlerfälle 1 und 3), gesteuert über die **Connectoren**.

## Inhalte nach Abschnitt

### 1. Introduction (S. 1127)
- Bedarf an effektiver und effizienter kollaborativer Fehleranalyse; viel implizites Wissen aus Vorgängergenerationen.
- Methode nach Gladysz et al. (2017) integriert Gestalt und Funktion. Zwei Laborstudien mit **80 projekterfahrenen Masterstudierenden**, Fehlerfälle aus realen Projekten der Antriebsstrangentwicklung, ein **pneumatisches Getriebeschaltsystem** und eine **Hochdruckpumpe für die Benzineinspritzung** ("high-pressure pump for gasoline fuel injection").

### 2.1 Fehleranalyse im Stand der Technik (S. 1127 bis 1128)
- FMEA etabliert, aber erfahrungsbasiert und mit unzureichender Beschreibung technischer Risiken; modellbasierte Ansätze (SysML, CAD/PLM, Ontologien) setzen auf Formalisierung und Automatisierung.
- Review 40 Jahre FMEA (Spreafico et al. 2017) bemängelt fehlende Modelle für Ursache-Wirkungs-Ketten; die Methode adressiert diese Lücke.

### 2.2 Fehlermechanismen mit C&C²-A (S. 1128 bis 1129)
- Basis Albers und Matthiesen (2002). Kern ist die visuelle Beschreibung von Ursache-Wirkungs-Beziehungen auf Gestaltebene mit drei C&C²-Elementen; daraus das **Wirknetz (Wirk-Net)** (Albers und Wintergerst 2014), das Funktionen und Fehler beschreibt.
- Wörtliche Definitionen von WFP, LSS und Connector (nach Albers und Wintergerst 2014; Matthiesen et al. 2018), siehe Befunddatei.
- Systematische Analyse des Wirknetzes ausgehend vom Fehlerort ergibt Fehlermechanismen und damit Ursachen oder Folgen.
- Beispiel **pneumatischer Aktuator** (Abb. 1), der wegen **ungleichmäßiger Wärmedehnung des Gehäuses durch Motorabwärme** klemmt. WFP2, LSS2, WFP5, LSS3 = mögliche Ursachenorte; das Wirknetz zwischen ihnen und den Fehlerwirkorten WFP3, WFP4 spannt den Fehlermechanismus auf.
- Vorherige Interviewstudien zeigten Potenzial, aber keine Quantifizierung.

### 3. Research methodology (S. 1129 bis 1131)
- Forschungshypothese: kollaborative Anwendung verbessert Effizienz, Analyseumfang und Nachvollziehbarkeit. Operationale Hypothesen:
  - H1 mehr identifizierte Ursachen pro Zeit mit integriertem Modell (C&C²-A) gegenüber getrennten Modellen (CAD-Zeichnungen, Internal Block Diagram)
  - H2 höhere Nachvollziehbarkeit mit integriertem Modell
  - H3 erweiterter Analyseumfang mit C&C²-Wirknetz gegenüber Fehlerbäumen
- Laborstudien mit Masterstudierenden Maschinenbau mit Live-Lab-Erfahrung (Live-Labs dauern mehrere Monate, Co-Creation mit Industriepartnern); homogene Stichprobe bewusst gewählt.
- Alle 80 mit grundlegender bis fortgeschrittener FMEA-Erfahrung; Teams zu zwei oder drei Personen; Test- und Kontrollgruppe (Abb. 2).
- **Studie 1**: **38 Studierende** aus dem Live-Lab "Integrated Product Development 2016/17", physisches Team-Workshop-Format; Modelle vorgegeben; Zeiten je Phase gemessen; Fragebogen; Bewertung durch zwei unabhängige Systemexperten.
- **Studie 2**: **42 Studierende (davon 7 Moderatoren)** aus dem Live-Lab "ProVIL 2017", virtuelles moderiertes Format; mehr Modellierungsfreiheit; Bildschirm- und Audioaufzeichnung.
- **Nachvollziehbarkeit** (Abb. 3) aus drei Indikatoren: Zuordenbarkeit der Ursache (0 bis 3), Präzision der Ursachenbeschreibung mit messbarer Eigenschaft (0 bis 3), Plausibilität (0 bis 1); Teamwert als Mittel über j Ursachen; zusätzlich korrigierter Wert unter Einbezug von Ursachenanzahl und Phasendauer.
- **Analyseumfang**: **Schalenmodell mit drei Zonen**. Zone 1 primärer Bereich am Fehlerort, Zone 2 erweiterter Bereich innerhalb der Systemgrenze mit wechselwirkenden Teilsystemen, Zone 3 peripherer Bereich auf oder jenseits der gezeichneten Systemgrenze. **226 Ursachen** in Studie 2 zugeordnet.

### 4. Empirical results (S. 1131)
- Nichtparametrische Tests, Mann-Whitney-U (unabhängig), Wilcoxon (abhängig), exakte zweiseitige Werte; p < 0,05 signifikant; Effektstärke r nach Gignac und Szodorai (2016) klein 0,1, typisch 0,2, relativ groß 0,3.

### 4.1 Studie 1, Schaltaktuator (S. 1132 bis 1134)
- System: **pneumatischer Getriebeschaltaktuator eines Rennwagens**. Fehlerfälle FM1 Gleitlager bricht, FM2 Aluminiumhalter verbiegt, FM3 Kolben klemmt.
- Testgruppe mit C&C²-Modell von Funktion und Fehlfunktion und Dokumentationsformular mit Zuordnung zu C&C²-Elementen; Kontrollgruppe mit vereinfachten Skizzen und reduziertem FMEA-Formblatt; beide mit Internal Block Diagrams und CAD-Zeichnungen; 10 min Einarbeitung.
- **Effizienz** (Ursachen pro Minute, Abb. 5): FM1 U = 136,5, p = 0,220, r = 0,202; FM2 U = 172,5, p = 0,862, r = 0,029; **FM3 U = 81,0, p = 0,004, r = 0,467**. FM3 wurde als komplexester, FM2 als einfachster Fall empfunden. Effizienzgewinn steigt mit Fehlerkomplexität.
- **Nachvollziehbarkeit** (326 bewertete Ursachen, Abb. 6): Qualität FM1 p = 0,005, r = 0,440; FM2 p = 0,008, r = 0,417; FM3 p = 0,001, r = 0,487. Korrigiert (Q mal n/min) FM1 p = 0,022, r = 0,371; **FM2 p = 0,073, r = 0,301 (nicht signifikant)**; FM3 p = 0,008, r = 0,417.
- Fragebogen FM2 (Abb. 7): Kontrollgruppe gewichtet die Bauteilansicht höher, Testgruppe die Systemansicht.

### 4.2 Studie 2, Hochdruckpumpe (S. 1134 bis 1136)
- Fehlerfälle FM1 **Kolben klemmt**, FM2 **Leckage an der Kolbendichtung**, FM3 **Druckventil öffnet unterhalb des Sollwerts**.
- Testgruppe mit C&C²-Vorlagen, Kontrollgruppe mit Fehlerbaum-Vorlagen; Liste physikalischer und chemischer Beanspruchungen (Verschleißarten, Korrosion, Reibkorrosion, Kriechen, Ermüdung, Verformung) für Test nach C&C²-Elementen, für Kontrolle nach Effekten sortiert; identische CAD-Zeichnungen, bei Testgruppen mit C&C²-Overlay.
- 1 h Einführung, Einzelkabinen, Cloud-Kollaboration; 10 min Einarbeitung in die Pumpe (System für alle neu); **30 min je Fehlerfall** mit moderierten Teilphasen; daher keine Effizienzaussage.
- Zonenvergleich (Abb. 8): **FM1 Zone 3 p = 0,014, r = 0,382**; **FM3 Zone 3 p = 0,022, r = 0,368**; FM2 Zone 2 p = 0,051, r = 0,322 (knapp nicht signifikant); übrige Zonen nicht signifikant.
- Kontrollgruppen orientierten sich stärker an der Beanspruchungsliste, Testgruppen bauten Ursachenketten systematisch vom Fehlerort bis zu den **über Connectoren definierten äußeren Einflüssen** auf.

### 5. Discussion (S. 1136)
- Initialer Modellierungsaufwand nicht berücksichtigt; Autoren schätzen ihn für C&C²-Modelle meist höher ein.
- Fehlerkomplexität analog Fehlerbaum (mehr Äste und Ebenen = komplexer), nur retrospektiv bestimmbar; Priorisierungsansatz in Gladysz et al. (2018).
- Nachvollziehbarkeit steigt durch Zuordnung von Ursachen zu Eigenschaften von WFP, LSS und Connector; wichtig für gemeinsames Risikoverständnis im Team.
- Beim Analyseumfang zeigte sich, dass bei FM2 **nur Testgruppen die zwei Vorspannfedern der Dichtung** als mögliche Ursache betrachteten. Fehlermechanismen unterscheiden sich in der Elementanzahl kaum; Unterschied ist die Orientierung am Wirknetz.
- **Grenze**: Wirknetz ist auf die physikalische und chemische Domäne beschränkt; Fehlerbäume können zwischen System- und Prozessdomäne wechseln.

### 6. Summary and outlook (S. 1136 bis 1137)
- Positive Wirkung auf Effizienz, Nachvollziehbarkeit, Umfang; kein Nutzen in jedem Fall; nur mechanische Domäne untersucht; als Potenzialbewertung zu verstehen.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Fehlermechanismus = Pfad im Wirknetz vom Ursachen- zum Wirkort | Modus "Fehleranalyse" mit Markierung Fehlerort und Ursachenort und automatischer Pfadsuche im Elementgraph |
| Ursachen zugeordnet zu WFP, LSS, Connector mit messbarer Eigenschaft | Ursachenformular mit Pflichtfeldern Element-ID, Eigenschaft/Parameter, Tendenz (steigt/fällt) |
| Bewertungsschema Zuordenbarkeit 0 bis 3, Präzision 0 bis 3, Plausibilität 0 bis 1 | Qualitätsampel je Ursache, automatisch aus Feldvollständigkeit |
| Drei-Zonen-Schalenmodell | Zonenattribut je Element relativ zum Fehlerort; Abdeckungsanzeige "Zone 3 noch nicht betrachtet" |
| Connector als Träger äußerer Einflüsse (Wärme, Last) | Connector-Typen (thermisch, mechanisch, fluidisch, chemisch) mit Checkliste |
| Beanspruchungsliste nach C&C²-Elementen sortiert | Hinterlegter Katalog Schädigungsmechanismen je Elementtyp (Verschleiß, Korrosion, Kriechen, Ermüdung, Verformung) |
| Nutzen steigt mit Fehlerkomplexität | Empfehlung im Tool, C&C²-Fehleranalyse für komplexe, mehrstufige Fehlerfälle zu priorisieren |
| Wirknetz deckt keine Prozessdomäne ab | Verknüpfung zu FMEA/Fehlerbaum-Export für Prozessursachen |
| Hochdruckpumpe mit Dichtung, Vorspannfedern, Druckventil | Beispielprojekt Pumpe als Lerninhalt für Wasser/Energie (Einschätzung, Übertrag auf Wasserpumpen) |

## Im Paper zitierte Schlüsselquellen

Albers und Matthiesen 2002 (Grundmodell, Konstruktion 54 Nr. 7/8, S. 55 bis 60); Albers und Wintergerst 2014 (Anthology, im Literaturverzeichnis als "The Contact and Channel Approach (C&C2-A): Relating a System's Physical Structure to Its Functionality", S. 151 bis 171); Matthiesen et al. 2018 (CIRP Design, From Reality to Simulation, Quelle der Definitionen); Gladysz, Spandl und Albers 2017 (ICED, Fehleranalysemethode); Gladysz et al. 2018 (ZWF, Priorisierung von Funktionsumfängen); Albers et al. 2017 (ICL, Live-Labs).
