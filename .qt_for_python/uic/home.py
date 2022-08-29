# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 580)
        MainWindow.setMinimumSize(QSize(710, 580))
        MainWindow.setMaximumSize(QSize(710, 580))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	padding: 0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.rootScreen = QTabWidget(self.centralwidget)
        self.rootScreen.setObjectName(u"rootScreen")
        self.rootScreen.setStyleSheet(u"QTabBar:tab:last:pane {\n"
"	height: 0px;\n"
"}")
        self.rootScreen.setTabPosition(QTabWidget.South)
        self.rootScreen.setUsesScrollButtons(False)
        self.rootScreen.setDocumentMode(True)
        self.rootScreen.setTabsClosable(False)
        self.rootScreen.setMovable(False)
        self.rootScreen.setTabBarAutoHide(True)
        self.welcomeTab = QWidget()
        self.welcomeTab.setObjectName(u"welcomeTab")
        self.welcomeTab.setStyleSheet(u"background-color: rgb(36, 34, 52);")
        self.verticalLayout_10 = QVBoxLayout(self.welcomeTab)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.welcomeTab)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.welcomeTopBar = QFrame(self.frame_12)
        self.welcomeTopBar.setObjectName(u"welcomeTopBar")
        self.welcomeTopBar.setMinimumSize(QSize(710, 30))
        self.welcomeTopBar.setMaximumSize(QSize(710, 30))
        self.welcomeTopBar.setStyleSheet(u"")
        self.welcomeTopBar.setFrameShape(QFrame.NoFrame)
        self.welcomeTopBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.welcomeTopBar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(647, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.startMiniBtn = QPushButton(self.welcomeTopBar)
        self.startMiniBtn.setObjectName(u"startMiniBtn")
        self.startMiniBtn.setMinimumSize(QSize(30, 30))
        self.startMiniBtn.setMaximumSize(QSize(30, 30))
        self.startMiniBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/mini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startMiniBtn.setIcon(icon)
        self.startMiniBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.startMiniBtn)

        self.startCloseBtn = QPushButton(self.welcomeTopBar)
        self.startCloseBtn.setObjectName(u"startCloseBtn")
        self.startCloseBtn.setMinimumSize(QSize(30, 30))
        self.startCloseBtn.setMaximumSize(QSize(30, 30))
        self.startCloseBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startCloseBtn.setIcon(icon1)
        self.startCloseBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.startCloseBtn)


        self.verticalLayout_7.addWidget(self.welcomeTopBar)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(250, 400))
        self.frame_13.setMaximumSize(QSize(250, 600))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.pushButton_7 = QPushButton(self.frame_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(90, 90))
        self.pushButton_7.setMaximumSize(QSize(90, 90))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(250, 122, 72);\n"
"border-radius: 20px;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/turbo vpn logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(70, 70))

        self.verticalLayout_8.addWidget(self.pushButton_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"backgroud-color: #00000000;")

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.statusFrame = QFrame(self.frame_13)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMinimumSize(QSize(200, 30))
        self.statusFrame.setMaximumSize(QSize(200, 30))
        self.statusFrame.setFrameShape(QFrame.NoFrame)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.statusFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.statusFrame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(0, 30))
        self.status_label.setMaximumSize(QSize(200, 30))
        self.status_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_9.addWidget(self.status_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.statusFrame, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_7.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.rootScreen.addTab(self.welcomeTab, "")
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.verticalLayout = QVBoxLayout(self.homeTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.homeTab)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 37))
        self.topBar.setMaximumSize(QSize(16777215, 37))
        self.topBar.setCursor(QCursor(Qt.SizeAllCursor))
        self.topBar.setStyleSheet(u"background-color: rgb(250, 123, 71);")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.pushButton = QPushButton(self.topBar)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"text-align: left;\n"
