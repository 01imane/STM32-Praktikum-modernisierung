from .context_loader import load_context
from .sysml_reader import load_models
from .prompts import build_prompt
from .llm_client import ask_llm


def student_agent(
    test_name,
    expected,
    average,
    tolerance,
    requirement,
    uart_output
):

    # SysML-Modelle laden Vorlesungsmodell und Praktikum
    lecture, practical = load_models()

    # Gemeinsamen Kontext laden
    context = load_context()

    # Prompt erzeugen
    prompt = build_prompt(

        test_name=test_name,

#zum Beispiel 1000 ms.        
        expected=expected,


        average=average,
        tolerance=tolerance,

#ID der geprüften SysML-Anforderung,        
        requirement=requirement,
# Inhalt des Vorlesungsmodells.
        lecture_model=lecture,
        practical_model=practical,

# Beschreibung der verwendeten Hardware.
        hardware=context["hardware"],
        c_code=context["c_code"],
        traceability=context["traceability"],
#Messwerten
        uart_output=uart_output

    )

    # LLM aufrufen
    answer = ask_llm(prompt)

    print("\n========== AI FEEDBACK ==========\n")
    print(answer)
    print("\n===============================\n")
# KI-Antwort in einer Textdatei speichern
    with open("student_feedback.txt", "a", encoding="utf-8") as f:
         f.write(answer)

    return answer