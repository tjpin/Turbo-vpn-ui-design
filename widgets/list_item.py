from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem)

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
leading_styles = """
    QPushButton {
        border: none;
        border-radius: 16px;
        background-color: #00000000;
    }
"""

frame_style = """
    QFrame {
        color: #fff;
        border: none;
        background-color: rgb(58, 56, 77);
        border-top: 1px solid rgb(97, 95, 112);
    }
    
    QFrame:hover {
        border: none;
        background-color: rgb(97, 95, 112);
    }
"""

optimal_style = """
    QFrame {
        color: #fff;
        border: none;
        background-color: #242234;
        # border-top: 1px solid rgb(97, 95, 112);
    }
"""


class CustomListItem(QFrame):
    def __init__(self, label, icon, value, tr_style, is_optimal=False):
        super(CustomListItem, self).__init__(None)
        self.label = label
        self.icon = icon
        self.value = value
        self.tr_style = tr_style
        self.is_optimal = is_optimal
        self.setFixedSize(QSize(250, 50))
        self.setContentsMargins(0, 0, 0, 0)
        if self.is_optimal:
            self.setStyleSheet(optimal_style)
        else:
            self.setStyleSheet(frame_style)

        # Chilrens ****************************************************************
        # *************************************************************************
        self.leadingBtn = QPushButton()
        self.leadingBtn.setFixedSize(QSize(40, 40))
        self.leadingBtn.setIcon(QIcon(self.icon))
        self.leadingBtn.setIconSize(QSize(30, 30))
        self.leadingBtn.setObjectName('leading')
        self.leadingBtn.setStyleSheet(leading_styles)

        self.textLabel = QLabel()
        self.textLabel.setStyleSheet(
            'background-color: #00000000; font-size: 15; font-weight: bold; border: none; color: #fff;')
        self.textLabel.setText(self.label)

        self.spacer = QSpacerItem(
            10, 1, QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.trailingBtn = QPushButton()
        self.trailingBtn.setFixedSize(QSize(38, 20))
        self.trailingBtn.setText(self.value)
        self.trailingBtn.setObjectName('trailing')
        self.trailingBtn.setStyleSheet(self.tr_style)
        # Chilrens End*************************************************************
        # *************************************************************************

        # Layouts *****************************************************************
        # *************************************************************************
        self.parent_layout = QHBoxLayout()
        self.parent_layout.setSpacing(0)
        self.parent_layout.setContentsMargins(10, 0, 10, 0)
        self.parent_layout.addWidget(self.leadingBtn)
        self.parent_layout.addWidget(self.textLabel)
        self.parent_layout.addItem(self.spacer)
        if self.is_optimal:
            pass
        else:
            self.parent_layout.addWidget(self.trailingBtn)
        # Layouts End *************************************************************
        # *************************************************************************

        # Set Parent Layouts ******************************************************
        # *************************************************************************
        self.setLayout(self.parent_layout)
