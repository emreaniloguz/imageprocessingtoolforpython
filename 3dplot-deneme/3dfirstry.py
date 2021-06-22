import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# GUI FILE
from ui_python import Ui_MainWindow
import matplotlib
import random
from functions import *
from mpl_toolkits import mplot3d
import numpy as np

# IMPORT FUNCTIONS

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=2, height=2, dpi=100,facecolor=(41/255,41/255,41/255,1)):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor=facecolor)
        self.fig=fig
        self.axes = fig.add_subplot(111,projection='3d')

        self.compute_initial_figure()
        #super(MplCanvas, self).__init__(fig)
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.axes.mouse_init()




    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MplCanvas):
    # Simple canvas with a sine plot.
    def compute_initial_figure(self):
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2 * pi * t)
        # self.axes.plot(t, s)
        xs = [1, 2]
        ys = [1, 2]
        zs = [1, 2]

        self.axes.scatter(xs, ys, zs,color=(141 / 255, 188 / 255, 142 / 255, 1))
        self.axes.set_facecolor((41/255,41/255,41/255,1))

        self.axes.mouse_init()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.yuv_graph_layout = QHBoxLayout()
        self.hsv_graph_layout = QHBoxLayout()
        self.rgb_graph_layout = QHBoxLayout()



        self.ui.yuv_graph_frame.setLayout(self.yuv_graph_layout)
        self.ui.hsv_graph.setLayout(self.hsv_graph_layout)
        self.ui.rgb_graph.setLayout(self.rgb_graph_layout)




        self.yuv_graph = MyStaticMplCanvas(self, width=5, height= 2, dpi=220)
        self.hsv_graph = MyStaticMplCanvas(self, width=5,height=2, dpi=220)
        self.rgb_graph = MyStaticMplCanvas(self, width=5,height=2,dpi=220)


        self.ui.import_button.clicked.connect(lambda : Functions.import_button_clicked(self))


        self.yuv_graph_layout.addWidget(self.yuv_graph)
        self.hsv_graph_layout.addWidget(self.hsv_graph)
        self.rgb_graph_layout.addWidget(self.rgb_graph)

        self.show()

    def update_plot(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())