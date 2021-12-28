from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DuckDuckGo PDF Downloader')
        self.layout = QVBoxLayout()
        self.resize(500, 500)
        self.show()