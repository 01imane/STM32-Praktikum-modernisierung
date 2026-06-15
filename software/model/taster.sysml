package Praktikum_Taster {

    private import Requirements::*;

    // -----------------------------
    // INPUT
    // -----------------------------
    requirement TASTER_LOGIC {
        attribute id = "TASTER_LOGIC";
        attribute text = "Alle Taster sind als aktive LOW-Eingänge mit Pull-Up konfiguriert.";
        attribute status = "Approved";
    }

    // -----------------------------
    // GPIO
    // -----------------------------
    requirement GPIO_CONFIG {
        attribute id = "GPIO_CONFIG";
        attribute text = "PA11–PA14 als Input, PC0–PC3 als Output.";
        attribute status = "Approved";
    }

    // -----------------------------
    // FUNKTIONAL
    // -----------------------------
    requirement TASTER_1_FUNCTION {
        attribute id = "TASTER_1";
        attribute text = "Bei PA11 LOW blinkt LED PC0.";
        attribute status = "Approved";
    }

    requirement TASTER_2_FUNCTION {
        attribute id = "TASTER_2";
        attribute text = "Bei PA12 LOW blinkt LED PC1.";
        attribute status = "Approved";
    }

    requirement TASTER_3_FUNCTION {
        attribute id = "TASTER_3";
        attribute text = "Bei PA13 LOW blinken alle LEDs.";
        attribute status = "Approved";
    }

    requirement TASTER_4_FUNCTION {
        attribute id = "TASTER_4";
        attribute text = "Bei PA14 LOW sind alle LEDs an.";
        attribute status = "Approved";
    }

    // -----------------------------
    // TIMING
    // -----------------------------
    requirement T1_TIMING {
        attribute id = "T1_TIMING";
        attribute text = "LED PC0 blinkt mit 1 Hz ±10%.";
        attribute status = "Approved";
    }

    requirement T2_TIMING {
        attribute id = "T2_TIMING";
        attribute text = "LED PC1 blinkt mit 0.5 Hz ±10%.";
        attribute status = "Approved";
    }
}