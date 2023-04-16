from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from widgets import RegistrationForm

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Hello word!")
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        
        window_menu = menu_bar.addMenu("Window")
        settings_menu = menu_bar.addMenu("Settings")
        help_menu = menu_bar.addMenu("Help")
        
        toolbar = QToolBar("My toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        toolbar.addAction(quit_action)
        
        action1 = QAction("Some action", self)
        action1.setStatusTip("Just some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon('res/icon.png'), "Some action with icon", self)
        action2.setStatusTip("Just some action with icon")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        toolbar.addSeparator()
        
        self.setCentralWidget(RegistrationForm())
        
    def quit_app(self):
        self.app.quit()
        
    def toolbar_button_click(self):
        self.statusBar().showMessage("Good job", 3000)
        """
        message = QMessageBox()
        message.setMinimumSize(500, 500)
        message.setWindowTitle("YOOOOOOO")
        message.setText("What are you doing")
        message.setInformativeText("Do you seriously think you can just press me?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")
        """
        
        ret = QMessageBox.critical(self, "Error", "Something went wrong", QMessageBox.Ok | QMessageBox.Cancel)
        
        if ret == QMessageBox.Ok:
            print("ok")
        else:
            print("Not ok")
        
        
    