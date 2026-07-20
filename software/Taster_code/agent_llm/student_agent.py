from sysml_reader import load_models
from prompt_builder import build_prompt
from llm_client import ask_llm


def student_agent(

        test_name,
        expected,
        average,
        requirement,
        uart_output

):

    lecture, practical = load_models()

    prompt = build_prompt(

        test_name,
        expected,
        average,
        requirement,
        lecture,
        practical,
        uart_output

    )

    answer = ask_llm(prompt)

    print("\n========== AI FEEDBACK ==========\n")

    print(answer)

    print("\n===============================\n")