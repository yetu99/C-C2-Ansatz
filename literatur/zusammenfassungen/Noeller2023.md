# Nöller et al. 2023: C&C²-Ansatz im mechanisch-elektromagnetischen Multi-Domain-Setup (Transversalflussmaschine)

| Feld | Wert |
|---|---|
| Autoren | Marcel Nöller, Joshua Huss, Sivasubramanian Chandramouli, Katharina Bause, Albert Albers (KIT IPEK; Chandramouli: National Institute of Technology Tiruchirappalli, Indien) |
| Titel | The C&C²-Approach in a Mechanical and Electromagnetic Multi Domain Setup - Identifying Possibilities and Challenges Throughout Product Engineering of an Additively Manufactured Transverse Flux Machine Stator (im PDF Halbgeviertstrich vor "Identifying", hier als Bindestrich wiedergegeben) |
| Quelle/Reihe | im PDF nicht angegeben (Manuskript mit Abschnitten "Declarations", "Article Highlights", ORCID; Einschätzung: für eine Zeitschrifteneinreichung formatiert); laut CSV KIT-Bericht |
| Jahr | im PDF nicht angegeben (CSV: 2023; Tröster et al. 2026 zitiert die Arbeit ebenfalls als 2023, KIT, 32 S.) |
| DOI | im PDF nicht angegeben |
| Lizenz | im PDF nicht angegeben |
| Volltext | lokal in Wissen/C&C2-Ansatz (Datei beginnt mit Noeller2023), nicht im Repo (Lizenz) (32 S.) |
| Status | gelesen, vollständig ausgewertet |

Seitenangaben = Seitenzahlen des Manuskripts (identisch mit PDF-S.).

## Kernaussage

Erstmals wird der **C&C²-Ansatz (C&C²-A)** gleichzeitig für die **mechanische und die elektromagnetische Domäne** angewendet, am Beispiel des Stators einer **Transversalflussmaschine (Transverse Flux Machine, TFM)** beim Übergang von geblechter zu **additiv gefertigter** Bauweise. Im Modell werden **Kraftfluss (mechanischer Leistungsfluss)** und **magnetischer Fluss** parallel in unterschiedlichen Farben dargestellt; Leitstützstrukturen schließen feldbeflutete Volumina (Luftspalt, Vakuum) ein, Materialübergänge gelten als Wirkflächenpaare, Luftvolumina werden in **Kontrollvolumina** unterteilt. Der Vergleich zweier Entwicklungsgenerationen zeigt Zielkonflikte (elektrischer Widerstand vs. Steifigkeit) und führt zu drei Syntheseideen; offene Punkte sind die Darstellung der **Energiewandlung zwischen Domänen** und der Kraftentstehung im Volumen.

## Inhalte nach Abschnitt

### Vorspann (S. 1 bis 2)
- Förderung: Ministerium für Wissenschaft, Forschung und Kunst Baden-Württemberg, Projekt "AM0 / EA0" im InnovationCampus Future Mobility.
- Verbund aus vier Instituten: IEW (Uni Stuttgart, elektromagnetischer Entwurf der TFM), IFSW (Uni Stuttgart, additive Fertigung und Werkstoffe), FAST (KIT, Sensor- und Aktorintegration für NVH-Kompensation), IPEK (KIT, Konstruktionsmethodik, hier berichtet).
- Article Highlights: erste Nutzung des C&C²-A für mechanische und elektromagnetische Domäne gleichzeitig; Modelle verschiedener Entwicklungsgenerationen; exemplarische methodische Synthese.

### 1. Introduction (S. 3 bis 4)
- Methoden sollen Zusammenhänge zwischen Funktion und Gestalt beschreiben; Produktprofile spezifizieren den Lösungsraum einer Produktgeneration (Albers et al. 2018).
- TFM mit dreidimensionalem Magnetfluss im Stator als ideales Beispiel für additive Fertigung (AM); erfordert enge Zusammenarbeit von Elektro-, Maschinenbau-, Produktions- und Werkstoffingenieuren.
- C&C²-A als gemeinsames Metamodell zwischen Disziplinen.

