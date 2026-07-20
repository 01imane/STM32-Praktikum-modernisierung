package Praktikum_Taster {

    private import Requirements::*;
    private import Mikroprozessor_Vorlesung::Vorlesung_GPIO::*;
    private import Mikroprozessor_Vorlesung::Vorlesung_Timer::*;

    doc /*
        Dieses Paket definiert die Anforderungen für den
        Praktikumsversuch "Taster und LED-Ansteuerung".
    */

    // =====================================================
    // GPIO
    // =====================================================

    requirement GPIO_CONFIG {

        attribute id = "GPIO_CONFIG";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            PA11–PA14 werden als digitale Eingänge
            mit Pull-Up konfiguriert.

            PC0–PC3 werden als digitale Ausgänge
            konfiguriert.
        */

        derived GPIO_Konfiguration;
    }

    // =====================================================
    // Tasterlogik
    // =====================================================

    requirement TASTER_LOGIC {

        attribute id = "TASTER_LOGIC";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            Alle Taster arbeiten als Active-Low-Eingänge.
            Ein gedrückter Taster liefert den logischen Wert 0.
        */

        derived Digitale_Eingaenge;
    }

    // =====================================================
    // Timer
    // =====================================================

    requirement TIMER_CONFIGURATION {

        attribute id = "TIMER_CONFIGURATION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            TIM2 wird als periodische Zeitbasis
            für die LED-Ansteuerung verwendet.
        */

        derived Timer_Grundlagen;
    }

    // =====================================================
    // Funktionale Anforderungen
    // =====================================================

    requirement TASTER_1_FUNCTION {

        attribute id = "TASTER_1_FUNCTION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            Wird Taster PA11 gedrückt,
            blinkt LED PC0.
        */

        derived Digitale_Ausgaenge;
    }

    requirement TASTER_2_FUNCTION {

        attribute id = "TASTER_2_FUNCTION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            Wird Taster PA12 gedrückt,
            blinkt LED PC1.
        */

        derived Digitale_Ausgaenge;
    }

    requirement TASTER_3_FUNCTION {

        attribute id = "TASTER_3_FUNCTION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            Wird Taster PA13 gedrückt,
            blinken alle LEDs gleichzeitig.
        */

        derived Digitale_Ausgaenge;
    }

    requirement TASTER_4_FUNCTION {

        attribute id = "TASTER_4_FUNCTION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            Wird Taster PA14 gedrückt,
            werden alle LEDs dauerhaft eingeschaltet.
        */

        derived Digitale_Ausgaenge;
    }

    // =====================================================
    // Zeitverhalten
    // =====================================================

    requirement T1_TIMING {

        attribute id = "T1_TIMING";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            LED1 wird periodisch
            mit einer Umschaltzeit von 1000 ms betrieben.
        */

        derived Prescaler_ARR;
    }

    requirement T2_TIMING {

        attribute id = "T2_TIMING";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
            LED2 wird periodisch
            mit einer Umschaltzeit von 1000 ms betrieben.
        */

        derived Prescaler_ARR;
    }

    // =====================================================
    // Ansicht
    // =====================================================

    view Anforderungen_Praktikum_Taster {

        doc /*
            Übersicht aller Anforderungen
            des Praktikumsversuchs "Taster".
        */
    }

}