# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authTNtaTh.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QToolButton, QWidget)

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(501, 532)
        Authorization.setMaximumSize(QSize(501, 532))
        Authorization.setStyleSheet(u"*\n"
"{\n"
"	font-family:Comic Sans MS;\n"
"	font-size:24px;\n"
"}\n"
"\n"
"#frame\n"
"{\n"
"	background:#333;\n"
"	border-radius:22px;\n"
"}\n"
"\n"
"#frame_2\n"
"{\n"
"	background:url(C:\\Users\\Wester35\\Downloads\\sgustok_fraktal_sirenevyj_132619_1600x1200.jpg);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#pushButton\n"
"{\n"
"color:white;\n"
"background:#4B0082;\n"
"border-radius:15px;\n"
"transition: background 1s;\n"
"}\n"
"\n"
"#pushButton:hover\n"
"{\n"
"	color:#4B0082;\n"
"	background:#696969;\n"
"	border-radius:15px;\n"
"\n"
"}\n"
"\n"
"#pushButton:pressed \n"
"{\n"
"background-color: #483D8B;\n"
"transform: scale(0.9);\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"background:#4B0082;\n"
"border-radius:60px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"background:url('resources/sgustok_fraktal_sirenevyj_132619_1600x1200.jpg');\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"#checkPassword\n"
"{\n"
"background:#333;\n"
"col"
                        "or:white;\n"
"border-radius:15px;\n"
"transition: background 1s;\n"
"}\n"
"\n"
"#checkPassword:hover\n"
"{\n"
"background:#4B0082;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"#checkPassword:pressed\n"
"{\n"
"background:#483D8B;\n"
"transform: scale(0.9);\n"
"}")
        self.frame = QFrame(Authorization)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 110, 361, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 121, 41))
        self.label.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 341, 61))
        self.usernameEdit = QLineEdit(self.frame)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setGeometry(QRect(20, 130, 321, 22))
        self.passwordEdit = QLineEdit(self.frame)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(20, 200, 321, 22))
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.checkPassword = QPushButton(self.frame)
        self.checkPassword.setObjectName(u"checkPassword")
        self.checkPassword.setGeometry(QRect(310, 190, 31, 31))
        self.frame_2 = QFrame(Authorization)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 501, 520))
        self.frame_2.setMinimumSize(QSize(501, 520))
        self.frame_2.setMaximumSize(QSize(501, 520))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.toolButton = QToolButton(Authorization)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(190, 40, 121, 121))
        icon = QIcon()
        icon.addFile(u"resources/free-icon-login-1674704.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(78, 78))
        self.frame_2.raise_()
        self.frame.raise_()
        self.toolButton.raise_()

        self.retranslateUi(Authorization)

        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"Form", None))
        self.label.setText(QCoreApplication.translate("Authorization", u"Login here", None))
        self.pushButton.setText(QCoreApplication.translate("Authorization", u"Log In", None))
        self.usernameEdit.setText("")
        self.usernameEdit.setPlaceholderText(QCoreApplication.translate("Authorization", u"Username", None))
        self.passwordEdit.setInputMask("")
        self.passwordEdit.setText("")
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("Authorization", u"Password", None))
        self.checkPassword.setText("")
        self.toolButton.setText("")
    # retranslateUi

