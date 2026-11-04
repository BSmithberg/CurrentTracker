CurrentTracker

Real-Time Electrical Current Monitoring and Analysis System
MSSE Capstone Project
CurrentTracker is a real-time electrical current monitoring and data acquisition platform developed as part of the Master of Science in Software Engineering (MSSE) Capstone Project.

The system combines embedded hardware, serial communications, desktop application development, real-time visualization, and data storage into a unified solution for monitoring electrical current measurements. CurrentTracker enables users to collect, visualize, analyze, and export electrical current data using an ESP32-based sensing platform and a Python desktop application.

Project Overview:

CurrentTracker was designed to provide a cost-effective, extensible, and user-friendly alternative to expensive industrial current monitoring solutions.

The platform enables users to:

Monitor electrical current measurements in real time
Visualize multiple current channels through live graphing
Record operational data for later analysis
Export measurements to CSV format
Operate with physical hardware or in simulator mode
Monitor system behavior through an intuitive graphical interface
The project demonstrates the integration of embedded systems, software engineering, data acquisition, visualization, and testing methodologies.

Problem Statement:

Many current monitoring systems rely on costly proprietary hardware and software solutions that are not accessible for educational, laboratory, research, or small-scale engineering environments.

The objective of CurrentTracker is to provide an affordable and flexible monitoring platform utilizing:

ESP32 microcontroller hardware
Electrical current sensors
USB serial communication
Python-based desktop software
Open-source visualization libraries
The resulting solution allows users to collect and analyze electrical measurements without requiring specialized industrial platforms.

System Architecture:

CurrentTracker follows a layered architecture that separates acquisition, communication, processing, visualization, and storage responsibilities.

Current Sensors
        │
        ▼
ESP32 Controller
        │
        ▼
Communication Layer
(PySerial)
        │
        ▼
Data Acquisition Layer
        │
        ▼
Processing Layer
        │
 ┌──────┴──────┐
 ▼             ▼
Visualization   Storage
(PyQtGraph)    (Pandas)
        │
        ▼
CSV Export
Additional architecture details are documented in:

System_Architecture.md

System Components:

Current Sensors
Responsibilities:

Measure electrical current
Convert current to analyzable signals
Provide data input to the ESP32 controller

ESP32 Controller:

Responsibilities:
Read sensor measurements
Generate timestamps
Format serial data packets
Transmit data through USB serial communication
Example packet:

1000,4.32,3.98
Format:

Timestamp, Current1, Current2

Communication Layer:
Technology:

PySerial
Capabilities:

COM port discovery
User-selectable connections
Serial communication management
Device connection monitoring

Data Acquisition Layer:
Responsibilities:

Receive incoming serial data
Validate packet format
Parse measurement values
Forward validated data for processing]

Processing Layer
Responsibilities:

Convert incoming data into usable formats
Maintain historical measurements
Provide data to visualization and storage systems
Example structure:

data = {
    "Timestamp": [],
    "Current1_A": [],
    "Current2_A": []
}

Visualization Layer
Technologies:

PyQt5
PyQtGraph
Capabilities:

Real-time plotting
Live current monitoring
Status display
User interaction

Storage Layer
Technology:

Pandas
Capabilities:

Structured data storage
CSV export
Automatic data persistence

Key Features:
Real-time electrical current monitoring
Dual-channel current acquisition
Live graphical visualization
Dynamic COM port discovery
User-selectable serial connections
Automatic CSV export
Periodic automatic data saving
Simulator mode for hardware-free testing
Connection status monitoring
Fault-tolerant communication handling
Portable Windows deployment

User Interface Features:
The CurrentTracker interface includes:

COM Port Selection
Refresh Ports Button
Connect Button
Disconnect Button
Connection Status Display
Real-Time Trend Graph
Save CSV Button
The interface was designed to provide intuitive operation for both technical and non-technical users.

Technology Stack:
Programming Language
Python
Libraries
PyQt5
PyQtGraph
PySerial
Pandas
Hardware
ESP32 Microcontroller
Electrical Current Sensors
Development Tools
Git
GitHub
Inno Setup

