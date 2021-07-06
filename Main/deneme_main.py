import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# GUI FILE
from deneme import Ui_MainWindow
import matplotlib
import random
import cv2
from mpl_toolkits import mplot3d
import numpy as np


from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111,projection='3d')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Creating Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.h_box = QHBoxLayout()
        self.ui.frame_2.setLayout(self.h_box)
        self.h_box.addWidget(self.canvas)

        #Import Image
        self.ui.pushButton.clicked.connect(self.import_button_clicked)

        #Create Color Space Graphs
        #Functions.create_graphs(self,self.ui.yuv_frame)
        #Functions.create_graphs(self, self.ui.hsv_frame)
        #Functions.create_graphs(self, self.ui.rgb_frame)








        self.show()


    def update_plot(self):
        try:
            img_path = self.path
            img = cv2.imread(img_path)
            scale = max(img.shape[0], img.shape[1], 128) / 128  # at most 64 rows and columns
        except:
            pass

        img = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)),
                         interpolation=cv2.INTER_NEAREST)

        if self.graph_type == 0:
            try:
                pass
            except:
                pass
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_rgb = img / 255

            self.canvas.axes.clear()
            self.canvas.axes.scatter(img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:, :, 2].ravel(),
                              c=img_rgb.reshape((-1, 3)), edgecolors='none')

            self.canvas.draw()

            #self.axes.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))
            #self.axes.set_xlabel("R", color=(1, 1, 1, 1))
            #self.axes.set_ylabel("G", color=(1, 1, 1, 1))
            #self.axes.set_zlabel("B", color=(1, 1, 1, 1))
            #self.axes.tick_params(axis="x", colors=(1, 1, 1, 1))
            #self.axes.tick_params(axis="y", colors=(1, 1, 1, 1))
            #self.axes.tick_params(axis="z", colors=(1, 1, 1, 1))


    def import_button_clicked(self):

        filename = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/emrea/Desktop',
                                               'Image Files (*.png *.jpg *.jpeg)')

        self.path = filename[0]
        pixmap = QPixmap(filename[0])
        pixmap = pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.label.setPixmap(pixmap)
        self.graph_type=0
        self.update_plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())