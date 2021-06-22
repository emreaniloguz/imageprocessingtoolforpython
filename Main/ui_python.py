# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainuxaWCw.ui'
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
        MainWindow.resize(1016, 645)
        MainWindow.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 30))
        self.header.setMaximumSize(QSize(16777215, 30))
        self.header.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.page_name = QFrame(self.header)
        self.page_name.setObjectName(u"page_name")
        self.page_name.setFrameShape(QFrame.StyledPanel)
        self.page_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.page_name)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 0, 0)
        self.label = QLabel(self.page_name)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_11.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.page_name)

        self.page_buttons = QFrame(self.header)
        self.page_buttons.setObjectName(u"page_buttons")
        self.page_buttons.setMaximumSize(QSize(120, 70))
        self.page_buttons.setFrameShape(QFrame.StyledPanel)
        self.page_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.page_buttons)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.minimize_button_frame = QFrame(self.page_buttons)
        self.minimize_button_frame.setObjectName(u"minimize_button_frame")
        self.minimize_button_frame.setMinimumSize(QSize(0, 25))
        self.minimize_button_frame.setMaximumSize(QSize(40, 16777215))
        self.minimize_button_frame.setFrameShape(QFrame.StyledPanel)
        self.minimize_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.minimize_button_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.minimize_button_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(0, 25))
        self.minimize_button.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	border: none solid;\n"
"	background-color: rgb(76, 76, 76);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Desktop/line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(14, 16))

        self.verticalLayout_11.addWidget(self.minimize_button)


        self.horizontalLayout_9.addWidget(self.minimize_button_frame)

        self.maximize_button_frame = QFrame(self.page_buttons)
        self.maximize_button_frame.setObjectName(u"maximize_button_frame")
        self.maximize_button_frame.setMaximumSize(QSize(40, 16777215))
        self.maximize_button_frame.setFrameShape(QFrame.StyledPanel)
        self.maximize_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.maximize_button_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.maximize_button = QPushButton(self.maximize_button_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMinimumSize(QSize(0, 25))
        self.maximize_button.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	border: none solid;\n"
"	background-color: rgb(76, 76, 76);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../Desktop/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setIconSize(QSize(12, 12))

        self.verticalLayout_10.addWidget(self.maximize_button)


        self.horizontalLayout_9.addWidget(self.maximize_button_frame)

        self.exit_button_frame = QFrame(self.page_buttons)
        self.exit_button_frame.setObjectName(u"exit_button_frame")
        self.exit_button_frame.setMaximumSize(QSize(40, 16777215))
        self.exit_button_frame.setFrameShape(QFrame.StyledPanel)
        self.exit_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.exit_button_frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.exit_button_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(0, 25))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	border: none solid;\n"
"	background-color: rgb(255, 45, 30);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../Desktop/\u00e7\u0131k\u0131\u015f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setIconSize(QSize(10, 10))
        self.exit_button.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.exit_button)


        self.horizontalLayout_9.addWidget(self.exit_button_frame)


        self.horizontalLayout_2.addWidget(self.page_buttons)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.frame)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.body)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget = QStackedWidget(self.body)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.color_space_page = QWidget()
        self.color_space_page.setObjectName(u"color_space_page")
        self.color_space_page.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.horizontalLayout = QHBoxLayout(self.color_space_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.photo_frame = QFrame(self.color_space_page)
        self.photo_frame.setObjectName(u"photo_frame")
        self.photo_frame.setStyleSheet(u"background-color: rgb(31,31,31);")
        self.photo_frame.setFrameShape(QFrame.StyledPanel)
        self.photo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.photo_frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.import_page = QFrame(self.photo_frame)
        self.import_page.setObjectName(u"import_page")
        self.import_page.setStyleSheet(u"\n"
"background-color: rgb(41, 41, 41);\n"
"")
        self.import_page.setFrameShape(QFrame.StyledPanel)
        self.import_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.import_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.import_photo = QFrame(self.import_page)
        self.import_photo.setObjectName(u"import_photo")
        self.import_photo.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.import_photo.setFrameShape(QFrame.StyledPanel)
        self.import_photo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.import_photo)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.photo = QLabel(self.import_photo)
        self.photo.setObjectName(u"photo")
        self.photo.setMinimumSize(QSize(480, 480))
        #self.photo.setMaximumSize(QSize(480, 480))
        self.photo.setScaledContents(1)


        self.horizontalLayout_5.addWidget(self.photo)


        self.verticalLayout_9.addWidget(self.import_photo)

        self.import_frame = QFrame(self.import_page)
        self.import_frame.setObjectName(u"import_frame")
        self.import_frame.setMaximumSize(QSize(480, 480))
        self.import_frame.setStyleSheet(u"border: 5px;\n"
"border-radius: 5px;\n"
"background-color:rgb(41, 41, 41);")
        self.import_frame.setFrameShape(QFrame.StyledPanel)
        self.import_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.import_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.import_button = QPushButton(self.import_frame)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setMinimumSize(QSize(120, 30))
        self.import_button.setMaximumSize(QSize(480, 16777215))
        self.import_button.setLayoutDirection(Qt.LeftToRight)
        self.import_button.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border: 5px;\n"
