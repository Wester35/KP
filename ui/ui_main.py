# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiwarvPN.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
"background-color:transparent;\n"
"}\n"
"#currentDate{\n"
"font-size:20px;\n"
"color:#696969;\n"
"}\n"
"#pair_teacher{\n"
"background-color:#111\n"
"}")
        self.comboBox = QComboBox(MainWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(870, 10, 271, 21))
        self.tableView = QTableView(MainWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(980, 160, 161, 611))
        self.profileButton = QPushButton(MainWindow)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setGeometry(QRect(10, 10, 70, 70))
        self.profileButton.setIconSize(QSize(48, 48))
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(520, 30, 401, 701))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"century gothic"])
        font1.setBold(True)
        self.login.setFont(font1)
        self.surname = QLabel(self.frame)
        self.surname.setObjectName(u"surname")
        self.surname.setGeometry(QRect(30, 370, 114, 30))
        self.surname.setFont(font1)
        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(30, 400, 55, 30))
        font2 = QFont()
        font2.setFamilies([u"century gothic"])
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.name.setFont(font2)
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
        self.lastname.setFont(font1)
        self.lastnameValue = QLabel(self.frame)
        self.lastnameValue.setObjectName(u"lastnameValue")
        self.lastnameValue.setGeometry(QRect(160, 430, 458, 30))
        self.phone = QLabel(self.frame)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(30, 460, 115, 30))
        self.phone.setFont(font1)
        self.phoneValue = QLabel(self.frame)
        self.phoneValue.setObjectName(u"phoneValue")
        self.phoneValue.setGeometry(QRect(160, 460, 480, 30))
        self.group = QLabel(self.frame)
        self.group.setObjectName(u"group")
        self.group.setGeometry(QRect(30, 490, 93, 30))
        self.group.setFont(font1)
        self.groupValue = QLabel(self.frame)
        self.groupValue.setObjectName(u"groupValue")
        self.groupValue.setGeometry(QRect(160, 490, 573, 31))
        self.calendarWidget = QCalendarWidget(MainWindow)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(1150, 60, 341, 451))
        self.formLayoutWidget = QWidget(MainWindow)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(100, 70, 611, 401))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lates = QLabel(self.formLayoutWidget)
        self.lates.setObjectName(u"lates")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lates)

        self.latesValue = QLabel(self.formLayoutWidget)
        self.latesValue.setObjectName(u"latesValue")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.latesValue)

        self.absence = QLabel(self.formLayoutWidget)
        self.absence.setObjectName(u"absence")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.absence)

        self.absenceValue = QLabel(self.formLayoutWidget)
        self.absenceValue.setObjectName(u"absenceValue")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.absenceValue)

        self.currentDate = QLabel(MainWindow)
        self.currentDate.setObjectName(u"currentDate")
        self.currentDate.setGeometry(QRect(120, 20, 291, 16))
        self.pair_teacher = QTableView(MainWindow)
        self.pair_teacher.setObjectName(u"pair_teacher")
        self.pair_teacher.setGeometry(QRect(980, 70, 161, 91))
        self.pair_teacher.raise_()
        self.comboBox.raise_()
        self.tableView.raise_()
        self.profileButton.raise_()
        self.calendarWidget.raise_()
        self.formLayoutWidget.raise_()
        self.frame.raise_()
        self.currentDate.raise_()

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
        self.lates.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043f\u043e\u0437\u0434\u0430\u043d\u0438\u0439:", None))
        self.latesValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.absence.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u043e\u0432:", None))
        self.absenceValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.currentDate.setText("")
    # retranslateUi

