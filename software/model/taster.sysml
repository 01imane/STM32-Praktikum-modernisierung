package Praktikum_Taster {

    private import Requirements::*;

    // -----------------------------
    // TASTER 1
    // -----------------------------
    requirement TASTER_1_BLINK_1HZ {
        attribute id = "TASTER_1";
        attribute text = "Bei Betätigung von Taster 1 (PA11 = LOW) blinkt LED1 (PC0) mit einer Frequenz von 1 Hz (Periode 1s, Tastverhältnis 50%).";
        attribute status = "Approved";
    }

    // -----------------------------
    // TASTER 2
    // -----------------------------
    requirement TASTER_2_BLINK_05HZ {
        attribute id = "TASTER_2";
        attribute text = "Bei Betätigung von Taster 2 (PA12 = LOW) blinkt LED2 (PC1) mit einer Frequenz von 0.5 Hz (Periode 2s).";
        attribute status = "Approved";
    }

    // -----------------------------
    // TASTER 3
    // -----------------------------
    requirement TASTER_3_ALL_BLINK {
        attribute id = "TASTER_3";
        attribute text = "Bei Betätigung von Taster 3 (PA13 = LOW) blinken alle LEDs (PC0–PC3) synchron mit 1 Hz.";
        attribute status = "Approved";
    }

    // -----------------------------
    // TASTER 4
    // -----------------------------
    requirement TASTER_4_ALL_ON {
        attribute id = "TASTER_4";
        attribute text = "Bei Betätigung von Taster 4 (PA14 = LOW) werden alle LEDs (PC0–PC3) dauerhaft eingeschaltet.";
        attribute status = "Approved";
    }

    // -----------------------------
    // INPUT LOGIK
    // -----------------------------
    requirement TASTER_INPUT_LOGIC {
        attribute id = "TASTER_LOGIC";
        attribute text = "Alle Taster sind als aktive LOW-Eingänge mit Pull-Up-Widerstand konfiguriert.";
        attribute status = "Approved";
    }

    // -----------------------------
    // GPIO CONFIG
    // -----------------------------
    requirement GPIO_CONFIGURATION {
        attribute id = "GPIO_CONFIG";
        attribute text = "GPIO Pins PA11–PA14 sind als Eingänge konfiguriert, PC0–PC3 als digitale Ausgänge.";
        attribute status = "Approved";
    }
}