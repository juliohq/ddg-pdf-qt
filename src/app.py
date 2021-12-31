import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from qt.window import Window
from worker import Worker

app = QApplication([])
window = Window()

worker = Worker()
# connect signals
window.clicked_search.connect(worker.search)
window.clicked_download.connect(worker.download)
window.clicked_quick.connect(worker.quick_download)

# set up worker thread
thread = QThread()
thread.started.connect(worker.run)
worker.moveToThread(thread)
thread.start()

sys.exit(app.exec())