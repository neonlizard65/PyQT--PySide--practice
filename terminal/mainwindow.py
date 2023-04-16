from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDateTimeEdit, QPushButton, QListView
from login import LoginWidget
from windowmanager import WindowManager


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Хранитель ПРО")
        self.setCentralWidget(LoginWidget(self))
        WindowManager.window = self
        
