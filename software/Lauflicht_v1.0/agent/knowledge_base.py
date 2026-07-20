ERROR_DB = {

    # =====================================================
    # TIMER
    # =====================================================

    "TIMER_TOO_FAST": {
        "cause": "Timer falsch konfiguriert (zu schnelle Zeitbasis)",
        "lecture": "Vorlesung Timer",
        "topic": "Prescaler und ARR",
        "hint": "Prescaler erhöhen oder ARR vergrößern"
    },

    "TIMER_TOO_SLOW": {
        "cause": "Timer zu langsam konfiguriert",
        "lecture": "Vorlesung Timer",
        "topic": "Prescaler und ARR",
        "hint": "Prescaler verkleinern oder ARR verkleinern"
    },

    # =====================================================
    # LAUFLICHT
    # =====================================================

    "LED_SEQUENCE_ERROR": {
        "cause": "Die LEDs leuchten nicht in der richtigen Reihenfolge.",
        "lecture": "Vorlesung GPIO",
        "topic": "Digitale Ausgänge",
        "hint": "Überprüfen Sie die Laufvariable und die GPIO-Ausgänge."
    },

    "LED_TIMING_ERROR": {
        "cause": "Die Zeit zwischen zwei LEDs entspricht nicht der Anforderung.",
        "lecture": "Vorlesung Timer",
        "topic": "Prescaler und ARR",
        "hint": "Kontrollieren Sie TIM2->PSC und TIM2->ARR."
    },

    "LED_MISSING": {
        "cause": "Mindestens eine LED wurde nicht angesteuert.",
        "lecture": "Vorlesung GPIO",
        "topic": "GPIO-Ausgänge",
        "hint": "Überprüfen Sie die Schleife und die GPIO-Konfiguration."
    },

    # =====================================================
    # TEST OK
    # =====================================================

    "TEST_OK": {
        "cause": "Alle Anforderungen wurden erfolgreich erfüllt.",
        "lecture": "-",
        "topic": "-",
        "hint": "Keine Fehler erkannt."
    }
}