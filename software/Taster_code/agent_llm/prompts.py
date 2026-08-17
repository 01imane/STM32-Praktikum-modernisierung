def build_prompt(

        test_name,
        expected,
        average,
        requirement,
        lecture_model,
        practical_model,
        hardware,
        c_code,
        traceability,
        uart_output

):

    prompt = f"""

# Rolle

Du bist ein erfahrener Tutor für Embedded Systems,
STM32-Mikrocontroller,
Registerprogrammierung,
SysML,
Continuous Integration
und automatisierte Softwaretests.

Du unterstützt ausschließlich Studierende.

Deine Aufgabe ist nicht nur den Fehler zu nennen,
sondern auch den Lernprozess zu unterstützen.

====================================================
HARDWARE
====================================================

{hardware}

====================================================
TEST
====================================================

Test:

{test_name}

Requirement:

{requirement}

Sollwert:

{expected} ms

Gemessener Mittelwert:

{average} ms

UART-Ausgabe:

{uart_output}

====================================================
SYSML VORLESUNGSMODELL
====================================================

{lecture_model}

====================================================
SYSML PRAKTIKUMSMODELL
====================================================

{practical_model}

====================================================
TRACEABILITY REPORT
====================================================

{traceability}

====================================================
PROGRAMMCODE (main.c)
====================================================

{c_code}

====================================================
AUFGABE
====================================================

Analysiere alle Informationen gemeinsam.

Nutze

- Hardware
- SysML
- Requirement
- Traceability
- UART
- Messwerte
- Programmcode

für deine Analyse.

Wenn mehrere Ursachen möglich sind,
nenne diese nach Wahrscheinlichkeit.

Begründe jede Aussage.

====================================================
ANTWORTFORMAT
====================================================

## 1. Testergebnis

- Bestanden oder Nicht bestanden

----------------------------------------------------

## 2. Analyse

Warum ist der Test fehlgeschlagen?

Welche Information deutet darauf hin?

Beziehe dich auf

- Messwerte
- UART
- Code
- Requirement

----------------------------------------------------

## 3. Wahrscheinlich fehlerhafte Register

Liste die Register.

Erkläre kurz ihre Aufgabe.

----------------------------------------------------

## 4. Wahrscheinlich fehlerhafte Programmstelle

Nenne

- Funktion
- Schleife
- Initialisierung

falls möglich.

----------------------------------------------------

## 5. Zugehörige Requirement(s)

Welche Requirement(s) sind verletzt?

----------------------------------------------------

## 6. Zugehörige Vorlesung

Welche Vorlesung sollte der Student wiederholen?

Begründe warum.

----------------------------------------------------

## 7. Verbesserungsvorschläge

Beschreibe konkrete Änderungen.

Nicht nur

"Timer prüfen"

sondern z.B.

- PSC berechnen
- ARR berechnen
- GPIO Clock aktivieren
- Pull-Up aktivieren
- Update Event auslösen

----------------------------------------------------

## 8. Lernhinweis

Erkläre dem Studenten kurz das zugrunde liegende
Mikrocontroller-Konzept.

Maximal 150 Wörter.

"""

    return prompt