"border: none;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(292, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.topBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(160, 0))
        self.frame_4.setMaximumSize(QSize(160, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.giftBtn = QPushButton(self.frame_4)
        self.giftBtn.setObjectName(u"giftBtn")
        self.giftBtn.setMinimumSize(QSize(30, 30))
        self.giftBtn.setMaximumSize(QSize(30, 30))
        self.giftBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/gift.png", QSize(), QIcon.Normal, QIcon.Off)
        self.giftBtn.setIcon(icon3)
        self.giftBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.giftBtn)

        self.accBtn = QPushButton(self.frame_4)
        self.accBtn.setObjectName(u"accBtn")
        self.accBtn.setMinimumSize(QSize(30, 30))
        self.accBtn.setMaximumSize(QSize(30, 30))
        self.accBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accBtn.setIcon(icon4)
        self.accBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.accBtn)

        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(30, 30))
        self.settingsBtn.setMaximumSize(QSize(30, 30))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.settingsBtn)

        self.miniBtn = QPushButton(self.frame_4)
        self.miniBtn.setObjectName(u"miniBtn")
        self.miniBtn.setMinimumSize(QSize(30, 30))
        self.miniBtn.setMaximumSize(QSize(30, 30))
        self.miniBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.7;\n"
"}")
        self.miniBtn.setIcon(icon)
        self.miniBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.miniBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(30, 30))
        self.closeBtn.setMaximumSize(QSize(30, 30))
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.4;\n"
"}")
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.topBar)

        self.frame = QFrame(self.homeTab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(36, 34, 52);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 33))
        self.frame_8.setMaximumSize(QSize(16777215, 33))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.globalBtn = QPushButton(self.frame_8)
        self.globalBtn.setObjectName(u"globalBtn")
        self.globalBtn.setMinimumSize(QSize(0, 33))
        self.globalBtn.setMaximumSize(QSize(16777215, 33))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.globalBtn.setFont(font2)
        self.globalBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(211, 104, 60);\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_5.addWidget(self.globalBtn)

        self.specialBtn = QPushButton(self.frame_8)
        self.specialBtn.setObjectName(u"specialBtn")
        self.specialBtn.setMinimumSize(QSize(0, 33))
        self.specialBtn.setMaximumSize(QSize(16777215, 33))
        self.specialBtn.setFont(font2)
        self.specialBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	color: #000;\n"
"}")

        self.horizontalLayout_5.addWidget(self.specialBtn)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(58, 56, 77);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 33))
        self.lineEdit.setMaximumSize(QSize(16777215, 33))
        font3 = QFont()
        font3.setPointSize(11)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	color: #fff;\n"
