from PySide6.QtWidgets import QWidget, QToolBar, QPushButton, QStatusBar, QMessageBox, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QSizePolicy


class ButtonPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OOF")
        
        button1 = QPushButton("Btn1")
        button1.clicked.connect(self.btn1_clicked)
        button2 = QPushButton("Btn2")
        button1.clicked.connect(self.btn2_clicked)
    
        widget_layout = QHBoxLayout()
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)
    
    
    def btn1_clicked(self):
        pass
    
    def btn2_clicked(self):
        pass
    
class RegistrationForm(QWidget):
    
        def __init__(self):
            super().__init__()
    
            label = QLabel("Full name: ")
            self.line_edit = QLineEdit()
            self.line_edit.textChanged.connect(self.line_text_changed)
            
            
            button = QPushButton("Get data")
            button.setFixedSize(100, 20)
            button.clicked.connect(self.button_clicked)
            
            self.label2 = QLabel("Live updated text")
            self.text_holder_label = QLabel("Data will be here")
            
            
            h_layout = QHBoxLayout()
            h_layout.addWidget(label)
            h_layout.addWidget(self.line_edit)
            
            v_layout = QVBoxLayout()
            v_layout.addLayout(h_layout)
            v_layout.addWidget(button)
            v_layout.addWidget(self.label2)
            v_layout.addWidget(self.text_holder_label)
            
            self.setLayout(v_layout)
            
        def button_clicked(self):
            self.text_holder_label.setText(self.line_edit.text())
        
        def line_text_changed(self):
            self.label2.setText(self.line_edit.text())