from PySide6.QtWidgets import QApplication
from widgets import ButtonPanel
from mainwindow import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.setFixedSize(1000, 700)
window.show()

app.exec()