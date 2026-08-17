package Mikroprozessor_Vorlesung {

    private import ScalarValues::*;
    private import Requirements::*;

    doc /*
        Lernziele der Vorlesung Mikroprozessortechnik
        für die Praktikumsversuche Lauflicht, Taster,
        ADC/DAC und SPI.
    */

    // =====================================================
    // Definition eines Lernziels
    // =====================================================

    requirement def Lernziel {

        attribute endverhalten : String;
        attribute bedingung : String;
        attribute massstab : String;
    }

    // =====================================================
    // GPIO
    // =====================================================

    package Vorlesung_GPIO {

        requirement GPIO_Konfiguration : Lernziel {

            ::> endverhalten =
                "Die Studierenden können GPIO-Pins als Ein- oder Ausgang konfigurieren.";

            ::> bedingung =
                "Die Konfiguration erfolgt registerbasiert auf einem STM32-Mikrocontroller.";

            ::> massstab =
                "Die GPIO-Konfiguration funktioniert fehlerfrei und entspricht der Aufgabenstellung.";
        }

        requirement Digitale_Eingaenge : Lernziel {

            ::> endverhalten =
                "Die Studierenden können digitale Eingänge lesen und auswerten.";

            ::> bedingung =
                "Taster werden als Active-Low-Eingänge mit Pull-Up verwendet.";

            ::> massstab =
                "Tasterzustände werden korrekt erkannt und verarbeitet.";
        }

        requirement Digitale_Ausgaenge : Lernziel {

            ::> endverhalten =
                "Die Studierenden können digitale Ausgänge ansteuern.";

            ::> bedingung =
                "LEDs werden über GPIO-Ausgänge angesteuert.";

            ::> massstab =
                "Die LEDs reagieren entsprechend der Anforderung.";
        }
    }

    // =====================================================
    // Timer
    // =====================================================

    package Vorlesung_Timer {

        requirement Timer_Grundlagen : Lernziel {

            ::> endverhalten =
                "Die Studierenden können einen Hardware-Timer konfigurieren.";

            ::> bedingung =
                "Die Konfiguration erfolgt ausschließlich über Timer-Register.";

            ::> massstab =
                "Der Timer erzeugt periodische Ereignisse mit der geforderten Zeitbasis.";
        }

        requirement Prescaler_ARR : Lernziel {

            ::> endverhalten =
                "Die Studierenden können Prescaler und Auto-Reload Register berechnen und konfigurieren.";

            ::> bedingung =
                "Gegeben sind Systemtakt und gewünschte Zeitbasis.";

            ::> massstab =
                "Die berechneten Registerwerte erzeugen die geforderte Periodendauer.";
        }

        requirement Zeitmessung : Lernziel {

            ::> endverhalten =
                "Die Studierenden können Zeitintervalle mit einem Hardware-Timer messen.";

            ::> bedingung =
                "Zur Messung wird ein Hardware-Timer verwendet.";

            ::> massstab =
                "Die gemessenen Zeitintervalle entsprechen den erwarteten Sollwerten.";
        }
    }

}