"	padding-left: 7px;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(97, 95, 112);\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 33))
        self.pushButton_4.setMaximumSize(QSize(50, 33))
        self.pushButton_4.setStyleSheet(u"border: none;\n"
"border-radius: 7px;\n"
"background-color: rgb(200, 98, 56);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.sideNav = QTabWidget(self.frame_2)
        self.sideNav.setObjectName(u"sideNav")
        self.sideNav.setStyleSheet(u"QTabBar:tab:last:pane {\n"
"	height: 0px;\n"
"}")
        self.sideNav.setDocumentMode(True)
        self.sideNav.setTabsClosable(False)
        self.sideNav.setTabBarAutoHide(True)
        self.globalServerList = QWidget()
        self.globalServerList.setObjectName(u"globalServerList")
        self.verticalLayout_11 = QVBoxLayout(self.globalServerList)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.globalServerList)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setStyleSheet(u"QScrollBar {\n"
"	width: 5px;\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"QScrollBar:handle {\n"
"	background-color:  rgb(97, 95, 112);\n"
"	border-radius: 2px;\n"
"	height: 70px;\n"
"}\n"
"\n"
"QScrollBar:add-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"QScrollBar:sub-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 250, 443))
        self.scrollAreaWidgetContents.setStyleSheet(u"QListWidget {\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"\n"
"QListWidget:item {\n"
"	height: 45px;\n"
"	padding-left: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(58, 56, 77);\n"
"	border-top: 1px solid rgb(97, 95, 112);\n"
"}\n"
"\n"
"QListWidget:item:hover {\n"
"	background-color: rgb(97, 95, 112);\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	width: 5px;\n"
"	max-height: 100px;\n"
"}\n"
"QScrollBar:handle {\n"
"	background-color:  rgb(97, 95, 112);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar:add-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"QScrollBar:sub-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollWidget = QWidget(self.scrollAreaWidgetContents)
        self.scrollWidget.setObjectName(u"scrollWidget")
        self.verticalLayout_16 = QVBoxLayout(self.scrollWidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.content = QVBoxLayout()
        self.content.setSpacing(1)
        self.content.setObjectName(u"content")

        self.verticalLayout_16.addLayout(self.content)


        self.verticalLayout_14.addWidget(self.scrollWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.sideNav.addTab(self.globalServerList, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_12 = QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.specialList = QListWidget(self.tab_4)
        self.specialList.setObjectName(u"specialList")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.specialList.setFont(font4)
        self.specialList.setStyleSheet(u"QListWidget {\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"\n"
"QListWidget:item {\n"
"	height: 45px;\n"
"	padding-left: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(58, 56, 77);\n"
"	border-top: 1px solid rgb(97, 95, 112);\n"
"}\n"
"\n"
"QListWidget:item:hover {\n"
"	background-color: rgb(97, 95, 112);\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	width: 5px;\n"
"}\n"
"QScrollBar:handle {\n"
"	background-color:  rgb(97, 95, 112);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar:add-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"QScrollBar:sub-page {\n"
"	background-color: rgb(58, 56, 77);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.specialList.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_12.addWidget(self.specialList)

        self.sideNav.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.sideNav)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 251, 250);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 234, 71, 91))
        self.label.setStyleSheet(u"image: url(:/icons/rabit (1).png);")

        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 221))
        self.frame_10.setStyleSheet(u";\n"
"border-image: url(:/icons/bg.png);\n"
"background-color: #00000000;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.frame_10.setLineWidth(0)
        self.connectBtn = QPushButton(self.frame_10)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setGeometry(QRect(200, 120, 64, 64))
        self.connectBtn.setMinimumSize(QSize(64, 64))
        self.connectBtn.setMaximumSize(QSize(70, 70))
        self.connectBtn.setStyleSheet(u"QPushButton {\n"
"	border-image: none;\n"
"	background-color: rgb(250, 123, 72);\n"
"	border-radius: 32px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	opacity: 0.8;\n"
"	background-color: rgb(186, 100, 53);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/carotLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connectBtn.setIcon(icon7)
        self.connectBtn.setIconSize(QSize(37, 37))
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 60, 171, 31))
        font5 = QFont()
        font5.setPointSize(16)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"image: none;\n"
"color: #fff;\n"
"background-color: #00000000;")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(-10, 210, 471, 61))
        self.frame_11.setStyleSheet(u"image: none;\n"
"background-color: rgb(70, 80, 169);")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_2.raise_()
        self.frame_11.raise_()
        self.connectBtn.raise_()

        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_10.raise_()
        self.frame_9.raise_()

        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.rootScreen.addTab(self.homeTab, "")
        self.accountTab = QWidget()
        self.accountTab.setObjectName(u"accountTab")
        self.verticalLayout_6 = QVBoxLayout(self.accountTab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.accountTab)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 160))
        self.header.setMaximumSize(QSize(16777215, 160))
        self.header.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.0848806 rgba(227, 178, 125, 255), stop:0.0901857 rgba(226, 154, 90, 255), stop:0.183024 rgba(221, 131, 66, 255), stop:0.278515 rgba(221, 119, 63, 255), stop:0.281167 rgba(221, 131, 66, 255), stop:0.527851 rgba(223, 143, 71, 255), stop:0.530504 rgba(221, 119, 63, 255), stop:1 rgba(250, 123, 71, 255));")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.homeBtn = QPushButton(self.header)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setGeometry(QRect(10, 10, 50, 33))
        self.homeBtn.setMinimumSize(QSize(50, 33))
        self.homeBtn.setMaximumSize(QSize(50, 33))
        self.homeBtn.setStyleSheet(u"border: none;\n"
"border-radius: 7px;\n"
"background-color: #00000000;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/back-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon8)
        self.homeBtn.setIconSize(QSize(27, 27))
        self.label_7 = QLabel(self.header)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 50, 171, 31))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"background-color: #00000000;\n"
