def build_prompt(

        test_name,
        expected,
        average,
        requirement,
        lecture_model,
        practical_model,
        uart_output

):

    prompt = f"""

Du bist ein Embedded-Systems Tutor.

Analysiere folgenden Test.

Test:
{test_name}

Requirement:
{requirement}

Erwartete Blinkzeit:

{expected} ms

Gemessene Blinkzeit:

{average} ms

UART Ausgabe:

{uart_output}

========================

Vorlesungsmodell

========================

{lecture_model}

========================

Praktikumsmodell

========================

{practical_model}

Bitte beantworte:

1. Wurde Requirement erfüllt?

2. Welche Ursache hat der Fehler?

3. Welche Register sind wahrscheinlich falsch?

4. Welche Vorlesung muss wiederholt werden?

5. Gib Verbesserungsvorschläge.

"""

    return prompt