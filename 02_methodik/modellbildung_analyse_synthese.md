# Modellbildung, Analyse, Verifikation, Synthese

Praktische Vorgehensweise mit dem C&C²-Ansatz. Hauptquellen: Lehrbuchfassung `Matthiesen2021` (Pahl/Beitz Kap. 13), `Matthiesen2018a` (KIT SWP 58), Prozessmodell `Troester2025b`, Heuristiken `Thau2013`. Stand 27.10.2026, gegen Volltexte geprüft.

## 1. Grundlogik

Gestaltung = iteratives Wechselspiel aus **Synthese** und **synthesegetriebener Analyse** (`Matthiesen2021`). Das C&C²-Modell macht den sonst impliziten Gestalt-Funktion-Zusammenhang (GFZ, EFR) explizit und prüfbar. Einsatzzwecke laut `Albers2014` (S. 158): Analyse (Funktionen und relevante Gestaltmerkmale erkennen), Synthese (Merkmale optimieren, Wirkstruktur erweitern oder reduzieren), **Dokumentation und Kommunikation**.

**Risikologik nach `Matthiesen2018a`:**

| | GFZ unbekannt | GFZ implizit bekannt | GFZ explizit dokumentiert |
|---|---|---|---|
| Gestalt dokumentiert | hohes Risiko | mittleres Risiko | geringes Risiko |
| Gestalt nicht dokumentiert | hohes Risiko (Cluster 4) | hohes Risiko | nicht möglich |

Faustregel `Thau2013` (S. 97): ein explizites Modell lohnt sich ab zwei beteiligten Personen oder ab mehr als einer Funktion.

## 2. Klassisches Vorgehen in der Analyse (Schritte a bis g)

Die Inhalte sind in `Matthiesen2018a`, `Matthiesen2021` und `Grauberger2022b` gleich, die **Reihenfolge von b und c unterscheidet sich**. Maßgeblich ist die Lehrbuchfassung 2021 (Abb. 13.15, S. 428 bis 429). "Die beschriebenen Schritte müssen dabei nicht zwangsläufig in dieser Reihenfolge ablaufen" (S. 427).

| Schritt | Tätigkeit (`Matthiesen2021`) | Ergebnis | Abweichung SWP 58 |
|---|---|---|---|
| a | Zweck des Modells notieren | Zweck-Statement | gleich |
| b | Systemgrenze in Raum und Zeit festlegen | Betrachtungsraum, Zustandsliste | in SWP 58 Schritt c |
| c | System bei der Funktionserfüllung abbilden (Foto, Skizze, CAD-Schnitt, CT, Video) | Systemabbild | in SWP 58 Schritt b |
| d | Fluss der Systemgrößen verfolgen (Energie, Stoff, Information) | Flusspfade | gleich |
| e | Gestaltfunktionselemente im Systemabbild darstellen | C&C²-Modell (Wirknetz) | gleich |
| f | Funktionsrelevante Gestaltparameter identifizieren und Zusammenhang formulieren | Parameterliste | gleich |
| g | Modell verifizieren (gedanklich, Beobachtung, Konstruktionshypothesen) | geprüftes Modell | gleich |

Ältere Leitfäden: vier Kernaktivitäten nach Albers (Systemgrenzen, Ort festlegen, Detaillierung, Sequenzmodell; `Thau2013` S. 34 bis 36 nach `Albers2008a`), Tab. 8.1 in `Albers2014` (Vorbereitung, Problemklärung, Gestaltspezifikation mit QFD, DSM, DoE, FMEA), Aktivitäten mit Leitfragen in `Alink2010` (Tab. 16).

## 3. Extended C&C²-Approach: fünf Schritte (`Troester2025b`)

Begründung: Der klassische Ansatz bietet zu wenig Vorgehensführung für Unerfahrene und keine systematische **Wissensdokumentation**. Bausteine sind Designation Guide (`Troester2023`), Functional Delimitation (`Troester2023b`) und strukturierte Templates.

