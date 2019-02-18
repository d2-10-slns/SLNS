import sys

from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QColorDialog
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette, QColor
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer



class cssden(QMainWindow):
    def __init__(self):
        super().__init__()
        
        numAL = self.pingPong()
        
        print(numAL[0][0])
        labelGeo = 80+numAL[1][0]*50


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        buttonNum = [1, 2]
        
        #size
        self.setFixedSize(500, 300)
        self.center
        
        #Label2
        self.label2 = QLabel(self)

        self.label2.setStyleSheet(# "background-color: rgb(0,0,0);"
                               "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        self.label2.setGeometry(5,15,labelGeo,50) # 249
        
        if len(numAL[0]) > 1:
            # Label2
            self.label3 = QLabel(self)

            self.label3.setStyleSheet(# "background-color: rgb(0,0,0);"
                                   "border: 2px solid red;" )
                                   # "color: rgb(255,255,255);"
                                   # "font: bold italic 12pt 'Times New Roman';")
            self.label3.setGeometry(5,70,249,50)
        
        # Label2
        # self.label4 = QLabel(self)

        # self.label4.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label4.setGeometry(5,125,249,50)
        
        # Label2
        # self.label5 = QLabel(self)
        # self.label5.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label5.setGeometry(5,180,249,50)
        
        # Label2
        # self.label6 = QLabel(self)

        # self.label6.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label6.setGeometry(5,235,249,50)

        #Butts
        self.Ebtn = QPushButton(self)
        self.Ebtn.setText("Exit")
        self.Ebtn.clicked.connect(self.exitButton)
        self.Ebtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
        self.Ebtn.setGeometry(435,20,60,40)
        
        #ArduinoButts
        self.Abtn = QPushButton(self)
        self.Abtn.setText("A1")
        # self.Abtn.clicked.connect(self.pressedlgt1)
        self.Abtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 10pt 'Times New Roman';")
        self.Abtn.setGeometry(10,35,35,20)

        #Butts
        self.btn = QPushButton(self)
        self.btn.setText("Light 1")
        self.btn.clicked.connect(self.pressedlgt1)
        self.btn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
        # self.btn.setGeometry(5,5,60,40)
        self.btn.setGeometry(50,20,60,40)
        
        #Butts2
        self.btn2 = QPushButton(self)
        self.btn2.setText("Light 2")

        self.btn2.clicked.connect(self.pressedlgt2)
        self.btn2.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
        self.btn2.setGeometry(115,20,60,40)
        
        #Butts3
        # self.btn3 = QPushButton(self)
        # self.btn3.setText("Light 3")

        # self.btn3.clicked.connect(self.pressedlgt2)
        # self.btn3.setStyleSheet("background-color: rgb(0,0,0);"
                               # "border: 2px solid red;"
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.btn3.setGeometry(180,20,60,40)
        
        # Label1
        self.label1 = QLabel(self)
        self.label1.setText("Sensor Reading: %d" % self.sensorRead())

        self.label1.setStyleSheet(# "background-color: rgb(0,0,0);"
                               "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        self.label1.setGeometry(335,200,120,40)

        self.show()
        
    # center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def sendInfo(self, red, blue, green, light):
        print("Red: %d; Blue: %d; Green: %d; Light address: %s" % (red, blue, green, light))
		
    def exitButton(self):
	    sys.exit()
        
    def pressedlgt1(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = "light1"
            self.btn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;" #"border-color: red;")
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, light)
                
        self.show()
        
    def pressedlgt2(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = "light2"
            self.btn2.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, light)
                
        self.show()
        
        
    def sensorRead(self):
        return 200
        
    def pingPong(self):
        return [[1,1],[2,1]]
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())