ERROR_DB = {

    "TIMER_TOO_FAST": {

        "requirement": "T1_TIMING",

        "learning_goal": "Prescaler_ARR",

        "lecture": "Vorlesung_Timer",

        "cause":
            "Der Timer erzeugt Blinkereignisse zu schnell.",

        "hint":
            "Prescaler erhöhen oder ARR vergrößern.",

        "code":
            "TIM2->PSC, TIM2->ARR"
    },

    "TIMER_TOO_SLOW": {

        "requirement": "T1_TIMING",

        "learning_goal": "Prescaler_ARR",

        "lecture": "Vorlesung_Timer",

        "cause":
            "Der Timer erzeugt Blinkereignisse zu langsam.",

        "hint":
            "Prescaler verkleinern oder ARR verkleinern.",

        "code":
            "TIM2->PSC, TIM2->ARR"
    },

    "WRONG_TEST": {

        "requirement": "TASTER_1_FUNCTION",

        "learning_goal": "Digitale_Eingaenge",

        "lecture": "Vorlesung_GPIO",

        "cause":
            "Der falsche Taster wurde gedrückt.",

        "hint":
            "Den Taster betätigen, der zum ausgewählten Test gehört.",

        "code":
            "GPIOA->IDR"
    },

    "NO_BLINK_DETECTED": {

        "requirement": "T1_TIMING",

        "learning_goal": "Timer_Grundlagen",

        "lecture": "Vorlesung_Timer",

        "cause":
            "Es wurden keine Blinkereignisse erkannt.",

        "hint":
            "Timer und UART-Ausgabe überprüfen.",

        "code":
            "TIM2 / printf()"
    },

    "TRACEABILITY_ERROR": {

        "requirement": "TRACEABILITY",

        "learning_goal": "Requirements Engineering",

        "lecture": "SysML",

        "cause":
            "Eine Anforderung wurde im C-Code nicht implementiert.",

        "hint":
            "@satisfies-Kommentar ergänzen oder Requirement implementieren.",

        "code":
            "@satisfies"
    }

}