| Schritt | Ziel | Unterschritte (S. 619 bis 621) |
|---|---|---|
| 1 Pre-Analysis | Grundlage, Umfang und Ziele | 1 vorhandene Informationen sammeln (Spezifikationen, frühere Analysen, Experten, Use Cases; FMEA oder Persona-Methode möglich); 2 Umfang und Zweck festlegen; 3 **Bauteilbaum** anlegen und nach Designation Guide benennen; 4 Aufwand und Ressourcen schätzen |
| 2 Analysis | EFR systematisch untersuchen | 1 Systemzustände und Einbindungspunkte (Connectoren) mit **System State-Function Diagram (SFD)** bestimmen; 2 EFR analysieren (WSP, CSS den Funktionen zuordnen); 3 **Konfidenzniveaus** je Zusammenhang dokumentieren; 4 **funktionale Parameter** festlegen (z. B. Kräfte, Maße) |
| 3 Documentation | Ergebnisse strukturiert ablegen | 1 Templates (Gestaltparameter, Funktionen, Konfidenz); 2 Dokumentation per Hyperlink mit C&C²-Modellen verknüpfen; 3 Vollständigkeit periodisch prüfen |
| 4 Synthesis | Optimierungen entwickeln und testen | 1 Optimierungspotenziale filtern; 2 **Referenzsystemelemente** suchen; 3 **Hypothesen** formulieren und per Simulation oder Prototyp testen; 4 Modifikationen dokumentieren |
| 5 Evaluation and Adjustment | Ergebnis bewerten, nachsteuern | 1 gegen Ziele testen; 2 Lücken identifizieren; 3 anpassen; 4 **Abschlussdokumentation** mit finalen Parametern |

**Functional Delimitation:** Zerlegung eines Bauteils bzw. einer LSS in funktional unterschiedliche Abschnitte, besonders bei einteiligen, nachgiebigen oder multifunktionalen Bauteilen (Beispiel Schraubenfeder, `Troester2025a` Abb. 2). Wird in `Troester2024b` als "new virtual model element" mit eigenem Symbol geführt, in der Tröster-Farbkonvention blau. Primärquelle `Troester2023b` noch nicht beschafft.

**Evaluation:** siehe [Evidenz und Lehre](../03_anwendungen/evidenz_und_lehre.md). Hauptbarrieren: Zeitaufwand der Templates und zu kurze Einführung (20 min).

## 4. Analysetechniken

| Technik | Beschreibung | Quelle |
|---|---|---|
| Zoom-In / Zoom-Out | Element in kleinere Elemente auflösen bzw. zusammenfassen (GH 3); Modelle anderer Ebenen bleiben gültig; Punktnotation WFP1.2 | `Matthiesen2021` S. 435 bis 436, `Albers2008a` S. 248 |
| Shift | Fokus entlang des Wirknetzes verschieben. "Dadurch wird die Systemgrenze erweitert, indem ein Connector in Wirkflächenpaare und Leitstützstrukturen aufgelöst wird." Umgekehrt WFP und LSS zu neuem Connector zusammenfassen | `Matthiesen2021` S. 436 |
| Perspektivenwechsel | Gleiches Detail aus anderer Sicht (Kehrmaschine aus Sicht des Auffangbehälters) | `Matthiesen2021` Abb. 13.23 |
| Zustandsmodellierung | C&C²-Sequenzmodell, siehe Abschnitt 5 | `Albers2008a`, `Matthiesen2019b` |
| Comb Approach / Kammstruktur | Detaillierte "Kammzähne" an den Orten der Funktionserfüllung, grobe "Kammbrücke" dazwischen; laut `Matthiesen2019b` schwer anwendbar und kaum weiter genutzt | `Albers2008a` S. 249, `Thau2013` S. 93 bis 97 |
| Systemebenenmodell | Relative Ebenen −1, 0, +1 über Zoom-Out, Shift, Zoom-In; Kritikalität je Element aus Wirkung, Unsicherheit, Einstellbarkeit | `Troester2021a` S. 886 bis 891 |
| Ideal- vs. Realzustand | WFP ideal, nach Fertigungsabweichung, nach Verschleiß getrennt betrachten | `Matthiesen2018a`, `Lemburg2009` |
| Indizienregeln | "Verschleißspuren sind Indizien für Wirkflächenpaare. Druck- und Versagensstellen sind Indizien für Leitstützstrukturen." | `Matthiesen2021` S. 441 |
| Beobachtung schwer zugänglicher WFP | Tuschierpaste, Hochgeschwindigkeitsvideo, Röntgen, CT, Schliffe, Spannungsoptik, vergrößerte Prototypen | `Thau2013` Kap. 6.2 bis 6.3, `Matthiesen2021` |
| Eliminieren zur Prüfung | Alle Elemente außer dem vermuteten entfernen (Funktion bleibt?) bzw. nur das vermutete entfernen (Funktion fällt aus?) | `Thau2013` S. 130 bis 133 |
| Entwicklungsprüfstände, XiL | Reproduzierbares Systemverhalten, Connectoren als Prüfstandsschnittstellen | `Matthiesen2018a`, `Troester2021a` |
| analyseKIT | Gestaltparameter + Versuchsdaten + Beobachtung | `Matthiesen2017b` (Abstract) |

### Heuristiken nach `Thau2013`

Aus fünf Jahren Anwendung bei Hilti (62 Anwender), ohne feste Reihenfolge, je mit Merksatz.

