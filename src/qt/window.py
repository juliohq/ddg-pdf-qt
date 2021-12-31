import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    clicked_search = pyqtSignal(str) # search
    clicked_download = pyqtSignal()
    changed_output = pyqtSignal(str) # path
    clicked_quick = pyqtSignal(str) # search
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DuckDuckGo PDF Downloader')
        self.resize(800, 600)
        self.setup_ui()
        self.changed_output.connect(self._on_changed_output)
    
    def _on_changed_output_text(self, path):
        enabled = True if path and os.path.isdir(path) else False
        self.download_button.setEnabled(enabled)
        self.quick_button.setEnabled(enabled)
    
    def _on_changed_output(self, path):
        self.output.setText(path)
    
    def choose_output(self):
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.fileSelected.connect(lambda path: self.changed_output.emit(path))
        dialog.exec()
    
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
        # search line edit
        self.search = QLineEdit()
        self.search.setPlaceholderText('Search here...')
        self.search_layout.addWidget(self.search)
        # search button
        self.search_button = QPushButton('Search')
        self.search_layout.addWidget(self.search_button)
        # quick download button
        self.quick_button = QPushButton('Quick Download...')
        self.quick_button.clicked.connect(lambda: self.clicked_quick.emit(self.search.text()))
        self.quick_button.setEnabled(False)
        self.search_layout.addWidget(self.quick_button)
        # add search group
        self.layout.addWidget(self.search_group)
        
        # scroll area
        self.scroll_area = QScrollArea()
        self.scroll_layout = QVBoxLayout(self.scroll_area)
        self.layout.addWidget(self.scroll_area)
        # no search label
        self.search_label = QLabel('Please, search in the bar above to see results')
        self.search_label.setAlignment(Qt.AlignCenter)
        self.scroll_layout.addWidget(self.search_label)
        
        # set up button group (download, output folder, about, quit)
        self.button_group = QWidget()
        self.button_layout = QHBoxLayout(self.button_group)
        # download button
        self.download_button = QPushButton('Download')
        self.download_button.setEnabled(False)
        self.button_layout.addWidget(self.download_button)
        # output
        self.output = QLineEdit()
        self.output.setPlaceholderText = 'Enter a valid path...'
        self.button_layout.addWidget(self.output)
        self.output.textChanged.connect(self._on_changed_output_text)
        # output button
        self.output_button = QPushButton('Choose output folder...')
        self.button_layout.addWidget(self.output_button)
        self.output_button.clicked.connect(self.choose_output)
        # about button
        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.about)
        self.button_layout.addWidget(self.about_button)
        # quit button
        self.quit_button = QPushButton('Quit')
        self.button_layout.addWidget(self.quit_button)
        # add button group
        self.layout.addWidget(self.button_group)
        
        self.centralWidget.setLayout(self.layout)
        self.show()