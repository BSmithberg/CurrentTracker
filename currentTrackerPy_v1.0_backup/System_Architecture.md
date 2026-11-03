System Architecture
Project Overview
CurrentTracker is a real-time electrical current monitoring system consisting of embedded hardware and desktop software integrated through serial communication.

The architecture follows a layered design approach separating hardware acquisition, communication, processing, visualization, and storage responsibilities.

High-Level Architecture
+--------------------+ | Current Sensors | +--------------------+ | v +--------------------+ | ESP32 Controller | +--------------------+ | USB Serial | v +--------------------+ | Communication | | Layer | +--------------------+ | v +--------------------+ | Data Acquisition | | Module | +--------------------+ | v +--------------------+ | Processing Layer | +--------------------+ | +---------------+---------------+ | | v v +--------------------+ +--------------------+ | Visualization | | Data Storage | | Layer | | Layer | +--------------------+ +--------------------+ | v +--------------------+ | CSV Export | +--------------------+

Hardware Architecture

Current Sensors
Responsibilities
Measure electrical current
Convert current into measurable signal
Provide data to ESP32

Inputs
Circuit current

Outputs
Sensor signal

ESP32 Microcontroller
Responsibilities
Read sensor values
Generate timestamps
Format data packets
Transmit data over USB

Inputs
Current sensor signals

Outputs
Timestamp, Current1, Current2

Example:

1000,4.32,3.98

Software Architecture

Layer 1 - Communication
Technologies
PySerial
Responsibilities
Detect serial ports
Establish connection
Receive data packets
Main Functions
Port discovery
User-selected connection
Data reception

Layer 2 - Data Acquisition
Responsibilities
Read incoming packets
Validate packet integrity
Parse measurements
Processing Flow
Raw Data

↓

String Format

↓

Validation

↓

Timestamp + Measurements

↓

Storage

Layer 3 - Processing
Responsibilities
Convert strings to floating-point values
Prepare graph updates
Maintain data history
Data Structure
data = {
    "Timestamp": [],
    "Current1_A": [],
    "Current2_A": []
}

Layer 4 - Visualization
Technologies
PyQt5
PyQtGraph
Responsibilities
Display live data
Plot current values
Display connection status
User Features
Real-time graph
Connect button
Refresh ports
Save CSV
Port selection dropdown

Layer 5 - Storage
Technology
Pandas
Responsibilities
Create DataFrame
Export data
Preserve measurements
Output Format

CSV

Columns:

Timestamp
Current1_A
Current2_A
User Interface Architecture

+--------------------------------------------------+ | COM Port Selection | | Refresh Button | | Connect Button | | Status Label | +--------------------------------------------------+

+--------------------------------------------------+ | Real-Time Plot Area | | | | Current Channel 1 | | Current Channel 2 | +--------------------------------------------------+

+--------------------------------------------------+ | Save CSV Button | +--------------------------------------------------+

Data Flow Diagram

Step 1:

Current Sensors generate measurements.

↓

Step 2:

ESP32 packages data.

↓

Step 3:

Serial communication transfers data.

↓

Step 4:

Python application receives packets.

↓

Step 5:

Data validation occurs.

↓

Step 6:

Real-time graph updates.

↓

Step 7:

Measurements stored.

↓

Step 8:

CSV generated.

Error Handling Architecture
Serial Connection Errors

Problem:

Unavailable COM port.

Solution:

User-selected ports
Refresh button
Connection status feedback
Malformed Data

Problem:

Unexpected packet structure.

Solution:

Python
if len(parts) != 3:
return
Hardware Unavailable

Problem:

ESP32 disconnected.

Solution:

Simulator Mode.

Future Architecture Enhancements
Phase 2

Potential improvements include:

Automatic ESP32 detection
SQLite database storage
Multi-device support
Alarm thresholds
Historical analytics
PDF reporting
Cloud synchronization
REST API interface
Design Principles Applied
Separation of Concerns
Modular Architecture
Fault Tolerance
Maintainability
Scalability
User-Centered Design
Conclusion

The CurrentTracker architecture separates acquisition, communication, processing, visualization, and storage into independent layers. This modular structure simplifies maintenance, testing, and future expansion while providing reliable real-time monitoring of electrical current measurements.