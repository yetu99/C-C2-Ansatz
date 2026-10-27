# Tröster et al. 2026: Technische Mechanik im C&C²-Ansatz für gezielte Gestaltsynthese

| Feld | Wert |
|---|---|
| Autoren | Peter M. Tröster, Benjamin Pfaff, Albert Albers (IPEK, KIT) |
| Titel | Integrating Engineering Mechanics into the Contact and Channel Approach for Targeted Embodiment Synthesis |
| Quelle/Reihe | KIT Scientific Working Papers, Band 272, Karlsruher Institut für Technologie (KIT), IPEK, Karlsruhe |
| Jahr | 2026 |
| ISSN | 2194-1629 |
| DOI | im PDF nicht angegeben |
| Lizenz | CC BY-SA 4.0 |
| Volltext | [`../volltexte/Troester2026.pdf`](../volltexte/Troester2026.pdf) (10 S.) |
| Status | gelesen, vollständig ausgewertet |

Seitenangaben unten sind Druckseiten 1 bis 8 (= PDF-S. 2 bis 9; PDF-S. 1 Deckblatt, PDF-S. 10 Impressum).

## Kernaussage

C&C²-Modelle unterstützen die Analyse und Kommunikation bestehender **Gestalt-Funktion-Zusammenhänge (Embodiment Function Relations, EFR)**, liefern aber zu wenig für konkrete Syntheseentscheidungen; diese Lücke heißt **Synthesis Gap**. Das Paper führt **Wirkflächenpaarorientierung (Working Surface Pair Orientation, WSPO)** und **Wirkflächenpaar-Flächeninhalt (Working Surface Pair Area, WSPA)** als explizite, quantifizierbare **Vektorattribute** des WFP ein, indem die Wirkfläche in projizierte Komponenten eines kartesischen Koordinatensystems zerlegt wird. Daraus werden zwei **erweiterte Syntheseprinzipien** und ein dreistufiges Vorgehen abgeleitet, illustriert an einer **Wippe** und einem **Fangsystem (safety catcher)** hydraulischer Hebebühnen; eine empirische Validierung steht aus.

## Inhalte nach Abschnitt

### 1. Introduction (S. 1 bis 2)
- C&C²-Ansatz modelliert EFR mit WSP, CSS und Connectoren; WSP als Grenzflächen für Austausch von Energie, Stoff oder Information, CSS verbinden diese und übertragen oder speichern Systemgrößen.
- Beobachtung aus Lehre und Industrie: Modellieren bestehender Lösungen gelingt, Ableiten konkreter Gestaltentscheidungen für neue Lösungen fällt schwer; der Ansatz zeigt **wo** Wechselwirkungen stattfinden müssen, wenig **wie** deren Geometrie gestaltet werden soll.
- **Synthesis Gap:** Lücke zwischen qualitativer EFR-Modellierung und direkter Nutzung mechanikbasierter quantitativer Argumentation; gestützt auf Nöller et al. 2023 (C&C²-Modelle enthalten zu wenig quantitative Daten, um Kräfte festzulegen).
- WSPO wird zunächst für **ebene oder lokal angenäherte Wirkflächen** betrachtet; gekrümmte oder räumlich verteilte Kontakte über lokale Flächennormalen oder diskretisierte Flächensegmente.
- Abgrenzung: kein Ersatz für Freikörperbild, Gleichgewichtsbedingungen oder Spannungsanalyse; Neuheit liegt im vorgelagerten Übersetzungsschritt vom C&C²-Modell zu mechanisch lesbaren Gestaltparametern.
- Drei Beiträge: (1) Synthesis Gap identifizieren, (2) WSPO und WSPA als Attribute, (3) erweiterte Syntheseprinzipien.

### 2. Related Work (S. 2 bis 3)
- **2.1 Grundlagen:** C&C²-A als besonders gestaltorientierte Sicht unter Produktmodellen (Funktionsstrukturen, Effektketten, Organstrukturen, Function-Means, SysML, Produktarchitektur). Kernelemente WSP, CSS, C (Albers & Matthiesen 2002, Matthiesen 2021).
  - WSP: Grenzflächen, an denen Bauteile, Fluide oder Felder sich berühren und Energie, Stoff und/oder Information übertragen.
  - CSS: Werkstoffvolumen, das die Wirkflächen innerhalb eines Bauteils verbindet, zuständig für interne Kraftübertragung, definiert elastische oder starre Struktureigenschaften.
