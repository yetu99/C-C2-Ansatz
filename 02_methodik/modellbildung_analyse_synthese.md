# Modellbildung, Analyse, Verifikation, Synthese

Praktische Vorgehensweise mit dem C&C²-Ansatz. Hauptquelle ist das im Repo liegende `Matthiesen2018a` (KIT SWP 58, [Zusammenfassung](../literatur/zusammenfassungen/Matthiesen2018_SWP58.md)), ergänzt um neuere Arbeiten.

## 1. Grundlogik

Gestaltung = iteratives Wechselspiel aus **Analyse** (Gestalt-Funktion-Zusammenhang verstehen) und **Synthese** (Gestalt erzeugen, die die Funktion erfüllt). Das C&C²-Modell macht den sonst impliziten GFZ explizit und prüfbar.

**Risikologik nach `Matthiesen2018a`:**

| | GFZ unbekannt | GFZ implizit bekannt | GFZ explizit dokumentiert |
|---|---|---|---|
| Gestalt dokumentiert | hohes Risiko | mittleres Risiko | geringes Risiko |
| Gestalt nicht dokumentiert | hohes Risiko (Cluster 4) | hohes Risiko | nicht möglich |

## 2. Vorgehen Modellbildung in der Analyse (SWP 58, Schritte a bis g)

| Schritt | Tätigkeit | Ergebnis |
|---|---|---|
| a | Modellzweck festlegen und dokumentieren | Zweck-Statement |
| b | Geeignete Visualisierung des Systems wählen (Foto, Skizze, CAD-Schnitt, CT, Mikroskopbild) | Systemabbild |
| c | Systemgrenzen definieren: zeitlich (Zustände) und räumlich (Teilsysteme) | Zustandsliste, Betrachtungsraum |
| d | Fluss der Systemgrößen verfolgen (Energie, Stoff, Information) | Flusspfade |
| e | Gestaltfunktionselemente einzeichnen (WFP, LSS, C) | C&C²-Modell (Wirknetz) |
| f | Funktionsrelevante Gestaltparameter identifizieren | Parameterliste |
| g | Modell verifizieren | geprüftes Modell |

## 3. Extended C&C²-Approach (Fünf-Schritte-Prozess)

`Troester2025b` ergänzt den klassischen Ansatz, weil Novizen zu wenig Vorgehensführung haben. Bausteine:
- **Functional Delimitation:** Funktion vor der Modellierung abgrenzen
- **Designation Guide** (`Troester2023`): einheitliche Benennung von WFP, LSS und Teilsystemen über Systemebenen
- **Fünf-Schritte-Prozessmodell** zur Analyse und Dokumentation von GFZ

Evaluation in `Troester2025a` (27 Studierende, 9 Ingenieure): bessere Identifikation von GFZ. Die fünf Schritte im Wortlaut sind noch aus dem Volltext zu übernehmen (OA, siehe [Beschaffungsliste](../literatur/beschaffungsliste.md)).

## 4. Analysetechniken

| Technik | Beschreibung | Quelle |
|---|---|---|
| Zoom (Zoom-In / Zoom-Out) | Detaillierungsgrad an einer Stelle ändern (GH 3) | `Matthiesen2018a`, ASE-Wiki |
| Shift | Fokus entlang des Wirknetzes verschieben, gleiche Detailstufe. Systemgrenze ggf. erweitern | `Matthiesen2018a` |
| Change Perspective | Gleiches Detail aus anderer Sicht betrachten | ASE-Wiki |
| C&C²-Sequenzmodell | Zustände während der Funktionserfüllung verknüpfen. Neuer Zustand bei Änderung von Anzahl oder Eigenschaften der GFE | `Albers2008c`, `Thau2013`, `Matthiesen2019b` |
| Ideal- vs. Realzustand | WFP im Idealzustand, nach Fertigungsabweichung, nach Verschleiß getrennt betrachten | `Matthiesen2018a`, `Lemburg2009` |
| Beobachtung schwer zugänglicher WFP | Spannungsoptik, Hochgeschwindigkeitsaufnahmen, CT, Verschleißspuren | `Matthiesen2018a`, `Thau2013` |
| Entwicklungsprüfstände | Reproduzierbare Abbildung des Systemverhaltens, z. B. Roboter mit Hand-Arm-Modell | `Matthiesen2018a`, `Matthiesen2014` |
| analyseKIT | Kombination aus Gestaltparametern, Versuchsdaten und Beobachtung des Funktionsorts | `Matthiesen2017b` |
| Heuristiken | Erfahrungsregeln für Analyse und Synthese aus Industrieprojekten | `Thau2013` |

## 5. Modellverifikation mit Konstruktionshypothesen

Quelle: `Matthiesen2017a` (KIT SWP 61), angewandt in `Matthiesen2018a`, empirisch untersucht in `Grauberger2022c`.

Aufbau einer Konstruktionshypothese:

| Feld | Inhalt | Beispiel (Schnellbauschraube) |
|---|---|---|
| Gestaltparameter | einstellbares Merkmal am GFE | Gewindehöhe |
| Ausprägung | angenommener Wert / Bereich | Y mm |
| Funktionsgröße | messbare Wirkung | Eindrehzeit |
| Prüfung | Experiment, Messung, Simulation | Versuchsreihe |
| Ergebnis | gestützt / widerlegt | gestützt |

Weitere Fallbeispiel-Logik (Nageldetektion Bolzensetzgerät): Hypothese 1 (Kräfte aus Hauptfunktion) falsifiziert, Hypothese 2 (Trägheit aus Rückstoß) durch Verschleißspuren gestützt.

## 6. Synthese

**Drei Syntheseprinzipien** (`Ohmer2008`, `Albers2005b`, angewandt in `Matthiesen2018a`):

| Prinzip | Beschreibung | Typische Anwendung |
|---|---|---|
| Hinzufügen | WFP und/oder LSS ergänzen | Lastverteilung, zusätzliche Führung |
| Entfernen | WFP und/oder LSS weglassen | Überbestimmung auflösen, Teile sparen |
| Eigenschaften ändern | Form, Lage, Größe, Werkstoff, Oberfläche von WFP/LSS variieren | Kraftfluss optimieren, Reibung anpassen |

Ergänzend:
- Synthese-Heuristiken auf abstrakter Ebene (`Albers2004a`, `Albers2005a`, `Thau2013`)
- **Synthesis Gap:** C&C² unterstützt Analyse deutlich besser als quantitative Synthese (`Troester2026`). Abhilfe siehe [Erweiterungen](erweiterungen.md)

## 7. Beispiele aus SWP 58 zum Nachvollziehen

| Beispiel | Technik | Erkenntnis |
|---|---|---|
| Schiebernase Bolzensetzgerät | Analyse Kraftfluss | Ungünstiger Kraftfluss als Bruchursache |
| Schnellbauschraube / Blechbohrschraube | Initialmodell, Zoom-In, Shift, Sequenzmodell, Hypothese | Spanloses Durchdringen, Patent US 8,342,788 |
| Kunststoffdübel | Spannungsoptik | Unterschiedliche Krafteinleitung zweier Varianten |
| Nageldetektion | Hypothesenbildung | Querbelastung durch Trägheit |
| Auflager | Ideal / gefertigt / verschlissen | WFP-Größe und -Lage verändern Verhalten |
