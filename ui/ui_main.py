# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uihFAXYh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QHeaderView, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 780)
        MainWindow.setBaseSize(QSize(1000, 800))
        MainWindow.setStyleSheet(u"*{\n"
"font-size: 16px;\n"
"font-family: century gothic;\n"
"}\n"
"#profileButton{\n"
"border-radius:35px;\n"
"background-color:#333\n"
"}\n"
"#profileButton:pushed{\n"
"background-color: #483D8B;\n"
"}\n"
"#closeButton{\n"
"background-color: transparent;\n"
"border-radius:20px;\n"
"}\n"
"#frame{\n"
"background-color:#333;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#282226\n"
"}\n"
"#tableView{\n"
"background-color:#111\n"
"}\n"
"#comboBox{\n"
"background-color:#111\n"
"}\n"
"QFrame{\n"
"border-radius:20px;\n"
"}\n"
"")
        self.comboBox = QComboBox(MainWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(830, 10, 271, 21))
        self.tableView = QTableView(MainWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(110, 60, 1001, 711))
        self.profileButton = QPushButton(MainWindow)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setGeometry(QRect(10, 10, 70, 70))
        self.profileButton.setIconSize(QSize(48, 48))
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(470, 40, 401, 701))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 290, 121, 31))
        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(330, 20, 51, 51))
        self.photo = QFrame(self.frame)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(20, 20, 261, 261))
        self.photo.setFrameShape(QFrame.Shape.StyledPanel)
        self.photo.setFrameShadow(QFrame.Shadow.Raised)
        self.logoutButton = QPushButton(self.frame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(300, 650, 81, 31))
        self.calendarWidget = QCalendarWidget(MainWindow)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(1120, 60, 281, 351))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student", None))
        self.profileButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Photo", None))
        self.closeButton.setText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
    # retranslateUi

