from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys


app = QApplication(sys.argv)

window = MainWindow(app)
window.setGeometry(0, 0, 400, 250)
window.show()

app.exec()