### 2.1 Transverse Flux Machine (S. 4 bis 9)
- TFM nach Herbert Weh (Patente späte 1980er); hohe Drehmomentdichte durch Entkopplung von elektrischer Ebene (senkrecht zur Drehachse) und magnetischer Ebene (parallel), daher viele Polpaare; drei Phasen axial hintereinander, um 120° elektrisch versetzt.
- Hemmnisse: nichtlineares Verhalten, Fertigung, Rastmoment; Anwendung z. B. radnah oder im Rad bei E-Fahrzeugen.
- Fertigungsverfahren: Blechpaket (ungeeignet für 3D-Flussgeometrie, Wirbelströme am Umfang nicht unterdrückt) und SMC (Soft Magnetic Composites; 3D-Formen möglich, feine Details schwierig, höhere Hystereseverluste, geringere Wirbelstromverluste).
- Topologien (Fig. 1 bis 4): U-Eisen, I-Rückschluss, einseitig/doppelseitig, Oberflächenmagnete vs. Sammleranordnung (flux concentrating, im Deutschen "Sammleranordnung").
- Untersucht: einseitige permanenterregte Außenläufer-TFM, anfangs U-Stator mit Sammler-Rotor, zuletzt Klauenpol-Stator mit Oberflächenmagneten.
- Multidisziplinarität (elektromagnetisch, thermisch, mechanisch, NVH, EMV, CFD für Kühlung); Disziplinen konkurrieren um dasselbe Bauvolumen, z. B. innere Kühlkanäle im Statorkern verändern Flusspfade und nehmen weichmagnetisches Material weg; Bedarf an gemeinsamem Referenzmodell vor fachspezifischen Modellen.

### 2.2 Additive Manufacturing of Electric Machines (S. 9 bis 10)
- Nachfrage nach Hochleistungs-Magnetwerkstoffen durch Elektrifizierung, u. a. **Windkraft** und elektrische Antriebsstränge.
- AM: komplexe Geometrien, weniger Teile, Funktionsintegration, gezielter Einsatz kritischer Werkstoffe; Laser-Pulverbettschmelzen (laser powder bed fusion) dominierend.
- Bisherige Forschung zu Spulen, Wickelkopf-Wärmetauschern, Multimaterialdruck; nicht zum Gesamtentwurf.

### 2.3 Contact and Channel Approach (S. 10 bis 12)
- C&C²-A "created by Matthiesen and Albers"; Metamodell aus Elementen und Regeln, vergleichbar einer Sprache mit Wörtern und Grammatik (nach Matthiesen et al. 2018, Procedia CIRP 70).
- Drei Kernelemente (WSP, CSS, C) und drei Grundhypothesen (paraphrasiert, wörtlich im Befund).
- WSP: Schnittstelle, an der Systemteile dauerhaft oder zeitweise in Verbindung stehen, während das System seine Funktion erfüllt. CSS: verläuft durch Systemteile und verbindet WSP; kann Bauteilteile, ganze Teilsysteme oder das **von einem Feld durchsetzte Volumen** umfassen. C: Modell der Umgebung, setzt die Grenze, überträgt Wirkungen.
- Parameterbeispiele: Reibwert als WSP-Parameter, Steifigkeit als CSS-Parameter; diese Parameter sind relevant für Simulationsmodelle.
- Fig. 5: Beispielmodell Zahnradstufe (Modellzweck "Explain torque transmission in a gear stage"; C1 Antriebsmoment, C2 Lastmoment).
- Änderungsregel: "The only way to change the system is to add, remove, or alter a CSS or WSP" (nach Matthiesen et al. 2018).
- Nach Grauberger et al. 2020 ist C&C²-A theoretisch auf Flüssigkeiten, Gase sowie magnetische und elektrische Felder anwendbar, eine direkte Umsetzung war den Autoren nicht bekannt.

