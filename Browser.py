from typing import Sized
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.browser.setZoomFactor(self.browser.zoomFactor() + 1.0)

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        back_btn = QAction('<--', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #Forward Button
        for_btn = QAction('-->', self)
        for_btn.triggered.connect(self.browser.forward)
        navbar.addAction(for_btn)

        #Refresh
        ref_btn = QAction('</>', self)
        ref_btn.triggered.connect(self.browser.reload)
        navbar.addAction(ref_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_home)
        navbar.addWidget(self.url_bar)
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
app = QApplication(sys.argv)
QApplication.setApplicationName('Garg Browser')
window = MainWindow()
app.exec_()