| Gruppe | Heuristiken |
|---|---|
| HMA Modellaufbau (Kap. 5) | Systemgrenze der Gestalt (TOPDOWN/BOTTOMUP, Connectoren neu definieren bei Änderung), Systemgrenze der Zeit (Zustand, Sequenz), Ort der Funktionserfüllung, Kammstruktur, obligatorische Modellbestandteile (mindestens eine Funktion, zwei WFP, ein Connector je WFP an der Grenze, eine LSS; Aussagen als Wissen, Hypothese oder Idee kennzeichnen) |
| HMB Modellbildung (Kap. 6) | Orientierung (Einstieg über WFP, LSS oder Funktion, dem Kraftfluss folgen), WFP bestimmen (7 Techniken), LSS bestimmen (Versagensstellen, Simulation, Spannungsoptik), Funktionen bestimmen (Zeitlupe, Anhalten, Nachstellen, Eliminieren, Verändern), Funktions- und Gestalteigenschaften verknüpfen (Statistik über Lose, DoE, Ersatzgestalt, Simulation) |

## 5. C&C²-Sequenzmodell

**Ursprung:** "Sequenced Product Model" in `Albers2008a` (S. 249 bis 250): neuer Zustand, wenn ein WSP sich auflöst oder bildet; Sequenz ab zwei Zuständen; Sequenzen an eine Systemgrenze gebunden; Einflüsse zwischen Sequenzen (Pause, Stopp, Neustart). Ausgearbeitet in `Thau2013` (hierarchische Zustände 1.3.1, Kammstruktur), erweitert um logische Zustände in `Matthiesen2012`.

**Zustand (2021):** Zeitraum, in dem sich das Modell nicht ändert; neuer Zustand bei Änderung von Anzahl und/oder Eigenschaften der Gestaltfunktionselemente (`Matthiesen2021` S. 423). Thau ergänzt: jeder Zustand hat mindestens zwei Connectoren (S. 82).

**Struktur mit vier Dimensionen (`Matthiesen2019b`, S. 1487 bis 1489):**

| Dimension | Rolle | Herkunft |
|---|---|---|
| Logischer Zustand | übergeordnet, verbindet mehrere Koordinatensysteme; Auslöser (Trigger) bestimmen das Systemverhalten | `Matthiesen2012` |
| Systemzustand | Achse 1 im 3D-Koordinatensystem eines logischen Zustands, Kern des bisherigen Sequenzmodells | `Albers2008a` |
| Detaillierungsgrad | Achse 2, aus GH 3 (Fraktalität) | GH 3 |
| Ort der Funktionserfüllung | Achse 3, für angepasste Systemgrenzen | `Thau2013` |

Jedes Einzelmodell erhält **Metadaten** zu seiner Position; daraus lassen sich **Ansichten** filtern (ein Ort über mehrere Zustände, ein Zustand über mehrere Orte). Industrieanwendung Schiebedach mit 131 Modellen und 12 Orten. Grenze: Dimensionen für **hydraulische oder elektrische Systeme nicht untersucht**.

## 6. Modellverifikation mit Konstruktionshypothesen

Quelle: `Matthiesen2017a` (KIT SWP 61), Lehrbuchfassung `Matthiesen2021` (S. 451 bis 453).

**Leitsatz:** "Wenn [messbarer Gestaltparameter als Stellgröße, mit Referenz], dann [messbare Funktion als Zielgröße, Änderung relativ zur Referenz], weil [Begründung der Vermutung]." Der Weil-Teil kam nach einem Live-Lab (70 Studierende, 25 Umfragedatensätze, 160 Hypothesen) hinzu, weil die Wenn-Dann-Form zur Modellbildung auf Konzeptebene missbraucht wurde.

| Feld | Inhalt | Beispiel Schnellbauschraube (`Matthiesen2018a`, Weil-Teil eigene Illustration) |
|---|---|---|
| Wenn | Gestaltparameter mit Referenz und Änderung | Gewindehöhe gegenüber Referenzschraube verändert |
| Dann | messbare Funktionsänderung relativ zur Referenz | Eindrehzeit ändert sich |
| Weil | Modellvorstellung der Ursache (Bezug zum C&C²-Modell) | Wirkung im WFP Gewinde/Blech |
| Prüfung | Experiment, Messung, Simulation | Versuchsreihe |
| Ergebnis | gestützt / widerlegt | siehe `Matthiesen2018a` Abschn. 5 |

Varianten: Hypothesen als Leitsätze mit Prüf- und Ergebnisfeld in `Troester2021a`; Kennzeichnung von Aussagen als Wissen, Hypothese oder Idee in `Thau2013` (S. 100); Konfidenzniveaus je EFR in `Troester2025b`; sechs getestete Hypothesen am Klemmrollenfreilauf in `Matthiesen2019b`.

## 7. Synthese

### 7.1 Syntheseprinzipien und ihre Herkunft