Performance Characteristics:
Metric	Value
Serial Baud Rate	115200
Update Interval	200 ms
Refresh Rate	5 Updates/Second
Current Channels	2
Data Storage Format	CSV
Auto Save Interval	60 Seconds
Plot History Window	500 Samples

Simulator Mode:
CurrentTracker includes a built-in simulator mode that generates synthetic current measurements when physical hardware is unavailable.

Benefits include:

Development without ESP32 hardware
Software testing on any workstation
Demonstration capability without connected devices
Improved validation and debugging
Reduced hardware dependency
Simulator mode was instrumental in supporting continuous development and testing throughout the project lifecycle.

Requirements:
Functional Requirements
ID	Requirement
FR-001	Acquire current sensor data from ESP32
FR-002	Support serial communication
FR-003	Display real-time current values
FR-004	Plot live trend graphs
FR-005	Save collected data to CSV
FR-006	Support multiple current channels
FR-007	Permit user COM port selection
FR-008	Operate without hardware using simulator mode
Non-Functional Requirements
ID	Requirement
NFR-001	Update every 200 ms
NFR-002	Responsive user interface
NFR-003	Portable across Windows systems
NFR-004	Utilize open-source software
NFR-005	Automatic periodic data saving

Installation:
Clone Repository
git clone https://github.com/yourusername/CurrentTracker.git
cd CurrentTracker
Install Dependencies
pip install -r requirements.txt
Launch Application
python currentTrackerPy_v1.0.py
Repository Structure
CurrentTracker/
│
├── currentTrackerPy_v1.0.py
├── README.md
├── requirements.txt
├── System_Architecture.md
├── Design_and_Testing.md
├── Drivers/
├── install.bat
├── setup_script.iss
├── build/
├── dist/
└── currentTrackerPy_v1.0_backup/

Testing and Validation:
Testing covered:

GUI startup validation
Simulator mode functionality
Serial communication reliability
Real-time plotting performance
Data export verification
Data integrity validation
Test Summary
Test Case	Status
GUI Launch	PASS
Simulator Mode	PASS
Serial Communication	PASS
Real-Time Plotting	PASS
CSV Export	PASS
Data Integrity Validation	PASS
Pass Rate: 100%

Detailed testing documentation is available in:

Design_and_Testing.md

Requirements Verification Matrix:
Requirement	Verification Method	Status
FR-001	Serial Communication Test	Pass
FR-002	Serial Communication Test	Pass
FR-003	Real-Time Plot Test	Pass
FR-004	Real-Time Plot Test	Pass
FR-005	CSV Export Test	Pass
FR-006	Multi-Channel Plot Test	Pass
FR-007	COM Port Selection Test	Pass
FR-008	Simulator Mode Test	Pass

Engineering Challenges and Solutions:
COM Port Variability
Problem: Different systems assigned varying COM port numbers.

Solution: Implemented dynamic COM port discovery with manual selection.

Malformed Serial Data
Problem: Unexpected serial packets could cause parsing failures.

Solution: Implemented packet validation checks before processing.

Hardware Dependency
Problem: Software development required connected hardware.

Solution: Implemented simulator mode for development and testing.

Software Engineering Principles Applied
The project incorporates:

Layered Architecture
Modular Design
Separation of Concerns
Fault Tolerance
Maintainability
Scalability
User-Centered Design
Testability
Hardware/Software Integration
Future Enhancements

Planned improvements include:

Automatic ESP32 detection
SQLite database integration
Multi-device monitoring
Configurable alarm thresholds
Historical trend analysis
PDF report generation
Cloud synchronization
REST API integration
Authentication and user management
Web-based dashboard support

Capstone Deliverables:
This repository contains the primary artifacts required for the MSSE Capstone Project:

Source Code
System Architecture Documentation
Design Documentation
Testing Documentation
Deployment Assets
Requirements Traceability
Version Control History

CurrentTracker
Real-Time Electrical Current Monitoring and Analysis System
MSSE Capstone Project
CurrentTracker is a real-time electrical current monitoring and data acquisition platform developed as part of the Master of Science in Software Engineering (MSSE) Capstone Project.

