import sys

from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QColorDialog
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette, QColor
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer

class Lights():
    def __init__(self, LightNum, Add, redd, greenn, bluee):
        self.LightNum = QPushButton()    
        self.Add = 0
        self.redd = 255
        self.greenn = 0
        self.bluee = 0
        
class Joe():
    def _init_(self):
        self.btn = []


class cssden(QMainWindow):
    def __init__(self):
        super().__init__()
        
        numAL = self.pingPong()
        labelGeo=[]
        
        for i in range(len(numAL[0])):
            labelGeo.append(65+numAL[1][i]*65)


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        buttonNum = [1, 2]
        
        #size
        self.setFixedSize(800, 460)
        self.center
        
        #Label2
        self.label2 = QLabel(self)
        
        if len(numAL[0]) > 0:
            self.label2.setStyleSheet("border: 2px solid red;" )
            self.label2.setGeometry(5,15,labelGeo[0],50) # 249         

            #ArduinoButts
            self.Abtn = QPushButton(self)
            self.Abtn.setText("A1")
            self.Abtn.clicked.connect(self.pressedard1)
            self.Abtn.setStyleSheet("background-color: rgb(0,0,0);"
                           "border: 2px solid red;"
                           "color: rgb(255,255,255);"
                           "font: bold italic 10pt 'Times New Roman';")
            self.Abtn.setGeometry(10,30,35,20)
            
            if numAL[1][0] > 0:
                    #Butts
                self.btn = QPushButton(self)
                self.btn.setText("Light 1")
                self.btn.clicked.connect(self.pressedlgt1)
                self.btn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
                # self.btn.setGeometry(5,5,60,40)
                self.btn.setGeometry(70,20,60,40)
            if numAL[1][0] > 1:
                    #Butts2
                self.btn2 = QPushButton(self)
                self.btn2.setText("Light 2")

                self.btn2.clicked.connect(self.pressedlgt2)
                self.btn2.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
                self.btn2.setGeometry(135,20,60,40)   
            if numAL[1][0] > 2:
                    #Butts3
                self.btn3 = QPushButton(self)
                self.btn3.setText("Light 3")

                self.btn3.clicked.connect(self.pressedlgt3)
                self.btn3.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
                self.btn3.setGeometry(200,20,60,40)
                
            if numAL[1][0] > 2:
                    #Butts4
                self.btn4 = QPushButton(self)
                self.btn4.setText("Light 4")

                self.btn4.clicked.connect(self.pressedlgt4)
                self.btn4.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
                self.btn4.setGeometry(265,20,60,40)
            
        
        if len(numAL[0]) > 1:
            # Label2
            self.label3 = QLabel(self)

            self.label3.setStyleSheet(# "background-color: rgb(0,0,0);"
                                   "border: 2px solid red;" )
                                   # "color: rgb(255,255,255);"
                                   # "font: bold italic 12pt 'Times New Roman';")
            self.label3.setGeometry(5,80,labelGeo[1],50)
            
            #ArduinoButts
            self.Abtn2 = QPushButton(self)
            self.Abtn2.setText("A1")
            # self.Abtn.clicked.connect(self.pressedlgt1)
            self.Abtn2.setStyleSheet("background-color: rgb(0,0,0);"
                                   "border: 2px solid red;"
                                   "color: rgb(255,255,255);"
                                   "font: bold italic 10pt 'Times New Roman';")
            self.Abtn2.setGeometry(10,95,35,20)
        
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
        
        # Label1
        self.label1 = QLabel(self)
        self.label1.setText("Sensor Reading: %d" % self.sensorRead())

        self.label1.setStyleSheet(# "background-color: rgb(0,0,0);"
                               "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        self.label1.setGeometry(350,200,120,40)

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
        
    def pressedlgt3(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = "light3"
            self.btn3.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, light)
                
        self.show()
        
    def pressedlgt4(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = "light4"
            self.btn4.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, light)
                
        self.show()
        
    def pressedard1(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = ["light1", "light2", "light3", "light4"]
            self.btn4.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            self.btn3.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            self.btn2.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            self.btn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;"
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))                
                
            for i in range(len(light)):
                self.sendInfo(red, blue, green, light[i])
            
        self.show()
        
        
    def sensorRead(self):
        return 200
        
    def pingPong(self):
        return [[1,1],[4,0]]
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())