- **Fig. 1:** angepasste Übersicht mit **Farbcode** WSP rot, CSS gelb, Connector grün, Functional Delimitation blau (aus Tröster, Schön & Albers 2025, basierend auf Matthiesen 2021).
- **Fig. 2:** Modellbildung mit dem C&C²-Ansatz in der Synthese (übersetzt aus Matthiesen 2021).
- **2.2 Stand der Synthese:** bestehende Heuristik mit **drei Syntheseprinzipien** (WSP/CSS hinzufügen, entfernen, Eigenschaften ändern) nach Matthiesen 2021; überwiegend qualitativ. Neuere Erweiterungen: Extended C&C² Approach mit **Designation Guideline** (Tröster, Schmidt & Albers 2023) und **Functional Delimitation** (Tröster, Prager, Schmid & Albers 2023).
- **2.3 Lücke zur Technischen Mechanik:** Orientierung und Flächeninhalt der WSP bleiben unter dem Prinzip "modifying properties" implizit; Mechanik braucht explizit Kontaktflächen, Normalenvektoren, Kraftpfade.

### 3. Research Methodology and Objectives (S. 3 bis 4)
- Problem aus Live-Lab-Studien zum Extended C&C²-Approach (Tröster et al. 2025, zwei Quellen) und Industriebeobachtungen; Zahlen werden hier nicht berichtet.
- RQ1: Grenzen der qualitativen Syntheseprinzipien bei mechanikbasierten Gestaltparametern; RQ2: Erweiterung durch WSPO und WSPA; RQ3: strukturiertes Vorgehen.
- Konzeptionell-methodischer Ansatz; Fälle zeigen logische Konsistenz und Anwendbarkeit, **keine empirische Validierung**.
- Deutsche Begriffe laut Paper: "Wirkflächenpaarorientierung" und "Wirkflächenpaar-Flächeninhalt"; als Attribute des **C&C²-Metamodells** eingeführt.

### 4.1 Anforderungen an die Erweiterung (S. 4)
1. Abstraktionslogik erhalten, kompatibel mit WSP, CSS, Connector
2. mechanisch relevante Gestaltattribute explizit ohne vollständiges CAD-Modell
3. Parameter direkt mechanisch interpretierbar (Flächennormalen, projizierte Flächen, Kraftrichtungen, Hebelarme, Flächenpressung)

### 4.2 Konzept WSPO und WSPA (S. 4)
- Zerlegung der aktiven Wirkfläche in projizierte Komponenten entlang eines kartesischen Koordinatensystems (x, y, z); Fläche als **Flächenvektor**.
- **Gleichung (1):** A⃗_WSP = (A_x, A_y, A_z)ᵀ
- A_x, A_y, A_z sind die Beträge der Projektionen auf die jeweiligen Koordinatenebenen, ihre Richtungen entsprechen den Flächennormalen.
- **Fig. 3:** Projektion von A_WSP auf die XY-Ebene ergibt die Komponente A_z.
- Verknüpfung zu Reibung, Flächenpressung und Strömungsmechanik (fluid mechanics) wird ausdrücklich genannt.

### 4.3 Erweiterte Syntheseprinzipien (S. 4)
- Ausgangspunkt: generalisiertes Prinzip "changing WSP/CSS properties".
- **Variation of WSP Orientation and Area:** in 3D Vektorkomponenten von A⃗_WSP anpassen, um Kraftübertragungswinkel zu ändern (z. B. Formschluss maximieren, Keilwinkel einstellen), oder Absolutfläche skalieren, um die Flächenpressung p = F/A zu beeinflussen; in 2D-Vereinfachung Änderung der Wirkflächenlänge.
- **Variation of CSS Volume, Area, or Length:** verändert interne Lastpfade und Hebelarme, wirkt auf Biegemomente und Steifigkeit.

