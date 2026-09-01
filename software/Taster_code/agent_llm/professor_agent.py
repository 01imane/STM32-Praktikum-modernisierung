from .sysml_reader import load_models
from .prof_prompts import build_prof_prompt
from .llm_client import ask_llm
from .context_loader import load_context


def professor_agent(

        student,
        test_name,
        requirement,
        expected,
        measured,
        tolerance,
        result,
        uart_output

):
    """
    KI-Agent für Lehrende.

    Analysiert nicht nur das aktuelle Testergebnis,
    sondern den gesamten Entwicklungsprozess anhand von

    - main.c
    - SysML
    - Traceability
    - Git-Historie
    - Hardware
    - UART
    """

    # SysML-Modelle laden
    lecture_model, practical_model = load_models()

    # Gemeinsamen Kontext laden
    context = load_context()

    # Prompt erzeugen
    prompt = build_prof_prompt(

        student=student,

        test_name=test_name,

        requirement=requirement,

        expected=expected,

        measured=measured,

        tolerance=tolerance,

        result=result,

        traceability=context["traceability"],

        uart_output=uart_output,
        

        lecture_model=lecture_model,

        practical_model=practical_model,

        hardware=context["hardware"],

        c_code=context["c_code"],

        git_information=context["git_information"]

    )

    # LLM aufrufen
    print("=" * 80) 
    print("PROMPT-LÄNGE:", len(prompt))
    print("=" * 80)
    answer = ask_llm(prompt)
   
    with open("professor_prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    print("Prompt gespeichert.")

    print("\n========== PROFESSOR FEEDBACK ==========\n")
    print(answer)
    print("\n========================================\n")

    with open("professor_feedback.txt", "a", encoding="utf-8") as f:
         f.write(answer)
    
    return answer