# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screencAQAPD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(700, 700)
        SplashScreen.setMaximumSize(QSize(700, 700))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(700, 700))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.progress_bar = QFrame(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximumSize(QSize(330, 330))
        self.progress_bar.setStyleSheet(u"background-color:qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(121, 121, 121, 190), stop:0.652174 rgba(140, 140, 140, 190), stop:0.659091 rgba(13, 135, 216, 255), stop:1 rgba(13, 132, 211, 255));\n"
"border-radius:150px;")
        self.progress_bar.setFrameShape(QFrame.StyledPanel)
        self.progress_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.progress_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splash_main = QFrame(self.progress_bar)
        self.splash_main.setObjectName(u"splash_main")
        self.splash_main.setMaximumSize(QSize(700, 550))
        self.splash_main.setStyleSheet(u"background-color: rgb(70,70,70);\n"
"border-radius: 135px;")
        self.splash_main.setFrameShape(QFrame.StyledPanel)
        self.splash_main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.splash_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setContentsMargins(9, 43, -1, 41)
        self.Image_processing = QLabel(self.splash_main)
        self.Image_processing.setObjectName(u"Image_processing")
        self.Image_processing.setStyleSheet(u"font: 16pt \"Nirmala UI\";\n"
"color: rgb(180,180,180);\n"
"background:none;")
        self.Image_processing.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Image_processing, 0, 0, 1, 1)

        self.percent = QLabel(self.splash_main)
        self.percent.setObjectName(u"percent")
        self.percent.setStyleSheet(u"background: none;\n"
"font: 25 8pt \"Roboto Light\";\n"
"color: rgb(38, 155, 232)")
        self.percent.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.percent, 1, 0, 1, 1)

        self.creators = QLabel(self.splash_main)
        self.creators.setObjectName(u"creators")
        self.creators.setStyleSheet(u"background:none;\n"
"color: rgb(170, 170, 170);\n"
"font: 8pt \"Roboto\";")
        self.creators.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.creators, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.splash_main)


        self.horizontalLayout.addWidget(self.progress_bar)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.Image_processing.setText(QCoreApplication.translate("SplashScreen", u"Image Processing \n"
" Tool", None))
        self.percent.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:26pt;\">%</span></p></body></html>", None))
        self.creators.setText(QCoreApplication.translate("SplashScreen", u"Rabia E. \u00c7elik & Emre A. O\u011fuz", None))
    # retranslateUi

