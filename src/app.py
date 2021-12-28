import sys
from PyQt5.QtWidgets import QApplication
from qt.window import Window

app = QApplication([])
window = Window()
sys.exit(app.exec())