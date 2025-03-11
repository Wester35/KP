# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uioQnOld.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 532)
        MainWindow.setMinimumSize(QSize(501, 532))
        MainWindow.setMaximumSize(QSize(501, 532))
        icon = QIcon()
        icon.addFile(u"../../../Downloads/free-icon-login-1674704.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(501, 532))
        self.centralwidget.setMaximumSize(QSize(501, 532))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(190, 40, 121, 121))
        icon1 = QIcon()
        icon1.addFile(u"resources/free-icon-login-1674704.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(78, 78))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(370, 430, 121, 31))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 260, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Authorization", None))
        self.toolButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

