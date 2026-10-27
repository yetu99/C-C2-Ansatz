# Erkenntnisse aus der Literatur für ein späteres Ingenieur-Tool

Status: **Sammlung, keine Spezifikation.** Diese Seite übersetzt Befunde aus der Recherche in mögliche Anforderungen. Sie wird verfeinert, sobald die Pflichtlektüre (Prio A) gelesen ist.

## 1. Was die Literatur fordert

| Befund | Quelle | Mögliche Tool-Anforderung |
|---|---|---|
| Kein öffentlich verfügbarer, gepflegter C&C²-Editor, kein GitHub-Projekt | Recherche 2026 | Marktlücke |
| Autoren fordern selbst digitale Integration | `Troester2025a` | Forschungsanschluss gegeben |
| Novizen brauchen Prozessführung | `Troester2025b`, `Paehler2022` | Geführter Modus mit fünf Schritten |
| Benennung und Funktionsabgrenzung schwer | `Troester2023`, `Troester2025c`, `Eckert2011` | Benennungsassistent nach Designation Guide, Pflichtfeld Modellzweck |
| C&C² wird stets mit anderen Modellen kombiniert | `Grauberger2020b`, `Paehler2024` | Verknüpfungen zu CAD, Messdaten, Simulation |
| Einfachheit, Skizzenniveau, "show rather than tell" | `Grauberger2022c` | Modell direkt auf Foto, Skizze, CAD-Schnitt zeichnen |
| Hypothesen und Verifikation zentral | `Matthiesen2017a`, `Grauberger2022c` | Hypothesenregister mit Status und Evidenz |
| Dynamische Systeme brauchen Zustände | `Matthiesen2019b` | Zustands-Timeline, Sequenzmodell |
| Synthesis Gap | `Troester2026` | Berechnungsschicht je WFP (Fläche, Orientierung, Reibung, Pressung) |
| Fehleranalyse ist bester Use Case | `Gladysz2018a`, `Gladysz2018b` | Modus Fehler- und Ursachenanalyse |
| Ideal vs. real | `Matthiesen2018a` | Varianten je WFP: ideal, gefertigt, verschlissen |
| Generationsvergleich | `Troester2024a` | Diff zwischen Modellversionen, PGE-Variationstyp |

## 2. Datenmodell-Skizze (aus Definitionen abgeleitet)

```
Projekt
 └─ C&C²-Modell
     ├─ zweck: Text (Pflicht)
     ├─ systemabbild: Bild | Skizze | CAD-Schnitt
     ├─ systemgrenze: { räumlich: [Teilsystem], zeitlich: [Zustand] }
     ├─ zustaende: [Zustand]                  # Sequenzmodell = geordnete Liste
     │    └─ wirknetz
     │        ├─ wirkflaechen:  [WF  { id, bauteil, medium: fest|fluid|gas|feld }]
     │        ├─ wfp:           [WFP { id, wf_a, wf_b, austausch: [Energie|Stoff|Information],
     │        │                        flaeche?, orientierung?, reibwert?, variante: ideal|gefertigt|verschlissen }]
     │        ├─ lss:           [LSS { id, wfp: [≥2], medium, werkstoff? }]
     │        ├─ connectoren:   [C   { id, wfp, umgebungseigenschaften }]
     │        └─ gestaltparameter: [{ element, name, wert, einheit }]
     ├─ hypothesen: [{ gestaltparameter, funktionsgroesse, erwartung, pruefung, status, evidenz }]
     └─ verknuepfungen: [{ ziel: CAD|Messung|Simulation|SysML|FMEA, referenz }]
```

**Prüfregeln direkt aus den Grundhypothesen:**
- GH 1: Jede Wechselwirkung braucht ein WFP aus zwei WF
- GH 2: Eine Funktion braucht ≥ 2 WFP, ≥ 1 LSS dazwischen und je einen Connector zur Umgebung
- GH 3: Jedes Element darf in ein Untermodell aufgelöst werden (Zoom)
- Zustand: Änderung von Anzahl oder Eigenschaften der GFE erzeugt einen neuen Zustand

## 3. Offene Fragen vor einer Spezifikation

- Exakte Struktur des Sequenzmodells (vier Dimensionen in `Matthiesen2019b`)
- Formalisierung aus `Albers2011c` (JMD) als Vorlage für das Datenmodell
- Fünf Schritte des Extended C&C² im Wortlaut (`Troester2025b`)
- Darstellungskonventionen (Farben, Symbole) aus `Matthiesen2018a` und `Grauberger2022a`
- Zielgruppe: Lehre, Fehleranalyse in der Industrie, oder Entwicklung im Wasser-/Energiebereich

## 4. Pflichtlektüre vor dem Tool-Konzept (Reihenfolge)

1. `Grauberger2020a`: Review 20 Jahre (KIT-Zugang)
2. `Matthiesen2018a`: Modellbildungstechniken (liegt vor)
3. `Albers2014`: Kanonische Definition (KIT-Zugang)
4. `Troester2025b` + `Troester2023`: Prozessmodell und Benennung (OA)
5. `Matthiesen2019b`: Sequenzmodell (OA)
6. `Albers2011c`: Formalisierung im Software-Tool (KIT-Zugang)
7. `Troester2026`: Quantitative WFP-Attribute (OA)
8. `Gladysz2018a`: Fehleranalyse (KIT-Zugang)
9. `Vogel2021`: Wandlungselemente für Energiesysteme (OA)
10. `Prager2024`: Bondgraph-Kopplung (OA)
