from  main import *
import cv2
import numpy as np

#class MplCanvas(FigureCanvas):
#
#    def __init__(self,graph_type, parent=None, width=2, height=2, dpi=100,facecolor=(41/255,41/255,41/255,1)):
#        global fig
#        fig = Figure(figsize=(width, height), dpi=dpi,facecolor=facecolor)
#
#        self.graph_type = graph_type
#
#
#        self.fig=fig
#        self.axes = fig.add_subplot(111,projection='3d')
#
#
#
#
#        self.compute_initial_figure()
#        #super(MplCanvas, self).__init__(fig)
#        FigureCanvas.__init__(self,self.fig)
#        self.setParent(parent)
#
#        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
#        FigureCanvas.updateGeometry(self)
#        self.axes.mouse_init()
#
#
#
#
#
#    def compute_initial_figure(self):
#        pass
#
#class MyStaticMplCanvas(MplCanvas):
#    # Simple canvas with a sine plot.
#    def compute_initial_figure(self):
#        try:
#            img_path=path
#            img = cv2.imread(img_path)
#            scale = max(img.shape[0], img.shape[1], 128) / 128  # at most 64 rows and columns
#        except:
#            pass
#
#        img = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)),interpolation=cv2.INTER_NEAREST)
#
#
#
#        if self.graph_type == 0:
#            try:
#                pass
#            except:
#                pass
#            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#            img_rgb = img / 255
#
#            self.axes.clear()
#            self.axes.scatter(img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:, :, 2].ravel(),
#                              c=img_rgb.reshape((-1, 3)), edgecolors='none')
#
#            self.axes.draw()
#
#            self.axes.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))
#            self.axes.set_xlabel("R",color=(1,1,1,1))
#            self.axes.set_ylabel("G",color=(1,1,1,1))
#            self.axes.set_zlabel("B",color=(1,1,1,1))
#            self.axes.tick_params(axis="x",colors=(1,1,1,1))
#            self.axes.tick_params(axis="y",colors=(1,1,1,1))
#            self.axes.tick_params(axis="z",colors=(1,1,1,1))
#
#
#
#
#
#            self.axes.mouse_init()
#
#        elif self.graph_type==1:
#            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#            img_hsv_c = img_hsv / 255
#
#            self.axes.scatter(img_hsv[:, :, 0].ravel(), img_hsv[:, :, 1].ravel(), img_hsv[:, :, 2].ravel(),
#                              c=img_hsv_c.reshape((-1, 3)), edgecolors='none')
#
#            self.axes.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))
#
#            self.axes.mouse_init()
#            self.axes.set_xlabel("H",color=(1,1,1,1))
#            self.axes.set_ylabel("S",color=(1,1,1,1))
#            self.axes.set_zlabel("V",color=(1,1,1,1))
#            self.axes.tick_params(axis="x",colors=(1,1,1,1))
#            self.axes.tick_params(axis="y",colors=(1,1,1,1))
#            self.axes.tick_params(axis="z",colors=(1,1,1,1))
#
#            self.axes.mouse_init()
#
#        else:
#            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
#            img_yuv_c = img_yuv / 255
#
#            self.axes.scatter(img_yuv[:, :, 0].ravel(), img_yuv[:, :, 1].ravel(), img_yuv[:, :, 2].ravel(),
#                              c=img_yuv_c.reshape((-1, 3)), edgecolors='none')
#
#            self.axes.set_facecolor((41 / 255, 41 / 255, 41 / 255, 1))
#            self.axes.set_xlabel("Y",color=(1,1,1,1))
#            self.axes.set_ylabel("U",color=(1,1,1,1))
#            self.axes.set_zlabel("V",color=(1,1,1,1))
#            self.axes.tick_params(axis="x",colors=(1,1,1,1))
#            self.axes.tick_params(axis="y",colors=(1,1,1,1))
#            self.axes.tick_params(axis="z",colors=(1,1,1,1))
#
#            self.axes.mouse_init()
class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111,projection='3d')
        super(MplCanvas, self).__init__(fig)


i=0
class Functions(MainWindow):

    def prepare_canvas(self):
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.h_box = QHBoxLayout()
        self.ui.rgb_frame.setLayout(self.h_box)
        self.h_box.addWidget(self.canvas)


    def import_button_clicked(self):
        global path
        Functions.prepare_canvas(self)



        filename = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/emrea/Desktop', 'Image Files (*.png *.jpg *.jpeg)')
        path = filename[0]


        pixmap = QPixmap(filename[0])
        pixmap = pixmap.scaled(480, 480, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.photo.setPixmap(pixmap)
        #Functions.create_graphs(self, self.ui.rgb_frame,0)
        #Functions.create_graphs(self, self.ui.hsv_frame,1)
        #Functions.create_graphs(self, self.ui.yuv_frame,2)
        self.graph_type = 0
        Functions.update_plot(self)


        ### Her frame için ayrı self.'li attributelar oluştur, 0, ve sonrası için grafikleri ayarla.




    #def create_graphs(self,frame,graph):
    #    global i
    #    self.temp_layout = QHBoxLayout()
    #    self.temp_frame = frame
    #    self.temp_frame.setLayout(self.temp_layout)
#
#
    #    if i == 0:
#
    #        self.temp_graph = MyStaticMplCanvas(graph_type=graph, width=5, height=5, dpi=120)
    #        self.temp_layout.addWidget(self.temp_graph)
    #        i+=1
#
    #    elif i == 1:
    #        self.temp_graph = MyStaticMplCanvas(graph_type=graph, width=5, height=5, dpi=120)
    #        self.temp_layout.addWidget(self.temp_graph)
    #        i+=1
#
    #    elif i ==2 :
    #        self.temp_graph = MyStaticMplCanvas(graph_type=graph, width=5, height=5, dpi=120)
    #        self.temp_layout.addWidget(self.temp_graph)
    #        i+=1




    #def create_graph_rgb(self):
#
    #    try:
    #        self.rgb_graph.axes.cla()
    #        self.rgb_layout = QHBoxLayout()
    #        self.ui.rgb_frame.setLayout(self.rgb_layout)
    #        self.rgb_graph = MyStaticMplCanvas(graph_type=0, width=5, height=5, dpi=120)
    #        self.rgb_layout.addWidget(self.rgb_graph)
    #        self.rgb_graph.axes.draw()
    #        print("i")
#
    #    except:
    #        self.rgb_layout = QHBoxLayout()
    #        self.ui.rgb_frame.setLayout(self.rgb_layout)
    #        self.rgb_graph = MyStaticMplCanvas(graph_type=0, width=5, height=5, dpi=120)
    #        self.rgb_layout.addWidget(self.rgb_graph)

    def update_plot(self):
        try:
            img_path = path
            img = cv2.imread(img_path)
            scale = max(img.shape[0], img.shape[1], 128) / 128  # at most 64 rows and columns
            img = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)),
                             interpolation=cv2.INTER_NEAREST)

        except:
            pass


        if self.graph_type == 0:

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


        #self.temp_graph.draw()

        #print(i)
        #self.temp_graph = MyStaticMplCanvas(graph_type=graph,width=5, height=5, dpi=120)
        #self.temp_layout.addWidget(self.temp_graph)






    def clean_widget(self):
        self.temp_graph.axes.cla()




