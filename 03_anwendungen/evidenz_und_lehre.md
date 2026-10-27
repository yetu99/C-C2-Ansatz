# Empirische Evidenz und Lehre

Stand 27.10.2026. Zahlen aus den Volltexten geprüft, soweit nicht (Abstract) vermerkt.

## Was die Studien zeigen

### Für den Nutzen

| Studie | Design | Ergebnis | Quelle |
|---|---|---|---|
| Fehleranalyse Live-Labs | 80 Masterstudierende in zwei Studien (38; 42 inkl. 7 Moderatoren), Auswertung auf Teamebene; Schaltaktuator (pneumatisch) und Hochdruck-Benzinpumpe | Nachvollziehbarkeit in allen drei Fehlerfällen signifikant besser; **Effizienzgewinn nur im komplexesten Fall** (p = 0,004, r = 0,467, Einstufung nach Gignac und Szodorai); größerer Analyseumfang in der peripheren Zone, gesteuert über Connectoren | `Gladysz2018a` |
| Fehleranalyse Beobachtungsstudie | 22 Teilnehmende, realer Fehlerfall | Mit C&C² mehr und komplexere Fehlerursachen als mit CAD, FTA oder SysML IBD allein | `Gladysz2018b` (Abstract) |
| Kontrolliertes Experiment | N = 35 (36, 1 Ausschluss), videobasiertes Training, jede Person erst Kontrolle, dann Test | Signifikanter Effekt mittlerer bis starker Größe **nur auf Systemebene**; auf Detailebene kein Effekt | `Grauberger2022b` |
| Projektbefragung | 23 Projekte, 17 Personen aus dem IPEK-Umfeld | WFP und Parameter besonders hilfreich; LSS und Connector oft nur formal modelliert; viele zusätzliche Modelle (CAD am häufigsten) | `Grauberger2020b` |
| Review 20 Jahre | 39 Anwendungsfälle aus rund 14.500 gescreenten Publikationen | Schwerpunkt "obtain insight" (20 von 39); Anwendung #24 mit 16 Entwicklern: 69 % Verständlichkeit, 75 % Bedienbarkeit, 81 % Wissenstransfer | `Grauberger2020a` |
| Industrieprojekte | Grounded Theory, 10 Projekte | 9 Kategorien in 3 Clustern | `Grauberger2022c` (Abstract) |
| Extended C&C² | 27 Studierende + 9 Ingenieure, 90 min, Zange | Im Mittel 8 statt 5 Funktionen, mehr Zwischenzustände, rund 4 Abschnitte mehr, 25 % mehr Optimierungsvorschläge; **keine Teststatistik angegeben** | `Troester2025a` |
| Heuristiken in der Industrie | 62 Anwender bei Hilti, 9 Projekte, 11 Workshops, Schulung n = 20 | Schulung Note 2,1 (1 = sehr gut), "alleine anwenden" 3,1; 8 von 10 bewerten HMA, 7 von 8 HMB als hilfreich | `Thau2013` |
| Lastpfad- und Knotenmodell | Crossover, N = 28 | Bessere Ersatzgrößenauswahl nach Schulung, p = 0,044, r = 0,33; im zweiten Durchgang nicht signifikant | `Vogel2021` |
| Konstruktionshypothesen | Live-Lab mit 70 Studierenden, 25 Umfragedatensätze, 160 Hypothesen | Wenn-Dann-Form wurde zur Konzeptmodellierung missbraucht, daher Weil-Teil ergänzt | `Matthiesen2017a` |
| Versuchsaktivitäten | Studentisches Projekt | Erkenntnisgewinn zu GFZ korreliert mit Projekterfolg | `Grauberger2019` (Abstract) |
| EFRT mit Novizen | Cross-over-Studie | Novizen können EFRT-Methode anwenden | `Li2024b` (Abstract) |
| Industrieerfahrung | über 20 veröffentlichte und unveröffentlichte Studien (ohne Einzelzahlen) | Hauptanwendung Problemanalyse an bestehenden Produkten | `Albers2014` S. 166 |

### Einschränkungen und Gegenbefunde