### 4.4 Beispiel 1: Wippe (S. 5)
- Annahme starrer Körper, Masse vernachlässigbar gegenüber den Kräften; Benennung nach Designation Guideline.
- Analyseschritte: WSP, CSS, Connectoren identifizieren; **Functional Delimitation FD A1//A2** der Achse am mittleren Drehlager; CSS-Längen l₁ = l_x(A1~C1) und l₂ = l_x(A2~C2); Kräfte und WSP-Orientierungen; Funktionsbeschreibung in Tabelle.
- **Table 1** (Notation "//" für WSP bzw. FD, "~" für CSS; Zuordnung der Orientierungen zu den Zeilen aus der Textextraktion rekonstruiert, Spaltenreihenfolge im extrahierten Text vertauscht):
  - A1//C1, Orientierung y: Kraftübertragung von C1 zur Achse
  - A2//C2, Orientierung y: Kraftübertragung von C2 zur Achse
  - A1//A2 (FD), Orientierung x: Aufteilung der Achse in linken und rechten Lastpfad, Verzweigung vom Lager in beide Achsabschnitte
  - A//B, Orientierung x und y: Kraftübertragung in x und y von der Achse ins Lager
  - A1~C1, l₁ = l_x(A1~C1): interne Kraftübertragung, linker Hebelarm
  - A2~C2, l₂ = l_x(A2~C2): interne Kraftübertragung, rechter Hebelarm
- **Gleichung (2):** M_Center,z = F₁,y · l₁ − F₂,y · l₂ (Moment in Achsmitte, aus Freikörperbild)
- Synthesehypothesen (Fig. 5): l₂ verlängern → größerer Hebelarm, Wippe kippt bei gleichen Vertikalkräften rechts nach unten; WSP A1//C1 neigen, F₁ wirkt senkrecht zur WSP → F₁,y sinkt, wirksames Moment ändert sich, Achse geht rechts nach unten.

### 4.5 Beispiel 2: Fangvorrichtung (Safety Catchers) (S. 5 bis 7)
- Einsatz in **hydraulischen Hebebühnen** (hydraulic lifts), verhindert Absturz einer Stange bei **Druckausfall**; mehrere Reibkeile verzögern die Stange; Betrachtung eines Viertelschnitts (Fig. 6).
- **Vier Zustände** (Benennung S1 bis S4):
  - S1 Disconnected: Keile ohne Kontakt, Stange mit v_rod
  - S2 Active, Sliding: WSP R//SC1.1 aktiv mit Gleitreibung, Normalkraft durch Keilgeometrie verstärkt
  - S3 Active, Fixed: Haftreibung, Stange gesichert (v_rod = 0)
  - S4 Active, Overload: Haftreibung überschritten, Stange rutscht, wird aber verzögert
- Fig. 7 zeigt C&C²-Modelle der Zustände S1 bis S3.
- **Table 2** (WSP, Orientierung, Fläche, Funktionsbeitrag):
  - R//SC1.1: x; A_x,R//SC1.1; Reibung Keil-Stange, Verzögerung in y; aktiv in S2, S3, S4
  - SC2//SC1.1: x, y (Winkel φ); A_x und A_y; Lage der Keile zum Gehäuse, Keilwinkel wandelt Vertikalbewegung in Normalkraft in x; aktiv in allen Zuständen
  - SC3.1//SC1.1: y; A_y; Kraft in +y vom Kolben auf den Keil zum Lösen, Verschiebbarkeit in x gegen Verklemmen (Zustandsangabe fehlt)
  - SC4.1//SC1.1: y; A_y; Federschnittstelle, Vorspannkraft in y; aktiv in allen Zuständen
- Synthesehypothesen: Winkel φ an SC2//SC1.1 variieren → Verhältnis A_x zu A_y ändert sich, bestimmt kinematische Zwangsbedingung des Keils und die Normalkraft an R//SC1.1; Fläche A_x,R//SC1.1 skalieren → Flächenpressung steuern, Fließen des Werkstoffs in S3 oder S4 vermeiden.

### 4.6 Initiales methodisches Vorgehen (S. 6 bis 7)
1. **Extended System Analysis:** Koordinatensystem festlegen (2D oder 3D); WSPO (Vektorkomponenten) und Flächen bestimmen und quantifizieren; relevante CSS-Volumina, -Flächen oder -Längen bestimmen
2. **Mechanical Mapping:** Analogien zur Technischen Mechanik bilden (CSS-Längen als Hebelarme, WSP-Flächenkomponenten für Freikörperbilder)
3. **Hypothesis-driven Embodiment Synthesis:** erweiterte Syntheseprinzipien anwenden und Gestaltparameter systematisch variieren
- Ausdrücklich keine voll validierte Methode.

