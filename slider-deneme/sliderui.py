# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledyIpjrA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1144, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 70))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.top_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.invert_button = QPushButton(self.top_frame)
        self.invert_button.setObjectName(u"invert_button")

        self.verticalLayout_6.addWidget(self.invert_button)

        self.normal_button = QPushButton(self.top_frame)
        self.normal_button.setObjectName(u"normal_button")

        self.verticalLayout_6.addWidget(self.normal_button)


        self.verticalLayout_5.addWidget(self.top_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(450, 0))

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame_2)

        self.graph_frame = QFrame(self.centralwidget)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.graph_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.graph_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.r_frame = QFrame(self.graph_frame)
        self.r_frame.setObjectName(u"r_frame")
        self.r_frame.setFrameShape(QFrame.StyledPanel)
        self.r_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.r_frame)

        self.rSlider_a = QSlider(self.graph_frame)
        self.rSlider_a.setObjectName(u"rSlider_a")
        self.rSlider_a.setMaximum(255)
        self.rSlider_a.setOrientation(Qt.Horizontal)
        self.rSlider_a.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.rSlider_a)

        self.rSlider = QSlider(self.graph_frame)
        self.rSlider.setObjectName(u"rSlider")
        self.rSlider.setMaximum(255)
        self.rSlider.setValue(255)
        self.rSlider.setOrientation(Qt.Horizontal)
        self.rSlider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.rSlider)

        self.label_3 = QLabel(self.graph_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.g_frame = QFrame(self.graph_frame)
        self.g_frame.setObjectName(u"g_frame")
        self.g_frame.setFrameShape(QFrame.StyledPanel)
        self.g_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.g_frame)

        self.horizontalSlider_2 = QSlider(self.graph_frame)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.horizontalSlider_2)

        self.gSlider = QSlider(self.graph_frame)
        self.gSlider.setObjectName(u"gSlider")
        self.gSlider.setMaximum(255)
        self.gSlider.setValue(255)
        self.gSlider.setOrientation(Qt.Horizontal)
        self.gSlider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.gSlider)

        self.label_4 = QLabel(self.graph_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.b_frame = QFrame(self.graph_frame)
        self.b_frame.setObjectName(u"b_frame")
        self.b_frame.setFrameShape(QFrame.StyledPanel)
        self.b_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.b_frame)

        self.bSlider_a = QSlider(self.graph_frame)
        self.bSlider_a.setObjectName(u"bSlider_a")
        self.bSlider_a.setMaximum(255)
        self.bSlider_a.setOrientation(Qt.Horizontal)
        self.bSlider_a.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.bSlider_a)

        self.bSlider = QSlider(self.graph_frame)
        self.bSlider.setObjectName(u"bSlider")
        self.bSlider.setMaximum(255)
        self.bSlider.setValue(255)
        self.bSlider.setOrientation(Qt.Horizontal)
        self.bSlider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.bSlider)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.graph_frame)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.invert_button.setText(QCoreApplication.translate("MainWindow", u"invert mask", None))
        self.normal_button.setText(QCoreApplication.translate("MainWindow", u"normal mask", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"B", None))
    # retranslateUi