### 3.1 Model Visualization (S. 12 bis 13)
- Fraktaler Charakter erlaubt beliebige Vereinfachungen; voll detailliert könnten WSP- und CSS-Anzahl **über tausend** liegen (Blech-Lack-Wechsel im Stator).
- **Vereinfachung 1, Wiederholungen:** sich wiederholende WSP und CSS werden einmal dargestellt und teilen Nummer, Eigenschaften und Bezeichnung; Synthese-Änderungen gelten für die ganze Wiederholungskette, auch die Anzahl ist änderbar.
- **Vereinfachung 2, zusammengefasste CSS:** mehrere CSS in einem Volumen werden als eine CSS dargestellt (Fig. 6); "CSS 1.2.3" steht für CSS 1.2, CSS 1.3 und CSS 2.3. Begründung: eine CSS verbindet immer zwei WSP, was die Darstellung im Stator unhandlich machen würde.

### 3.2 Multi Domain C&C²-A, elektromagnetische Domäne (S. 13 bis 16)
- Hauptfunktion des Motors: Wandlung elektrischer in mechanische Rotationsleistung und umgekehrt über wechselwirkende Magnetfelder zwischen Stator und Rotor.
- Zwei Flüsse gleichzeitig: **mechanischer Leistungsfluss (Kraftfluss)** und **magnetischer Fluss**, letzterer analog, aber in anderer Farbe.
- **Drei Kernbeobachtungen:**
  1. Felder sind nicht an Körper gebunden, durchdringen sie und existieren in Fluiden und Vakuum
  2. Kräfte auf Stator und Rotor bilden innerhalb der elektromagnetischen Betrachtung keinen geschlossenen Kraftkreis mehr, da Energie in einer anderen Domäne gewandelt und übertragen wird
  3. Kraft entsteht bzw. wird übertragen in ein Volumen; ein Flächen-zu-Flächen-Übergang wie in der Mechanik liegt nicht vor
- **Modellierungsregeln für Felder:**
  - CSS = alle kontinuierlichen Volumina, die vom Magnetfeld durchsetzt werden und es zwischen zwei Flächen führen; auch Volumina außerhalb fester Körper
  - Übergang von einem Material zum anderen bzw. Bauteil zu Bauteil = WSP (im Einklang mit Matthiesen 2002: Wirkflächen bilden sich an feldgenerierenden Körpern und an Körpern im feldbefluteten Raum)
  - Fluid- oder Vakuumvolumina mit unterschiedlichen Funktionen in **Kontrollvolumina** unterteilen; an deren Grenzen entstehen WSP (Vorgehen nach Brezger 2013 für Fluide)
- **Fig. 7:** zwei Festkörper (CSS 1.X, CSS 2.X), dazwischen Vakuum (CSS 1.2), das keine mechanische Kraft direkt überträgt, aber Energie transportiert; Kraft entsteht in den benachbarten Volumenanteilen. Vereinfachung: Kraft wird an der Oberfläche (WSP) angreifend dargestellt, da die Summe der Kräfte nahe der Oberfläche wirkt.

### 4.1 Development Generations (S. 16 bis 19)
- Drei Generationen, detailliert modelliert werden die erste und die letzte.
- **"Laminated":** U-Stator aus Elektroblech M250-35A mit Isolierlack, Querbalken (cross bars) mit gedrehter Blechorientierung, Keile halten Statorhälften und Querbalken; Rotor mit vergrabenen Magneten in Sammleranordnung (Fig. 8 Nomenklatur).
- **"SMC":** Klauenpol-Statorhälften als gesinterte SMC-Teile, über die Wicklung greifend; Oberflächenmagnete (Fig. 9).
- **"AM":** Klauenpolform beibehalten, zwei Hälften; feine radiale Schlitze unterbrechen ringförmige Wirbelströme bei geringer Drehmomenteinbuße; Wicklung und Rotor aus Generation 2.

