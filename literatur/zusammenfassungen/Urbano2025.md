# Urbano et al. 2025: Domänenübergreifende Rückverfolgbarkeit in Cyber-Physischen Systemen

| Feld | Wert |
|---|---|
| Autoren | Francesco Pio Urbano, Maximilian Beck, Katharina Bause, Arne Bischofberger, Eric Sax, Albert Albers (KIT, Institut für Produktentwicklung IPEK und Institut für Technik der Informationsverarbeitung ITIV) |
| Titel | Ansatz zur domänenübergreifenden Rückverfolgbarkeit in Cyber-Physischen Systemen (englischer Paralleltitel: Approach to cross-domain traceability in Cyber-Physical-Systems) |
| Quelle/Reihe | Stuttgarter Symposium für Produktentwicklung 2025 (Kopfzeile); Band, Herausgeber und Seitenzahlen des Tagungsbands im PDF nicht angegeben (PDF-Paginierung 1 bis 12) |
| Jahr | 2025 |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Urbano2025), nicht im Repo (Lizenz) (12 S.) |
| Status | gelesen, vollständig ausgewertet |

Sprache: Titel, Abstract und Keywords deutsch und englisch, Haupttext englisch. Seitenangaben = Seitenzahlen des PDF (identisch mit PDF-S.).

## Kernaussage

Das Paper nutzt den **C&C²-Ansatz als semantische Zwischenschicht** zwischen CAD-Modellen (ohne Semantik) und Modellen anderer Domänen (E/E-Architektur, Software, Anforderungen), um **domänenübergreifende Rückverfolgbarkeit (cross-domain traceability)** herzustellen. Kernbausteine sind ein **UML-Profil** für C&C² (CSS und Connector als Stereotypen von Class, WSP als Erweiterung von Association), eine vereinfachte **Mapping-Sprache** auf Basis von Vitruvius (Klare et al. 2021), ein **Editor** und **Rückverfolgbarkeitsberichte** mit Filtern über einen Abhängigkeitsbaum. Die Fallstudie (elektromechanische Bremse, ein Hinterrad) zeigt Machbarkeit, aber hohen manuellen Aufwand (ca. zehn Stunden, über 70 % für manuelle Schritte); als Ausblick wird **KI zur Erkennung semantischer Überlappungen** genannt.

## Inhalte nach Abschnitt

### 1. Introduction (S. 2)
- Moderne CPS (Fahrzeuge) mit bis zu 150 vernetzten Steuergeräten (ECUs) und geschätzt 10.000 Einzelteilen (zitiert: Vetter & Sax 2021, Friedrich & Müller 2024).
- Beispiel Bremssystem: hybride Bremsen kombinieren klassische Bremshydraulik mit Antriebsstrangteilen (Motoren, Getriebe) und mehreren ECUs; Rekuperation als neue Anforderung.
- MBSE strebt integrierte Systemdarstellung an, Werkzeuge bleiben domänenspezifisch und isoliert.
- These: Methoden werden in der Praxis nur nachhaltig genutzt, wenn sie direkt zum Produkt beitragen oder gesetzlich gefordert sind; Automatisierung ist entscheidend.
- Beitrag: Methoden zur Verknüpfung mechanischer und elektrischer Modelle, ein konkretes Domänenmodell, ein Werkzeug zur Analyse und Bearbeitung, eine einfache Fallstudie.

### 2. State of the Art (S. 2 bis 4)
- CAD-Modelle enthalten keine semantische Information über physikalische Zusammenhänge; E/E-Modelle (z. B. PREEvision) bilden funktionale und logische Ebenen ab.
- Standards: SSP (System Structure and Parameterization), FMI (Co-Simulation, Fokus Verhalten), UAF (Unified Architecture Framework).
- Semantische Modellverknüpfung über Ontologien (Beispielbegriffe "torque", "force"); Vitruvius-Ansatz von Klare et al. 2021 koppelt Modelle über eine Sprache für semantische Abhängigkeiten, liefert aber keine domänenspezifischen Modelle.
- DSLs und Abfragesprachen, Werkzeuge wie Smartfacts (meist closed source), Digital Twins, KI zur Erkennung semantischer Überlappungen (Wu et al. 2024).
- C&C² nach Albers & Wintergerst 2014 als zusätzliche Architekturmethode; Erweiterungen zu SysML und Simulink (Zingel et al. 2012).
- Forschungslücken: manuelle Link-Erstellung, Werkzeuggebundenheit, selten alle drei Domänen (Mechanik, Elektrik, Software) gleich tief, unzureichende Visualisierung; Skalierung bis 80 Mio. Modellartefakte (Eigner et al. 2014).
- Forschungsfrage: Wie lässt sich domänenübergreifende Rückverfolgbarkeit in CPS über Mechanik, Elektrik und Software automatisieren und semantisch anreichern?

