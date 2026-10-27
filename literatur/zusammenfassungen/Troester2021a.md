# Tröster et al. 2021: C&C²-Modellierung einer Einscheibentrockenkupplung zum zwangserregten Kupplungsrupfen

| Feld | Wert |
|---|---|
| Autoren | Peter M. Tröster, Thomas Klotz, Simon Rapp, Holger Wessels, Sascha Ott, Albert Albers (alle IPEK, KIT) |
| Titel | Modellierung einer Einscheibentrockenkupplung mithilfe des C&C²-Ansatzes zur Identifikation von kritischen Gestalt-Funktion-Zusammenhängen bezüglich des Schwingungsphänomens zwangserregtes Kupplungsrupfen |
| Quelle | Forschung im Ingenieurwesen (Forsch Ingenieurwes) 85 (2021), S. 881 bis 894, Rubrik Originalarbeiten/Originals; eingegangen 18.06.2021, angenommen 30.09.2021, online 23.11.2021 |
| Jahr | 2021 |
| DOI | 10.1007/s10010-021-00560-0 |
| Lizenz | CC BY 4.0 (Open Access, Projekt DEAL) |
| Volltext | [`../volltexte/Troester2021a.pdf`](../volltexte/Troester2021a.pdf) (14 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Der Beitrag entwickelt ein **systematisches Vorgehen**, um mit dem C&C²-Ansatz **kritische Gestalt-Funktion-Zusammenhänge** für das zwangserregte Kupplungsrupfen zu identifizieren. Kern sind ein **C&C²-Systemebenenmodell** (Ebenen −1, 0, +1, erzeugt mit Zoom-Out, Shift, Zoom-In), **Hypothesen als Leitsätze** mit Prüf- und Ergebnisfeld sowie eine **Kritikalitätsbewertung** aus Wirkung, Unsicherheit und Einstellbarkeit. Ein neuer XiL-Prüfaufbau, dessen Schnittstellen zur Kupplung als **Connectoren mit Nummernschema** modelliert sind, dient zur Verifizierung und Quantifizierung.

## Inhalte nach Abschnitt

### 0. Zusammenfassung / Abstract (S. 881)
- Ziel ist, Entwickler bei der Auswahl kritischer Einflussfaktoren auf zwangserregtes Rupfen zu unterstützen und Lücken in der Erklärung der Wirkzusammenhänge zu schließen.
- C&C²-Modelle werden "über verschiedene Systemebenen hinweg" gebildet, die **Kritikalität von Modellelementen** wird eingeschätzt, Einflussfaktoren aus der Systemumgebung werden konsistent integriert.
- Hypothesen aus den Modellen sind Grundlage für einen Prüfaufbau. Später sollen Variationsideen mit Elementen aus dem Modell der PGE abgeleitet werden.
- Gefördert durch DFG, Projekt AL 533/39-1, Projektnummer 416374536 (S. 893).

### 1. Motivation (S. 882)
- Kupplungssysteme sind schwierig in Analyse und Synthese wegen tribologischer, thermischer und schwingungsdynamischer Effekte.
- Rupfen erzeugt beim Anfahren Längsschwingungen, die Insassen als unangenehm wahrnehmen. Einflussfaktoren sind qualitativ teilweise bekannt, aber selten quantifiziert.

### 2. Stand der Forschung (S. 882 bis 885)
- **2.1 Kupplungsrupfen (S. 882):** Rupfen tritt in der Synchronisierungsphase beim Anfahren auf, Torsionsschwingungen werden über die Antriebsräder zu Längsschwingungen (Abb. 1). Unterscheidung selbsterregt (Reibwertänderung über Gleitgeschwindigkeit) und zwangserregt (periodische Anregung einer äußeren Erregerquelle). Nach Albers und Herbst (1998) braucht Zwangsanregung immer "mindestens zwei Abweichungen" (Abb. 2), etwa Erhebung der Kupplungsscheibe plus Winkelversatz der antriebsseitigen Scheibe.
- **2.2 Unsicherheiten bei der Modellierung (S. 882):** Modellmerkmale nach Stachowiak (Abbildung, Verkürzung, Pragmatik), Reduktionsdilemma nach Lohmeyer, Systemgrenze bestimmt Modellierungsaufwand, Unsicherheitsursachen nach Hastings und McManus (Lack of Knowledge, Lack of Definition), induktives und deduktives Vorgehen.
- **2.3 PGE (S. 883):** Referenzsystemelemente (RSE), drei Variationsarten (Übernahme-, Gestalt-, Prinzipvariation). Prinzipvariation geht "praktisch immer" mit einer Veränderung der Anzahl von WFP und LSS einher. Bei Gestaltvariation bleiben Anzahl und Anordnung der WFP "weitgehend gleich" (Quellen [14 bis 17]).
- **2.4 Systemtheorie nach Ropohl (S. 883):** System, Umgebung, Attribute, Input/Output. "Zustand" hier systemtheoretisch als Attribut, das weder Input noch Output ist (Abb. 3).
- **2.5 C&C²-Ansatz (S. 883 bis 884):**
  - Drei Kernelemente WFP, LSS, Connector (C) "unter Berücksichtigung der drei Grundhypothesen" (Abb. 4 nach SWP 58). Als Vorteil gilt die geringe Anzahl an Kernelementen auch für komplexe Wirknetze.
  - **Freie Modellierungsreihenfolge:** zuerst WFP, dann LSS, oder zuerst die Systemgrenze über Connectoren, dann das Wirknetz.
  - Connector und seine Beschreibung sind "ein zentrales Element in der Lösung von Gestaltungsproblemen" (zitiert nach Thau, im Literaturverzeichnis mit Jahr 2009).
  - Meist werden viele Modelle aus unterschiedlichen Perspektiven, Detaillierungsgraden und Zeitpunkten erstellt.
  - **Vier Aktivitäten** zum Schließen auf weitere Modelle (nach Matthiesen 2021): Zoom-In und Zoom-Out, Shift, C&C²-Sequenzmodell (zeitliche Veränderungen im Wirknetz), Perspektivenwechsel (Beobachtungsbarrieren durch andere Betrachtungsrichtung überwinden).
- **2.6 Versuchsergebnisse in C&C²-Modellen (S. 884 bis 885, Abb. 5):** Nach Albers, Gladysz, Kniel (2016): WFP einer Anpressplatte wird über gemessene Temperaturverteilung präzisiert. Variation der LSS-Steifigkeit vergrößert die tatsächlichen Wirkkontakte. Generation 2 hat drei größere tatsächliche Wirkkontakte statt zwei kleinerer in Generation 1, die Temperaturverteilung wird homogener.

### 3. Forschungsfragen und Forschungsansatz (S. 885 bis 886)
- Offen: welcher Detailgrad von C&C²-Modellen (Untersuchungsgegenstand und RSE) nötig ist, wo quantitative Versuchsdaten die qualitativen Modelle sinnvoll ergänzen, ob Aussagen zum Entwicklungsrisiko von Variationen möglich sind.
- Drei Forschungsfragen: Identifikation von Einflussfaktoren, Bewertung und Selektion, Quantifizierung.
- Forschungsdesign (Abb. 6): Stand der Forschung dokumentieren, C&C²-Systemebenenmodell entlang des Kraftflusses (Abb. 7), Hypothesen (Abb. 8), Kritikalitätsbetrachtung im **Workshop mit sieben Experten des VDI-Kupplungsausschusses**, Skala 0 (kein Einfluss) bis 3 (sehr großer Einfluss) (Abb. 9).
- Prüfaufbau aus Referenzsystem bestehender Prüfstände (Krüger, Stier, Berger, Basiewicz, unveröffentlichte Arbeiten), teils Übernahmevariation, teils Neuentwicklung. Als Vereinfachung ersetzt eine starre Schwungscheibe das ZMS.

### 4. Ergebnisse (S. 886 bis 890)
- **4.1 C&C²-Systemebenenmodell (S. 886 bis 888, Abb. 7):** Bestehendes Modell erweitert. Zoom-Out auf Antriebsstrang des Gesamtfahrzeugs als Ebene −1. Shift auf angrenzende Systeme entlang der Kraftflüsse (Getriebe bis WFP Reifen/Fahrbahn, Fahrereingaben). Ebene 0 Kupplung und Ausrücker, Ebene +1 Subsysteme der Kupplung. Je Subsystem werden geometrische und physikalische Einflussfaktoren gesammelt.
- **4.2 Hypothesen als Leitsätze (S. 888 bis 889, Abb. 8):** Felder Einflussfaktor mit Ausprägung, Wirkrichtung (positiv/negativ auf Rupfen), Begründung des Wirkmechanismus, "Prüfung", "Ergebnis", ein oder mehrere C&C²-Modelle. Beispiel: größerer Tellerungswinkel der Sekundärscheibe soll Rupfen verringern, weil reibaktive Bereiche am Außenradius bleiben. Prüfung über Gestaltvariation in neuen Entwicklungsgenerationen.
- **4.3 Priorisierung (S. 889, Abb. 9):** Drei Kriterien, Summe = **Kritikalitätswert**, Vergleich mit Kritikalitätsmatrix (angelehnt an Albers et al. 2014, Gundlach, Kleppmann):
  - Wirkung (W): von "keine Aussage möglich" über "keine Wirkung" bis "hohe Wirkung"
  - Unsicherheit (U): hoch ohne Versuchsdaten oder Erfahrungswerte, gering mit Versuchsdaten
  - Einstellbarkeit (E): Kontrollierbarkeit (Reproduzierbarkeit, Genauigkeit der Faktorstufen) und Zeitaufwand, von "schlecht einstellbar" bis "gut einstellbar"
  - Numerische Stufen von W, U, E und Matrixgrenzen nur in Abb. 9, im Text nicht angegeben.
- **4.4 Prüfaufbau (S. 889 bis 890, Abb. 10 bis 12):** Physische und virtuelle Subsysteme im IPEK-XiL-Framework, Koppelsysteme grün markiert (E-Motor überträgt echtzeitsimuliertes Motormoment). Untersucht: Kupplung, Ausrücker, Getriebeeingangswelle mit Lagerung. Einstellbare Torsionssteifigkeit (Torsionswelle plus Federpaket) und Massenträgheit für die ersten zwei Eigenfrequenzen, E-Motoren bis 10.000 min⁻¹, 1200 Nm, Drehmomentanregung bis 500 Hz. Berührungslose Dichtungen nach der Kupplungsscheibe zur Dämpfungsminimierung.
  - **Connector-Nummernschema "Cx.1"** (S. 889, Abb. 12): x = laufende Nummer, ".1" = Kupplung. C1.1 Sekundärscheibe, C1.2 bildet mit C1.1 ein WFP (am Prüfstand an einem Schwungrad, bildet über virtuelles Subsystem Fahrer, Umwelt und Motoranregung ab), C2.1/C2.2 WFP der Verzahnung, C3.x Ausrücklager, C4 hydraulische Aktuierung, C5 Umgebungsbedingungen (Temperatur, Luftfeuchtigkeit, Partikel).
- **4.5 Variationsideen und erste Ergebnisse (S. 890 bis 891, Abb. 13, Tab. 1):** Virtuelle Variationen (Kraftstoffversorgung eines Zylinders, Ausrück- und Drehmomentregelung, Dämpfung, Steifigkeit), Klimakammer für Umgebungsbedingungen.
  - Tab. 1, ΔMmax in Nm: 100 % Kraftstoff bei 1500 U/min 15,54. 0 % bei 1500 U/min 29,55. 0 % bei 800 U/min 22,41. 80 % bei 800 U/min 17,90.
  - Luftfeuchtigkeit: Drehmomentdifferenz bis zu +65 % in den ersten Anfahrvorgängen durch Quellen des Belags (Scheibendicke +0,117 mm, +1,27 %), nach [28] (EEE 2021).

### 5. Diskussion (S. 891 bis 893)
- **5.1:** Drei Ebenen reichen wohl nicht, das tribologische System fehlt noch. **Vorschlag neuer Ebenennomenklatur (Abb. 14):** Untersuchungsgegenstand (Lupe) = "Ebene 0", Zoom-In führt zu +1, +2, Zoom-Out zu −1, −2. Ziel: schnellere Orientierung und ein systemübergreifender Leitfaden.
- **5.2:** Leitsatz-Hypothesen erlauben tabellarische Übersicht vieler Einflussfaktoren. Am Beispiel Tellerung zeigt das C&C²-Modell den Zusammenhang allein nicht. Zusätzlich nötig sind weitere Perspektiven und ein **Sequenzmodell**, um das Wandern der reibaktiven Fläche darzustellen.
- **5.3:** Kritikalität erlaubt Vorauswahl, ist aber abhängig von Vorwissen und bewertender Person. Nutzen: Modellersteller hinterfragt eigene Annahmen.
- **5.4:** Übernahmevariation für klimatisierte Prüfkammer, Antriebslagerung, hydraulischen Aktuator, Motorsimulationsmodell. Gestalt- und Prinzipvariation für andere Subsysteme. Immer gleiche Betriebspunkte, Verallgemeinerung offen.
- **5.5:** Virtuelle Variationen erlauben frühe Versuche. Schwächung eines Zylinders verstärkt Rupfneigung, daher auch Gemischbildungsmängel relevant.

### 6. und 7. Zusammenfassung und Ausblick (S. 893)
- Modell um weitere Ebenen, Perspektiven und die Zeit (Sequenzmodelle) erweitern, um den erfolgversprechenden Designraum zu identifizieren.
- Ziel sind ein teilquantifiziertes Systemmodell und ein übergreifender **Leitfaden** zur Analyse und Synthese unerwünschter Phänomene.
- Erweiterung des Prüfaufbaus um zwei Shaker für Axial- und Biegeschwingungen denkbar.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Relative Systemebenen (Ebene 0 = Untersuchungsgegenstand, ±n) | Datenmodell: Feld `ebene_relativ` je Modell, Navigation Zoom-In/Zoom-Out erzeugt Kindmodell mit Ebene ±1 |
| Vier Aktivitäten (Zoom, Shift, Sequenzmodell, Perspektivenwechsel) | Werkzeugleiste mit diesen vier Aktionen, jede erzeugt ein verknüpftes Folgemodell mit Herkunftsvermerk |
| Freie Modellierungsreihenfolge (WFP zuerst oder Connector/Systemgrenze zuerst) | Wizard mit zwei Startpfaden, keine erzwungene Reihenfolge |
| Connector-Schema "Cx.y" (x laufend, y Teilsystem) | Automatische ID-Vergabe für Connectoren, Präfix je Teilsystem, Paarbildung C1.1/C1.2 als WFP |
| Connector C5 für Umgebungsbedingungen | Vorlage "Umgebungs-Connector" mit Attributen Temperatur, Feuchte, Partikel, Medium |
| Hypothese als Leitsatz (Faktor, Ausprägung, Wirkrichtung, Begründung, Prüfung, Ergebnis, Modelle) | Objekt `Hypothese` mit diesen Pflichtfeldern, Status offen/geprüft/verworfen, Verknüpfung zu Modellelementen |
| Kritikalität W + U + E | Bewertungsmaske je Einflussfaktor, Summenwert, Sortierung, Matrixansicht; Hinweis auf Bewerterabhängigkeit, Feld "Bewerter" |
| Expertenworkshop mit Skala 0 bis 3 | Mehrbenutzer-Bewertung mit Mittelwert und Streuung je Faktor |
| Integration Versuchsergebnisse (Temperaturbild präzisiert WFP) | Anhänge (Messbilder) an WFP, Versionierung "ideal" vs. "präzisiert nach Versuch" |
| Variationsideen mit Umsetzungsaufwand (Abb. 13) | Ideenliste je Element mit PGE-Variationsart und Aufwandsklasse (virtuell, Prüfstand, Prototyp) |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Diss., Basisdefinition), Matthiesen et al. 2018 (SWP 58, Abb. 4 und Grundhypothesen), Albers und Wintergerst 2014 (Anthology), Thau (Heuristiken zur Analyse und Synthese mit dem C&C²-Ansatz, im Verzeichnis als 2009), Matthiesen 2021 (Pahl/Beitz, vier Aktivitäten), Albers, Gladysz, Kniel 2016 (KT 2016, Versuchsergebnisse in C&C²-Modellen), Tröster et al. 2021 (EEE 2021, erweiterte Analyse Einscheibentrockenkupplung), Albers, Bursac, Rapp 2017 (PGE am Beispiel ZMS), Albers et al. 2019 (Referenzsystem), Albers und Herbst 1998 (Kupplungsrupfen).
