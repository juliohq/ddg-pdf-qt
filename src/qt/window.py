from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QApplication,
    QLineEdit,
)
from PyQt5.QtCore import pyqtSignal

class Window(QMainWindow):
    clicked_search = pyqtSignal(str) # search
    clicked_download = pyqtSignal()
    changed_output = pyqtSignal(str) # path
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DuckDuckGo PDF Downloader')
        self.resize(800, 600)
        self.setup_ui()
    
    def about(self):
        app = QApplication.instance()
        app.aboutQt()
    
    def setup_ui(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        
        # set up search
        self.search_group = QWidget()
        self.search_layout = QHBoxLayout(self.search_group)
        self.search = QLineEdit()
        self.search_button = QPushButton('Search')
        self.search_layout.addWidget(self.search)
        self.search_layout.addWidget(self.search_button)
        self.search.setPlaceholderText('Search here...')
        self.layout.addWidget(self.search_group)
        
        # set up button group (download, output folder, about, quit)
        self.button_group = QWidget()
        self.button_layout = QHBoxLayout(self.button_group)
        
        self.download_button = QPushButton('Download')
        self.button_layout.addWidget(self.download_button)
        self.output_button = QPushButton('Choose output folder...')
        self.button_layout.addWidget(self.output_button)
        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.about)
        self.button_layout.addWidget(self.about_button)
        self.quit_button = QPushButton('Quit')
        self.button_layout.addWidget(self.quit_button)
        
        self.layout.addWidget(self.button_group)
        
        self.centralWidget.setLayout(self.layout)
        self.show()