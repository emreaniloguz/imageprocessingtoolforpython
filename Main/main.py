import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient,QImage)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# GUI FILE
from ui_python import Ui_MainWindow
import matplotlib
import cv2
import random
from functions import *
from mpl_toolkits import mplot3d
import numpy as np

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



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Creating Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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
        self.rgb_layout.addWidget(self.rgb_pushbutton)


        self.hsv_layout = QVBoxLayout()
        self.ui.hsv_frame.setLayout(self.hsv_layout)
        self.hsv_layout.addWidget(self.hsv_canvas)
        self.hsv_layout.addWidget(self.hsv_pushbutton)

        self.yuv_layout = QVBoxLayout()
        self.ui.yuv_frame.setLayout(self.yuv_layout)
        self.yuv_layout.addWidget(self.yuv_canvas)
        self.yuv_layout.addWidget(self.yuv_pushbutton)


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



        self.ui.pushButton_3.clicked.connect(self.prepare_when_return)








        self.show()


    def update_plot(self,graph_type):
        self.graph_type = graph_type
        try:
            img_path = self.path
            img = cv2.imread(img_path)

            scale = max(img.shape[0], img.shape[1], 128) / 128  # at most 64 rows and columns
        except:
            pass
        self.img = img
        img = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)),
                         interpolation=cv2.INTER_NEAREST)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = img / 255

        if self.graph_type == 0:




            self.canvas.axes.clear()
            self.canvas.axes.set_xlabel("R", color=(1, 1, 1, 1))
            self.canvas.axes.set_ylabel("G", color=(1, 1, 1, 1))
            self.canvas.axes.set_zlabel("B", color=(1, 1, 1, 1))
            self.canvas.axes.tick_params(axis="x", colors=(1, 1, 1, 1))
            self.canvas.axes.tick_params(axis="y", colors=(1, 1, 1, 1))
            self.canvas.axes.tick_params(axis="z", colors=(1, 1, 1, 1))

            self.canvas.axes.scatter(img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:, :, 2].ravel(),
                              c=img_rgb.reshape((-1, 3)), edgecolors='none')

            self.canvas.draw()

        elif self.graph_type==1:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            img_hsv_c = img_hsv / 255

            self.hsv_canvas.axes_2.clear()
            self.hsv_canvas.axes_2.scatter(img_hsv[:, :, 0].ravel(), img_hsv[:, :, 1].ravel(), img_hsv[:, :, 2].ravel(),
                              c=img_hsv_c.reshape((-1, 3)), edgecolors='none')
            self.hsv_canvas.axes_2.set_xlabel("H", color=(1, 1, 1, 1))
            self.hsv_canvas.axes_2.set_ylabel("S", color=(1, 1, 1, 1))
            self.hsv_canvas.axes_2.set_zlabel("V", color=(1, 1, 1, 1))
            self.hsv_canvas.axes_2.tick_params(axis="x", colors=(1, 1, 1, 1))
            self.hsv_canvas.axes_2.tick_params(axis="y", colors=(1, 1, 1, 1))
            self.hsv_canvas.axes_2.tick_params(axis="z", colors=(1, 1, 1, 1))
            self.hsv_canvas.draw()

        elif self.graph_type==2:

            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            img_yuv_c = img_yuv / 255

            self.yuv_canvas.axes_3.clear()
            self.yuv_canvas.axes_3.scatter(img_yuv[:, :, 0].ravel(), img_yuv[:, :, 1].ravel(), img_yuv[:, :, 2].ravel(),
                              c=img_yuv_c.reshape((-1, 3)), edgecolors='none')
            self.yuv_canvas.axes_3.set_xlabel("Y", color=(1, 1, 1, 1))
            self.yuv_canvas.axes_3.set_ylabel("U", color=(1, 1, 1, 1))
            self.yuv_canvas.axes_3.set_zlabel("V", color=(1, 1, 1, 1))
            self.yuv_canvas.axes_3.tick_params(axis="x", colors=(1, 1, 1, 1))
            self.yuv_canvas.axes_3.tick_params(axis="y", colors=(1, 1, 1, 1))
            self.yuv_canvas.axes_3.tick_params(axis="z", colors=(1, 1, 1, 1))
            self.yuv_canvas.draw()






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
        self.rgb_pushbutton = QPushButton("Choose RGB")
        self.hsv_pushbutton = QPushButton("Choose HSV")
        self.yuv_pushbutton = QPushButton("Choose YUV")

        #pass

    def prepare_stylesheets(self,button):
        button.setStyleSheet("""QPushButton{
                	background-color: none;
                	background-color: rgb(189, 147, 249);
                	border: 5px;
                	border-radius: 5px;
                	border: rgb(35, 35, 35);
                	font: 8pt "Segoe MDL2 Assets";
                }
                QPushButton:hover{
                	background-color: rgb(150, 117, 198);
                	color: rgb(220, 220, 220);

                }""")


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
                self.mask_1_canvas.draw()


            elif self.graph_type==1:

                self.mask_2_canvas.axes.clear()
                self.histr_g = cv2.calcHist([self.img], [1], None, [256], [0, 256])
                self.mask_2_canvas.axes.plot(self.histr_g, color='g')
                self.mask_2_canvas.draw()

            elif self.graph_type==2:

                self.mask_3_canvas.axes.clear()
                self.histr_b = cv2.calcHist([self.img], [2], None, [256], [0, 256])
                self.mask_3_canvas.axes.plot(self.histr_b, color='b')
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
            self.mask_1_canvas.axes.clear()

            self.mask_1_canvas.axes.plot(self.histr, color='r')
            #self.r_canvas.axes.xlim([0, 256])
            self.mask_1_canvas.axes.axvline(self.ui.mask_1_above_slider.value(), 0, 255)
            self.mask_1_canvas.axes.axvline(self.ui.mask_1_below_slider.value(),0,255)

            self.mask_1_canvas.draw()
            self.update_pixmap()

    def slider_2(self):
        if self.ui.mask_2_above_slider.value()==0:
            pass
        else:
            self.mask_2_canvas.axes.clear()

            self.mask_2_canvas.axes.plot(self.histr_g, color='g')
            self.mask_2_canvas.axes.axvline(self.ui.mask_2_above_slider.value(), 0, 255)
            self.mask_2_canvas.axes.axvline(self.ui.mask_2_below_slider.value(),0,255)
            self.mask_2_canvas.draw()
            self.update_pixmap()


    def slider_3(self):
        if self.ui.mask_3_above_slider.value()==0:
            pass

        else:

            self.mask_3_canvas.axes.clear()
            self.mask_3_canvas.axes.plot(self.histr_b, color='b')
            self.mask_3_canvas.axes.axvline(self.ui.mask_3_above_slider.value(), 0, 255)
            self.mask_3_canvas.axes.axvline(self.ui.mask_3_below_slider.value(),0,255)
            self.mask_3_canvas.draw()
            self.update_pixmap()




    def update_pixmap(self):
        self.im_cpy = self.img
        self.lower_blue = np.array(
            [self.ui.mask_1_above_slider.value(), self.ui.mask_2_above_slider.value(), self.ui.mask_3_above_slider.value()])
        self.upper_blue = np.array([self.ui.mask_1_below_slider.value(), self.ui.mask_2_below_slider.value(), self.ui.mask_3_below_slider.value()])




        self.mask = cv2.inRange(self.im_cpy, self.lower_blue, self.upper_blue)
        self.mask = cv2.bitwise_and(self.im_cpy, self.im_cpy, mask=self.mask)
        # self.im_cpy  = cv2.cvtColor(self.im_cpy, cv2.COLOR_BGR2HSV)
        self.mask = cv2.cvtColor(self.mask, cv2.COLOR_HSV2RGB)
        height, width, channels = self.mask.shape
        bpl = 3 * width
        self.pixmap = QImage(self.mask, width, height, bpl, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(self.pixmap)
        self.pixmap = self.pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.mask_photo.setPixmap(self.pixmap)


    def prepare_when_return(self):
        self.mask_1_canvas.axes.clear()
        self.mask_2_canvas.axes.clear()
        self.mask_3_canvas.axes.clear()
        self.ui.StackedWidget.setCurrentWidget(self.ui.color_space_page)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())