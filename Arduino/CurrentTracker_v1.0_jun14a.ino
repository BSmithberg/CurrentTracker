#include <SPI.h>
#include <SD.h>

#define SENSOR1_PIN 34  // ADC pin for Current Transformer 1
#define SENSOR2_PIN 35  // ADC pin for Current Transformer 2
#define SD_CS_PIN 5     // Chip Select (CS) pin for SD card

File dataFile;

void setup() {
    Serial.begin(115200);
    
    // Initialize SD card
    if (!SD.begin(SD_CS_PIN)) {
        Serial.println("SD Card initialization failed!");
        return;
    }
    Serial.println("SD Card initialized successfully.");
    
    // Open CSV file and write headers
    dataFile = SD.open("/current_log.csv", FILE_WRITE);
    if (dataFile) {
        dataFile.println("Timestamp,Current1_A,Current2_A");
        dataFile.close();
    }
}

void loop() {
    unsigned long timestamp = millis();
    
    // Read sensor values
    int raw1 = analogRead(SENSOR1_PIN);
    int raw2 = analogRead(SENSOR2_PIN);
    
    // Convert ADC values to current (adjust based on calibration)
    float voltage1 = raw1 * (3.3 / 4095.0);
    float voltage2 = raw2 * (3.3 / 4095.0);
    float current1 = voltage1 * 20;  // Example scaling factor
    float current2 = voltage2 * 20;
    
    // Log data to SD card
    dataFile = SD.open("/current_log.csv", FILE_WRITE);
    if (dataFile) {
        dataFile.print(timestamp);
        dataFile.print(",");
        dataFile.print(current1);
        dataFile.print(",");
        dataFile.println(current2);
        dataFile.close();
    }
    
    // Send data to PC
    Serial.print(timestamp);
    Serial.print(",");
    Serial.print(current1);
    Serial.print(",");
    Serial.println(current2);
    
    delay(1000);  // Delay for readability
}

