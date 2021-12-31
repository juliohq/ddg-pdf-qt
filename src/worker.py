from PyQt5.QtCore import QObject, pyqtSignal
from ddgpdf.src.search import Search

class Worker(QObject):
    def search(self):
        pass
    
    def download(self):
        pass
    
    def quick_download(self, search_str):
        pass
    
    def run(self):
        pass