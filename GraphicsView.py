import sys
import cv2
import numpy as np
import PIL

from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.pyplot import *

from PIL import Image, ImageColor, ImageQt
from GraphicsScene import GraphicsScene
from coordCatch import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore



class ProcessWorker(QObject):
    imageChanged = pyqtSignal(QImage)

    def doWork(self):
        self.eApp = ExampleApp()
        self.ui = Ui_MainWindow()
        self.image_list = [r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\1.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\2.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\3.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\4.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\5.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\6.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\7.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\8.jpg',
                           r'E:\RQC Projects\QGraphicsView\QGraphicsView + mpl\pngForDispleying\9.jpg']
        f = 1
        
        while True:
            objects = list(self.eApp.graphicsView.scene().items()) 
            self.cmap = 10


            for i in range(objects.__len__()):
                gi = objects[i]
                if gi.parentItem() == None:
                    if type(gi) is QtWidgets.QGraphicsPixmapItem:
                        del gi
                    
            if f <= len(self.image_list) - 1:
                img = ImageQt.ImageQt(self.image_list[f])
                self.imageChanged.emit(img)
                QThread.msleep(50)
                f += 1
            else:
                f = 1
                img = ImageQt.ImageQt(self.image_list[f])
                self.imageChanged.emit(img)
                QThread.msleep(50)
################################################################################        
################################################################################



class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()

        self.setupUi(self)
        self.resize(640, 490) 

        self.gscene = GraphicsScene(self)        
        self.graphicsView.setScene(self.gscene)
        self.graphicsView.show()

        self.pixmap = QGraphicsPixmapItem()
        self.graphicsView.scene().addItem(self.pixmap) 

        self.workerThread = QThread()
        self.worker = ProcessWorker()
        self.worker.moveToThread(self.workerThread)
        self.workerThread.finished.connect(self.worker.deleteLater)
        self.workerThread.started.connect(self.worker.doWork)
        self.worker.imageChanged.connect(self.setImage)


#---------------------- Создает виджет QGridLayout -----------------------------
        self.sublayout = QtWidgets.QVBoxLayout()
        self.sublayout.addWidget(self.comboBox)
        self.sublayout.addWidget(self.pushButton)
        self.sublayout.addWidget(self.pushButton_1)
        self.sublayout.addWidget(self.radioButton)

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.graphicsView, 0, 0)
        self.layout.addLayout(self.sublayout, 0, 2)

        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 0)
        self.layout.setColumnStretch(0, 4)
#-------------------------------------------------------------------------------
        
        self.pushButton.clicked.connect(self.start)

        self.colorLayout = QtWidgets.QVBoxLayout()
        self.nameLayout = QtWidgets.QVBoxLayout()
        self.moveCheck = False

        # self.pushButton.clicked.connect(self.start)
        # self.pushButton_1.clicked.connect(self.makeScreenshot)
        #self.comboBox.currentIndexChanged.connect(self.imgConvert)


    def checkIndex(self):
        index = self.comboBox.currentIndex()
        print(index, 'С мэйна')
        #return(index)


    def setImage(self, image):
        pixmap = QPixmap.fromImage(image)
        self.pixmap.setPixmap(pixmap)


    def start(self):
        self.workerThread.start() 



def main():
    app = QtWidgets.QApplication(sys.argv) 

    window = ExampleApp()
    window.show() 
    app.exec_()  

if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv) 
    main() 