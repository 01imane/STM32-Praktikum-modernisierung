package Vorlesung_GPIO_Timer {

    private import Requirements::*;

    requirement GPIO_Konfiguration {
        attribute id = "GPIO_Konfiguration";
        attribute text = "Die Studierenden können GPIO-Pins als digitale Ausgänge konfigurieren.";
        attribute status = "Approved";
    }

    requirement Digitale_Ausgaenge {
        attribute id = "Digitale_Ausgaenge";
        attribute text = "Die Studierenden können digitale Ausgänge zur LED-Ansteuerung verwenden.";
        attribute status = "Approved";
    }

    requirement Timer_Grundlagen {
        attribute id = "Timer_Grundlagen";
        attribute text = "Die Studierenden können einen Hardware-Timer konfigurieren und verwenden.";
        attribute status = "Approved";
    }

    requirement Prescaler_ARR {
        attribute id = "Prescaler_ARR";
        attribute text = "Die Studierenden verstehen die Bedeutung von Prescaler und Auto-Reload-Register zur Einstellung der Timerperiode.";
        attribute status = "Approved";
    }

}