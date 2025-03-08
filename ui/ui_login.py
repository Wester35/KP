# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sign.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(382, 501)
        MainWindow.setStyleSheet(u"*\n"
"{\n"
"	font-family:Comic Sans MS;\n"
"	font-size:24px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"	background:#333;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"color:white;\n"
"/*background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.545, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 0, 255));   url(:/images/free-icon-login-1674704.png)*/\n"
"	background:red;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color:red;\n"
"	background:#333;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"background:red;\n"
"border-radius:60px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 80, 361, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 121, 41))
        self.label.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 341, 61))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(130, 10, 121, 121))
        icon = QIcon()
        icon.addFile(u"resources/free-icon-login-1674704.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(78, 78))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Authorization", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.toolButton.setText("")
    # retranslateUi

