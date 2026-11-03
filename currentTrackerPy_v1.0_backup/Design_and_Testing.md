1. Project Overview
Project Title

CurrentTracker: Real-Time Electrical Current Monitoring and Analysis System

Purpose

CurrentTracker was developed to provide real-time monitoring, visualization, and historical logging of electrical current measurements obtained from an ESP32 microcontroller platform.

The system allows users to:

Acquire current measurements from multiple channels
Visualize current values in real time
Store data for later analysis
Monitor circuit behavior during operation
Export recorded measurements to CSV format
Problem Statement

Traditional current monitoring solutions often require expensive industrial hardware or proprietary software. The objective of this project was to create a cost-effective monitoring solution utilizing:

ESP32 microcontroller
Current sensing hardware
Python-based desktop application
Open-source visualization tools


2. System Requirements
Functional Requirements
Requirement ID	DescriptionFR-001	Acquire current sensor data from ESP32
FR-002	Support serial communication
FR-003	Display real-time current values
FR-004	Plot live trend graphs
FR-005	Save collected data to CSV
FR-006	Support multiple current channels
FR-007	Permit user COM port selection
FR-008	Operate without hardware using simulator mode
Non-Functional Requirements
Requirement ID	DescriptionNFR-001	Update every 200 ms
NFR-002	Responsive user interface
NFR-003	Portable to multiple Windows systems
NFR-004	Use open-source software libraries
NFR-005	Automatic periodic data saving


3. System Architecture
Hardware Components
ESP32

Responsibilities:

Read current sensor values
Generate timestamps
Transmit measurements via serial communication
Current Sensors

Responsibilities:

Sense current flowing through monitored circuits
Convert measured values into analog signals
Host Computer

Responsibilities:

Receive serial data
Display measurements
Store historical data
Software Components
Data Acquisition Layer

Responsibilities:

Read serial input
Validate incoming records
Parse timestamps
Convert strings to floating-point values
Visualization Layer

Implemented using:

PyQt5
PyQtGraph

Responsibilities:

Real-time plotting
User interaction
Display system status
Storage Layer

Implemented using:

Pandas

Responsibilities:

Store measurements
Export CSV files
Periodic backups


4. Design Decisions
Why ESP32?

Reasons:

Low cost
Built-in USB communication
High sampling capability
Large community support
Why Python?

Reasons:

Rapid development
Excellent visualization libraries
Easy serial integration
Strong data-analysis ecosystem
Why PyQtGraph?

Reasons:

High-performance plotting
Better real-time rendering than Matplotlib
Native Qt integration
Why CSV Storage?

Reasons:

Human-readable
Excel-compatible
Lightweight
Easy import into analysis tools


5. Development Process
Initial Prototype

Features:

Single current channel
Fixed COM port
Basic terminal output

Issues Discovered:

Required code modifications when COM port changed
Difficult usability for non-technical users
GUI Development

Features Added:

Graphical interface
Save button
Real-time plotting

Challenges:

Plot update timing
Window responsiveness
Data synchronization
Simulator Mode Development

Purpose:

Allow testing without hardware.

Features:

Randomized current values
Real-time graph generation
CSV logging

Benefits:

Software debugging without ESP32
Easier demonstration during development
COM Port Selection Enhancement

Original Design:

Python
SERIAL_PORT = "COM3"

Problem:

Port assignments varied between computers.

Solution Implemented:

COM Port dropdown
Refresh Ports button
Connect button
Connection status indicator

Benefit:

Improved usability and portability.

6. Test Plan
Test Case 1: GUI Launch

Objective:

Verify application starts correctly.

Procedure:

Launch application
Observe interface

Expected Result:

GUI opens with no errors.

Result:

PASS

Test Case 2: Simulator Mode

Objective:

Verify operation without hardware.

Procedure:

Enable simulator mode
Launch application

Expected Result:

Random data generated.

Result:

PASS

Test Case 3: Serial Connection

Objective:

Verify ESP32 communication.

Procedure:

Connect ESP32
Refresh COM ports
Select port
Press Connect

Expected Result:

Connection established.

Result:

PASS

Test Case 4: Real-Time Plotting

Objective:

Verify graph updates.

Procedure:

Stream live data
Observe graph behavior

Expected Result:

Continuous updates every 200 ms.

Result:

PASS

Test Case 5: CSV Export

Objective:

Verify data persistence.

Procedure:

Collect sensor data
Select Save CSV

Expected Result:

CSV file generated.

Result:

PASS

Test Case 6: Data Integrity

Objective:

Verify received values match transmitted values.

Procedure:

Compare ESP32 serial output with CSV records

Expected Result:

Values match.

Result:

PASS

7. Defects Encountered and Resolutions
Issue 1

Problem:

Serial connection failed when COM port assignment changed.

Root Cause:

Hardcoded COM port.

Resolution:

Implemented dropdown port selection.

Status:

Resolved

Issue 2

Problem:

Application crashed when malformed serial data arrived.

Root Cause:

Unexpected packet format.

Resolution:

Added validation checks:

Python
if len(parts) != 3:
return

Status:

Resolved

Issue 3

Problem:

Software testing required hardware availability.

Root Cause:

ESP32 dependency.

Resolution:

Implemented simulator mode.

Status:

Resolved

8. Performance Evaluation
Data Acquisition Rate

Measured update interval:

200 ms

Approximate refresh rate:

5 updates/second

Status:

Acceptable

Memory Management

Optimization implemented:

Python
self.x = self.x[-500:]
self.y1 = self.y1[-500:]
self.y2 = self.y2[-500:]

Benefit:

Controlled memory growth.

9. Lessons Learned

The project demonstrated the integration of embedded hardware and desktop software into a unified monitoring solution.

Key lessons included:

Serial communication reliability
Real-time visualization techniques
GUI design principles
Data acquisition architecture
Error handling strategies
System testing methodologies

10. Future Improvements

Planned enhancements include:

Automatic ESP32 detection
Database storage
Alarm notifications
Historical trend analysis
PDF report generation
Cloud synchronization
Multi-device support
User authentication
Web dashboard

11. Conclusion

CurrentTracker successfully met the project objectives by providing a cost-effective and flexible current monitoring platform capable of acquiring, visualizing, and storing real-time electrical measurements from an ESP32-based sensing system.

The final system demonstrates concepts from software engineering, embedded systems, data acquisition, visualization, testing, and system integration while providing a foundation for future expansion.