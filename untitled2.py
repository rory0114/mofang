# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:02:51 2017

@author: lyr
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
class MainWindows(QtWidgets.QMainWindow): # 创立主窗口，继承QMainWindow类
    
    def __init__(self):
        super(MainWindows, self).__init__()   # 显性调用父类构造函数
        self.setWindowTitle("QtDockWidgets demo")
        aw = CreateWidget()    # 创建一个准备放入dockwidget的窗体控件
        self.CreateDockWidget(aw)   # 创建dock，并将上一步创建的QWidget放入dock中
        

    def CreateDockWidget(self, widget):  # 定义一个createDock方法创建一个dockwidget
        dock = QtWidgets.QDockWidget("selectQuote")  # 实例化dockwidget类
        dock.setWidget(widget)   # 带入的参数为一个QWidget窗体实例，将该窗体放入dock中
        dock.setObjectName("selectQuote")
        dock.setFeatures(dock.DockWidgetFloatable|dock.DockWidgetMovable)    #  设置dockwidget的各类属性
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)  # 设置dockwidget放置在QMainWindow中的位置，并且将dockwidget添加至QMainWindow中
        
app = QtWidgets.QApplication(sys.argv)
     
aw = MainWindows()
aw.showMaximized()
    
app.exec_()