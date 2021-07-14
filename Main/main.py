import sys
import platform
import time
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient,QImage)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# GUI FILE
from ui_python import Ui_MainWindow
import matplotlib
import cv2
import random
from functions import *
from mpl_toolkits import mplot3d
import numpy as np
from ui_splash_screen import Ui_SplashScreen

# IMPORT FUNCTIONS
class HistCanvas(FigureCanvas):

    def __init__(self, graph_type,parent=None, width=5, height=4, dpi=100,facecolor=(31/255,31/255,31/255,1)):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor=facecolor)
        self.axes = fig.add_subplot(111)
        self.axes.set_facecolor((31 / 255, 31 / 255, 31 / 255, 1))


        super(HistCanvas, self).__init__(fig)

class MplCanvas(FigureCanvas):

    def __init__(self, graph_type,parent=None, width=5, height=4, dpi=100,facecolor=(41/255,41/255,41/255,1)):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor=facecolor)

        if graph_type==0:
           self.axes = fig.add_subplot(111, projection='3d')
           self.axes.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))


        elif graph_type == 1:

          self.axes_2 = fig.add_subplot(111, projection='3d')
          self.axes_2.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))



        elif graph_type==2:
          self.axes_3 = fig.add_subplot(111, projection='3d')
          self.axes_3.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))

        super(MplCanvas, self).__init__(fig)

