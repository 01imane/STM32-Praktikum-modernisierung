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
        result,
        uart_output

):
    """
    KI-Agent für den Dozenten.
    Analysiert den Entwicklungsprozess eines Studierenden.
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
    answer = ask_llm(prompt)

    print("\n========== PROFESSOR FEEDBACK ==========\n")
    print(answer)
    print("\n========================================\n")

    return answer