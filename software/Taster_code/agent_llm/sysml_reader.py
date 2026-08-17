from pathlib import Path

def load_file(path):

    with open(path,"r",encoding="utf-8") as f:

        return f.read()


def load_models():

    lecture = load_file(
        "../model/Praktikum_Taster.sysml"
    )

    practical = load_file(
        "../model/Praktikum_Taster.sysml"
    )

    return lecture, practical