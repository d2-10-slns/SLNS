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


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        buttonNum = [1, 2]
        
        #size
        self.setFixedSize(500, 300)
        self.center

        #Butts
        self.Ebtn = QPushButton(self)
        self.Ebtn.setText("Exit")
        self.Ebtn.clicked.connect(self.exitButton)
        self.Ebtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 20pt 'Times New Roman';")
        self.Ebtn.setGeometry(5,5,60,40)

        #Butts
        self.btn = QPushButton(self)
        self.btn.setText("btn1")
        self.btn.clicked.connect(self.pressedbtn1)
        self.btn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 20pt 'Times New Roman';")
        self.btn.setGeometry(370,5,60,40)
        
        #Butts2
        self.btn2 = QPushButton(self)
        self.btn2.setText("btn2")

        self.btn2.clicked.connect(self.pressedbtn2)
        self.btn2.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 20pt 'Times New Roman';")
        self.btn2.setGeometry(435,5,60,40)

        self.show()

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
		
    def exitButton(self):
	    sys.exit()
        
    def pressedbtn1(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            print(int(colour.red()), colour.green(), colour.blue())
            # self.btn.setStyleSheet(
            #"background-color: rgb(0,0,0);"
                                   # "border: rgb(255,0,0);"
                                   # "color: rgb(int(colour.red()),int(colour.green()),int(color.blue()));"
                                   # "font: bold italic 20pt 'Times New Roman';"
                                   # )
        self.show()
        
    def pressedbtn2(self):
        colour = QColorDialog.getColor()
        # self.btn2.setStyleSheet("background-color: rgb(0,0,0);"
                               # "border: lpx solid red;"
                               # "color: lpx colour.name();"
                               # "font: bold italic 20pt 'Times New Roman';")

                               
app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())