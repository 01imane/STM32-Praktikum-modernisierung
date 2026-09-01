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

    # SysML-Modelle laden
    lecture, practical = load_models()

    # Gemeinsamen Kontext laden
    context = load_context()

    # Prompt erzeugen
    prompt = build_prompt(

        test_name=test_name,
        expected=expected,
        average=average,
        tolerance=tolerance,
        requirement=requirement,

        lecture_model=lecture,
        practical_model=practical,


        hardware=context["hardware"],
        c_code=context["c_code"],
        traceability=context["traceability"],

        uart_output=uart_output

    )

    # LLM aufrufen
    answer = ask_llm(prompt)

    print("\n========== AI FEEDBACK ==========\n")
    print(answer)
    print("\n===============================\n")

    with open("student_feedback.txt", "a", encoding="utf-8") as f:
         f.write(answer)

    return answer