# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import magiccube
startx=[100,160,220,280,340,220]
starty=[200,200,200,200,260,140]

xx=[0,0,0,20,20,20,40,40,40]
yy=[0,20,40,0,20,40,0,20,40]
class PaintArea(QtWidgets.QWidget):
    def __init__(self):
        super(PaintArea,self).__init__()
        self.setMinimumSize(400,400)
        self.pen = QPen()
        self.brush = QBrush()
        self.setWindowTitle("woyouyongm")

    def paintEvent(self,faceid):
        qp=QtGui.QPainter()
        for i in range(9):
             col = QColor(0, 0, 255)
             qp.setBrush(col)
             qp.drawRect(50,50,20,20)
        self.update()

        
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralWidget = PaintArea()
        self.centralWidget.setObjectName("centralWidget")
        self.widget = PaintArea()
        
        
        self.tWidget = QtWidgets.QWidget(self.centralWidget)
        
        self.tWidget.setGeometry(QtCore.QRect(100, 100, 500, 350))
        self.drawer = QtWidgets.QVBoxLayout(self.tWidget)
        self.drawcube = PaintArea()
        self.drawer.addWidget(self.drawcube)
        self.drawcube.setObjectName("drawcube")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 200, 161, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chooseface = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chooseface.setContentsMargins(11, 11, 11, 11)
        self.chooseface.setSpacing(6)
        self.chooseface.setObjectName("chooseface")
        self.face1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face1.setObjectName("face1")
        self.chooseface.addWidget(self.face1)
        self.face2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face2.setObjectName("face2")
        self.chooseface.addWidget(self.face2)
        self.face3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face3.setObjectName("face3")
        self.chooseface.addWidget(self.face3)
        self.face4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face4.setObjectName("face4")
        self.chooseface.addWidget(self.face4)
        self.face5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face5.setObjectName("face5")
        self.chooseface.addWidget(self.face5)
        self.face6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.face6.setObjectName("face6")
        self.chooseface.addWidget(self.face6)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralWidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(760, 60, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(750, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(100, -20, 650, 131))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        qp=QtGui.QPainter()
        brush = QBrush(Qt.SolidPattern)  
        qp.setBrush(brush)  
        qp.drawRect(10, 15, 90, 60)
        qp.begin(mm)
        col = QColor(0, 175, 255)
        qp.setBrush(col)
        qp.drawRect(200,200,20,20)
        qp.end()
        self.centralWidget.update()
        print(type(self.centralWidget))       
        
        MainWindow.setCentralWidget(self.centralWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
       
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.face1.clicked.connect(lambda:self.getpic(MainWindow,1))
        

    def getpic(self,MainWindow,faceid=0):
        try:
            fname,ftype = QtWidgets.QFileDialog.getOpenFileName(self.centralWidget,"Open file","/")
        except:
            pass
        
        face_cube=magiccube.cubeproess(fname)
        print(face_cube)
        if fname != "":
            MainWindow.centralWidget.paintEvent(faceid)

    
        
            
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face1.setText(_translate("MainWindow", "face1"))
        self.face2.setText(_translate("MainWindow", "face2"))
        self.face3.setText(_translate("MainWindow", "face3"))
        self.face4.setText(_translate("MainWindow", "face4"))
        self.face5.setText(_translate("MainWindow", "face5"))
        self.face6.setText(_translate("MainWindow", "face6"))
        self.label.setText(_translate("MainWindow", "选择魔方的表面"))
        self.label_2.setText(_translate("MainWindow", "欢迎使用魔方颜色识别程序！！！"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mm=QtWidgets.QMainWindow()
    cc=Ui_MainWindow().setupUi(mm)
    mm.show()
    sys.exit(app.exec_()) 
