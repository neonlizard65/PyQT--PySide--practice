from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDateTimeEdit,\
                              QPushButton, QListView, QLayout
from PySide6.QtCore import Qt
import requests
import json
from mainwidget import MainWidget
from windowmanager import WindowManager


class LoginWidget(QWidget):
    def __init__(self, mainwindow: QMainWindow):
        super().__init__()
        self.mainwindow = mainwindow
        
        page_layout = QVBoxLayout()
        page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        login_field = QHBoxLayout()
        login_field.setContentsMargins(5, 30, 5, 10)
        password_field = QHBoxLayout()
        password_field.setContentsMargins(5, 10, 5, 10)
        
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(5, 10, 5, 10)
        
        login_label = QLabel("Логин: ")
        self.login_edit = QLineEdit()
        
        password_label = QLabel("Пароль: ")        
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        login_field.addWidget(login_label)
        login_field.addWidget(self.login_edit)
        password_field.addWidget(password_label)
        password_field.addWidget(self.password_edit)
        
        submit_button = QPushButton("Войти")
        submit_button.setFixedWidth(175)
        submit_button.clicked.connect(self.submit_clicked)
        button_layout.addWidget(submit_button)
        
        page_layout.addLayout(login_field)
        page_layout.addLayout(password_field) 
        page_layout.addLayout(button_layout)
        
        self.setLayout(page_layout)
        
    def submit_clicked(self):
        employee_id = self.login_edit.text()
        employee_json = requests.get(f"http://127.0.0.1:5000/employee/{employee_id}")
        employee_info = json.loads(employee_json.content)
        if self.password_edit.text() == employee_info['password']:
            print("Успешная авторизация")
            WindowManager.window.setCentralWidget(MainWidget())
            
        else:
            print("Failed")
        
        