Requirements Traceability Matrix (RTM)
Project Information
Project: CurrentTracker - Real-Time Electrical Current Monitoring System

Author: Brian Smithberger

Purpose: The Requirements Traceability Matrix (RTM) demonstrates how each project requirement is implemented, tested, and validated throughout the development lifecycle.

Functional Requirements Traceability
Requirement ID	Requirement Description	Design Component	Implementation	Test Case	Status
FR-001	Acquire current measurements from ESP32	Data Acquisition Layer	PySerial communication	TC-01	Pass
FR-002	Receive real-time data through USB serial interface	Serial Communication Module	serial.Serial()	TC-02	Pass
FR-003	Display sensor data graphically	Visualization Layer	PyQtGraph	TC-03	Pass
FR-004	Record timestamped measurements	Data Storage Layer	Python data structures	TC-04	Pass
FR-005	Export collected data to CSV	Storage Module	Pandas DataFrame	TC-05	Pass
FR-006	Support multiple current channels	Dual Channel Architecture	Current1_A, Current2_A	TC-06	Pass
FR-007	Allow user COM port selection	Connection Manager	QComboBox Port Selection	TC-07	Pass
FR-008	Support operation without ESP32 hardware	Simulator Module	Random Data Generator	TC-08	Pass
FR-009	Provide system connection status	User Interface Layer	Connection Status Label	TC-09	Pass
FR-010	Allow port refresh without restart	Connection Manager	Refresh Ports Button	TC-10	Pass
Non-Functional Requirements Traceability
Requirement ID	Requirement Description	Validation Method	Status
NFR-001	Update display every 200 ms	Performance Testing	Pass
NFR-002	Responsive GUI during operation	User Interface Testing	Pass
NFR-003	Operate on Windows systems	Platform Validation	Pass
NFR-004	Use open-source software components	Design Review	Pass
NFR-005	Prevent excessive memory growth	Data Buffer Management	Pass
NFR-006	Automatic file persistence	Auto-Save Timer	Pass
NFR-007	Graceful handling of malformed serial data	Error Handling Validation	Pass

Test Case Mapping
TC-01: Sensor Data Acquisition
Objective
Verify current measurements are received from ESP32.

Procedure
Connect ESP32.
Select COM port.
Start transmission.
Expected Result
Sensor measurements appear continuously.

Outcome
Pass

TC-02: Serial Communication
Objective
Validate USB serial communication.

Procedure
Connect to COM port.
Monitor incoming packets.
Expected Result
No communication errors.

Outcome
Pass

TC-03: Real-Time Visualization
Objective
Verify graph updates.

Procedure
Start data stream.
Observe graph updates.
Expected Result
Graph updates every 200ms.

Outcome
Pass

TC-04: Timestamp Recording
Objective
Verify timestamps are stored.

Procedure
Collect data.
Review CSV output.
Expected Result
Timestamp column contains valid entries.

Outcome
Pass

TC-05: CSV Export
Objective
Validate data export capability.

Procedure
Collect data.
Press Save CSV.
Expected Result
CSV file is generated.

Outcome
Pass

TC-06: Multi-Channel Support
Objective
Verify dual-channel monitoring.

Procedure
Acquire values from both channels.
Observe graph.
Expected Result
Two independent trend lines appear.

Outcome
Pass

TC-07: COM Port Selection
Objective
Verify user selection of communication port.

Procedure
Open application.
Select port from dropdown.
Connect.
Expected Result
Successful connection.

Outcome
Pass

TC-08: Simulator Mode
Objective
Verify application without hardware.

Procedure
Enable simulator mode.
Launch application.
Expected Result
Randomized current values populate graph.

Outcome
Pass

TC-09: Connection Status Display
Objective
Verify user receives connection feedback.

Procedure
Connect to ESP32.
Observe status label.
Expected Result
Status indicates connected state.

Outcome
Pass

TC-10: Port Refresh Function
Objective
Verify dynamic discovery of connected devices.

Procedure
Plug in ESP32 after program launch.
Select Refresh Ports.
Expected Result
New COM port appears in list.

Outcome
Pass

Traceability Summary
Total Functional Requirements: 10

Total Non-Functional Requirements: 7

Total Test Cases: 10

Requirements Successfully Tested: 17/17

Traceability Coverage: 100%

Conclusion
All identified requirements were implemented, tested, and validated. The resulting CurrentTracker solution meets the project objectives for real-time monitoring, visualization, storage, and user interaction.