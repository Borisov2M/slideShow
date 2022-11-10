from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from coordCatch import *

from PyQt5 import QtWidgets, QtCore, Qt



class GraphicsScene(QtWidgets.QGraphicsScene):
    clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(parent)
        self.parent = parent

#-------------------------------------------------------------------------------
        self._pos = QPointF()
        self._current_item = None
#-------------------------------------------------------------------------------
        self.startPos = QPointF()
        self.finPose = QPointF()
        self.rulerItem = None
        self.textItem = None
        self.lineItem = None    
#-------------------------------------------------------------------------------
        
        self.xpos = None
        self.ypos = None
        self.selecting = False
        self.setSceneRect(0,0,1063,1418)
        self.selection = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle)
        self.addWidget(self.selection)
        self.originQPoint = None
        self.originCropPoint = None
        self.currentQRect = None

        
    def mousePressEvent(self, event):
        self.selecting = True
        self.originQPoint = event.scenePos()
        self.selection.hide()
        self.originCropPoint = event.scenePos()
        
        if not self.parent.radioButton.isChecked():
#-------------------------------------------------------------------------------  
            self.removeItem(self.lineItem)
            self.removeItem(self.textItem)
            self.lineItem = None
            self.textItem = None
            self._pos = event.scenePos()
            self._current_item = QGraphicsRectItem()
            self._current_item.setPen(QPen(QColor('#ff0000'), 3, QtCore.Qt.DashLine))
            self.addItem(self._current_item)
            self._current_item.setRect(QRectF(self._pos, self._pos))

            #txt_font 
#-------------------------------------------------------------------------------
        else:
            self.startPos = event.scenePos().toPoint()
            self.rulerItem = QGraphicsLineItem()
            self.rulerItem.setPen(QPen(QColor('#ff00aa'), 3))
            self.addItem(self.rulerItem)
            self.rulerItem.setLine(QLineF(self.startPos, self.startPos))

            self.coordinates = QLineF(self.startPos, self.startPos)
            self.letter = 'С.П. = ' + str(int(self.coordinates.length()))
            if self.textItem == None:
                self.textItem = QGraphicsSimpleTextItem()
                self.textItem.setText(self.letter)
                f = self.textItem.font()
                f.setPointSize(2)
                self.textItem.setFont(f)
                self.textItem.setPos(self.startPos)
                self.textItem.setBrush(QColor('#ff0000'))
                self.textItem.setPen(QColor('#ff0000'))
                self.addItem(self.textItem)
            else:
                self.removeItem(self.textItem)
                self.removeItem(self.lineItem)
                self.lineItem = None
                self.textItem = None

                self.textItem = QGraphicsSimpleTextItem()
                self.textItem.setText(self.letter)
                self.textItem.setPos(self.startPos)
                self.textItem.setBrush(QColor('#ff0000'))
                self.textItem.setPen(QColor('#ff0000'))
                f = self.textItem.font()
                f.setPointSize(2)
                self.textItem.setFont(f)
                self.addItem(self.textItem)
#-------------------------------------------------------------------------------

        self.clicked.emit()

    
    def mouseMoveEvent(self, event):
        if self.originQPoint is not None and self.selecting:
            rect = QtCore.QRect(self.originQPoint.toPoint(), 
                                event.scenePos().toPoint())
            self.selection.setGeometry(rect)
            self.selection.show()

        if not self.parent.radioButton.isChecked():
#-------------------------------------------------------------------------------
            if self._current_item:
                rect = QRectF(self._pos, event.scenePos()).normalized()
                self._current_item.setRect(rect)
#-------------------------------------------------------------------------------
        else:
            if self.rulerItem:
                self.coordinates = QLineF(self.startPos, event.scenePos())
                self.rulerItem.setLine(QLineF(self.coordinates))
                
                self.letter = 'С.П. = ' + str(int(self.coordinates.length()))
                self.textItem.setText(self.letter)
                self.textItem.setPos(event.scenePos())
                self.removeItem(self.textItem)
                self.addItem(self.textItem)
#-------------------------------------------------------------------------------


    def mouseReleaseEvent(self, event):
        self.selecting = False
        self.selection.hide()
        self.currentQRect = QtCore.QRect(self.originCropPoint.toPoint(), 
                                         event.scenePos().toPoint())
        print(self.currentQRect)

        if not self.parent.radioButton.isChecked():
#-------------------------------------------------------------------------------
            self.removeItem(self._current_item)
            self._current_item = None
#-------------------------------------------------------------------------------
        else:
            self.finPose = event.scenePos().toPoint()
            self.removeItem(self.rulerItem)    
            self.rulerItem = None  

            self.lineItem = QGraphicsLineItem()
            self.addItem(self.lineItem)
            self.lineItem.setLine(QLineF(self.startPos, self.finPose))
            self.lineItem.setPen(QPen(QColor('#ff00aa'), 3)) 

            self.set_Message()
            
                   
#-------------------------------------------------------------------------------

    def set_Message(self):
        coords = QLineF(self.startPos, self.finPose)
        letter = 'Сумма пикселей = ' + str(int(coords.length()))
        print(letter)
        
    