import sys
import cmapSelection_UI

import matplotlib as mpl
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets

from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.pyplot import *
from GraphicsView import ExampleApp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class selectMainWindow(QtWidgets.QMainWindow, cmapSelection_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.resize(200, 640)
        self.eApp = ExampleApp() 

        self.collorView()

        # i = 0
        # bins = []
        # for clr in self.eApp.collorsList:
        #     bins += [i]
        #     i += 0.5

        
        # fig1, ax1 = plt.subplots(figsize=(6, 1))
        # fig1.subplots_adjust(bottom=0.5)

        # try:
        #     win = fig1.canvas.manager.window
        # except AttributeError:
        #     win = fig1.canvas.window()
        # toolbar = win.findChild(QtWidgets.QToolBar)
        # toolbar.setVisible(False)

        # cmap = mpl.colors.ListedColormap(self.eApp.collorsList)
        # norm = mpl.colors.BoundaryNorm(boundaries=bins, 
        #                                ncolors=len(cmap.colors) - 1 )

        # fig1.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        #      cax=ax1, orientation='horizontal', label='Some Units')
        # fig1.show()


        # self.fig, self.ax = subplots(figsize=(6, 0.5))
        # self.fig.subplots_adjust(bottom=0.5)
        # self.plotWidget = FigureCanvas(self.fig)

        
        # self.layout.addLayout(self.colorLayout, 0, 0)
        # self.layout.addLayout(self.nameLayout, 0, 1)

        # print(self.eApp.comboBox.currentIndex())
        # if self.eApp.comboBox.currentIndex() == 0:
        #     self.colorList = ['#0065ff', '#0069ff', '#0061ff', '#0079ff', '#0095ff', '#00c7ff']
        # elif self.eApp.comboBox.currentIndex() == 1:
        #     self.colorList = ['#ccc2ab', '#cabda3', '#c8b99b', '#dad5d7', '#c9c7c0', '#6161a6']
        # else:
        #     self.colorList =  ['#196600', '#146100', '#266e00', '#468400', '#78a50a', '#c5d88b']

        # self.eApp.collorsList = self.colorList



        # cmap = mpl.colors.ListedColormap(self.eApp.collorsList)

        

        # norm = mpl.colors.BoundaryNorm(boundaries=bins, 
        #                                ncolors=len(cmap.colors)-1 )

        # self.cb2 = mpl.colorbar.ColorbarBase(self.ax, 
        # cmap=cmap,
        # norm=norm,
        # boundaries= [-.1] + bins + [2.1],
        # ticks=bins,
        # spacing='uniform',
        # orientation='horizontal')
        # self.cb2.set_label('Custom colour bar')

        # self.plotWidget.draw()

    def collorView(self):

        for collor in self.eApp.collorsList:
            newColorLabel = QtWidgets.QLabel('')
            newColorLabel.resize(50, 40)
            newColorLabel.setStyleSheet('background-color: ' + collor + ';' + 
                                   'border: 1px solid black;')
            self.verticalLayout_2.addWidget(newColorLabel)

            newNameLabel = QtWidgets.QLabel('')
            newNameLabel.resize(50, 40)
            newNameLabel.setText(collor)
            self.verticalLayout.addWidget(newNameLabel)

