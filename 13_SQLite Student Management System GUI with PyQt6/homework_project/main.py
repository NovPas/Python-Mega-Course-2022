import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, \
    QGridLayout, QLineEdit, QComboBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")

        # Create the main widget and layout
        main_widget = QWidget()
        grid = QGridLayout()
        main_widget.setLayout(grid)

        # Create the input fields
        self.distance_field = QLineEdit()
        self.metric_field = QComboBox()
        self.metric_field.addItems(["km", "miles"])
        self.time_field = QLineEdit()

        # Create the result label
        self.result_label = QLabel()

        # Create the calculate button
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_average_speed)

        # Add the input fields, button, and result label to the layout
        grid.addWidget(QLabel("Distance:"), 0, 0)
        grid.addWidget(self.distance_field, 0, 1)
        grid.addWidget(self.metric_field, 0, 2)
        grid.addWidget(QLabel("Time (hours):"), 1, 0)
        grid.addWidget(self.time_field, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.result_label, 3, 0, 1, 3)

        # Set the main widget
        self.setCentralWidget(main_widget)

    def calculate_average_speed(self):
        distance = float(self.distance_field.text())
        metric = self.metric_field.currentText()
        time = float(self.time_field.text())
        average_speed = distance / time
        self.result_label.setText(f"Average speed: {average_speed:.2f} {metric}/h")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
