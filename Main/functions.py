from  main import *


class Functions(MainWindow):


    def import_button_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/emrea/Desktop', 'Image Files (*.png *.jpg *.jpeg)')
        pixmap = QPixmap(filename[0])
        pixmap = pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.photo.setPixmap(pixmap)