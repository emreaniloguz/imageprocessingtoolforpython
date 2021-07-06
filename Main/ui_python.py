# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainXQkpRN.ui'
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
        MainWindow.resize(1115, 645)
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
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximize_button.sizePolicy().hasHeightForWidth())
        self.maximize_button.setSizePolicy(sizePolicy)
        self.maximize_button.setMinimumSize(QSize(40, 25))
        self.maximize_button.setMaximumSize(QSize(16777215, 16777215))
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

        self.verticalLayout_10.addWidget(self.maximize_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)


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
        font = QFont()
        font.setStrikeOut(False)
        self.StackedWidget.setFont(font)
        self.StackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.StackedWidget.setAcceptDrops(False)
        self.StackedWidget.setFrameShape(QFrame.NoFrame)
        self.StackedWidget.setFrameShadow(QFrame.Plain)
        self.StackedWidget.setLineWidth(1)
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
        self.photo.setMinimumSize(QSize(300, 0))
        self.photo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.photo)


        self.verticalLayout_9.addWidget(self.import_photo)

        self.import_frame = QFrame(self.import_page)
        self.import_frame.setObjectName(u"import_frame")
        self.import_frame.setMaximumSize(QSize(16777215, 70))
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
        self.import_button.setMaximumSize(QSize(70, 16777215))
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
        self.horizontalLayout_12 = QHBoxLayout(self.graph_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.graph_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setBaseSize(QSize(0, 0))
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"	 height: 40px;\n"
"	 width:167px;\n"
"	 background: #ff5555;\n"
"	color: white;\n"
"	border: 1px solid;\n"
"\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"border-color: rgb(41, 41, 41);\n"
"}QTabBar::tab::selected{\n"
"	border-color:white;  \n"
"\n"
"}\n"
"\n"
"QTabBar::tab::!selected{\n"
"border-color:black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"   \n"
" margin-left: -4px;\n"
"    margin-right: -1px;\n"
"}")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.RGB = QWidget()
        self.RGB.setObjectName(u"RGB")
        self.RGB.setMinimumSize(QSize(100, 300))
        self.RGB.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.RGB)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.rgb_frame = QFrame(self.RGB)
        self.rgb_frame.setObjectName(u"rgb_frame")
        self.rgb_frame.setFrameShape(QFrame.StyledPanel)
        self.rgb_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.rgb_frame)

        self.tabWidget.addTab(self.RGB, "")
        self.HSV = QWidget()
        self.HSV.setObjectName(u"HSV")
        self.HSV.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.HSV)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.hsv_frame = QFrame(self.HSV)
        self.hsv_frame.setObjectName(u"hsv_frame")
        self.hsv_frame.setFrameShape(QFrame.StyledPanel)
        self.hsv_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.hsv_frame)

        self.tabWidget.addTab(self.HSV, "")
        self.YUV = QWidget()
        self.YUV.setObjectName(u"YUV")
        self.YUV.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.YUV)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.yuv_frame = QFrame(self.YUV)
        self.yuv_frame.setObjectName(u"yuv_frame")
        self.yuv_frame.setFrameShape(QFrame.StyledPanel)
        self.yuv_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.yuv_frame)

        self.tabWidget.addTab(self.YUV, "")

        self.horizontalLayout_12.addWidget(self.tabWidget)


        self.horizontalLayout_3.addWidget(self.graph_frame)


        self.horizontalLayout.addWidget(self.photo_frame)

        self.StackedWidget.addWidget(self.color_space_page)
        self.masking_page = QWidget()
        self.masking_page.setObjectName(u"masking_page")
        self.horizontalLayout_16 = QHBoxLayout(self.masking_page)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.masking_page_general_vlayout = QVBoxLayout()
        self.masking_page_general_vlayout.setObjectName(u"masking_page_general_vlayout")
        self.mask_top_frame = QFrame(self.masking_page)
        self.mask_top_frame.setObjectName(u"mask_top_frame")
        self.mask_top_frame.setMaximumSize(QSize(16777, 80))
        self.mask_top_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.mask_top_frame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton = QPushButton(self.mask_top_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"../../../Desktop/chgk.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.horizontalLayout_19.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.mask_top_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 70))
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.pushButton_2)


        self.masking_page_general_vlayout.addWidget(self.mask_top_frame)

        self.mask_bottom_frame = QFrame(self.masking_page)
        self.mask_bottom_frame.setObjectName(u"mask_bottom_frame")
        self.mask_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.mask_bottom_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.mask_bottom_frame_layout = QHBoxLayout()
        self.mask_bottom_frame_layout.setObjectName(u"mask_bottom_frame_layout")
        self.mask_photo_frame = QFrame(self.mask_bottom_frame)
        self.mask_photo_frame.setObjectName(u"mask_photo_frame")
        self.mask_photo_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_photo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.mask_photo_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.mask_photo = QLabel(self.mask_photo_frame)
        self.mask_photo.setObjectName(u"mask_photo")
        self.mask_photo.setMinimumSize(QSize(450, 0))

        self.horizontalLayout_18.addWidget(self.mask_photo)


        self.mask_bottom_frame_layout.addWidget(self.mask_photo_frame)

        self.mask_graph_frame = QFrame(self.mask_bottom_frame)
        self.mask_graph_frame.setObjectName(u"mask_graph_frame")
        self.mask_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_graph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mask_graph_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mask_1_graph_frame = QFrame(self.mask_graph_frame)
        self.mask_1_graph_frame.setObjectName(u"mask_1_graph_frame")
        self.mask_1_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_1_graph_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.mask_1_graph_frame)

        self.mask_1_above_slider = QSlider(self.mask_graph_frame)
        self.mask_1_above_slider.setObjectName(u"mask_1_above_slider")
        self.mask_1_above_slider.setMaximum(254)
        self.mask_1_above_slider.setOrientation(Qt.Horizontal)
        self.mask_1_above_slider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.mask_1_above_slider)

        self.mask_1_below_slider = QSlider(self.mask_graph_frame)
        self.mask_1_below_slider.setObjectName(u"mask_1_below_slider")
        self.mask_1_below_slider.setMaximum(255)
        self.mask_1_below_slider.setSliderPosition(255)
        self.mask_1_below_slider.setOrientation(Qt.Horizontal)
        self.mask_1_below_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.mask_1_below_slider)

        self.mask_2_graph_frame = QFrame(self.mask_graph_frame)
        self.mask_2_graph_frame.setObjectName(u"mask_2_graph_frame")
        self.mask_2_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_2_graph_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.mask_2_graph_frame)

        self.mask_2_above_slider = QSlider(self.mask_graph_frame)
        self.mask_2_above_slider.setObjectName(u"mask_2_above_slider")
        self.mask_2_above_slider.setMaximum(255)
        self.mask_2_above_slider.setOrientation(Qt.Horizontal)
        self.mask_2_above_slider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.mask_2_above_slider)

        self.mask_2_below_slider = QSlider(self.mask_graph_frame)
        self.mask_2_below_slider.setObjectName(u"mask_2_below_slider")
        self.mask_2_below_slider.setMaximum(255)
        self.mask_2_below_slider.setSliderPosition(255)
        self.mask_2_below_slider.setOrientation(Qt.Horizontal)
        self.mask_2_below_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.mask_2_below_slider)

        self.mask_3_graph_frame = QFrame(self.mask_graph_frame)
        self.mask_3_graph_frame.setObjectName(u"mask_3_graph_frame")
        self.mask_3_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.mask_3_graph_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.mask_3_graph_frame)

        self.mask_3_above_slider = QSlider(self.mask_graph_frame)
        self.mask_3_above_slider.setObjectName(u"mask_3_above_slider")
        self.mask_3_above_slider.setMaximum(255)
        self.mask_3_above_slider.setSliderPosition(0)
        self.mask_3_above_slider.setOrientation(Qt.Horizontal)
        self.mask_3_above_slider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.mask_3_above_slider)

        self.mask_3_below_slider = QSlider(self.mask_graph_frame)
        self.mask_3_below_slider.setObjectName(u"mask_3_below_slider")
        self.mask_3_below_slider.setMaximum(255)
        self.mask_3_below_slider.setValue(255)
        self.mask_3_below_slider.setSliderPosition(255)
        self.mask_3_below_slider.setOrientation(Qt.Horizontal)
        self.mask_3_below_slider.setInvertedAppearance(False)
        self.mask_3_below_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_2.addWidget(self.mask_3_below_slider)


        self.mask_bottom_frame_layout.addWidget(self.mask_graph_frame)


        self.horizontalLayout_17.addLayout(self.mask_bottom_frame_layout)


        self.masking_page_general_vlayout.addWidget(self.mask_bottom_frame)


        self.horizontalLayout_16.addLayout(self.masking_page_general_vlayout)

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
        self.tabWidget.setCurrentIndex(0)


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
#if QT_CONFIG(tooltip)
        self.StackedWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>background-color:none;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.StackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.StackedWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.photo.setText("")
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"Import Image ", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RGB), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HSV), QCoreApplication.translate("MainWindow", u"HSV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YUV), QCoreApplication.translate("MainWindow", u"YUV", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mask_photo.setText("")
    # retranslateUi