The system combines embedded hardware, serial communications, desktop application development, real-time visualization, and data storage into a unified solution for monitoring electrical current measurements. CurrentTracker enables users to collect, visualize, analyze, and export electrical current data using an ESP32-based sensing platform and a Python desktop application.

Project Overview
CurrentTracker was designed to provide a cost-effective, extensible, and user-friendly alternative to expensive industrial current monitoring solutions.

The platform enables users to:

Monitor electrical current measurements in real time
Visualize multiple current channels through live graphing
Record operational data for later analysis
Export measurements to CSV format
Operate with physical hardware or in simulator mode
Monitor system behavior through an intuitive graphical interface
The project demonstrates the integration of embedded systems, software engineering, data acquisition, visualization, and testing methodologies.

Problem Statement
Many current monitoring systems rely on costly proprietary hardware and software solutions that are not accessible for educational, laboratory, research, or small-scale engineering environments.

The objective of CurrentTracker is to provide an affordable and flexible monitoring platform utilizing:

ESP32 microcontroller hardware
Electrical current sensors
USB serial communication
Python-based desktop software
Open-source visualization libraries
The resulting solution allows users to collect and analyze electrical measurements without requiring specialized industrial platforms.

System Architecture
CurrentTracker follows a layered architecture that separates acquisition, communication, processing, visualization, and storage responsibilities.

Current Sensors
        │
        ▼
ESP32 Controller
        │
        ▼
Communication Layer
(PySerial)
        │
        ▼
Data Acquisition Layer
        │
        ▼
Processing Layer
        │
 ┌──────┴──────┐
 ▼             ▼
Visualization   Storage
(PyQtGraph)    (Pandas)
        │
        ▼
CSV Export
Additional architecture details are documented in:

System_Architecture.md
System Components
Current Sensors
Responsibilities:

Measure electrical current
Convert current to analyzable signals
Provide data input to the ESP32 controller
ESP32 Controller
Responsibilities:

Read sensor measurements
Generate timestamps
Format serial data packets
Transmit data through USB serial communication
Example packet:

1000,4.32,3.98
Format:

Timestamp, Current1, Current2
Communication Layer
Technology:

PySerial
Capabilities:

COM port discovery
User-selectable connections
Serial communication management
Device connection monitoring
Data Acquisition Layer
Responsibilities:

Receive incoming serial data
Validate packet format
Parse measurement values
Forward validated data for processing
Processing Layer
Responsibilities:

Convert incoming data into usable formats
Maintain historical measurements
Provide data to visualization and storage systems
Example structure:

data = {
    "Timestamp": [],
    "Current1_A": [],
    "Current2_A": []
}
Visualization Layer
Technologies:

PyQt5
PyQtGraph
Capabilities:

Real-time plotting
Live current monitoring
Status display
User interaction
Storage Layer
Technology:

Pandas
Capabilities:

Structured data storage
CSV export
Automatic data persistence
Key Features
Real-time electrical current monitoring
Dual-channel current acquisition
Live graphical visualization
Dynamic COM port discovery
User-selectable serial connections
Automatic CSV export
Periodic automatic data saving
Simulator mode for hardware-free testing
Connection status monitoring
Fault-tolerant communication handling
Portable Windows deployment
User Interface Features
The CurrentTracker interface includes:

COM Port Selection
Refresh Ports Button
Connect Button
Disconnect Button
Connection Status Display
Real-Time Trend Graph
Save CSV Button
The interface was designed to provide intuitive operation for both technical and non-technical users.

Technology Stack
Programming Language
Python
Libraries
PyQt5
PyQtGraph
PySerial
Pandas
Hardware
ESP32 Microcontroller
Electrical Current Sensors
Development Tools
Git
GitHub
Inno Setup
Performance Characteristics
Metric	Value
Serial Baud Rate	115200
Update Interval	200 ms
Refresh Rate	5 Updates/Second
Current Channels	2
Data Storage Format	CSV
Auto Save Interval	60 Seconds
Plot History Window	500 Samples
Simulator Mode
CurrentTracker includes a built-in simulator mode that generates synthetic current measurements when physical hardware is unavailable.

