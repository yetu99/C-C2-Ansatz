# Elemente und Grundhypothesen des C&C²-Ansatzes

Der C&C²-Ansatz (Contact and Channel Approach, C&C²-A) ist laut IPEK ein **Denkzeug**, also ein Werkzeug zur Unterstützung und Strukturierung des Denkens während der Gestaltung. Er ist das **Metamodell**, mit dem konkrete **C&C²-Modelle** zum Gestalt-Funktion-Zusammenhang gebildet werden. Quellen: `Web_IPEK_Glossar`, `Albers2014`, `Matthiesen2021`, `Matthiesen2018a`.

> Zitierschlüssel in `Backticks` verweisen auf [`literatur/quellen.csv`](../literatur/quellen.csv) bzw. das [Literaturverzeichnis](../literatur/literaturverzeichnis.md).
> Wortlaute stammen aus Suchtreffern der Glossarseiten (IPEK, Fraunhofer ASE-Wiki). Vor wörtlicher Zitation im Original prüfen.

## 1. Elementübersicht

| Kategorie | Element (DE) | Element (EN) | Kürzel | Kurzdefinition | Quelle |
|---|---|---|---|---|---|
| Kern | Wirkflächenpaar | Working Surface Pair | WFP / WSP | Entsteht, wenn zwei beliebig geformte Oberflächen fester Körper oder generalisierte Grenzflächen von Flüssigkeiten, Gasen oder Feldern in Kontakt treten und am Energie-, Stoff- und/oder Informationsaustausch beteiligt sind | IPEK-Glossar 11667, ASE-Wiki |
| Kern | Leitstützstruktur | Channel and Support Structure | LSS / CSS | Volumen von festen Körpern, Flüssigkeiten, Gasen oder felddurchsetzten Räumen, das zwei WFP verbindet und die Leitung von Energie, Stoff und/oder Information zwischen ihnen ermöglicht (sinngemäß, Wortlaut in `Albers2014` / `Matthiesen2021` prüfen) | abgeleitet aus IPEK-Glossar (Reststruktur), `Albers2005a` |
| Kern | Connector | Connector | C | Integriert die wirkungsrelevanten Eigenschaften außerhalb des Betrachtungsbereichs, ist eine relevante Abstraktion der Systemumgebung und hat eine repräsentative Wirkfläche. Liegt im Betrachtungsraum, aber außerhalb des Gestaltungsraums | IPEK-Glossar 11363, ASE-Wiki |
| Neben | Wirkfläche | Working Surface | WF / WS | Oberflächen fester Körper oder generalisierte Grenzflächen von Flüssigkeiten, Gasen oder Feldern, die dauernd oder zeitweise mit einer anderen Wirkfläche in Kontakt stehen und dann ein WFP bilden | IPEK-Glossar 11666 |
| Neben | Reststruktur | Residual Structure | RS | Volumina von festen Körpern, Flüssigkeiten, Gasen oder felddurchsetzte Räume, die nicht zur LSS werden | IPEK-Glossar 11578 |
| Neben | Begrenzungsfläche | Boundary Surface | BF | Oberflächen bzw. Grenzflächen, die mit keiner zweiten Fläche in Kontakt stehen und kein WFP bilden (werden nie zu Wirkflächen) | IPEK-Glossar 11347, `Behrendt_FB36` |
| Struktur | Tragstruktur | Carrier Structure | TS | Menge aller möglichen LSS. Wird benötigt, wenn LSS aus mehreren C&C²-Modellen (Anwendungsfälle, Zustände) berücksichtigt werden müssen | ASE-Wiki Tragstruktur |
| Struktur | Wirknetz | Effect Net | | Summe der Gestaltfunktionselemente eines C&C²-Modells in **einem** Systemzustand. Jedes C&C²-Modell enthält genau ein Wirknetz | IPEK-Glossar 11664, `Matthiesen2018a` |
| Struktur | Wirkstruktur | Effect Structure | | Summe aller Wirknetze über alle betrachteten Zustände, typischerweise als C&C²-Sequenzmodell dargestellt | IPEK-Glossar 11665, `Matthiesen2018a` |

### Weitere Begriffe

| Begriff | Bedeutung | Quelle |
|---|---|---|
| Gestaltfunktionselemente (GFE) | WFP und LSS. Liegen im Gestaltungsraum und enthalten veränderbare Gestaltparameter. Connectoren gehören nicht dazu | IPEK-Glossar 11437 |
| Gestalt-Funktion-Zusammenhang (GFZ) / Embodiment Function Relation (EFR) | Zusammenhang einer Gestalt mit einer Funktion oder einem Systemverhalten | IPEK-Glossar |
| Zustand | Zeitraum, in dem das C&C²-Modell unverändert bleibt. Ein neuer Zustand beginnt, wenn sich Anzahl oder Eigenschaften der GFE ändern | IPEK-Glossar Zustand, ASE-Wiki |
| C&C²-Sequenzmodell | Mindestens zwei C&C²-Modelle zeitlich aufeinanderfolgender Zustände | IPEK-Glossar, `Matthiesen2019b` |
| Wirkprinzip | Physikalische Effekte, Relativbewegungen und Anordnung von WFP und LSS | IPEK-Glossar 11668 |
| Tribosystem | Alle an einer tribologischen Beanspruchung beteiligten WFP und LSS, ihre Eigenschaften, das Beanspruchungskollektiv und relevante Eigenschaften des Restsystems | IPEK-Glossar 11640 |
| Gestaltparameter | Einstellbare Merkmale der GFE (Geometrie, Werkstoff, Oberfläche usw.), die den GFZ bestimmen | `Matthiesen2018a` |
| Systemgrenze | Zeitlich (welche Zustände) und räumlich (welche Teilsysteme) | `Matthiesen2018a` |
| Modellzweck | Pflichtbestandteil jedes C&C²-Modells, wird dokumentiert | `Matthiesen2018a` |

