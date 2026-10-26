# Empirische Evidenz und Lehre

## Was die Studien zeigen

### Für den Nutzen

| Studie | Design | Ergebnis | Quelle |
|---|---|---|---|
| Fehleranalyse Live-Labs | 80 Studierende, 2 reale Fehlerfälle (Getriebeschaltung, Einspritzpumpe) | Integrierte C&C²-Modelle effizienter und verständlicher als getrennte Modelle, größerer Analyseumfang als Fehlerbäume | `Gladysz2018a` |
| Fehleranalyse Beobachtungsstudie | 22 Teilnehmende, realer Fehlerfall | Mit C&C² mehr und komplexere Fehlerursachen gefunden als mit CAD, FTA oder SysML IBD allein | `Gladysz2018b` |
| Projektbefragung | 23 Entwicklungs- und Forschungsprojekte | Vorteile in Anwendbarkeit und Nutzen, C&C² wird mit vielen anderen Modellen kombiniert | `Grauberger2020b` |
| Industrieprojekte | Grounded Theory, 10 Projekte | 9 Kategorien in 3 Clustern (u. a. Modellierungsunterstützung, Modellverifikation) | `Grauberger2022c` |
| Extended C&C² | 27 Studierende (Live-Lab) + 9 Ingenieure | Bessere Identifikation und Analyse von GFZ | `Troester2025a` |
| Versuchsaktivitäten | Studentisches Projekt | Erkenntnisgewinn zu GFZ korreliert mit Projekterfolg | `Grauberger2019` |
| EFRT mit Novizen | Cross-over-Studie | Novizen können EFRT-Methode anwenden | `Li2024b` |

### Einschränkungen und Gegenbefunde

| Befund | Quelle |
|---|---|
| Kein signifikanter Effekt auf Systemverständnis nach Videoschulung und angeleiteter Übung. Drittsemester verschlechterten sich auf Detailebene | `Paehler2022` (Teil der Studie in `Grauberger2022b`) |
| Klassischer Ansatz bietet Novizen zu wenig Vorgehensführung | `Troester2025b` |
| Funktionsbenennung und Funktionsabgrenzung schwer vermittelbar | `Troester2025c` |
| Funktionsbegriff selbst bei KIT-geschulten Ingenieuren uneinheitlich | `Eckert2011` |
| Experten analysieren im Systemkontext, Novizen an der Oberfläche | `Ruckpaul2015` |
| C&C² unterstützt Analyse besser als quantitative Synthese (Synthesis Gap) | `Troester2026` |
| Fast alle Studien stammen von den entwickelnden Instituten, kleine Stichproben, unabhängige Replikation fehlt | eigene Bewertung |

### Fazit

Der Nutzen ist am besten belegt für **Fehler- und Ursachenanalyse** an existierenden Systemen. Für Novizen braucht es **Führung im Prozess** (Schritte, Benennung, Abgrenzung). Eine Schulung allein reicht nach aktueller Evidenz nicht.

## Lehre

| Kontext | Inhalt | Quelle |
|---|---|---|
| KaLeP (Karlsruher Lehrmodell für Produktentwicklung) | C&CM seit 1999 in Maschinenkonstruktionslehre, Studienleistung getestet | `Albers2003b` |
| Maschinenkonstruktionslehre, Mechatronische Systeme und Produkte (KIT) | Projektarbeit mit bereitgestellter Produktdokumentation | `Matthiesen2018a` |
| Lehramt NwT ("Technik erleben und vermitteln") | C&C² für Lehramtsstudierende | `Matthiesen2018a` |
| EnhanCE Modelling | Methodenschulung zur Vermittlung qualitativer Modellbildung | `Grauberger2022a` |
| Live-Lab IP (Integrierte Produktentwicklung) | Modulares Lehrkonzept Extended C&C² | `Troester2025c` |

**Lehrmaterial:** Öffentliche Übungsblätter wurden nicht gefunden. Als KIT-Student sind die ILIAS-Kurse zu MKL I bis IV der direkte Weg (IPEK-Seiten: [MKL](https://www.ipek.kit.edu/english/70_2824.php), [KaLeP](https://www.ipek.kit.edu/english/104.php)).

## Mögliche Evaluationsmethodik für ein eigenes Tool

Übertragbar aus der Literatur:
- Kontrollgruppe ohne Tool vs. Testgruppe mit Tool, gleiche technische Systeme, Aufgabe Ursachenanalyse (`Grauberger2022b`)
- Messung auf System- und Detailebene (`Paehler2022`)
- Live-Lab mit Studierenden + kleine Industriegruppe (`Troester2025a`)
- Eye-Tracking zur Bewertung der Ansichten (`Matthiesen2013`, `Lohmeyer2014`)