### 5. Discussion (S. 7)
- RQ1: bestehende Prinzipien sagen, dass eine Eigenschaft geändert werden soll, nicht welche und mit welcher mechanischen Folge.
- Präzise C&C²-Analyse bleibt Voraussetzung: erst aktive Flächen korrekt identifizieren, dann Vektorattribute zuweisen.
- Außerhalb des Umfangs: Rauheit, Werkstoffpaarung, Beschichtung, Schmierzustand, Härte, temperaturabhängiges Verhalten; attributbasierte Logik könne diese später aufnehmen.
- Auswirkung auf Entwurfsgeschwindigkeit, Qualität und physikalische Genauigkeit nicht gemessen; kontrolliertes Experiment ausstehend.

### 6. Conclusion and Outlook (S. 7 bis 8)
- Übertragung auf komplexe dynamische tribologische Systeme, Kandidat **Kupplungsrupfen (clutch judder)** als Wechselwirkung aus Grenzflächenadhäsion und Strukturmechanik des Reibbelags.
- Förderung: DFG, Projektnummer 520437230. Offenlegung der Nutzung von Gemini, ChatGPT, DeepL, Grammarly, LanguageTool für Sprache.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| A⃗_WSP = (A_x, A_y, A_z) | WFP-Attribute `flaeche_vektor` (3 Komponenten, m²) plus abgeleitete Gesamtfläche und Normale; Koordinatensystem je Modell als Pflichtangabe |
| WSPO für ebene oder lokal angenäherte Flächen | Attribut `geometrietyp` (eben, gekrümmt diskretisiert); bei gekrümmt Liste von Segmenten mit eigener Normale |
| CSS-Länge l = l_x(A~B) | LSS-Attribute Länge, Fläche, Volumen mit Achsbezug; Verwendung als Hebelarm |
| p = F/A, M = F·l | eingebaute Mechanik-Rechner, die WFP-Fläche und LSS-Länge direkt übernehmen |
| Zwei erweiterte Syntheseprinzipien | Syntheseassistent: je WFP "Orientierung/Fläche variieren", je LSS "Volumen/Fläche/Länge variieren", mit erwarteter mechanischer Folge als Hypothese |
| Drei Schritte Analyse, Mapping, Synthese | Workflow-Wizard mit Statusanzeige je Schritt |
| Zustände S1 bis S4 mit aktiven WSP | Zustandsmatrix WFP × Zustand (aktiv/inaktiv), Prüfregel auf fehlende Zustandsangaben |
| Benennung nach Designation Guideline ("//", "~", FD) | automatische Namensvergabe und Syntaxprüfung der Elementbezeichner |
| Farbcode rot/gelb/grün/blau | Standard-Farbschema für WFP, LSS, C, Functional Delimitation |
| Out-of-scope-Attribute (Rauheit, Werkstoffpaarung, Schmierung, Härte, Temperatur) | erweiterbare Attributliste je WFP für spätere Versionen |
| Fangvorrichtung in hydraulischer Hebebühne | Lernbeispiel mit Bezug Fluidtechnik/Druckausfall |

## Im Paper zitierte Schlüsselquellen
Albers & Matthiesen 2002 (Konstruktion 54, Elementmodell WFP und LSS), Matthiesen 2021 (Pahl/Beitz, Gestaltung, Quelle der drei Syntheseprinzipien), Matthiesen & Grauberger 2024 (Konstruktionswissen für Ingenieure), Grauberger et al. 2020 (JED, 20 Jahre), Albers & Zingel 2011 (ICED, SysML), Gladysz, Megner, Mayer & Albers 2018 (NordDesign, Fehleranalyse), Tröster, Schmidt & Albers 2023 (Procedia CIRP 119, Designation Guide), Tröster, Prager, Schmid & Albers 2023 (SSP 2023, abschnittsweise EFR, Functional Delimitation), Tröster, Schön & Albers 2025 (IEOM, Lehrkonzept), Tröster, Dieck & Albers 2025 (CIRP Design, Live Lab Extended C&C²), Nöller et al. 2023 (Multi-Domain TFM), Matthiesen et al. 2019 (SN Applied Sciences, Produktmodelle in der Gestaltung).
