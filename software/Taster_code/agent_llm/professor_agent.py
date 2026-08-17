from .sysml_reader import load_models
from .prof_prompts import build_prof_prompt
from .llm_client import ask_llm


def professor_agent(
    student,
    test_name,
    requirement,
    expected,
    measured,
    result,
    traceability,
    uart_output
):
    """
    KI-Agent für den Dozenten.
    Bewertet den aktuellen Stand eines Praktikumsversuchs.
    """

    lecture_model, practical_model = load_models()

    prompt = build_prof_prompt(
        student=student,
        test_name=test_name,
        requirement=requirement,
        expected=expected,
        measured=measured,
        result=result,
        traceability=traceability,
        uart_output=uart_output,
        lecture_model=lecture_model,
        practical_model=practical_model
    )

    answer = ask_llm(prompt)

    print("\n========== PROFESSOR FEEDBACK ==========\n")
    print(answer)
    print("\n========================================\n")

    return answer