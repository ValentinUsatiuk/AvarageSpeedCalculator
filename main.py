import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.metric = QComboBox()
        self.metric.addItems(["Metric(km)", "Imperial(miles)"])

        time_label = QLabel("Time(hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate speed")
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.metric, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance/time

        if self.metric.currentText() == "Metric(km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.metric.currentText() == "Imperial(miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.output_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
