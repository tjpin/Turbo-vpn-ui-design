from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFrame, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import loadUiType
from PySide6.QtCore import Qt, QRunnable, QThreadPool, QSize
import time

from src.server_data import Servers
from widgets.list_item import CustomListItem


class Worker(QRunnable):
    def __init__(self, func) -> None:
        super().__init__()
        self.func = func
        
    def run(self, *args):
        for i in range(3):
            time.sleep(1)
        self.func(args)


ui, _ = loadUiType('ui/home.ui')

gs1 = """
    QPushButton {
        border: none;
        background-color: rgb(211, 104, 60);
        border-radius: 5px;
        color: #fff;
}

"""
gs2 = """
    QPushButton {
        border: none;
        background-color: #fff;
        border-radius: 5px;
        color: #000;
}

    QPushButton:hover {
        background-color: #fff3ea;
}
"""

trailing_styles = """
    QPushButton {
        background-color: qlineargradient(spread:pad, x1:0.544, y1:0.993955, x2:0.550986, y2:0, stop:0.352657 rgba(190, 176, 90, 255), stop:1 rgba(255, 251, 250, 255));
        border: none;
        color: #fff;
        border-radius: 3px;
        font-weight: bold;
        font-size: 13px;
    }
"""

trailing_free_styles = """
    QPushButton {
        background-color: #00000000;
        border: none;
        color: #fa7b47;
        border-radius: 3px;
        font-weight: bold;
        font-size: 13px;
    }
"""


class TurboMainWindow(QMainWindow, ui):
    def __init__(self):
        super(TurboMainWindow, self).__init__()
        self.dragPos = None
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.update_events()
        
    def update_events(self):
        self.topBar.mouseMoveEvent = self.moveWindow
        self.welcomeTopBar.mouseMoveEvent = self.moveWindow
        self.topBar.setCursor(Qt.CursorShape.SizeAllCursor)
        self.welcomeTopBar.setCursor(Qt.CursorShape.SizeAllCursor)
        self.globalBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.specialBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.connectBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.frame_4.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.globalBtn.clicked.connect(lambda: self.sideNav.setCurrentIndex(0))
        self.specialBtn.clicked.connect(lambda: self.sideNav.setCurrentIndex(1))
        self.specialBtn.clicked.connect(self.toggle_switch_a)
        self.globalBtn.clicked.connect(self.toggle_switch_b)
        self.closeBtn.clicked.connect(self.closeWindow)
        self.startCloseBtn.clicked.connect(self.closeWindow)
        self.startMiniBtn.clicked.connect(self.miniMize)
        self.miniBtn.clicked.connect(self.miniMize)
        self.homeBtn.clicked.connect(self.back_home)
        self.accBtn.clicked.connect(self.account_home)
        self.opener()
        self.add_optimal_location()
        self.list_global_servers()
        self.list_special_servers()
    
    def load_home(self, *args):
        self.rootScreen.setCurrentIndex(1)
    
    def opener(self):
        self.tr = QThreadPool()
        self.worker = Worker(self.load_home)
        self.tr.start(self.worker)
    
    def account_home(self):
        self.rootScreen.setCurrentIndex(2)
    
    def back_home(self):
        self.rootScreen.setCurrentIndex(1)
    
    def closeWindow(self):
        self.close()
        
    def miniMize(self):
        self.showMinimized()
    
    def list_global_servers(self):
        servers = Servers()
        text = "VIP"
        tr = trailing_styles       
        self.scrollArea.setWidgetResizable(True)
        free_servers = ["South Africa", 'Rusia', 'India']
        for server in servers.special_servers:
            if server.name in free_servers:
                text = 'FREE'
                tr = trailing_free_styles
            else:
                text = "VIP"
                tr = trailing_styles
            item = CustomListItem(label=server.name, icon=server.icon, value=text, tr_style=tr)
            self.content.addWidget(item)
            
    def list_special_servers(self):
        servers = Servers()
        for server in servers.global_servers:
            item = QListWidgetItem(server.name)
            icon = QIcon(server.icon)
            size = QSize(30, 30)
            self.specialList.setIconSize(size)
            item.setIcon(icon)
            self.specialList.addItem(item)
    
    def add_optimal_location(self):
        op = CustomListItem(label='Optimal Location', icon='./assets/location.png', value='', tr_style='', is_optimal=True)
        self.content.addWidget(op)
        
    
    def toggle_switch_a(self):
        self.specialBtn.setStyleSheet(gs1)
        self.globalBtn.setStyleSheet(gs2)
        
    def toggle_switch_b(self):
        self.specialBtn.setStyleSheet(gs2)
        self.globalBtn.setStyleSheet(gs1)
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        gpos = event.globalPosition().toPoint()
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + gpos - self.dragPos)
            self.dragPos = gpos
            event.accept()


if __name__ == "__main__":
    app = QApplication()
    win = TurboMainWindow()
    win.show()
    app.exec()

