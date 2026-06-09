package Praktikum {

    package Lauflicht {

        requirement <'MP1_LED_Lauflicht_1'> {
            attribute id = "MP1_LED_Lauflicht_1";
            attribute requirement_status = "Approved";
            doc /* Das System soll ein Lauflicht mit LEDs realisieren */
        }

        requirement <'MP1_LED_Lauflicht_2'> {
            attribute id = "MP1_LED_Lauflicht_2";
            attribute requirement_status = "Approved";
            doc /* Es sollen 8 LEDs über GPIO Port C (PC0–PC7) angesteuert werden */
        }

        requirement <'MP1_LED_Lauflicht_3'> {
            attribute id = "MP1_LED_Lauflicht_3";
            attribute requirement_status = "Approved";
            doc /* Die LEDs sollen nacheinander aktiviert werden (Lauflicht) */
        }

        requirement <'MP1_LED_Lauflicht_4'> {
            attribute id = "MP1_LED_Lauflicht_4";
            attribute requirement_status = "Approved";
            doc /* Das Lauflicht soll periodisch wiederholt werden */
        }

        requirement <'MP1_LED_Lauflicht_5'> {
            attribute id = "MP1_LED_Lauflicht_5";
            attribute requirement_status = "Approved";
            doc /* Die Zeit zwischen zwei LED-Wechseln soll ca. 1 Sekunde betragen */
        }

        requirement <'MP1_LED_Lauflicht_6'> {
            attribute id = "MP1_LED_Lauflicht_6";
            attribute requirement_status = "Approved";
            doc /* Die Zeitsteuerung soll über einen Hardware-Timer erfolgen */
        }

        requirement <'MP1_LED_Lauflicht_7'> {
            attribute id = "MP1_LED_Lauflicht_7";
            attribute requirement_status = "Approved";
            doc /* Die GPIO Pins sollen als Output initialisiert werden */
        }

    }

}