Benefits include:

Development without ESP32 hardware
Software testing on any workstation
Demonstration capability without connected devices
Improved validation and debugging
Reduced hardware dependency
Simulator mode was instrumental in supporting continuous development and testing throughout the project lifecycle.

Requirements
Functional Requirements
ID	Requirement
FR-001	Acquire current sensor data from ESP32
FR-002	Support serial communication
FR-003	Display real-time current values
FR-004	Plot live trend graphs
FR-005	Save collected data to CSV
FR-006	Support multiple current channels
FR-007	Permit user COM port selection
FR-008	Operate without hardware using simulator mode
Non-Functional Requirements
ID	Requirement
NFR-001	Update every 200 ms
NFR-002	Responsive user interface
NFR-003	Portable across Windows systems
NFR-004	Utilize open-source software
NFR-005	Automatic periodic data saving
Installation
Clone Repository
git clone https://github.com/yourusername/CurrentTracker.git
cd CurrentTracker
Install Dependencies
pip install -r requirements.txt
Launch Application
python currentTrackerPy_v1.0.py
Repository Structure
CurrentTracker/
│
├── currentTrackerPy_v1.0.py
├── README.md
├── requirements.txt
├── System_Architecture.md
├── Design_and_Testing.md
├── Drivers/
├── install.bat
├── setup_script.iss
├── build/
├── dist/
└── currentTrackerPy_v1.0_backup/
Testing and Validation
Testing covered:

GUI startup validation
Simulator mode functionality
Serial communication reliability
Real-time plotting performance
Data export verification
Data integrity validation
Test Summary
Test Case	Status
GUI Launch	PASS
Simulator Mode	PASS
Serial Communication	PASS
Real-Time Plotting	PASS
CSV Export	PASS
Data Integrity Validation	PASS
Pass Rate: 100%

Detailed testing documentation is available in:

Design_and_Testing.md
Requirements Verification Matrix
Requirement	Verification Method	Status
FR-001	Serial Communication Test	Pass
FR-002	Serial Communication Test	Pass
FR-003	Real-Time Plot Test	Pass
FR-004	Real-Time Plot Test	Pass
FR-005	CSV Export Test	Pass
FR-006	Multi-Channel Plot Test	Pass
FR-007	COM Port Selection Test	Pass
FR-008	Simulator Mode Test	Pass
Engineering Challenges and Solutions
COM Port Variability
Problem: Different systems assigned varying COM port numbers.

Solution: Implemented dynamic COM port discovery with manual selection.

Malformed Serial Data
Problem: Unexpected serial packets could cause parsing failures.

Solution: Implemented packet validation checks before processing.

Hardware Dependency
Problem: Software development required connected hardware.

Solution: Implemented simulator mode for development and testing.

Software Engineering Principles Applied
The project incorporates:

Layered Architecture
Modular Design
Separation of Concerns
Fault Tolerance
Maintainability
Scalability
User-Centered Design
Testability
Hardware/Software Integration
Future Enhancements
Planned improvements include:

Automatic ESP32 detection
SQLite database integration
Multi-device monitoring
Configurable alarm thresholds
Historical trend analysis
PDF report generation
Cloud synchronization
REST API integration
Authentication and user management
Web-based dashboard support

Capstone Deliverables
This repository contains the primary artifacts required for the MSSE Capstone Project:

Source Code
System Architecture Documentation
Design Documentation
Testing Documentation
Deployment Assets
Requirements Traceability
Version Control History

Screenshots:

Main Dashboard
Simulator Mode
Sprint 1
Sprint 2
Sprint 3
Sprints_for_Capstone

License and Legal Notice
Copyright © Brian Smithberger.

All original software, documentation, system designs, and project-specific intellectual property contained within this repository remain the property of Brian Smithberger unless otherwise stated.

Third-party libraries and frameworks remain subject to their respective licenses, including but not limited to:

Python
PyQt5
PyQtGraph
PySerial
Pandas
This software is provided "as is" without warranty of any kind. Users assume all responsibility for installation, configuration, deployment, and operation of the software.