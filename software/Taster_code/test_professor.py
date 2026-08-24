from agent_llm.professor_agent import professor_agent

# -----------------------------------------
# Testdaten
# -----------------------------------------

student = "Max Mustermann"

test_name = "LED2 TOGGLE"

requirement = "TASTER_2_FUNCTION"

expected = 1000

measured = 1000

tolerance = 20

result = "PASS"

uart_output = """
LED2 TOGGLE 2678000
LED2 TOGGLE 2679000
LED2 TOGGLE 2680000
LED2 TOGGLE 2681000
LED2 TOGGLE 2682000
LED2 TOGGLE 2683000
LED2 TOGGLE 2684000
LED2 TOGGLE 2685000
LED2 TOGGLE 2686000
LED2 TOGGLE 2687000
"""

# -----------------------------------------
# Professor-Agent starten
# -----------------------------------------

professor_agent(

    student=student,

    test_name=test_name,

    requirement=requirement,

    expected=expected,

    measured=measured,

    tolerance=tolerance,

    result=result,

    uart_output=uart_output

)