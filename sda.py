#!/usr/bin/python3  
# -*- coding: utf-8 -*-  
  
"""  
ZetCode PyQt5 tutorial   
  
This example draws three rectangles in three  
#different colours.   
  
author: Jan Bodnar  
website: zetcode.com   
last edited: January 2015  
"""  
  
import sys  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 
import magiccube

global startx
global starty

global xx
global yy
startx=[100,220,340,460,220,220]
starty=[300,300,300,300,420,180]

xx=[0,0,0,40,40,40,80,80,80]
yy=[0,40,80,0,40,80,0,40,80]
colour={"w":"#ffffff","r":"#ff0000","b":"#0000ff","g":"#00ff00","y":"#ffff00","o":"#ffa500"}
class Example(QWidget):  
      
    def __init__(self):  
        super().__init__()  
          
        self.initUI()  
          
          
    def initUI(self):        
       
        self.setGeometry(50, 50, 1000, 600)  
        self.setWindowTitle('Colours')
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self)
        self.dateTimeEdit.setGeometry(QtCore.QRect(760, 60, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(750, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(210, -20, 541, 131))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.retranslateUi()
        self.face1.clicked.connect(lambda:self.getpic(1))
        self.face2.clicked.connect(lambda:self.getpic(2))
        self.face3.clicked.connect(lambda:self.getpic(3))
        self.face4.clicked.connect(lambda:self.getpic(4))
        self.face5.clicked.connect(lambda:self.getpic(5))
        self.face6.clicked.connect(lambda:self.getpic(6))
        self.idnum=0
        self.colorlist=[]
        
        for i in range(6):
            for a in range(9):
                self.colorlist.append("r")
        self.show()
        print("stop1")
  


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
       
        self.face1.setText(_translate("MainWindow", "face1"))
        self.face2.setText(_translate("MainWindow", "face2"))
        self.face3.setText(_translate("MainWindow", "face3"))
        self.face4.setText(_translate("MainWindow", "face4"))
        self.face5.setText(_translate("MainWindow", "face5"))
        self.face6.setText(_translate("MainWindow", "face6"))
        self.label.setText(_translate("MainWindow", "选择魔方的表面"))
        self.label_2.setText(_translate("MainWindow", "欢迎使用魔方颜色识别程序！！！"))

    def paintEvent(self, e):  
       
        qp = QPainter()  
        qp.begin(self)
        self.drawRectangles(qp)  
        qp.end()
        
        
    def getpic(self,faceid=0):
        try:
            fname,ftype = QtWidgets.QFileDialog.getOpenFileName(self,"Open file","/")
        except:
            pass
        
        print(fname)
        print("stop4")
        face_cube=magiccube.cubeproess(fname)
        print(faceid)
        print(type(self.colorlist[0][0]))
      
        for i in range(9):
            self.colorlist[(faceid-1)*9+i]=face_cube[i].colour
        
        print("stop6")
        if fname != "":
            self.idnum=faceid
        print("stop7")  
          
    def drawRectangles(self, qp):           
        col = QColor(255,255,255)
        
        col.setNamedColor('#ffffff')  
        qp.setPen(col)
        qp.setBrush(QColor(255, 80, 0, 160))
      
        #if self.q==1:
        for y in range(6):
            for i in range(9):
                col1 = QColor()
                col1.setNamedColor(colour[self.colorlist[y*9+i]])
                qp.setBrush(col1) 
                qp.drawRect(startx[y]+xx[i],starty[y]+yy[i],40,40)
                   
       
        
##        qp.drawRect(200, 100, 30, 30)  
##  
##        qp.setBrush(QColor(255, 80, 0, 160))  
##        qp.drawRect(230, 100, 30, 30)  
##  
##        qp.setBrush(QColor(25, 0, 90, 200))  
##        qp.drawRect(260, 100, 30, 30)  
                
          
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  
