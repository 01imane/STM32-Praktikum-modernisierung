package Praktikum_Lauflicht {

    private import Requirements::*;
    private import Vorlesung_GPIO_Timer::*;

    //--------------------------------------------------------
    // GPIO
    //--------------------------------------------------------

    requirement GPIO_CONFIGURATION {

        attribute id = "GPIO_CONFIGURATION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        GPIOC wird aktiviert.
        PC0-PC7 werden als digitale Ausgänge konfiguriert.
        */

        derived GPIO_Konfiguration;
    }

    //--------------------------------------------------------
    // TIMER
    //--------------------------------------------------------

    requirement TIMER_CONFIGURATION {

        attribute id = "TIMER_CONFIGURATION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        TIM2 erzeugt die Zeitbasis
        für das Lauflicht.
        */

        derived Timer_Grundlagen;
    }

    //--------------------------------------------------------
    // LED INITIALISIERUNG
    //--------------------------------------------------------

    requirement LED_CONFIGURATION {

        attribute id = "LED_CONFIGURATION";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        Acht LEDs werden
        über GPIOC angesteuert.
        */

        derived Digitale_Ausgaenge;
    }

    //--------------------------------------------------------
    // LAUFLICHT
    //--------------------------------------------------------

    requirement RUNNING_LIGHT {

        attribute id = "RUNNING_LIGHT";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        Die LEDs werden
        nacheinander aktiviert.
        */

        derived Digitale_Ausgaenge;
    }

    //--------------------------------------------------------
    // REIHENFOLGE
    //--------------------------------------------------------

    requirement LED_SEQUENCE {

        attribute id = "LED_SEQUENCE";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        Die LEDs werden
        von LED1 bis LED8
        in der richtigen Reihenfolge aktiviert.
        */

        derived Digitale_Ausgaenge;
    }

    //--------------------------------------------------------
    // ZEITVERHALTEN
    //--------------------------------------------------------

    requirement LED_TIMING {

        attribute id = "LED_TIMING";
        attribute requirement_status = "Approved";
        attribute implementation_status = "Implemented";

        doc /*
        Jede LED bleibt
        0,5 Sekunden aktiv.
        */

        derived Prescaler_ARR;
    }

}