import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_browsefile import Ui_MainWindow

# IMPORT FUNCTIONS

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browse_file)









        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def browse_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', 'E:\Games', 'Image Files (*.png *.jpg *.jpeg)')
        self.ui.lineEdit.setText(filename[0])
        pixmap = QPixmap(filename[0])
        pixmap = pixmap.scaled(720,600, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.label.setPixmap(pixmap)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())