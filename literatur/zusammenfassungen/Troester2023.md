# Tröster, Schmidt, Albers 2023: Designation Guide für C&C²-Elemente

| Feld | Wert |
|---|---|
| Autoren | Peter M. Tröster, David Schmidt, Albert Albers |
| Titel | A Designation Guide for Consistent Cross-System-Level Modeling of Embodiment Function Relations |
| Quelle/Reihe | Procedia CIRP 119 (2023), S. 1222 bis 1227, 33rd CIRP Design Conference |
| Jahr | 2023 |
| DOI | 10.1016/j.procir.2023.03.158 |
| Lizenz | CC BY-NC-ND 4.0 |
| Volltext | [`../volltexte/Troester2023.pdf`](../volltexte/Troester2023.pdf) (6 S.) |
| Status | gelesen, vollständig ausgewertet |

## Kernaussage

Bisherige C&C²-Modelle benennen WSP, CSS und Connectoren uneinheitlich, wodurch Modelle schwer vergleichbar sind. Der **Designation Guide** legt eine Benennung in **fünf Schritten** fest: **Hauptsysteme mit Buchstaben**, **Subsysteme mit Punktnummern**, **"//" für WSP**, **"~" für CSS** und **Wirksequenzen in Klammern** (Beispiel `BD1.1//BD2.4(S[1; 6])`). Ziel ist Vergleichbarkeit vieler Modelle und langfristig eine **Modelldatenbank als Grundlage für KI**.

## Inhalte nach Abschnitt

### 1. Motivation (S. 1222)
- Dokumentation von EFR wichtig wegen Fachkräftemangel, Wartung, besserem Design. Voraussetzung ist eine konsistente Benennung.

### 2. Stand der Technik (S. 1223 bis 1224)
- Produktmodelle der Gestaltung nach Zweck (Abb. 1). C&C² als verbreiteter Ansatz zur EFR-Modellierung.
- **Definitionen** (S. 1223, nach Matthiesen 2021): WSP entstehen, wenn zwei beliebig geformte Festkörperoberflächen oder generalisierte Grenzflächen von Flüssigkeiten, Gasen oder Feldern in Kontakt treten und Energie, Stoff und/oder Information austauschen. CSS sind Volumina, die "connect precisely two pairs of working surface pairs" (Formulierung im Original doppelt, gemeint sind genau zwei WSP). Connectoren abstrahieren die Systemumgebung, haben eine repräsentative Wirkfläche und ein Umgebungsmodell, liegen im Betrachtungsraum, nicht im Gestaltungsraum.
- Drei Hypothesen knapp: Funktion braucht Interaktion, Mindestanzahl an Kernelementen, fraktale Modellierung.
- **Vier bisherige Benennungsarten** (Abb. 3):
  1. Fortlaufende Nummerierung (WSP1, WSP2, ...).
  2. WSP aus angrenzenden C und CSS ("C1 - CSS 3.1"), abhängig von der 2D-Lage, bei Drehung inkonsistent.
  3. WSP nach Zeitpunkt (A1, B2), Beispiel Schraubvorgang.
  4. Nach Haupt- und Teilfunktion (0.x, 1.x), CSS als "CSS0.1/0.2"; Systemgrenzen über CSS statt Connectoren.

### 3. Methodik und Forschungsfragen (S. 1224 bis 1225)
- Literaturanalyse zu C&C²-Modellen und allgemeinen Bezeichnungssystemen; Entwicklung in einem Automobil-Entwicklungsprojekt.
- RQ1 bis RQ5: Anforderungen, einheitliche Benennung, Einbindung von Lage und zeitlicher Wirkung, Merkbarkeit, Anpassbarkeit.

### 4. Ergebnisse (S. 1225 bis 1226)
- **Sechs Anforderungen (Tab. 1):** Eindeutigkeit, Verständlichkeit, Konsistenz, Relevanz, Flexibilität, Dokumentation.
- **Fünf Schritte:**
  1. **Systeme definieren:** Hauptsysteme (MS) mit Buchstaben, getrennt nach Funktion, auch mehrere MS in einem Bauteil möglich (Front = "F", Mitte der Front = "FC").
  2. **Subsysteme definieren:** Nummern, Verfeinerung mit Punkt ("1.1"), zusammen z. B. "F1.1".
  3. **CSS und WSP benennen:** zwei Wirkflächen mit "//" verbunden (Anlehnung an die Doppellinie für WSP), CSS mit "~" (Anlehnung an die Wellenlinie).
  4. **Relevante Sequenzen beschreiben:** Wirksequenzen je WSP in Tabellen; Angabe in runden Klammern, mehrere Sequenzen in eckigen Klammern mit Semikolon, "S" für Sequenz.
  5. **Auftretende Sequenzen festlegen:** Beispiel `BD1.1//BD2.4(S[1; 6])` für Wirkung in Fertigung (Sequenz 1) und Einbauzustand (Sequenz 6). MS-Bezeichnungen alphabetisch geordnet.
- **Symbole (Tab. 2):** `//` WSP, `~` CSS, `;` Trennung von Wirksequenzen.

### 5. Diskussion (S. 1226)
- Bisherige Systeme erfüllen die Anforderungen nicht; fortlaufende Nummerierung ist unflexibel.
- Buchstaben für MS sind besser merkbar (Psychologiestudien zitiert).
- Fraktalität: Detailtiefe durch weitere Nummern; domänenübergreifend nutzbar.
- Logischer Zustand anhängbar (`xxx(S[1; 3])`), auch Zeitpunkte wie `(t = 0.03s)` für Hochgeschwindigkeitsaufnahmen.
- Oft genügt es, nur CSS zu benennen; WSP erst bei mehreren angrenzenden Systemen.
- Validierung: Fallstudie Automobil, im Abstract "very successfully", **ohne Kennzahlen**.

### 6. Ausblick (S. 1226 bis 1227)
- Offene Frage: Unterscheidung mehrerer Funktionen innerhalb einer CSS bzw. eines Bauteils (besonders 3D-Druck). Wird später durch die Functional Delimitation adressiert.
- Vergleich vieler Modelle, **Datenbank als Grundlage für KI**.

## Relevanz für ein Ingenieur-Tool

| Aspekt aus dem Paper | Mögliche Tool-Funktion |
|---|---|
| Hauptsystem (Buchstabe) und Subsystem (Punktnummer) | Hierarchischer Systembaum, Bezeichner werden automatisch abgeleitet |
| `//` für WSP, `~` für CSS | Anzeigename generiert aus den beteiligten Flächen bzw. WSP, nicht manuell getippt |
| Sequenzangabe `(S[1; 6])` | Zuordnung Element ↔ Zustände als Relation; Anzeige als Suffix |
| Zeitstempel statt Sequenznummer | Unterstützung für Videoanalyse (Zeitmarke je Zustand) |
| Sechs Anforderungen an Benennung | Validierung: eindeutige IDs, keine Umbenennung bei Ergänzung (stabile interne UUID plus lesbarer Bezeichner) |
| Datenbank vieler Modelle als KI-Basis | Einheitliches Datenformat (JSON-Schema) und durchsuchbare Modellbibliothek |
| Nur CSS benennen genügt oft | Minimalmodus mit LSS-only, WFP optional |

## Im Paper zitierte Schlüsselquellen
Matthiesen 2021 (Pahl/Beitz, Definitionen), Paehler und Matthiesen (Produktmodelle der Gestaltung), Grauberger et al. 2020 (JED), Albers und Wintergerst 2014, Matthiesen et al. 2018 (SWP 58) sowie die Quellen der vier Benennungsarten (Abb. 3).