### 3.1 Describing Inter-Domain Connections (S. 4 bis 5)
- **Semantische Überlappung (semantic overlap):** Information, die in mehreren Modellen vorhanden ist (Beispiel: maximale Kraft bzw. Moment eines E-Motors auf eine Achse im elektrischen und im mechanischen Modell).
- Überlappungen sind oft indirekt; nötig sind physikalische Gesetze oder Expertenwissen (Beispiel: Signal des Bremsreglers über eine Lookup-Tabelle auf den Bremsdruck im Bremszylinder abbilden, solange kein Hydraulikmodell existiert).
- Idealbild: Architekten erstellen früh ein abstraktes Systemmodell, Fachabteilungen verfeinern; Mappings werden parallel konkretisiert.
- **Mapping-Sprache, Gleichung (1):** `{ID_Element_1} <-> {ID_Element_2}: Optional [{Instructions}]`
  - Instruktionen optional, damit auch nicht quantifizierbare Beziehungen im Bericht erscheinen
  - Zugriff auf alle Parameter der Elemente und grundlegende mathematische Funktionen
  - wird vor Ausführung in die Vitruvius-Sprache von Klare et al. kompiliert (dadurch auch Bedingungen möglich)
- **Beispiel, Gleichung (2):** `motor1 <-> cad_axis_1: motor1.max_torque = cad_axis_1.max_torque`
- CAD-Modelle bestehen aus Dreiecken ohne Semantik, daher Zwischenschicht nötig.

### 3.2 Modeling CAD Semantics using the C&C²-Approach (S. 5 bis 7)
- Elementdefinitionen (nach Albers & Wintergerst 2014):
  - WSP: Wechselwirkung zweier Flächen (Festkörper oder verallgemeinerte Grenzflächen von Flüssigkeiten, Gasen, Feldern) im Kontakt; Austausch von Energie, Stoff oder Information; ein WSP besteht aus zwei CSS oder aus einer CSS und einem Connector, wenn die CSS die Systemgrenze erreicht
  - CSS: Volumenelemente, die zwei WSP verbinden; entsprechen den Teilen und Geometrien im CAD-Modell
  - Connector: externe Einflüsse, außerhalb des Gestaltungsbereichs, mit repräsentativer Wirkfläche, parametrisiertes Umgebungsmodell, innerhalb der Beobachtungsgrenze
- **UML-Profil (Fig. 1):** CSS und Connector als Stereotypen, die die Metaklasse **Class** erweitern (instanziierbar); WSP als Erweiterung von **Association** (verbindet zwei CSS oder eine CSS und einen Connector).
- CSS-Eigenschaften: **CAD Part-Reference** (direkte Zuordnung zum CAD-Teil) plus Mapping-Speicher für zusätzliche Eigenschaften (Werkstoff, mechanische Randbedingungen, weitere Konstruktionsdaten).
- **Connector-Typen:** interne Connectoren (Grenzen innerhalb des Gestaltungsraums, Verbindung zwischen Teilsystemen) und externe Connectoren (Verknüpfung zu Modellen anderer Domänen, z. B. elektrisch oder thermisch) mit **External Connection ID**, die auf Mappings der Mapping-Sprache verweist.
- **Editor (Fig. 2):** CAD-Ansicht (Beispiel Bremsscheibe an Achse), Baumansicht der Elemente, C&C²-Ansicht. Darstellung im Viewer: CSS als graue Kästen, Connectoren als oranges Quadrat, WSP als gestrichelte Linien. Hierarchische Darstellung, Teilsystem erscheint auf oberer Ebene als CSS; interne Connectoren koppeln Teilsysteme.
- Beispiel: externer Connector an der Achse verknüpft mit dem Drehzahlsignal des Electronic Speed Controller (ESC) des Motors; Abhängigkeitsbaum (Fig. 3) verbindet Mechanik-, Kommunikations-, E/E-, Software- und Anforderungsmodelle.
- Große Abhängigkeitsbäume erfordern Filter.

