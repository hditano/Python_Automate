from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Test")
        
        button = QPushButton("Press me")
        label = QLabel("Testing")
        
        self.setCentralWidget(button, label)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()