"	border-radius: 5px;\n"
"	border: rgb(35, 35, 35);\n"
"	font: 8pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 117, 198);\n"
"	color: rgb(220, 220, 220);\n"
"	\n"
"}")

        self.horizontalLayout_4.addWidget(self.import_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.import_frame)


        self.horizontalLayout_3.addWidget(self.import_page)

        self.graph_frame = QFrame(self.photo_frame)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border: none solid;")
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.graph_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rgb = QFrame(self.graph_frame)
        self.rgb.setObjectName(u"rgb")
        self.rgb.setFrameShape(QFrame.StyledPanel)
        self.rgb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.rgb)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rgb_graph = QFrame(self.rgb)
        self.rgb_graph.setObjectName(u"rgb_graph")
        self.rgb_graph.setStyleSheet(u"background-color: rgb(41, 41, 41);")
        self.rgb_graph.setFrameShape(QFrame.StyledPanel)
        self.rgb_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.rgb_graph)

        self.rgb_button = QFrame(self.rgb)
        self.rgb_button.setObjectName(u"rgb_button")
        self.rgb_button.setMaximumSize(QSize(16777215, 30))
        self.rgb_button.setStyleSheet(u"background-color: #bd93f9;\n"
"border: 5px;\n"
"")
        self.rgb_button.setFrameShape(QFrame.StyledPanel)
        self.rgb_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.rgb_button)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.rgb_button)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border: 5px;\n"
"	border-radius: 5px;\n"
"\n"
"	\n"
"	font: 8pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 117, 198);\n"
"	\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.rgb_button)


        self.verticalLayout_2.addWidget(self.rgb)

        self.yuv = QFrame(self.graph_frame)
        self.yuv.setObjectName(u"yuv")
        self.yuv.setFrameShape(QFrame.StyledPanel)
        self.yuv.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.yuv)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.yuv_graph_frame = QFrame(self.yuv)
        self.yuv_graph_frame.setObjectName(u"yuv_graph_frame")
        self.yuv_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.yuv_graph_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.yuv_graph_frame)

        self.yuv_button_frame = QFrame(self.yuv)
        self.yuv_button_frame.setObjectName(u"yuv_button_frame")
        self.yuv_button_frame.setMaximumSize(QSize(16777215, 30))
        self.yuv_button_frame.setStyleSheet(u"background-color: #bd93f9;\n"
"border: 5px;\n"
"")
        self.yuv_button_frame.setFrameShape(QFrame.StyledPanel)
        self.yuv_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.yuv_button_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.yuv_button = QPushButton(self.yuv_button_frame)
        self.yuv_button.setObjectName(u"yuv_button")
        self.yuv_button.setMinimumSize(QSize(0, 30))
        self.yuv_button.setMaximumSize(QSize(16777215, 30))
        self.yuv_button.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border: 5px;\n"
"	border-radius: 5px;\n"
"\n"
"	font: 8pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 117, 198);\n"
"	\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.yuv_button)


        self.verticalLayout_4.addWidget(self.yuv_button_frame)


        self.verticalLayout_2.addWidget(self.yuv)

        self.hsv = QFrame(self.graph_frame)
        self.hsv.setObjectName(u"hsv")
        self.hsv.setFrameShape(QFrame.StyledPanel)
        self.hsv.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.hsv)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.hsv_graph = QFrame(self.hsv)
        self.hsv_graph.setObjectName(u"hsv_graph")
        self.hsv_graph.setFrameShape(QFrame.StyledPanel)
        self.hsv_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.hsv_graph)

        self.hsv_button = QFrame(self.hsv)
        self.hsv_button.setObjectName(u"hsv_button")
        self.hsv_button.setMaximumSize(QSize(16777215, 30))
        self.hsv_button.setStyleSheet(u"background-color: #bd93f9;\n"
"border: 5px;\n"
"border-color: #bd93f9;")
        self.hsv_button.setFrameShape(QFrame.StyledPanel)
        self.hsv_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.hsv_button)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.hsv_button)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border: 5px;\n"
"	border-radius: 5px;\n"
"\n"
"	font: 8pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 117, 198);\n"
"	\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.hsv_button)


        self.verticalLayout_2.addWidget(self.hsv)


        self.horizontalLayout_3.addWidget(self.graph_frame)


        self.horizontalLayout.addWidget(self.photo_frame)

        self.StackedWidget.addWidget(self.color_space_page)
        self.masking_page = QWidget()
        self.masking_page.setObjectName(u"masking_page")
        self.StackedWidget.addWidget(self.masking_page)

        self.horizontalLayout_6.addWidget(self.StackedWidget)


        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.frame)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 30))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.horizontalLayout_8.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Processing Tool", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image Processing Tool", None))
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.minimize_button.setWhatsThis(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.minimize_button.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.minimize_button.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_button.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.maximize_button.setWhatsThis(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.maximize_button.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.maximize_button.setText("")
#if QT_CONFIG(tooltip)
        self.exit_button.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.exit_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.exit_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.exit_button.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.exit_button.setText("")
        self.photo.setText("")
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"Import Image ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"RGB", None))
        self.yuv_button.setText(QCoreApplication.translate("MainWindow", u"YUV", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"HSV", None))
    # retranslateUi

