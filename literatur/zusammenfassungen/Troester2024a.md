# Tröster et al. 2024a: Variationsanteile durch Kombination von C&C²-Ansatz und PGE-Modell

| Feld | Wert |
|---|---|
| Autoren | Peter Michael Tröster, Giorgi Tsutskiridze, Tobias Dieck, Albert Albers (Karlsruhe Institute of Technology) |
| Titel | A new approach to derive variation shares by combining the C&C² approach and the PGE model |
| Quelle | International Design Conference DESIGN 2024, Rubrik "Design Theory and Research Methods", S. 165 bis 174, "Published online by Cambridge University Press" (Band der Proceedings of the Design Society im PDF nicht angegeben) |
| Jahr | 2024 |
| DOI | 10.1017/pds.2024.19 |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Troester2024a), nicht im Repo (Lizenz) (10 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag kombiniert den C&C²-Ansatz mit dem **Modell der PGE** (Produktgenerationsentwicklung, Product Generation Engineering), um **Variationsanteile** (variation shares) auch innerhalb **einteiliger Bauteile** zu bestimmen. Schlüssel ist die **funktionale Abgrenzung** (Functional Delimitation), die LSS in funktional unterschiedliche Abschnitte teilt. Am Flaschenbeispiel wird aus pauschal 100 % Gestaltvariation eine Aufteilung von **75/25 %** (Abschnittszählung) bzw. **65/35 %** (Längenanteil) Übernahme- zu Gestaltvariation.

## Inhalte nach Abschnitt

### 1. Introduction (S. 165)
- Qualitative Entwurfsansätze erlauben frühe Bewertung ohne numerische Analyse. Steigende Komplexität verlangt feinere qualitative Modellierung.
- Ziel ist, C&C² und PGE zusätzlich zu Baugruppen auch auf granularere Bauteile anzuwenden. Begründung der Kombination über Grauberger et al. 2020.

### 2. State of the art (S. 165 bis 168)
- Qualitative Modelle sind wichtig, werden aber in Werkzeugen kaum unterstützt; vorhandene Modellierungsunterstützung ist überwiegend rechnerbasiert und quantitativ (nach Grauberger et al. 2022).
- Definitionen **Design Method** und **Design Tool** wörtlich nach Gericke et al. 2017 (S. 166). Werkzeuge assistieren, ersetzen den kreativen Prozess nicht.
- Additive Fertigung und Topologieoptimierung erzeugen monolithische und nachgiebige Bauteile (compliant mechanisms), bei denen Gestalt-Funktion-Zusammenhänge schwer intuitiv ableitbar sind.
- **2.1 C&C² approach (S. 166 bis 167):** Name ausgeschrieben als "Contact & Channel-Connector-Approach". Elemente nach Matthiesen (Pahl/Beitz):
  - Wirkflächenpaare (Work-Surface-Pairs, WSP): Flächenelemente aus zwei Oberflächen fester Körper oder verallgemeinerten Grenzflächen von Flüssigkeiten, Gasen oder Feldern im Austausch von Energie, Stoff, Information.
  - Leitstützstrukturen (Channel-Support-Structure, CSS): Volumenelemente, die "exactly two pairs of effective surfaces" verbinden.
  - Connectoren (C): Abstraktion der funktionsrelevanten Systemumgebung, mit repräsentativer Wirkfläche und zugehörigem Umgebungsmodell, im betrachteten Raum, aber außerhalb des aktuellen Gestaltungsraums.
- **2.1.1 Benennungsleitfaden (Designation guideline, S. 167, nach Tröster et al. 2023a, Procedia CIRP 119):**
  - Hauptsystem erhält einen Buchstaben (Funktion oder Lage).
  - Teilsysteme werden hierarchisch nummeriert, z. B. "1.1".
  - WFP werden mit doppeltem Schrägstrich "//" bezeichnet, z. B. "F1.1//F2.2"; LSS mit Tilde "~".
- **2.1.2 Funktionale Abgrenzung (Functional Delimitation, S. 167 bis 168, Abb. 1 Schraubenfeder, nach Tröster et al. 2023b, SSP 2023):** LSS wird in funktional unterscheidbare Abschnitte geteilt, wenn ein einteiliges Bauteil mehrere Funktionen erfüllt oder eine LSS entlang ihres Weges Eigenschaften ändert. Besonders für einteilige Teile und nachgiebige Mechanismen.
- **2.2 SGE und PGE (S. 168):** Variationsarten nach Albers et al.:
  - Übernahmevariation (Carryover Variation, CV, auch adoption variation): Übertragung von Teilsystemen, konstruktive Anpassungen minimieren.
  - Prinzipvariation (Principle Variation, PV): neues Lösungsprinzip für Funktionseinheiten.
  - Gestaltvariation (Embodiment Variation, EV): Anpassung der Gestalt bei bekanntem Lösungsprinzip, häufigste Entwicklungsaktivität.
  - Zielsystem, Handlungssystem, Objektsystem nach Albers et al. 2019.
- **2.3 Verbindung PGE und C&C² (S. 168):** Nach Albers et al. 2017: PV verändert die Anzahl von WFP und LSS und erfordert umfangreiche Validierung. EV verändert Gestalt und Anordnung innerhalb bestehender Strukturen ohne Hinzufügen oder Entfernen von Elementen. CV betrifft vor allem die **Connectoren** bei erhaltener Kernstruktur.

### 3. Methodology (S. 169)
- Beispiele von Flaschen bis zu nachgiebigen Greifern, generische Beispiele wegen Vertraulichkeit.
- Drei Forschungsfragen: RQ1 bessere Integration C&C²/PGE, RQ2 genauere Bestimmung von Variationsanteilen, RQ3 welche quantitativen Maße existieren und wie unterscheiden sie sich.
- **Vorgehen in vier Schritten:**
  1. Schlüsselkomponenten und Schnittstellen mit C&C² identifizieren (Basis für Funktionsanalyse)
  2. Funktionale Abgrenzung anwenden, Komponenten weiter segmentieren
  3. PGE-Modell nutzen, um Entwicklung der Abschnitte über Iterationen zu verfolgen und Variationsart zuzuordnen
  4. Variationsanteile mit traditioneller Bestimmung vergleichen

### 4. Results (S. 169 bis 171)
- **Flaschen Variante A und B (Abb. 2, 3, S. 170):**
  - Ohne funktionale Abgrenzung: 100 % Gestaltvariation.
  - Mit funktionaler Abgrenzung: drei Bereiche Übernahmevariation, ein Bereich Gestaltvariation.
  - Zählung horizontal abgegrenzter Abschnitte: 75 % CV, 25 % EV.
  - Längenanteil: 65 % CV, 35 % EV.
  - LSS-Länge im EV-Abschnitt um 20 % verringert.
  - Alternative Bezugsgrößen: Flächenabschnitte, Volumenabschnitte (Abb. 2 rechts).
- **Nachgiebiger Greifer (Abb. 4 bis 6, S. 170 bis 171):** Ausgangsentwurf nach Hedge und Ananthasuresh 2009, Ziel Spannungsreduktion. Intuitive Gestaltvariationen verschlechterten das Verhalten (Autoren ohne Erfahrung mit nachgiebigen Mechanismen). Mit C&C²-Analyse und funktionaler Abgrenzung entsteht Generation 4 mit weniger Material und ohne wesentliche Einbuße der Hauptfunktion; Validierung per Lastsimulation (Abb. 6). Keine Zahlenwerte im Text.

### 5. Discussion (S. 172)
- Methode bildet subtile Variationen ab und unterstützt Optimierungsentscheidungen. Weitere Forschung, ggf. Automatisierung durch Rechenwerkzeuge und Algorithmen.

### 6. Summary and outlook (S. 172 bis 173)
- Höhere Granularität erhöht Analyseaufwand.
- Ausblick: Anwendung auf Prinzipvariationen; Variationsanteile mit **Funktionskritikalität** korrelieren, um Risiken abzuschätzen.
- Erklärung zur Nutzung von ChatGPT, DeepL, Grammarly, LanguageTool für Sprache (S. 173).

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Benennungsleitfaden (Buchstabe Hauptsystem, Nummer Teilsystem, "//" für WFP, "~" für LSS) | Automatische ID-Generierung, z. B. WFP-ID `F1.1//F2.2` aus den beiden Flächen-IDs, LSS-ID mit `~` |
| LSS verbindet genau zwei WFP | Validierungsregel: LSS-Objekt hat exakt zwei WFP-Referenzen |
| Funktionale Abgrenzung von LSS | LSS-Segmente als Unterobjekte mit eigener Funktion, Länge, Fläche, Volumen |
| Variationsart je Abschnitt (CV, EV, PV) | Attribut `variationsart` je Segment, Farbkodierung im Modell |
| Variationsanteile nach Anzahl, Länge, Fläche, Volumen | Rechenmodul mit wählbarer Bezugsgröße, Ausgabe in Prozent und Vergleichsansicht |
| Vergleich zweier Generationen (Variante A/B) | Generationenvergleich: Modell Gn−1 und Gn nebeneinander, Segmentzuordnung |
| CV betrifft vor allem Connectoren, PV ändert Anzahl WFP/LSS | Heuristik-Hinweis: Änderung der Elementanzahl markiert Kandidat für Prinzipvariation |
| Greifer: intuitive Variation schlechter als modellgestützte | Lerninhalt / Fallbeispiel "erst analysieren, dann variieren" |
| Ausblick Kritikalität × Variationsanteil | Risikoansicht: Segment mit hohem Variationsanteil und hoher Funktionskritikalität hervorheben |

## Im Paper zitierte Schlüsselquellen
Albers und Wintergerst 2014 (C&C²-A, Anthology), Matthiesen (Pahl/Beitz, Gestaltung, S. 397 bis 465), Matthiesen et al. 2018 (SWP 58), Grauberger et al. 2020 (20 Jahre Anwendungserfahrung, JED), Grauberger et al. 2022 (experimentelle Methodenvalidierung), Tröster, Schmidt, Albers 2023a (Designation Guide, Procedia CIRP 119), Tröster, Prager, Schmid, Albers 2023b (abschnittsweise Gestalt-Funktion-Zusammenhänge, SSP 2023), Albers, Bursac, Rapp 2017 (PGE am Beispiel ZMS).
