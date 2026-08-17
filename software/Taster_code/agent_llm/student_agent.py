from .sysml_reader import load_models
from .prompts import build_prompt
from .llm_client import ask_llm


def student_agent(

        test_name,
        expected,
        average,
        requirement,
        uart_output,
        hardware,
        c_code,
        traceability

):

    # SysML-Modelle laden
    lecture, practical = load_models()

    # Prompt erzeugen
    prompt = build_prompt(

        test_name=test_name,
        expected=expected,
        average=average,
        requirement=requirement,
        lecture_model=lecture,
        practical_model=practical,
        hardware=hardware,
        c_code=c_code,
        traceability=traceability,
        uart_output=uart_output

    )

    # LLM aufrufen
    answer = ask_llm(prompt)

    print("\n========== AI FEEDBACK ==========\n")
    print(answer)
    print("\n===============================\n")

    return answer