### 4.2 Modell "Laminated" (S. 19 bis 20)
- **Farben in Fig. 10:** gelb = magnetischer Fluss, rot = mechanischer Leistungsfluss; blau = elektrisch isolierende Beschichtung der Kupferdrähte.
- Kupferdrähte, Verguss (mechanische und thermische Anbindung an den Statorkern), fünf Bleche einer Statorhälfte; zwischen jedem Blech eine Lackschicht mit zwei WSP (je Lack-Blech-Kontakt).
- Luftspalt in Kontrollvolumina über Blechen und über Wicklung geteilt; Fluss durch WSP "Air Gap Center" zeigt Streufluss.
- Fig. 11 (90° gedreht, Querbalken): Kraftfluss läuft um das Querbalkenpaket herum, da die Keile nur positionieren und keine tragende Verbindung bilden; Querbalken schließen den Flusspfad.

### 4.3 Modell "AM" (S. 21 bis 22)
- Statorhälfte einteilig, alle Bleche und Lackschichten entfallen; Stator ragt über die Wicklung (mehr Fläche zum Rotor); Magnet erscheint in der Schnittebene (Oberflächenmagnet).
- Fig. 13: Schlitze durch das ganze Teil als elektrische Barrieren; magnetischer Fluss passiert die Schlitze über mehrere WSP und CSS mit schlechterem Material (Luft); Kraftfluss folgt dem Kern entlang der Schlitze.
- Wicklung bewusst vereinfacht als massives Kupferstück (gröbere Abstraktion).

### 5.1 Multi Domain C&C²-A und Unterstützung (S. 22 bis 23)
- C&C²-Modell vor Multiphysik-Simulation (z. B. COMSOL) als gemeinsame Basis in frühen Phasen.
- Vorgehen nach Albers & Wintergerst 2014: alle Disziplinen identifizieren gemeinsam (z. B. Workshop) Funktionen des aktuellen oder eines Referenzprodukts sowie beteiligte WSP und CSS; neue Generation ebenso modellieren; Modelle vergleichen, um Änderungen, Ergänzungen, Entfernungen von WSP/CSS und daraus neue Anforderungen abzuleiten.

### 5.2 Vergleich der Generationen (S. 23 bis 27)
- Alle drei Änderungsarten (hinzufügen, entfernen, ändern) wurden umfangreich genutzt (Fig. 14).
- Wegfall der CSS "Varnish": Funktion "Increase electrical resistance within the stator" muss der Statorwerkstoff übernehmen; Anforderungsliste: hohe Permeabilität und Sättigung, geringe Hystereseverluste, hohe Wärmeleitfähigkeit, hohe Steifigkeit, hoher elektrischer Widerstand (neu).
- **Zielkonflikt:** Wärme- und elektrische Leitfähigkeit beruhen auf denselben Mechanismen.
- Luftgefüllte Schlitze senken laut elektromagnetischer Simulation die Wirbelstromverluste bei kleinem Drehmomentverlust, schwächen aber Steifigkeit (kleineres Flächenträgheitsmoment, schwingungsanfällige "Metallsaiten", NVH); Chance für Luft- oder **Flüssigkeitskühlung** bzw. Sensor-/Aktorintegration.
- **Drei Syntheseideen:**
  1. Schlitze mit elektrisch nichtleitendem Feststoff (z. B. Vergussharz) füllen (Fig. 15): neue WSP für den Kraftfluss, geänderte Eigenschaften der Schlitz-CSS; magnetisch neutral; Schlitzanzahl elektrisch "mehr ist besser" vs. mechanisch weniger; Schlitzbreite magnetisch und mechanisch möglichst schmal, Untergrenze durch Fertigung
  2. poröse Bereiche über Prozessparameter statt Schlitze
  3. Rohpulver in geschlossenen Taschen als Partikeldämpfer (NVH), Verhalten weitgehend unerforscht