## 2. Die drei Grundhypothesen

Die Grundhypothesen sind die **Anwendungsregeln** für die Modellelemente (IPEK-Glossar 11445, `Albers2014`).

| Nr. | Kurzform (nach `Grauberger2020b`) | Inhalt (DE) | Englisch (sinngemäß) |
|---|---|---|---|
| GH 1 | Function needs interrelation | Wechselwirkungen finden nur bei Kontakt von Wirkflächen statt, die gemeinsam Wirkflächenpaare bilden. Jedes Grundelement erfüllt seine Funktion durch Wechselwirkung mit mindestens einem anderen Grundelement (Ursprungsformulierung `Matthiesen2002`) | Interactions only take place where working surfaces are in contact and form working surface pairs |
| GH 2 | Function needs a minimum number of elements | Eine Funktion erfordert mindestens zwei WFP, die durch eine LSS verbunden sind und durch jeweils einen Connector in die Umgebung eingebunden sind | A function requires at least two WSP connected by a CSS, each embedded in the environment by a connector |
| GH 3 | Fractal modelling | Jedes Teilsystem kann mit WFP, LSS und C auf verschiedenen Abstraktions- und Detaillierungsstufen beschrieben werden. Dazu werden Anzahl, Anordnung und/oder Eigenschaften der Grundelemente variiert | Any subsystem can be described with WSP, CSS and C at different levels of abstraction and detail |

**Historischer Hinweis:** In der C&CM-Phase (2002 bis ca. 2009) waren die Hypothesen ohne Connector formuliert. Der Connector kam mit dem C&C²-Ansatz hinzu (genauer Zeitpunkt unbestätigt, prüfen in `Alink2010` und `Matthiesen2012`).

## 3. Minimales Funktionsmodell (GH 2 als Schema)

```
 Umgebung                  Gestaltungsraum                   Umgebung
 ┌──────┐   WFP 1   ┌──────────────────────────┐   WFP 2   ┌──────┐
 │  C1  │◄────────► │           LSS 1-2        │ ◄────────►│  C2  │
 └──────┘           └──────────────────────────┘           └──────┘
  Connector           Leitstützstruktur verbindet           Connector
  (Abstraktion der    WFP 1 und WFP 2 und leitet            (z. B. Antrieb,
  Umgebung, z. B.     Energie, Stoff, Information           Bedienerkraft)
  Einspannung)
```

Beispiel Schnellbauschraube (`Matthiesen2018a`, Abb. 19):
- WFP 1 = Werkstück / Schraube, WFP 2 = Schraube / Bit, LSS 1-2 = Schraubenkörper
- C1 = Einspannung (Wandsteifigkeit), C2 = Axialkraft des Benutzers und Drehmoment des Schraubers

## 4. Begriffsentwicklung

| Zeitraum | Bezeichnung | Kennzeichen | Quelle |
|---|---|---|---|
| ab 1999 | Elementmodell "Wirkflächenpaare & Leitstützstrukturen" | Entwicklung am IPEK, Universität Karlsruhe (TH) | `Albers2005a` |
| 2002 | Elementmodell WFP & LSS | Basisdefinition, Dissertation Matthiesen | `Matthiesen2002` |
| 2003 bis 2009 | Contact & Channel Model (C&CM) | Englische Begriffe WSP, CSS | `Albers2003a`, `Albers2005a` |
| 2010 | C&C-Ansatz | Überarbeiteter Funktionsbegriff | `Alink2010` |
| ab ca. 2011/2013 | C&C²-Ansatz (C&C²-A) | Connector, Zustände, Sequenzmodell | `Thau2013`, `Albers2014` |
| ab 2023 | Extended C&C²-Approach | Designation Guide, Functional Delimitation, Fünf-Schritte-Prozess | `Troester2023`, `Troester2025b` |

## 5. Begriffszuordnung DE / EN (für Tool und Recherche)

| DE | EN (aktuell) | EN (ältere Varianten) |
|---|---|---|
| Wirkfläche | Working Surface | Active Surface |
| Wirkflächenpaar | Working Surface Pair | |
| Leitstützstruktur | Channel and Support Structure | |
| Connector | Connector | |
| Reststruktur | Residual Structure | |
| Begrenzungsfläche | Boundary Surface | Limiting Surface |
| Tragstruktur | Carrier Structure | Support Structure |
| Gestaltfunktionselement | Embodiment Function Element | |
| Gestalt-Funktion-Zusammenhang | Embodiment Function Relation (EFR) | |
| Wirknetz / Wirkstruktur | Effect Net / Effect Structure | Wirk-Net / Wirk-Structure |

## 6. Offene Punkte zur Verifikation

- [ ] Exakte LSS-Definition im Wortlaut (`Albers2014`, `Matthiesen2021`, `Matthiesen2002`)
- [ ] Ob eine LSS **genau** zwei WFP verbindet oder **mindestens** zwei (Quellen formulieren unterschiedlich)
- [ ] Jahr der Einführung des Connectors und der Schreibweise "C&C²"
- [ ] Aktuelle Darstellungskonventionen (Farben, Symbole). Connector laut Glossar als Mehreck mit hervorgehobener Wirkfläche
