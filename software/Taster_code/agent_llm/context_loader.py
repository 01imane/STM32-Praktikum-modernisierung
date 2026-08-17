from pathlib import Path
from .git_reader import load_git_information


# --------------------------------------------------
# Projektverzeichnis bestimmen
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# Datei lesen
# --------------------------------------------------

def read_file(path):

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return f"Datei konnte nicht gelesen werden:\n{e}"


# --------------------------------------------------
# main.c laden
# --------------------------------------------------

def load_c_code():

    path = PROJECT_ROOT / "Core" / "Src" / "main.c"

    return read_file(path)


# --------------------------------------------------
# Traceability Report laden
# --------------------------------------------------

def load_traceability():

    path = PROJECT_ROOT / "requirements_report.md"

    return read_file(path)


# --------------------------------------------------
# Hardwareinformationen
# --------------------------------------------------

def load_hardware():

    return """
Hardwareplattform

Board:
STM32 NUCLEO-F446RE

Mikrocontroller:
STM32F446RE

CPU:
ARM Cortex-M4

Programmierstil:
Registerbasierte Programmierung

Systemtakt:
84 MHz

Peripherie:

- GPIO
- Timer
- UART
- ADC
- DAC/PWM
- SPI
- I²C

Die tatsächlich verwendeten Peripheriemodule sind anhand
des Programmcodes (main.c) sowie der SysML-Modelle zu
identifizieren und bei der Analyse zu berücksichtigen.

Entwicklungsumgebung:

STM32CubeMX

Visual Studio Code

Git

GitHub / GitLab

Python Testframework

OpenRouter API

"""


# --------------------------------------------------
# Compiler Log
# --------------------------------------------------

def load_compiler_log():

    path = PROJECT_ROOT / "build" / "compile.log"

    if path.exists():

        return read_file(path)

    return "Kein Compiler-Log vorhanden."







# --------------------------------------------------
# Gesamten Kontext erzeugen
# --------------------------------------------------

def load_context():

    context = {

        "hardware": load_hardware(),

        "c_code": load_c_code(),

        "traceability": load_traceability(),

        "compiler_log": load_compiler_log(),

        "git_information": load_git_information()

    }

    return context