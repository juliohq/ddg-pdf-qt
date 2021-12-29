import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from qt.window import Window

app = QApplication([])
window = Window()

class Worker(QObject):
    def run(self):
        pass

worker = Worker()
thread = QThread()
thread.started.connect(worker.run)
worker.moveToThread(thread)

sys.exit(app.exec())