### 6. Summary and Future Outlook (S. 27 bis 29)
- Bestätigt Matthiesen 2002: C&C²-A ist auch für die elektromagnetische Domäne nutzbar; gemeinsames Modell als "lingua franca".
- Neue Parameter neben E-Modul und Oberflächengüte: magnetische Permeabilität, elektrischer Widerstand, thermische Anforderungen, Werkstoff- und Prozessgrenzen.
- **Grenzen:** Energiewandlung zwischen Domänen in der Darstellung nicht festgelegt (Kräfte scheinen "aus dem Nichts" zu kommen, gelöst durch Kopplung der Kraft an den magnetischen Fluss); feldbeflutete Volumina ohne klare Wirkfläche; Analyse rein qualitativ, zu wenig quantitative Daten für Kräfte und Flusskonzentration; mehr quantitative Daten je WSP und CSS würden Synthese verbessern.
- Folgeprojekte: innere Kühlung, Sensoren und Aktoren in Stator und Rotor.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Zwei Flüsse (Kraftfluss, Magnetfluss) im selben Modell | Fluss-Ebenen je Domäne mit eigener Farbe; ein- und ausblendbar (z. B. Kraft, Magnetfeld, Wärme, Fluid) |
| CSS als feldbeflutetes Volumen, auch Luft/Vakuum | LSS-Attribut `medium` (Festkörper, Fluid, Vakuum, Feld) und `domaenen` (Mehrfachauswahl) |
| Materialübergang = WSP | Regel bzw. Vorschlag: an jeder Materialgrenze im Feldpfad ein WFP anlegen |
| Kontrollvolumina in Fluid- und Luftbereichen (nach Brezger) | Werkzeug zum Unterteilen eines Fluidvolumens in Kontrollvolumina mit automatisch erzeugten WFP an den Grenzen; direkt relevant für Pumpen, Leitungen, Wärmeübertrager (Einschätzung) |
| Wiederholungen einmal darstellen | Attribut `wiederholungen` (Anzahl) an WFP und LSS; Änderung gilt für alle Instanzen |
| Zusammengefasste CSS ("CSS 1.2.3") | Gruppierungsobjekt, das mehrere LSS zusammenfasst, ohne die Einzel-LSS zu löschen |
| Domänenspezifische Parameter (Permeabilität, Widerstand, Wärmeleitfähigkeit, Steifigkeit) | Parameterkatalog je Domäne; Konfliktanzeige, wenn eine LSS widersprüchliche Anforderungen trägt |
| Vergleich zweier Generationen (hinzugefügt, entfernt, geändert) | Diff-Ansicht zwischen Modellversionen mit Markierung der drei Änderungsarten |
| Energiewandlung als offene Darstellungsfrage | Wandler-Element zwischen Domänen-Flüssen (Verbindung zu Prager et al. 2024: WSP als Wandler) |
| Funktion "wandert" vom entfallenen Element zum Werkstoff | Funktionszuordnung je Element; Warnung, wenn ein Element entfernt wird, das eine Funktion trägt |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2002 (Diss., Basisdefinition, Wirkflächen in feldbeflutetem Raum), Albers & Wintergerst 2014 (Anthology, Vorgehen), Grauberger et al. 2020 (JED, 20 Jahre, Anwendbarkeit auf Felder theoretisch), Matthiesen, Grauberger, Sturm & Steck 2018 (Procedia CIRP 70, Sprache/Metamodell, Fig. 5, Änderungsregel), Gladysz & Albers 2018 (DESIGN, Fehleranalyse Live-Labs), Matthiesen, Grauberger & Schrempp 2019 (ICED, Extended Sequence Modelling, Schiebedach), Brezger 2013 (Diss. KIT, Kontrollvolumina für Fluide, hybride Triebstränge).
