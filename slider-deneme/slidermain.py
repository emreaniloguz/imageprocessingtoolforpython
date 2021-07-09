import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient,QImage)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# GUI FILE
from sliderui import Ui_MainWindow
import cv2
import numpy  as np
import math


# IMPORT FUNCTIONS
class MplCanvas(FigureCanvas):

    def __init__(self, graph_type,parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.j=0


        self.r_canvas = MplCanvas(0,width=5, height=4, dpi=100)
        self.g_canvas = MplCanvas(0,width=5, height=4, dpi=100)
        self.b_canvas = MplCanvas(0,width=5, height=4, dpi=100)


        self.r_layout = QHBoxLayout()
        self.ui.r_frame.setLayout(self.r_layout)
        self.r_layout.addWidget(self.r_canvas)

        self.g_layout = QHBoxLayout()
        self.ui.g_frame.setLayout(self.g_layout)
        self.g_layout.addWidget(self.g_canvas)

        self.b_layout = QHBoxLayout()
        self.ui.b_frame.setLayout(self.b_layout)
        self.b_layout.addWidget(self.b_canvas)





        self.ui.pushButton.clicked.connect(self.import_button_clicked)
        self.ui.rSlider_a.valueChanged.connect(self.slider)
        self.ui.rSlider.valueChanged.connect(self.slider)
        self.ui.horizontalSlider_2.valueChanged.connect(self.slider_g)
        self.ui.gSlider.valueChanged.connect(self.slider_g)
        self.ui.bSlider_a.valueChanged.connect(self.slider_b)
        self.ui.bSlider.valueChanged.connect(self.slider_b)


        self.ui.invert_button.clicked.connect(self.invert_mask)
        self.ui.normal_button.clicked.connect(self.normal_mask)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



    def import_button_clicked(self):

        filename = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/emrea/Desktop',
                                               'Image Files (*.png *.jpg *.jpeg)')

        self.path = filename[0]
        self.pixmap = QPixmap(filename[0])
        self.pixmap = self.pixmap.scaled(720, 720, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.label.setPixmap(self.pixmap)
        self.update_plot(0)
        self.update_plot(1)
        self.update_plot(2)


    def update_plot(self,graph_type):
        self.graph_type = graph_type
        try:
            self.img_path = self.path
            self.img = cv2.imread(self.img_path)
            scale = max(self.img.shape[0], self.img.shape[1], 256) / 256  # at most 64 rows and columns
        except:
            pass

        self.img = cv2.resize(self.img, (np.int(self.img.shape[1] ), np.int(self.img.shape[0])),
                         interpolation=cv2.INTER_NEAREST)

        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        (self.r,self.g,self.b) = cv2.split(self.img)
        self.r=cv2.calcHist(self.img,[0], None, [255], [0, 255])
        self.g = cv2.calcHist(self.img,[1],None,[255],[0,255])
        self.b = cv2.calcHist(self.img,[2],None,[255],[0,255])
        self.img_rgb = self.img / 255
        #w = 7
        #n = math.ceil((self.r.ravel().max() - self.r.ravel().min()) / w)

        if self.graph_type == 0:

            self.r_canvas.axes.clear()
            self.histr = cv2.calcHist([self.img], [0], None, [256], [0, 256])
            self.r_canvas.axes.plot(self.histr, color='r')
            self.r_canvas.draw()







        elif self.graph_type==1:

            self.g

            self.histr_g = cv2.calcHist([self.img], [1], None, [256], [0, 256])
            self.g_canvas.axes.plot(self.histr_g, color='g')





        elif self.graph_type==2:

            self.histr_b = cv2.calcHist([self.img], [2], None, [256], [0, 256])
            self.b_canvas.axes.plot(self.histr_b, color='b')





    def slider(self):

        if self.ui.rSlider_a.value()==0:
            pass
        else:
            self.r_canvas.axes.clear()

            self.r_canvas.axes.plot(self.histr, color='r')
            #self.r_canvas.axes.xlim([0, 256])
            self.r_canvas.axes.axvline(self.ui.rSlider_a.value(), 0, 255)
            self.r_canvas.axes.axvline(self.ui.rSlider.value(),0,255)

            self.r_canvas.draw()
            self.update_pixmap()

    def slider_g(self):
        if self.ui.horizontalSlider_2.value()==0:
            pass
        else:
            self.g_canvas.axes.clear()

            self.g_canvas.axes.plot(self.histr_g, color='g')
            self.g_canvas.axes.axvline(self.ui.horizontalSlider_2.value(), 0, 255)
            self.g_canvas.axes.axvline(self.ui.gSlider.value(),0,255)
            self.g_canvas.draw()
            self.update_pixmap()


    def slider_b(self):
        if self.ui.gSlider.value()==0:
            pass
        else:
            self.b_canvas.axes.clear()
            self.b_canvas.axes.plot(self.histr_b, color='b')
            self.b_canvas.axes.axvline(self.ui.bSlider_a.value(), 0, 255)
            self.b_canvas.axes.axvline(self.ui.bSlider.value(),0,255)
            self.b_canvas.draw()
            self.update_pixmap()





    def invert_mask(self):

        pass

    def normal_mask(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())