| Quelle | Formulierung |
|---|---|
| `Matthiesen2002` (S. 70 bis 71) | Noch keine allgemeine Regel. Im Korrosionsbeispiel: WFP aufheben, LSS entfernen oder ändern, WFP einfügen (Lackschicht) |
| `Albers2003a` (S. 5) | Anordnung oder Eigenschaften von WFP und LSS ändern oder weitere WFP und LSS einführen |
| `Albers2005a` (S. 4 bis 5), `Albers2005b` | **Vier Anwendungsmuster:** WSP und CSS hinzufügen, entfernen, Eigenschaften der WSP ändern, Eigenschaften der CSS ändern. Abgeleitet aus Pahl/Beitz, TRIZ und Roth |
| `Thau2013` (S. 36) | Vier Regeln von Albers (nach Albers et al. 2004), von `Ohmer2008` als Metaregeln formuliert |
| `Albers2014` (S. 167) | **Drei Grundoperationen:** "integration or elimination of Working Surface Pairs or Channel and Support Structures as well as modification of their design characteristics" |
| `Grauberger2020a` (S. 249) | "add, remove or change the properties of WSP or CSS", sechs Metaregeln (Tab. 1), Ursprung uneinheitlich zitiert (2004) |
| `Matthiesen2021` (S. 430, 460) | "In der Synthese gibt es ausschließlich drei prinzipielle Möglichkeiten": hinzufügen, entfernen, Eigenschaften bzw. Merkmale verändern |
| `Troester2026` | Drittes Prinzip mechanisch konkretisiert: WFP-Orientierung und -Fläche variieren (Flächenvektor), LSS-Geometrie variieren |

Die verbreitete Zuschreibung "drei Syntheseprinzipien nach Ohmer 2008 und Albers et al. 2005" (`Matthiesen2018a`) ist damit zu präzisieren: 2005 sind es vier Muster, die Dreizahl ist spätestens 2014 belegt. Connectoren sind keine Gestaltungsobjekte der Synthese.

### 7.2 Vorgehen in der Synthese (`Matthiesen2021`, Abb. 13.16)

a) Syntheseprinzipien wählen, b) Hilfestellung suchen (Gestaltungsprinzipien, Richtlinien), c) adaptieren, d) funktionsrelevante Gestaltparameter definieren (z. B. Winkel im WFP mit Toleranzfeld). Danach erneut Analyse. Reihenfolgeregel: zuerst WFP und LSS gestalten, danach Begrenzungsflächen und Reststrukturen (`Matthiesen2021` S. 461; ebenso `Matthiesen2002` S. 122).

### 7.3 Synthesis Gap

C&C² unterstützt die Analyse deutlich besser als die quantitative Synthese (`Troester2026`; bereits `Albers2014` S. 168 und `Albers2011c` fordern Quantifizierung). Vorschlag `Troester2026`: Flächenvektor A_WSP = (A_x, A_y, A_z) je WFP, Flächenpressung p = F/A, Momentengleichgewicht mit LSS-Längen, dreistufiges Vorgehen (Analyse, Übersetzung in mechanische Parameter, hypothesengetriebene Synthese). Empirisch noch nicht validiert.

## 8. Beispiele zum Nachvollziehen

| Beispiel | Technik | Erkenntnis | Quelle |
|---|---|---|---|
| Schiebernase Bolzensetzgerät | Analyse Kraftfluss | Ungünstiger Kraftfluss als Bruchursache | `Matthiesen2018a` |
| Schnellbauschraube / Blechbohrschraube | Initialmodell, Zoom-In, Shift, Sequenz, Hypothese | Spanloses Durchdringen, Patent (Nummer abzugleichen) | `Matthiesen2018a`, `Thau2013` |
| Schraubenmagazin Standsetzgerät | Kompendium, fehlendes führendes WSP | Schraube fällt kopfüber ins Transportrohr | `Albers2008a`, `Thau2013` |
| Zahnradgetriebe (akademisch) | Sequenzmodell mit vier Dimensionen | Kraftfluss wechselt beim Zahneingriff | `Matthiesen2019b` |
| Schiebedach (Industrie) | 131 Modelle, Verschleißspuren | Kraft geht zeitweise in den Antriebsschlitten | `Matthiesen2019b` |
| Klemmrollenfreilauf | Logische Zustände, 6 Hypothesen | Unerwünschtes WFP3 durch Änderung an WFP1 vermieden | `Matthiesen2019b` |
| Lamellenkupplung | Qualitatives Modell + Simulation + DSM | Keramik statt Stahl, Reibleistung über 100 % verbessert | `Albers2014` |
| Nachgiebige Zange | Extended C&C², Functional Delimitation | Mehr Funktionen und Zwischenzustände | `Troester2025a`, `Troester2025b` |
| Wippe, Fangvorrichtung Hebebühne | WFP-Flächenvektor | Quantitative Synthese | `Troester2026` |
