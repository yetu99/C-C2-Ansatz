# Albers und Zingel 2013: SysML-Profil für den C&C²-A

| Feld | Wert |
|---|---|
| Autoren | Albert Albers, Christian Zingel (im PDF: "Albers, Albert; Zingel, Christian"; IPEK, KIT) |
| Titel | Extending SysML for Engineering Designers by Integration of the Contact & Channel - Approach (C&C²-A) for Function-Based Modeling of Technical Systems (im PDF steht zwischen "Channel" und "Approach" ein Halbgeviertstrich, hier als Bindestrich wiedergegeben) |
| Quelle/Reihe | Procedia Computer Science 16 (2013), S. 353 bis 362; Conference on Systems Engineering Research (CSER'13), Georgia Institute of Technology, Atlanta, GA, 19. bis 22. März 2013; Hrsg. C.J.J. Paredis, C. Bishop, D. Bodner |
| Jahr | 2013 |
| DOI | 10.1016/j.procs.2013.01.037 |
| Lizenz | Open access under CC BY-NC-ND license (Version im PDF nicht angegeben) |
| Volltext | [`../volltexte/Albers2013.pdf`](../volltexte/Albers2013.pdf) (10 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Das Paper stellt ein **SysML-Profil** vor, das den **Contact & Channel Approach (C&C²-A)** in die Systemmodellierung integriert. Funktionen werden über Aktivitäten und **Aktivitätspartitionen (Activity Partitions)** zerlegt, aus denen ein Plugin automatisch **Leitstützstrukturen (Channel and Support Structures, CSS)** und **Wirkflächen (Working Surfaces, WS)** als stereotypisierte Flow Ports erzeugt. **Wirkflächenpaare (Working Surface Pairs, WSP)** entstehen als stereotypisierte SysML-Connectoren mit einer Eigenschaft für **Systemzustände**, wodurch zustandsabhängige (dynamische) Strukturen modellierbar werden. Physische Komponenten **erben** über eine Mapping-Matrix die funktionsrelevanten Eigenschaften der CSS (Beispiel 2-Gang-Getriebe).

## Inhalte nach Abschnitt

### 1. Introduction (S. 353 bis 354)
- Motivation: MBSE in Software und Embedded Systems etabliert, Maschinenbauer haben Probleme bei der Anwendung; SysML seit September 2007 verfügbar.
- Eigene Umfrage unter deutschen Systems Engineers 2012 zu Begriffsverständnis und SysML-Nutzung (Albers & Zingel 2013, CIRP Design Conference); Zahlen werden hier nicht berichtet.
- Lücke: keine Modellierung funktionsrelevanter physikalischer Eigenschaften unter Erhalt eines maximalen Lösungsraums; zustandsabhängige Strukturänderungen werden nicht berücksichtigt.
- Baut auf eigenen Vorarbeiten zu C&C²-A in SysML auf (Albers & Zingel 2011 ICED; Zingel et al. 2012 IAENG). Neu: zustandsabhängige Strukturen, Funktionsstruktur mit CSS und WSP, Vererbung an physische Strukturen.
- Ziel: Übergang von komponentenbehaftetem zu funktionalem Denken (component-afflicted vs. functional thinking).

### 2. Related research work (S. 354 bis 355)
- Abgrenzung zu: Shah et al. (Multi-View-Modellierung), CONSENS (Gausemeier et al.; "active structure", Anwendungsszenarien), Wölkl & Shea (Use Cases, Activity Diagrams, NIST-Funktionsdatenbank nach Hirtz et al.), Kruse et al. (FBS-basiert, Allokationsmatrizen, Swimlanes), Eigner et al. (RFLP, Stereotyp "function", Allokation "realize"), Lamm & Weilkiens (FAS-Methode).
- Kritik an allen: direkte Zuordnung Funktion zu Komponente, kein expliziter Zwischenschritt über funktionsrelevante physikalische Eigenschaften, keine dynamischen Strukturen.
- Geplante Kombination mit der FAS-Methode im GfSE-Arbeitskreis FAS (GfSE = deutsches INCOSE-Chapter, Fußnote b).

### 3. The Contact & Channel Approach (C&C²-A) (S. 356)
- Motivationsbeispiel **Kupplung**: Kontakt der Kupplungsscheiben existiert nur im Zustand "geschlossen"; diese zustandsabhängige Struktur sei mit bestehenden Sprachen nicht modellierbar.
- Grundelemente: **Wirkfläche (Working Surface, WS)**; zwei WS bilden in Kontakt ein **WSP**; **CSS**; zusätzlich **Connector (C)**, der Eigenschaften angrenzender Systeme trägt.
- Grundelemente beschreiben funktionsrelevante Information, nämlich physikalische oder chemische Effekte (z. B. Reibung, Wärmeabgabe) und Eigenschaften (z. B. Werkstoff, Länge).
- **Drei Grundhypothesen** nach Matthiesen und Ruckpaul (DESIGN 2012), wörtlich im Befund dokumentiert; Hypothese 2 enthält explizit "at least two Connectors".
- **Fußnote c:** Das hochgestellte Quadrat an "C²" steht für das Element "Connector", das im vollen Namen üblicherweise nicht genannt wird.
- Elemente lassen sich auch abstrahiert zur gestaltneutralen Spezifikation über Eigenschaftsparameter nutzen.

### 4. Function-Based Modeling Approach using C&C²-A@SysML (S. 356 bis 359)
- Profil soll bestehende MBSE-Methoden ergänzen (z. B. SYSMOD nach Weilkiens, Methode in Zingel et al. 2012).
- Bisher: Allokation Funktion zu Physik ohne Übertragung von Values und Flow Ports. Neu: **Spezialisierung (Vererbung)** über eine Mapping-Matrix.
- **Vorgehen (Fig. 1, Schema):**
  1. Stakeholder-Ziele und Randbedingungen erfassen
  2. Use Cases als Top-Level-Funktionen definieren und Akteuren zuordnen
  3. Use Cases in logische Aktivitätsfolgen (Teilfunktionen) zerlegen; parallel Systemzustände definieren
  4. Objektflüsse (Stoff, Energie, Information) in Aktivitätsdiagramme einfügen
  5. Aktivitäten in Aktivitätspartitionen (Swimlanes) gruppieren, z. B. mit FAS-Heuristiken
  6. Plugin erzeugt per Menübefehl aus Partitionen automatisch CSS und aus partitionsgrenzen-überschreitenden Objektflüssen automatisch WS (Fig. 2)
  7. Funktionsstruktur in spezialisiertem Internal Block Diagram (IBD) modellieren: WS über stereotypisierte Connectoren zu WSP vernetzen
  8. Komponenten anlegen und CSS per Matrix zuordnen (Fig. 3); Komponenten erben alle Eigenschaften inkl. WS
  9. Physische Struktur in zweitem spezialisiertem IBD modellieren
  10. parallel technische Anforderungen iterativ ableiten
- **Kontinuierliche Funktionen** laufen innerhalb eines Zustands (Drehmoment nur bei eingelegtem Gang), **diskrete Funktionen** innerhalb von Zustandsübergängen (Gangwechsel).
- WS = stereotypisierte **Flow Ports** als Stoff-, Energie- und Informationsschnittstellen.
- WSP-Connector hat **Zusatzeigenschaft "Systemzustände"**; Prüfung gegen Zustandsdiagramme über Konsistenzregeln.
- In Fig. 3 (BDD) sind CSS grün, physische Komponenten grau dargestellt.
- **Constraints** für parametrische Beziehungen funktionsrelevanter Eigenschaften.
- Umsetzung über den UML/SysML-Profilmechanismus; Automatismen in Java über die API des Modellierungswerkzeugs (Werkzeugname im PDF nicht angegeben). Spezialisierte IBDs unterscheiden sich nur durch reduzierte Werkzeugleisten.

### 4.1 Modeling rules (S. 358 bis 359)
- Objektflusstypen (Stoff, Energie, Information) erlauben nur passende Datentypen.
- Beziehungen Partition zu CSS und CSS zu Komponente werden automatisch angelegt; WS erhalten automatisch den Datentyp des kreuzenden Objektflusses.
- Zusatzregeln nach **Bertsche** (5-Schichten-Modell, abgeleitet vom OSI-7-Schichten-Modell: mechanisch, elektromechanisch, elektronisch, Treiber, Software). Beispiel: Sensoren und Aktoren (elektromechanisch) interagieren nie direkt, nur über mechanische oder elektronische Systeme.

### 4.2 Tool interoperability options (S. 359)
- Fig. 4: drei Hauptmodellierungsschritte im erweiterten SysML (grün) und verknüpfbare Werkzeuge (blau).
- Aktivitäten, Objektflüsse und Partitionen speisen Multi-Domain-Simulationen (Modellrahmen mit Schnittstellen, Black Boxes); Simulationsergebnisse (z. B. Kräfte) zurück als Parameter in die Funktionsstruktur.
- Beispiel Zahnrad: CSS überträgt Kraft vom Zahn zur Welle; aus FEM mit vordefinierter Geometrie folgt der benötigte Zugmodul, zurück nach SysML, daraus Komponentenauswahl.

### 5. Application Example "Gearbox" (S. 359 bis 361)
- Kleines Getriebe mit 2 Gängen, rein mechanisch, retrospektive Analyse eines existierenden Getriebes.
- Hauptfunktion "Transmit and convert torque" mit **fünf Teilaktivitäten**, daraus **fünf CSS** mit je **drei Value Properties** (Eingangs- und Ausgangsdurchmesser, E-Modul) (Fig. 5).
- Beteiligte Komponenten: Eingangswelle, Schaltmuffe, zwei Zahnräder, Ausgangswelle.
- Constraint: Quotient der Durchmesser ergibt Übersetzung bzw. Wandlungsfaktor; die Übersetzung ist ein Value der Hauptfunktion (Fig. 6 links).
- Vererbung an Komponenten plus abstrakte Klasse "Gearwheel" mit Parameter Modul (Fig. 6 rechts).
- Dynamische physische Struktur (Fig. 7): Zustände an den Connectoren zwischen Schaltmuffe und den beiden Zahnrädern; Plugin blendet Connectoren abhängig vom Zustand ein oder aus.
- Hinweis der Autoren: reale Modellierung ist iterativer; CSS können auch zuerst manuell angelegt und dann Partitionen zugeordnet werden.

### 6. Discussion and Outlook (S. 361 bis 362)
- Anwendung im Forschungsprojekt "Function-based controlling of mechatronic products" mit Virtual Vehicle (Graz), AVL List, BMW, TU München (Lehrstuhl Produktentwicklung): funktionsbasiertes Produktportfoliomanagement auf semantischer Wissensbasis.
- Geplant: Artefakte für physikalische Eigenschaften von WSP (Fügeverfahren, Relativbewegung) und Effekte (Reibung, Korrosion, Wärmeabgabe).
- Offene Frage: Detaillierungsgrad und Auswahl relevanter Eigenschaften für multidisziplinäre Modelle.
- Keine empirische Evaluation; das Beispiel dient der Illustration.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| WSP-Connector mit Eigenschaft "Systemzustände" | Datenmodell: WSP hat Liste `aktiv_in_zustaenden`; Ansicht filtert WSP je gewähltem Zustand |
| Kontinuierliche Funktion im Zustand, diskrete Funktion im Zustandsübergang | Funktionsobjekt mit Typ `kontinuierlich` (Zustand) oder `diskret` (Übergang) |
| WS als Flow Port mit Typ Stoff/Energie/Information | WF-Attribut `flusstyp` mit erlaubten Datentypen; Prüfregel auf Typverträglichkeit beider WF eines WSP |
| Automatische Erzeugung von CSS aus Funktionsgruppen und WS aus grenzüberschreitenden Flüssen | Assistent: aus Funktionsstruktur mit Gruppen einen C&C²-Rohentwurf generieren |
| Mapping-Matrix CSS zu Komponente mit Vererbung | Zuordnungsmatrix LSS ↔ Bauteil; Bauteil übernimmt Parameter und Schnittstellen der LSS |
| Constraints (Übersetzung = Durchmesserverhältnis) | Parameter-Constraints je Funktion, einfache Formel-Engine |
| Konsistenzregeln Zustand vs. Aktivität | Prüfregel: Funktion in Zustand Z braucht alle beteiligten WSP aktiv in Z |
| Bertsche-Schichtenregel | optionale Prüfregel für mechatronische Modelle (keine direkte Kopplung Sensor zu Aktor) |
| Rückfluss von Simulationsergebnissen in die Funktionsstruktur | Import von Kennwerten (z. B. Kraft, benötigter Modul) als LSS-Parameter |
| Kupplung und 2-Gang-Getriebe | Lernbeispiele für zustandsabhängige WSP |

## Im Paper zitierte Schlüsselquellen
Albers & Braun 2009 (ICED, Contact and Channel Modelling im frühen Entwurf), Matthiesen 2011 (ICED, thinking tools), Albers & Zingel 2011 (ICED, C&C-Modell für SysML), Zingel, Albers, Matthiesen & Maletz 2012 (IAENG IJCS 39(2), ein Jahr explorative Anwendung C&C²-A in SysML), Matthiesen & Ruckpaul 2012 (DESIGN, Systeme mit mehreren logischen Zuständen, Quelle der Grundhypothesen), Albers & Zingel 2013 (CIRP Design, MBSE-Umfrage).
