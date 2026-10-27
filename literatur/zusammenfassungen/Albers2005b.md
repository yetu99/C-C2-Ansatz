# Albers et al. 2005: C&CM als konstruktionsmethodisches Denkmodell

| Feld | Wert |
|---|---|
| Autoren | A. Albers, N. Burkardt, S. Matthiesen, M. Ohmer (Ansprechpartner o. Prof. Dr.-Ing. Dr. h. c. A. Albers, IPEK, Universität Karlsruhe (TH)) |
| Titel | C&CM: ein konstruktionsmethodisches Denkmodell zum Zusammenhang von Gestalt und Funktion technischer Systeme |
| Quelle/Reihe | im PDF nicht angegeben (keine Veranstaltung, Festschrift, Reihe oder Seitenzahl genannt) |
| Jahr | im PDF nicht angegeben (2005 laut CSV; jüngste zitierte Quelle von 2004) |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Albers2005b), nicht im Repo (Lizenz) (3 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Kurzbeitrag (drei Seiten), der das **Elementmodell C&CM** als Denkansatz für **Analyse und Synthese** vorstellt. Grundelemente sind **Wirkflächenpaare (WFP)** und **Leitstützstrukturen (LSS)**, auch für Flüssigkeiten, Gase und Felder. Als Beispiel einer **Grundhypothese** wird die Mindestelement-Aussage (mindestens zwei WFP und eine verbindende LSS) zitiert. Alle Regeln beruhen auf **vier grundlegenden Anwendungsmustern** (WFP und LSS hinzufügen, entfernen, Eigenschaften von WFP ändern, Eigenschaften von LSS ändern).

## Inhalte nach Abschnitt

Seitenangaben als PDF-S. (keine Druckseitenzahlen im PDF).

### 1. Einführung (PDF-S. 1)
- Zusammenhang Gestalt und Funktion als Schlüssel zum Verständnis technischer Systeme. Methode soll Analyse- und Syntheseschritt unterstützen.
- Contact & Channel Model (C&CM) als Hauptforschungsfeld am IPEK, Universität Karlsruhe (TH). Stärke ist die Beschreibung beliebiger Systeme ohne unnötige Abstraktion, leichter Wechsel zwischen realer Gestalt und abstrakter Funktion.

### 2. Das Elementmodell C&CM (PDF-S. 1 bis 3)
- Grundelemente WFP und LSS. Jede technische Funktion als Wechselwirkung von WFP und den verbindenden LSS beschreibbar, einschließlich Wechselwirkungen mit der Umwelt.
- WFP sind generalisierte Flächen, die Funktion durch Wechselwirkung mit anderen Wirkflächen erfüllen (im Original mit der Abkürzung "WF" eingeleitet, S. 1). Definiert für Festkörper, Flüssigkeiten, Gase und Felder.
- Funktionserfüllung durch **Leitung oder Speicherung** der Systemgrößen Stoff, Energie, Information.
- Bild 1 Abstraktion eines realen Systems (Traverse und Stütze, Beschriftungen WF, WFP, LSS und einmal "WSP").
- Grundhypothese (Beispiel, PDF-S. 2): mindestens zwei WFP und eine verbindende LSS. Entfernt man ein WFP (Traverse-Stütze), entfällt die Funktion. Gilt für alle technischen Systeme.
- Regeln ermöglichen prinzipielle Problemlösung ohne Festlegung der konkreten Gestalt. Vier Anwendungsmuster (PDF-S. 3), daraus fallbezogene Handlungsanweisungen.

### 3. Ergebnisse (PDF-S. 3)
- In zahlreichen Industrieprojekten angewendet, zahlreiche Ideen und Patente (ohne Zahlen).
- Durchgängig über Abstraktionsebenen anwendbar, **fraktaler Charakter**.
- Grundlage des Karlsruher Lehrmodells für Produktentwicklung KaLeP.
- Weiterführende Literatur [1] bis [5], alle 2002 bis 2004.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Vier Anwendungsmuster (Hinzufügen, Entfernen, Eigenschaften WFP ändern, Eigenschaften LSS ändern) | Synthese-Aktionen im Modell-Editor, je Aktion Versionsschritt mit Begründung |
| Mindestelement-Hypothese mit Entfernungs-Gedankenexperiment | "Was-wäre-wenn"-Prüfung: WFP testweise entfernen und betroffene Funktionen anzeigen |
| Leitung oder Speicherung von Stoff, Energie, Information | Attribut je LSS "leitet / speichert" plus Systemgröße |
| WFP auch für Flüssigkeiten, Gase, Felder | Medienauswahl je Wirkfläche (relevant für Pumpen, Rohrleitungen, Wärmeübertrager) |
| Fraktaler Charakter | Verschachtelbare Modelle (Teilsystem als eigenes Modell) |
| Lösen ohne konkrete Gestalt | Abstrakte Modellierungsebene vor CAD, Elemente ohne Geometrie zulässig |

## Im Paper zitierte Schlüsselquellen
Albers und Matthiesen 2002 (Konstruktion 54, Grundmodell), Albers, Burkardt und Ohmer 2004 (TMCE, Principles for design on the abstract level), Albers, Burkardt und Ohmer 2004 (CIRP Design Seminar Kairo, Paarcharakter der Wirkflächen), Albers, Eckert und Ohmer 2004 (Visual and Spatial Reasoning in Design, MIT, kognitive Perspektive), Albers, Burkardt und Ohmer 2004 (KaLeP, TU Delft).