"color: #fff;")
        self.label_8 = QLabel(self.header)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 80, 241, 21))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(False)
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"background-color: #00000000;\n"
"color: #fff;")

        self.verticalLayout_6.addWidget(self.header)

        self.fields = QFrame(self.accountTab)
        self.fields.setObjectName(u"fields")
        self.fields.setMinimumSize(QSize(0, 140))
        self.fields.setMaximumSize(QSize(16777215, 140))
        self.fields.setFrameShape(QFrame.NoFrame)
        self.fields.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.fields)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, 0, 50, 0)
        self.lineEdit_2 = QLineEdit(self.fields)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_2.setFont(font7)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding-left: 30px;")

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.fields)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 50))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_3.setFont(font3)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding-left: 30px;")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addWidget(self.fields)

        self.actionsFrame = QFrame(self.accountTab)
        self.actionsFrame.setObjectName(u"actionsFrame")
        self.actionsFrame.setFrameShape(QFrame.StyledPanel)
        self.actionsFrame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.actionsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 140, 147, 20))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        self.label_3.setFont(font8)
        self.label_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_3.setStyleSheet(u"color: rgb(250, 133, 112);")
        self.pushButton_6 = QPushButton(self.actionsFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(190, 50, 280, 40))
        self.pushButton_6.setMinimumSize(QSize(280, 40))
        self.pushButton_6.setMaximumSize(QSize(280, 40))
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(252, 255, 252);\n"
"	background-color: rgb(70, 80, 169);\n"
"	border-radius: 7px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(103, 113, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(66, 76, 158);\n"
"}")
        self.label_4 = QLabel(self.actionsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(245, 120, 170, 16))
        font9 = QFont()
        font9.setBold(False)
        self.label_4.setFont(font9)
        self.label_4.setCursor(QCursor(Qt.ArrowCursor))
        self.label_5 = QLabel(self.actionsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 10, 109, 20))
        self.label_5.setFont(font7)
        self.label_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_5.setStyleSheet(u"color: rgb(250, 133, 112);")

        self.verticalLayout_6.addWidget(self.actionsFrame)

        self.rootScreen.addTab(self.accountTab, "")

        self.verticalLayout_13.addWidget(self.rootScreen)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startMiniBtn.setText("")
        self.startCloseBtn.setText("")
        self.pushButton_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#ffffff;\">Turbo VPN</span></p></body></html>", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"The client status is starting up....", None))
        self.rootScreen.setTabText(self.rootScreen.indexOf(self.welcomeTab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Turbo VPN 2.18.0.0", None))
        self.giftBtn.setText("")
        self.accBtn.setText("")
        self.settingsBtn.setText("")
        self.miniBtn.setText("")
        self.closeBtn.setText("")
        self.globalBtn.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.specialBtn.setText(QCoreApplication.translate("MainWindow", u"Special", None))
        self.pushButton_4.setText("")
        self.sideNav.setTabText(self.sideNav.indexOf(self.globalServerList), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.sideNav.setTabText(self.sideNav.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText("")
        self.connectBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tap to connect", None))
        self.rootScreen.setTabText(self.rootScreen.indexOf(self.homeTab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.homeBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Welcome to Turbo VPN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Start private and surfing with us", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name@example.com", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Create a New Account", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Don't have Turbo VPN Account?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.rootScreen.setTabText(self.rootScreen.indexOf(self.accountTab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

