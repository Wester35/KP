# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiwFALli.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFormLayout,
    QFrame, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

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
"background-color:#333;\n"
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
        self.frame.setGeometry(QRect(520, 40, 401, 701))
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
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 340, 581, 212))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.surname = QLabel(self.formLayoutWidget)
        self.surname.setObjectName(u"surname")
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setBold(True)
        self.surname.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.surname)

        self.surnameValue = QLabel(self.formLayoutWidget)
        self.surnameValue.setObjectName(u"surnameValue")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.surnameValue)

        self.name = QLabel(self.formLayoutWidget)
        self.name.setObjectName(u"name")
        font1 = QFont()
        font1.setFamilies([u"century gothic"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.name.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.name)

        self.nameValue = QLabel(self.formLayoutWidget)
        self.nameValue.setObjectName(u"nameValue")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nameValue)

        self.lastname = QLabel(self.formLayoutWidget)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastname)

        self.lastnameValue = QLabel(self.formLayoutWidget)
        self.lastnameValue.setObjectName(u"lastnameValue")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastnameValue)

        self.phone = QLabel(self.formLayoutWidget)
        self.phone.setObjectName(u"phone")
        self.phone.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.phone)

        self.phoneValue = QLabel(self.formLayoutWidget)
        self.phoneValue.setObjectName(u"phoneValue")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.phoneValue)

        self.group = QLabel(self.formLayoutWidget)
        self.group.setObjectName(u"group")
        self.group.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.group)

        self.groupValue = QLabel(self.formLayoutWidget)
        self.groupValue.setObjectName(u"groupValue")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.groupValue)

        self.login = QLabel(self.formLayoutWidget)
        self.login.setObjectName(u"login")
        self.login.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.login)

        self.loginValue = QLabel(self.formLayoutWidget)
        self.loginValue.setObjectName(u"loginValue")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.loginValue)

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
        self.surname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.surnameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.nameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lastname.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.lastnameValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.phoneValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.group.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430:", None))
        self.groupValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.loginValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

