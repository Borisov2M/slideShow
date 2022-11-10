# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coordCatch.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing. 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 490)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 441, 331))
        self.graphicsView.setObjectName("graphicsView")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 50, 171, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(460, 50, 171, 91))
        self.pushButton_1.setObjectName("pushButton_1")
        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(460, 50, 171, 141))
        self.radioButton.setObjectName("radioButton")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 10, 171, 31))
        self.comboBox.setObjectName("comboBox")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        cmapNames = ['AUTUMN', 'BONE', 'JET', 'WINTER', 'RAINBOW', 'OCEAN', 
        'SUMMER', 'SPRING', 'COOL', 'HSV', 'PINK', 'HOT', 'PARULA', 'MAGMA', 
        'INFERNO', 'PLASMA', 'VIRIDIS', 'CIVIDIS', 'TWILIGHT', 'SHIFTED', 
        'TURBO', 'DEEPGREEN']

        self.comboBox.clear()
        self.comboBox.addItems(cmapNames)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Отобразить скриншот"))
        self.pushButton_1.setText(_translate("MainWindow", "Скриншот"))
        self.radioButton.setText(_translate("MainWindow", "Линейка"))