# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 550)
        MainWindow.setMinimumSize(QSize(650, 550))
        MainWindow.setMaximumSize(QSize(650, 550))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(23, 20, 38);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.frame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(650, 30))
        self.topBar.setMaximumSize(QSize(650, 30))
        self.topBar.setStyleSheet(u"")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.topBar)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 400))
        self.frame_2.setMaximumSize(QSize(250, 600))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(90, 90))
        self.pushButton_2.setMaximumSize(QSize(90, 90))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(250, 122, 72);\n"
"border-radius: 20px;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/icons/turbo vpn logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"backgroud-color: #00000000;")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.statusFrame = QFrame(self.frame_2)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMinimumSize(QSize(200, 30))
        self.statusFrame.setMaximumSize(QSize(200, 30))
        self.statusFrame.setFrameShape(QFrame.NoFrame)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.statusFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.statusFrame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(0, 30))
        self.status_label.setMaximumSize(QSize(200, 30))
        self.status_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.status_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.statusFrame, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#ffffff;\">Turbo VPN</span></p></body></html>", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"The client status is starting up....", None))
    # retranslateUi