| Befund | Quelle |
|---|---|
| Wirkung nur auf Systemebene, nicht auf Detailebene; Kontrolle immer zuerst (Reihenfolgeeffekt möglich) | `Grauberger2022b` |
| Kein signifikanter Effekt auf Systemverständnis nach Videoschulung, Drittsemester auf Detailebene schlechter | `Paehler2022` (Abstract, Teil von `Grauberger2022b`) |
| "Leicht zu verstehen, schwer anzuwenden": in der Hilti-Schulung Note 3,1 für "alleine anwenden" | `Thau2013` |
| Funktionsbegriff uneinheitlich: im Pumpen-Experiment im Mittel 11,3 von 47 Funktionen gefunden, nur 2 von 20 erkannten den Motorbetrieb | `Alink2010` S. 134, 138; `Eckert2011` (Abstract) |
| Klassischer Ansatz bietet Novizen zu wenig Vorgehensführung | `Troester2025b` |
| Designation Guide und Functional Delimitation schwer vermittelbar (Wissenstest 11,9 von 20) | `Troester2025c` |
| 20 Minuten Einführung reichen nicht (70 % wünschen mehr Zeit) | `Troester2025a` |
| Zeitaufwand für Modellierung und Dokumentation als Hauptbarriere | `Troester2025b`, `Troester2025c` |
| Experten analysieren im Systemkontext, Novizen an der Oberfläche | `Ruckpaul2015` (Abstract) |
| C&C² unterstützt Analyse besser als quantitative Synthese (Synthesis Gap) | `Troester2026` |
| Keine der 39 Anwendungen in Fluid-, Gas- oder Feldsystemen als Schwerpunkt | `Grauberger2020a` S. 260 |
| Fast alle Studien stammen von den entwickelnden Instituten, kleine Stichproben, selten Teststatistik, keine unabhängige Replikation | eigene Bewertung |

### Fazit

Der Nutzen ist am besten belegt für **Fehler- und Ursachenanalyse** an bestehenden Systemen und für das **Systemverständnis auf Systemebene**. Detailverständnis, Synthese und Wissenstransfer sind schwächer belegt. Für Unerfahrene braucht es **Führung im Prozess** (Schritte, Benennung, Abgrenzung) und weniger Aufwand pro Modell. Eine Kurzschulung allein reicht nach aktueller Evidenz nicht. Das spricht für ein Werkzeug, das Vorgehen, Benennung und Dokumentation abnimmt.

## Lehre

| Kontext | Inhalt | Quelle |
|---|---|---|
| KaLeP (Karlsruher Lehrmodell für Produktentwicklung) | Elementmodell als Grundlage der Ausbildung; Lehre seit 1997, rund 20.000 Ingenieure | `Matthiesen2002` S. 143, `Grauberger2020a` S. 243, `Albers2003b` (Abstract) |
| MKL-Boxdarstellung | Große Box für Hauptfunktion, innere Boxen für Teilfunktionen, Zeile für LSS | `Alink2010` S. 153 f. |
| Maschinenkonstruktionslehre, Mechatronische Systeme und Produkte (KIT) | Projektarbeit mit Produktdokumentation | `Matthiesen2018a` |
| Lehramt NwT | C&C² für Lehramtsstudierende | `Matthiesen2018a` |
| Connector in der Lehre | seit 2013 | `Grauberger2020b` S. 905 |
| Videotraining | Grundlage des Experiments | `Grauberger2022b` |
| EnhanCE Modelling | Methodenschulung zur qualitativen Modellbildung | `Grauberger2022a` (Abstract) |
| Live-Lab IP24/25: modulares Lehrkonzept Extended C&C² | Teil 1 Grundlagen (40 min), Teil 2 Erweiterungen (70 min) im Gruppenpuzzle mit vier Modulen und Abschlussübung; Arbeitsblätter für WSP, Functional Delimitation, Produktarchitektur, Connectoren, Zustände; Erklärblätter mit Beispielen; Evaluation nach Kirkpatrick (Reaktion 12,9/15, Wissen nach einem Monat 11,9/20, Panel), n = 16 | `Troester2025c` |

**Lernpfad laut `Troester2025c`:** zuerst WSP und CSS erkennen, dann standardisierte Notation (Designation Guide), zuletzt Functional Delimitation. Empfehlungen: mehr Zeit je Modul, teamweite Workshops, Videos und Foren, **digitale Werkzeuge**.

**Lehrmaterial:** Öffentliche Übungsblätter wurden nicht gefunden. Als KIT-Student sind die ILIAS-Kurse zu MKL I bis IV der direkte Weg (IPEK-Seiten: [MKL](https://www.ipek.kit.edu/english/70_2824.php), [KaLeP](https://www.ipek.kit.edu/english/104.php)).

## Mögliche Evaluationsmethodik für ein eigenes Tool

Übertragbar aus der Literatur:
- Kontrollgruppe ohne Tool vs. Testgruppe mit Tool, gleiche Systeme, Aufgabe Ursachenanalyse; Reihenfolge randomisieren (Lehre aus `Grauberger2022b`).
- Messung auf System- und Detailebene getrennt (`Grauberger2022b`, `Paehler2022`).
- Zählgrößen: gefundene Funktionen, Zustände, Abschnitte, Optimierungsvorschläge (`Troester2025a`), dazu Teststatistik berichten.
- Kirkpatrick-Ebenen Reaktion, Lernen, Verhalten (`Troester2025c`).
- Live-Lab mit Studierenden + kleine Industriegruppe (`Troester2025a`).
- Eye-Tracking zur Bewertung der Ansichten (`Matthiesen2013`, `Lohmeyer2014`, Abstract).
