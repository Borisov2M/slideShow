# import sys
# import coordCatch

# from PyQt5.Qt import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5 import QtWidgets, QtCore


# class graphicsScene(QtWidgets.QGraphicsScene):
#     clicked = pyqtSignal()

#     def __init__(self, parent=None):
#         super(graphicsScene, self).__init__(parent)

#         self.xpos = None
#         self.ypos = None
#         self.selecting = False
#         self.setSceneRect(0,0,1063,1418)
#         self.selection = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle)
#         self.addWidget(self.selection)
#         self.originQPoint = None
#         self.originCropPoint = None
#         self.currentQRect = None


#     def mousePressEvent(self, event):
#         self.selecting = True
#         self.originQPoint = event.scenePos()
#         self.selection.hide()
#         self.originCropPoint = event.scenePos()       
#         self.clicked.emit()


#     def mouseMoveEvent(self, event):
#         if self.originQPoint is not None and self.selecting:
#             rect = QtCore.QRect(self.originQPoint.toPoint(), 
#                                 event.scenePos().toPoint())
#             self.selection.setGeometry(rect)
#             self.selection.show()


#     def mouseReleaseEvent(self, event):
#         self.selecting = False
#         self.selection.hide()
#         self.currentQRect = QtCore.QRect(self.originCropPoint.toPoint(), 
#                                          event.scenePos().toPoint())
#         print(self.currentQRect)



# class ProcessWorker(QObject):
#     imageChanged = pyqtSignal(QImage)


#     def doWork(self):
#         # self.image_list = ['E:/Projects/QGraphicsView + mpl/pngForDispleying/1.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/2.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/3.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/4.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/5.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/6.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/7.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/8.jpg',
#         #                 'E:/Projects/QGraphicsView + mpl/pngForDispleying/9.jpg']

#         self.image_list = ['E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/1.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/2.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/3.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/4.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/5.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/6.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/7.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/8.jpg',
#                         'E:/RQC Projects/QGraphicsView + mpl/pngForDispleying/9.jpg']
#         f = 0

#         while True:
#             if f <= len(self.image_list) - 1:
#                 img = QImage(self.image_list[f])
#                 self.imageChanged.emit(img)
#                 QThread.msleep(150)
#                 f += 1
#             else:
#                 f = 0
#                 img = QImage(self.image_list[f])
#                 self.imageChanged.emit(img)
#                 QThread.msleep(1)



# class ExampleApp(QtWidgets.QMainWindow, coordCatch.Ui_MainWindow):
#     def __init__(self):
#         super(ExampleApp, self).__init__()

#         self.setupUi(self)
#         self.resize(840, 740)  

#         self.gscene = graphicsScene()        
#         self.graphicsView.setScene(self.gscene)
#         self.graphicsView.show()
#         self.graphicsView.setFixedSize(710, 610)

#         self.pixmap = QGraphicsPixmapItem()
#         self.graphicsView.scene().addItem(self.pixmap) 

#         self.workerThread = QThread()
#         self.worker = ProcessWorker()
#         self.worker.moveToThread(self.workerThread)
#         self.workerThread.finished.connect(self.worker.deleteLater)
#         self.workerThread.started.connect(self.worker.doWork)
#         self.worker.imageChanged.connect(self.setImage)
#         self.workerThread.start()


#     @pyqtSlot(QImage)
#     def setImage(self, image):
#         pixmap = QPixmap.fromImage(image)
#         self.pixmap.setPixmap(pixmap)       


# def main():
#     app = QtWidgets.QApplication(sys.argv) 

#     window = ExampleApp()
#     window.show() 
#     app.exec_()  

# if __name__ == '__main__': 
#     app = QtWidgets.QApplication(sys.argv) 
#     main() 

#res_str = str.replace('t', '', 1) 

import re

stringName = '#40826d'
stringName = stringName[1:]
latterList = re.findall('..?', stringName)
latterList[0], latterList[2] = latterList[2], latterList[0]

print(latterList)

stringName = '#' + ''.join(latterList)
print(stringName)   