flag = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Creating Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Remove title bar

        self.canvas = MplCanvas(0,width=5, height=4, dpi=100)
        self.hsv_canvas = MplCanvas(1, width=5, height=4, dpi=100)
        self.yuv_canvas = MplCanvas(2,width=5, height=4, dpi=100)


        self.create_buttons()
        self.prepare_stylesheets(self.rgb_pushbutton)
        self.prepare_stylesheets(self.hsv_pushbutton)
        self.prepare_stylesheets(self.yuv_pushbutton)


        self.rgb_layout = QVBoxLayout()
        self.ui.rgb_frame.setLayout(self.rgb_layout)
        self.rgb_layout.addWidget(self.canvas)
        self.rgb_layout.addWidget(self.rgb_pushbutton, 0, Qt.AlignHCenter)


        self.hsv_layout = QVBoxLayout()
        self.ui.hsv_frame.setLayout(self.hsv_layout)
        self.hsv_layout.addWidget(self.hsv_canvas)
        self.hsv_layout.addWidget(self.hsv_pushbutton, 9, Qt.AlignHCenter)

        self.yuv_layout = QVBoxLayout()
        self.ui.yuv_frame.setLayout(self.yuv_layout)
        self.yuv_layout.addWidget(self.yuv_canvas)
        self.yuv_layout.addWidget(self.yuv_pushbutton, 9, Qt.AlignHCenter)



        #
        self.mask_1_canvas = HistCanvas(0,width=5,height=4,dpi=100)
        self.mask_2_canvas = HistCanvas(0,width=5,height=4,dpi=100)
        self.mask_3_canvas = HistCanvas(0)
        #
        self.mask_1_layout = QHBoxLayout()
        self.mask_2_layout = QHBoxLayout()
        self.mask_3_layout = QHBoxLayout()
        #
        self.ui.mask_1_graph_frame.setLayout(self.mask_1_layout)
        self.ui.mask_2_graph_frame.setLayout(self.mask_2_layout)
        self.ui.mask_3_graph_frame.setLayout(self.mask_3_layout)
        #
        self.mask_1_layout.addWidget(self.mask_1_canvas)
        self.mask_2_layout.addWidget(self.mask_2_canvas)
        self.mask_3_layout.addWidget(self.mask_3_canvas)




        #Import Image
        self.ui.import_button.clicked.connect(self.import_button_clicked)

        #Create Color Space Graphs
        #Functions.create_graphs(self,self.ui.yuv_frame)
        #Functions.create_graphs(self, self.ui.hsv_frame)
        #Functions.create_graphs(self, self.ui.rgb_frame)


        #self.rgb_pushbutton.clicked.connect(lambda: self.ui.StackedWidget.setCurrentWidget(self.ui.masking_page))
        self.rgb_pushbutton.clicked.connect(self.prepare_rgb_mask_page)
        self.hsv_pushbutton.clicked.connect(self.prepare_hsv_mask_page)


        self.ui.mask_1_above_slider.valueChanged.connect(self.slider_1)
        self.ui.mask_1_below_slider.valueChanged.connect(self.slider_1)

        self.ui.mask_2_above_slider.valueChanged.connect(self.slider_2)
        self.ui.mask_2_below_slider.valueChanged.connect(self.slider_2)


        self.ui.mask_3_above_slider.valueChanged.connect(self.slider_3)
        self.ui.mask_3_below_slider.valueChanged.connect(self.slider_3)

        global flag

        self.ui.pushButton_3.clicked.connect(self.prepare_when_return)
        self.ui.invert_mask_btn.clicked.connect(self.invert_mask)

        #to switch between mask and invert mask
        if flag == 0:
            self.ui.mask_btn.clicked.connect(self.update_pixmap)
            flag = 1
        else:
            self.ui.mask_btn.clicked.connect(self.invert_mask)
            flag = 0

        self.ui.export_btn.clicked.connect(self.export_as_function)
        self.ui.contour_btn.clicked.connect(self.apply_contour)
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_button.clicked.connect(lambda: self.restore_or_maximize_window())

        def move_window(e): #to moving window
            if self.isMaximized() == False:         #If page is maximized, it stays stable
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header.mouseMoveEvent = move_window

        self.show()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


    def update_plot(self,graph_type):
        self.graph_type = graph_type
        try:
            img_path = self.path
            img = cv2.imread(img_path)

            scale = max(img.shape[0], img.shape[1], 128) / 128  # at most 64 rows and columns
        except:
            pass
        self.img = img
        self.unchanged= self.img
        self.unchanged = cv2.cvtColor(self.unchanged, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)),
                         interpolation=cv2.INTER_NEAREST)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = img / 255

        if self.graph_type == 0:

            self.prepare_3d_graph(self.canvas,img,"RGB",img_rgb)


        elif self.graph_type==1:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            img_hsv_c = img_hsv / 255



            self.prepare_3d_graph(self.hsv_canvas,img_hsv,"HSV",img_hsv_c)

        elif self.graph_type==2:

            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            img_yuv_c = img_yuv / 255

            self.prepare_3d_graph(self.yuv_canvas,img_yuv,"YUV",img_yuv_c)








    def import_button_clicked(self):

        filename = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/emrea/Desktop',
                                               'Image Files (*.png *.jpg *.jpeg)')

        self.path = filename[0]
        self.pixmap = QPixmap(filename[0])
        self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.photo.setPixmap(self.pixmap)




        self.update_plot(0)
        self.update_plot(1)
        self.update_plot(2)




    def create_buttons(self):
        self.rgb_pushbutton = QPushButton("    Choose RGB    ")
        self.hsv_pushbutton = QPushButton("    Choose HSV    ")
        self.yuv_pushbutton = QPushButton("    Choose YUV    ")

        #pass

    def prepare_stylesheets(self,button):
        button.setStyleSheet("""QPushButton{
                background-color: none;
                background-color:rgb(80,80,80);
                border: 10px;
                border-radius: 5px;
                border: rgb(35, 35, 35);
                color: rgb(225, 225, 225);
                font: 75 8pt "MS Shell Dlg 2";
            }
            QPushButton:hover{
                background-color:#3f3f3f ;
                
            }""")
        button.setMaximumSize(QSize(120, 30))




    def prepare_rgb_mask_page(self):

        self.ui.StackedWidget.setCurrentWidget(self.ui.masking_page)
        self.ui.mask_photo.setPixmap(self.pixmap)

        #
        self.update_mask_plot(0,0)
        self.update_mask_plot(1,0)
        self.update_mask_plot(2,0)

    def prepare_hsv_mask_page(self):
        self.ui.StackedWidget.setCurrentWidget(self.ui.masking_page)
        self.ui.mask_photo.setPixmap(self.pixmap)
        #

        self.update_mask_plot(0,1)
        self.update_mask_plot(1,1)
        self.update_mask_plot(2,1)


    def update_mask_plot(self,graph_type,color_space):

        if color_space == 0:

            self.graph_type = graph_type
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

            self.img_rgb = self.img / 255

            if self.graph_type == 0:

                self.mask_1_canvas.axes.clear()
                self.histr = cv2.calcHist([self.img], [0], None, [256], [0, 256])
                self.mask_1_canvas.axes.plot(self.histr, color='r')
                self.mask_1_canvas.axes.tick_params(axis="x", colors=(1, 1, 1, 1))
                self.mask_1_canvas.axes.tick_params(axis="y", colors=(1, 1, 1, 1))

                self.mask_1_canvas.draw()


            elif self.graph_type==1:

                self.mask_2_canvas.axes.clear()
                self.histr_g = cv2.calcHist([self.img], [1], None, [256], [0, 256])
                self.mask_2_canvas.axes.plot(self.histr_g, color='g')
                self.mask_2_canvas.axes.tick_params(axis="x", colors=(1, 1, 1, 1))
                self.mask_2_canvas.axes.tick_params(axis="y", colors=(1, 1, 1, 1))

                self.mask_2_canvas.draw()

            elif self.graph_type==2:

                self.mask_3_canvas.axes.clear()
                self.histr_b = cv2.calcHist([self.img], [2], None, [256], [0, 256])
                self.mask_3_canvas.axes.plot(self.histr_b, color='b')
                self.mask_3_canvas.axes.tick_params(axis="x", colors=(1, 1, 1, 1))
                self.mask_3_canvas.axes.tick_params(axis="y", colors=(1, 1, 1, 1))

                self.mask_3_canvas.draw()
        if color_space == 1:
            self.graph_type = graph_type
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

            self.img_rgb = self.img / 255

            if self.graph_type == 0:

                self.mask_1_canvas.axes.clear()
                self.histr = cv2.calcHist([self.img], [0], None, [256], [0, 256])
                self.mask_1_canvas.axes.plot(self.histr, color='r')
                self.mask_1_canvas.draw()


            elif self.graph_type == 1:

                self.mask_2_canvas.axes.clear()
                self.histr_g = cv2.calcHist([self.img], [1], None, [256], [0, 256])
                self.mask_2_canvas.axes.plot(self.histr_g, color='g')
                self.mask_2_canvas.draw()

            elif self.graph_type == 2:

                self.mask_3_canvas.axes.clear()
                self.histr_b = cv2.calcHist([self.img], [2], None, [256], [0, 256])
                self.mask_3_canvas.axes.plot(self.histr_b, color='b')
                self.mask_3_canvas.draw()





    def slider_1(self):

        if self.ui.mask_1_above_slider.value()==0:
            pass
        else:
            self.prepare_hist_graph_styles(self.mask_1_canvas,self.ui.mask_1_above_slider.value()
                                           ,self.ui.mask_1_below_slider.value(),self.histr,"r")
            self.update_pixmap()

    def slider_2(self):
        if self.ui.mask_2_above_slider.value()==0:
            pass
        else:
            self.prepare_hist_graph_styles(self.mask_2_canvas,self.ui.mask_2_above_slider.value()
                                           ,self.ui.mask_2_below_slider.value(),self.histr_g,"g")

            self.update_pixmap()


    def slider_3(self):
        if self.ui.mask_3_above_slider.value()==0:
            pass

        else:

            self.prepare_hist_graph_styles(self.mask_3_canvas,self.ui.mask_3_above_slider.value()
                                           ,self.ui.mask_3_below_slider.value(),self.histr_b,"b")
            self.update_pixmap()




    def update_pixmap(self):
        self.im_cpy = self.img
        self.lower_blue = np.array(
            [self.ui.mask_1_above_slider.value(), self.ui.mask_2_above_slider.value(), self.ui.mask_3_above_slider.value()])
        self.upper_blue = np.array([self.ui.mask_1_below_slider.value(), self.ui.mask_2_below_slider.value(), self.ui.mask_3_below_slider.value()])




        self.mask = cv2.inRange(self.im_cpy, self.lower_blue, self.upper_blue)
        self.normal_mask = cv2.bitwise_and(self.unchanged, self.unchanged, mask=self.mask)
        # self.im_cpy  = cv2.cvtColor(self.im_cpy, cv2.COLOR_BGR2HSV)
        #self.mask = cv2.cvtColor(self.mask, cv2.COLOR_HSV2RGB)
        height, width, channels = self.normal_mask.shape
        bpl = 3 * width
        self.pixmap = QImage(self.normal_mask, width, height, bpl, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(self.pixmap)
        self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.mask_photo.setPixmap(self.pixmap)


    def prepare_when_return(self):
        self.mask_1_canvas.axes.clear()
        self.mask_2_canvas.axes.clear()
        self.mask_3_canvas.axes.clear()
        self.ui.mask_1_below_slider.setSliderPosition(255)
        self.ui.mask_1_above_slider.setSliderPosition(0)
        self.ui.mask_2_below_slider.setSliderPosition(255)
        self.ui.mask_2_above_slider.setSliderPosition(0)
        self.ui.mask_3_below_slider.setSliderPosition(255)
        self.ui.mask_3_above_slider.setSliderPosition(0)



        self.ui.StackedWidget.setCurrentWidget(self.ui.color_space_page)

    def prepare_hist_graph_styles(self,canvas,above,below,hist,clr):
        canvas.axes.clear()
        canvas.axes.tick_params(axis="x",colors=(1,1,1,1))
        canvas.axes.tick_params(axis="y",colors=(1,1,1,1))
        canvas.axes.axvline(above,0,255)
        canvas.axes.axvline(below,0,255)
        canvas.axes.plot(hist,color=clr)
        canvas.draw()



    def prepare_3d_graph(self,canvas,img,c_spc,dot_c):
        if canvas == self.canvas:
            axs = self.canvas.axes
        elif canvas == self.hsv_canvas:
            axs = self.hsv_canvas.axes_2
        else:
            axs = self.yuv_canvas.axes_3

        x_title =c_spc[0]
        y_title = c_spc[1]
        z_title = c_spc[2]
        axs.clear()
        axs.scatter(img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:, :, 2].ravel(),
                c=dot_c.reshape((-1, 3)), edgecolors='none')
        axs.set_xlabel(x_title, color = (1,1,1,1))
        axs.set_ylabel(y_title,color = (1,1,1,1))
        axs.set_zlabel(z_title, color = (1,1,1,1))
        axs.tick_params(axis="x",colors=(1,1,1,1))
        axs.tick_params(axis="y",colors=(1,1,1,1))
        axs.tick_params(axis="z",colors=(1,1,1,1))

        canvas.draw()


    def invert_mask(self):

        self.invert_msk =  cv2.bitwise_not(self.mask)
        self.invert_msk = cv2.bitwise_and(self.unchanged, self.unchanged, mask= self.invert_msk)
        height, width, channels = self.invert_msk.shape
        bpl = 3 * width
        self.pixmap = QImage(self.invert_msk, width, height, bpl, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(self.pixmap)
        self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.mask_photo.setPixmap(self.pixmap)

    def apply_contour(self):

        if self.invert_msk == None:
            im2, contours, hierarchy = cv2.findContours(self.pixmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(self.normal_mask, contours, -1, (0, 255, 0), 3)
            height, width, channels = self.normal_mask.shape
            bpl = 3 * width
            self.pixmap = QImage(self.normal_mask, width, height, bpl, QImage.Format_RGB888)
            self.pixmap = QPixmap.fromImage(self.pixmap)
            self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.ui.mask_photo.setPixmap(self.pixmap)

        elif self.normal_mask == None:
            im2, contours, hierarchy = cv2.findContours(self.pixmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(self.invert_msk, contours, -1, (0, 255, 0), 3)
            height, width, channels = self.invert_msk.shape
            bpl = 3 * width
            self.pixmap = QImage(self.invert_msk, width, height, bpl, QImage.Format_RGB888)
            self.pixmap = QPixmap.fromImage(self.pixmap)
            self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.ui.mask_photo.setPixmap(self.pixmap)




    def export_as_function(self):


        self.function_file = open("C:/Users/emrea/Desktop/image_mask_values.py", 'w')

        self.function_file.write("import numpy as np \nimport cv2 \nimport sys\n \n \n \n")
        self.function_file.write('original_img = cv2.imread("'+self.path+'"'+")\n")

        self.function_file.write(
                                 "min_value = np.array(["+str(self.ui.mask_3_above_slider.value())+","+str(self.ui.mask_2_above_slider.value())+","+
                                 str(self.ui.mask_1_above_slider.value())+"])\n"
                                 )

        self.function_file.write("max_value = np.array(["+str(self.ui.mask_3_below_slider.value()) + ","+ str(self.ui.mask_2_below_slider.value())+","+
                                 str(self.ui.mask_1_below_slider.value())+"])\n")


        self.function_file.write("masked_range = cv2.inRange(original_img, min_value, max_value)\n")

        self.function_file.write("masked_img = cv2.bitwise_and(original_img, original_img, mask=masked_range)\n")

        self.function_file.write("invert_masked_range= cv2.bitwise_not(masked_range)\n")


        self.function_file.write("invert_masked_img = cv2.bitwise_and(original_img, original_img, mask = invert_masked_range)\n")

        self.function_file.write("cv2.imshow('Masked',masked_img)\n")
        self.function_file.write("cv2.imshow('Invert Masked', invert_masked_img)\n")

        self.function_file.write("if cv2.waitKey(0) & 0xFF == ord('q'):\n \t sys.exit()\n")

        self.function_file.write("cv2.destroyAllWindows()")

        self.function_file.close()

    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "0.992"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

#GLOBALS
counter = 0
jumper = 10

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.progress_bar.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ## DEF TO LOANDING
        ########################################################################

    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))
        if (value >= jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.percent.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value > 100:
            value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

        ## DEF PROGRESS BAR VALUE
        ########################################################################

    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
           QFrame{
           	border-radius: 150px;
           	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
           }
           """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.progress_bar.setStyleSheet(newStylesheet)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())