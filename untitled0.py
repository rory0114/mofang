# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PyQt5 import QtGui,QtWidgets,QtCore  
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("LYR")
        
        
        extractAction=QtWidgets.QAction("&GEY#$@$%",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("leave the App")
        extractAction.triggered.connect(self.close_application)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')   
        fileMenu.addAction(extractAction)           
        self.home()
        
        
   
    
    def style_choice(self,text):
        self.stylechoice.setText(text)
      
    
    def home(self):
        btn = QtWidgets.QPushButton("q",self)
        btn.clicked.connect(self.close_application)
        btn.move(0,100)
        self.show()
    
    def close_application(self):
        print("关闭")
        sys.exit()
    
    
    
def run(): 
    app=QtWidgets.QApplication(sys.argv)
    Gui=Window()
    QtWidgets.Q
    sys.exit(app.exec_())
run()      
