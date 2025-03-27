# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiZMEjEa.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 780)
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
"border-radius:10px;\n"
"font-size: 36px;\n"
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
"QLabel{\n"
"font-size:24px;\n"
"background-color:transparent;\n"
"}")
        self.comboBox = QComboBox(MainWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(870, 10, 271, 21))
        self.tableView = QTableView(MainWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(90, 60, 1051, 711))
        self.profileButton = QPushButton(MainWindow)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setGeometry(QRect(10, 10, 70, 70))
        self.profileButton.setIconSize(QSize(48, 48))
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(520, 30, 401, 701))
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
        self.login = QLabel(self.frame)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(30, 340, 78, 30))
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setBold(True)
        self.login.setFont(font)
        self.surname = QLabel(self.frame)
        self.surname.setObjectName(u"surname")
        self.surname.setGeometry(QRect(30, 370, 114, 30))
        self.surname.setFont(font)
        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(30, 400, 55, 30))
        font1 = QFont()
        font1.setFamilies([u"century gothic"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.name.setFont(font1)
        self.loginValue = QLabel(self.frame)
        self.loginValue.setObjectName(u"loginValue")
        self.loginValue.setGeometry(QRect(160, 340, 448, 30))
        self.surnameValue = QLabel(self.frame)
        self.surnameValue.setObjectName(u"surnameValue")
        self.surnameValue.setGeometry(QRect(160, 370, 441, 30))
        self.nameValue = QLabel(self.frame)
        self.nameValue.setObjectName(u"nameValue")
        self.nameValue.setGeometry(QRect(160, 400, 441, 30))
        self.lastname = QLabel(self.frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(30, 430, 125, 30))
        self.lastname.setFont(font)
        self.lastnameValue = QLabel(self.frame)
        self.lastnameValue.setObjectName(u"lastnameValue")
        self.lastnameValue.setGeometry(QRect(160, 430, 458, 30))
        self.phone = QLabel(self.frame)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(30, 460, 115, 30))
        self.phone.setFont(font)
        self.phoneValue = QLabel(self.frame)
        self.phoneValue.setObjectName(u"phoneValue")
        self.phoneValue.setGeometry(QRect(160, 460, 480, 30))
        self.group = QLabel(self.frame)
        self.group.setObjectName(u"group")
        self.group.setGeometry(QRect(30, 490, 93, 30))
        self.group.setFont(font)
        self.groupValue = QLabel(self.frame)
        self.groupValue.setObjectName(u"groupValue")
        self.groupValue.setGeometry(QRect(160, 490, 573, 31))
        self.calendarWidget = QCalendarWidget(MainWindow)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(1150, 60, 341, 451))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student", None))
        self.profileButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Photo", None))
        self.closeButton.setText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.loginValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.surnameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lastname.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.lastnameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.phoneValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.group.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430:", None))
        self.groupValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