### 3.3 Generation of Traceability Reports (S. 7 bis 8)
- Berichte als Tabellen mit allen beteiligten Objekt-IDs und Namen; zwei Auslöser: Auswahl eines Elements (Element als Quelle) oder Änderung (alle betroffenen Elemente als Quellen).
- **Filter:**
  - **Distance:** maximale Anzahl Sprünge (hops) ab Quelle; Annahme abnehmender Wirkung mit Entfernung; Beispiel drei Schritte ab Bremsscheibe: Achse, Schrauben, ESC-Drehzahlsignal, ohne Softwaremodule
  - **Deviation:** propagiert eine Änderung über die Mapping-Instruktionen und zeigt Elemente mit Abweichung über Schwelle (z. B. 10 %); nur bei formal quantifizierten Mappings und nur in änderungsbasierten Berichten
  - **Combined:** Deviation wo Formeln vorhanden, sonst Distance ab dem letzten per Deviation gefundenen Element
  - **Type:** Pfad zu den nächsten n Elementen eines Typs (z. B. Requirements), kombinierbar mit anderen Filtern

### 4. Discussion (S. 8 bis 9)
- Fallstudie elektromechanisches Bremssystem eines E-Fahrzeugs, beschränkt auf **ein Hinterrad**; CAD in **PTC Creo**, E/E- und Softwarearchitektur in **PREEvision** (funktionale, logische, Hardware-, Kommunikationsebene).
- Ablauf (laut Paper "five-step workflow outlined in Section 3.2", dort jedoch nicht als Liste enthalten):
  1. CAD importieren, CSS automatisch extrahieren, Baugruppen hierarchisch als Teilsysteme
  2. interne Connectoren und WSP manuell definieren (z. B. Kontakt Bremsbelag/Scheibe)
  3. externe Connectoren zu E/E-Elementen (Motordrehzahlsignale, Sensorpositionen, Bremssteuerventile)
  4. semantische Mappings je externem Connector in der Mapping-Syntax
  5. Berichte erzeugen und filtern
- **Aufwand:** ca. zehn Stunden für C&C²-Struktur und Mappings; manuelle Schritte über 70 % des Gesamtaufwands.
- Wirksamste Filterkombination: Type plus Deviation.
- Schwächen: manueller Aufwand, Usability, statische Excel-Ausgabe, Skalierbarkeit nicht evaluiert, Mapping-Sprache für bedingte und nichtlineare Zusammenhänge zu schwach.

### 5. Future Work and Conclusion (S. 10)
- **KI** zur Identifikation semantischer Überlappungen und Automatisierung der Mappings.
- Interaktive, integrierte Visualisierung mit dynamischer Filterung statt Excel.
- Datensicherheit und Datenaustausch zwischen Zulieferern und Herstellern.
- Bisher nur Brems-HiL-Fallstudie, keine empirischen Daten zu Leistung und Skalierbarkeit; Prüfung der Integration in CI/CD-Pipelines.
- Förderung: DFG, SFB 1608, Projektnummer 501798263.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| UML-Profil: CSS und C als Klassen, WSP als Assoziation | Datenmodell: Tabellen `lss`, `connector`, `wfp` mit genau zwei Endpunkten (LSS-LSS oder LSS-Connector) |
| WSP als Paar aus zwei CSS oder CSS plus Connector | Prüfregel: jedes WFP hat genau zwei Enden, mindestens eines ist eine LSS |
| CAD Part-Reference an der CSS | Attribut `cad_referenz` (Datei, Teil-ID) je LSS; Import von Baugruppenstruktur als Teilsysteme |
| Interne und externe Connectoren, External Connection ID | Connector-Attribut `art` (intern/extern) und Fremdschlüssel auf Mapping-Einträge |
| Mapping-Syntax `A <-> B: Instruktion` | Beziehungsobjekt mit optionaler Formel; erlaubt Kopplung an Pumpenkennlinie, Regler oder Messdaten (Einschätzung) |
| Hierarchie, Teilsystem als CSS auf oberer Ebene | Zoom-Navigation zwischen Systemebenen |
| Filter Distance, Deviation, Combined, Type | Impact-Analyse bei Parameteränderung mit einstellbarer Tiefe und Schwellwert |
| Hoher manueller Aufwand (über 70 %) | Vorschlagsfunktion für WFP-Kandidaten aus Kontaktflächen und KI-gestützte Mapping-Vorschläge |
| Kritik an Excel-Berichten | interaktiver Abhängigkeitsgraph mit Filterleiste |
| Darstellung: CSS grau, Connector orange, WSP gestrichelt | alternative Darstellungsvariante im Graphmodus |

## Im Paper zitierte Schlüsselquellen
Albers & Wintergerst 2014 (Anthology, Quelle der Elementdefinitionen), Zingel, Albers, Matthiesen & Maletz 2012 (C&C²-A in SysML; im Literaturverzeichnis als "Zingel et al. 2021" geführt), Klare et al. 2021 (Vitruvius, Basis der Mapping-Sprache).
