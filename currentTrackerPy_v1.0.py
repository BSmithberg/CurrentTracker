import sys
import time
import random
import serial
import pandas as pd
import pyqtgraph as pg

from serial.tools import list_ports

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QComboBox
)

BAUD_RATE = 115200
SIMULATOR_MODE = True

ser = None

data = {
    "Timestamp": [],
    "Current1_A": [],
    "Current2_A": []
}


class RealTimePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ESP32 Current Sensor Visualization")
        self.setGeometry(100, 100, 900, 600)

        # -----------------------------
        # GRAPH
        # -----------------------------
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground("w")
        self.graphWidget.setTitle("Real-Time Current Sensor Data")

        self.graphWidget.setLabel(
            "left",
            "Current (A)"
        )

        self.graphWidget.setLabel(
            "bottom",
            "Timestamp"
        )

        # -----------------------------
        # COM PORT CONTROLS
        # -----------------------------
        self.portLabel = QLabel("COM Port:")

        self.portCombo = QComboBox()

        self.refreshButton = QPushButton(
            "Refresh Ports"
        )
        self.refreshButton.clicked.connect(
            self.load_ports
        )

        self.connectButton = QPushButton(
            "Connect"
        )
        self.connectButton.clicked.connect(
            self.connect_port
        )

        self.disconnectButton = QPushButton(
            "Disconnect"
        )
        self.disconnectButton.clicked.connect(
            self.disconnect_port
        )

        self.connectionLabel = QLabel(
            "Status: Not Connected"
        )

        self.load_ports()

        # -----------------------------
        # SAVE BUTTON
        # -----------------------------
        self.saveButton = QPushButton(
            "Save CSV"
        )

        self.saveButton.clicked.connect(
            self.save_csv
        )

        # -----------------------------
        # LAYOUTS
        # -----------------------------
        controlLayout = QHBoxLayout()

        controlLayout.addWidget(
            self.portLabel
        )

        controlLayout.addWidget(
            self.portCombo
        )

        controlLayout.addWidget(
            self.refreshButton
        )

        controlLayout.addWidget(
            self.connectButton
        )

        controlLayout.addWidget(
            self.disconnectButton
        )

        controlLayout.addWidget(
            self.connectionLabel
        )

        layout = QVBoxLayout()

        layout.addLayout(
            controlLayout
        )

        layout.addWidget(
            self.graphWidget
        )

        layout.addWidget(
            self.saveButton
        )

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # -----------------------------
        # PLOT DATA
        # -----------------------------
        self.x = []
        self.y1 = []
        self.y2 = []

        self.plot1 = self.graphWidget.plot(
            self.x,
            self.y1,
            pen=pg.mkPen("r", width=2),
            name="Current 1"
        )

        self.plot2 = self.graphWidget.plot(
            self.x,
            self.y2,
            pen=pg.mkPen("b", width=2),
            name="Current 2"
        )

        # -----------------------------
        # UPDATE TIMER
        # -----------------------------
        self.timer = pg.QtCore.QTimer()

        self.timer.timeout.connect(
            self.update_plot
        )

        self.timer.start(200)

        # -----------------------------
        # AUTO SAVE EVERY MINUTE
        # -----------------------------
        self.save_timer = pg.QtCore.QTimer()

        self.save_timer.timeout.connect(
            self.save_csv
        )

        self.save_timer.start(60000)

    # ---------------------------------
    # LOAD COM PORTS
    # ---------------------------------
    def load_ports(self):
        self.portCombo.clear()

        ports = list(list_ports.comports())

        if not ports:
            self.portCombo.addItem(
                "No Ports Found"
            )
            return

        for port in ports:
            self.portCombo.addItem(
                f"{port.device} - {port.description}"
            )

    # ---------------------------------
    # CONNECT TO SELECTED PORT
    # ---------------------------------
    def connect_port(self):
        global ser

        try:
            selected_text = (
                self.portCombo.currentText()
            )

            if selected_text == "No Ports Found":
                self.connectionLabel.setText(
                    "Status: No Ports Found"
                )
                return

            selected_port = (
                selected_text.split(" - ")[0]
            )

            if ser is not None:
                if ser.is_open:
                    ser.close()

            ser = serial.Serial(
                selected_port,
                BAUD_RATE,
                timeout=1
            )

            self.connectionLabel.setText(
                f"Status: Connected ({selected_port})"
            )

            print(
                f"Connected to {selected_port}"
            )

        except Exception as e:
            self.connectionLabel.setText(
                "Status: Connection Failed"
            )

            print(
                f"Connection Error: {e}"
            )

    # ---------------------------------
    # DISCONNECT PORT
    # ---------------------------------
    def disconnect_port(self):
        global ser

        try:

            if ser is not None:

                if ser.is_open:

                    port_name = ser.port

                    ser.close()

                    print(
                        f"Disconnected from {port_name}"
                    )

            ser = None

            self.connectionLabel.setText(
                "Status: Simulator Mode"
            )

        except Exception as e:

            print(
                f"Disconnect Error: {e}"
            )

            self.connectionLabel.setText(
                "Status: Disconnect Failed"
            )

    # ---------------------------------
    # UPDATE PLOT
    # ---------------------------------
    def update_plot(self):
        global ser

        try:

            # -----------------------------
            # HARDWARE CONNECTED
            # -----------------------------
            if (
                ser is not None
                and ser.is_open
            ):

                self.connectionLabel.setText(
                    f"Status: Connected ({ser.port})"
             )

                if ser.in_waiting > 0:

                    line = (
                        ser.readline()
                        .decode(errors="ignore")
                        .strip()
                    )

                    if line:

                        parts = line.split(",")

                        if len(parts) == 3:

                            timestamp, current1, current2 = map(
                                float,
                                parts
                            )

                            self.x.append(timestamp)
                            self.y1.append(current1)
                            self.y2.append(current2)

                # KEEP THE PLOT ALIVE
                # even if no new serial data
                self.plot1.setData(
                    self.x[-500:],
                    self.y1[-500:]
                )

                self.plot2.setData(
                    self.x[-500:],
                    self.y2[-500:]
                )

                return

            # -----------------------------
            # SIMULATOR MODE
            # -----------------------------
            if SIMULATOR_MODE:

                self.connectionLabel.setText(
                    "Status: Simulator Mode"
                )

                timestamp = time.time() * 1000

                current1 = random.uniform(
                    0.0,
                    10.0
                )

                current2 = random.uniform(
                    0.0,
                    10.0
                )

                self.x.append(timestamp)
                self.y1.append(current1)
                self.y2.append(current2)

                self.x = self.x[-500:]
                self.y1 = self.y1[-500:]
                self.y2 = self.y2[-500:]

                self.plot1.setData(
                    self.x,
                    self.y1
                )

                self.plot2.setData(
                    self.x,
                    self.y2
                )

                data["Timestamp"].append(
                    timestamp
                )

                data["Current1_A"].append(
                    current1
                )

                data["Current2_A"].append(
                    current2
                )

        except Exception as e:

            print(
                f"Error: {e}"
            )


    # ---------------------------------
    # SAVE CSV
    # ---------------------------------
    def save_csv(self):
        try:
            import os

            csv_path = os.path.join(
                os.path.expanduser("~"),
                "Documents",
                "current_sensor_data.csv"
            )

            df = pd.DataFrame(data)

            df.to_csv(
                csv_path,
                index=False
            )

            print(
                f"Data saved to {csv_path}"
            )

        except Exception as e:
            print(
                f"CSV Save Error: {e}"
            )

    # ---------------------------------
    # SAFE APPLICATION SHUTDOWN
    # ---------------------------------
    def closeEvent(self, event):
        global ser

        try:

            if (
                ser is not None
                and ser.is_open
            ):
                ser.close()

                print(
                    "Serial port closed."
                )

        except Exception as e:

            print(
                f"Shutdown Error: {e}"
            )

        event.accept()


app = QApplication(sys.argv)

window = RealTimePlot()
window.show()

sys.exit(app.exec_())