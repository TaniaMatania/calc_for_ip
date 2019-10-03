import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,QSettings
import urllib
import requests
import webbrowser
from .CheckWindow import CheckWindow
from .CalcWindow import CalcWindow



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secondWin = None
        self.thirdWin = None

        self.setupUi()
        self.initSignals()
        self.setWindowTitle('Календарь бухгалтера')
        self.setWindowIcon(QIcon('pic/web.png'))

        self.setStyleSheet(
        """QToolButton {background-color: #FFE4B5;
                        font-size: 25px;
                        color: #696969; border-radius: 10px;}

        """)


    def setupUi(self):
        self.resize(900, 800)
        self.setMinimumSize(QtCore.QSize(900, 800))
        self.setMaximumSize(QtCore.QSize(900, 800))

        self.calcbutton = QtWidgets.QToolButton(self)
        self.calcbutton.setGeometry(QtCore.QRect(20, 60, 250, 35))


        self.statusbutton = QtWidgets.QToolButton(self)
        self.statusbutton.setGeometry(QtCore.QRect(20, 120, 250, 35))


        self.linkbutton = QtWidgets.QToolButton(self)
        self.linkbutton.setGeometry(QtCore.QRect(20, 180, 250, 35))

        self.fnsbutton = QtWidgets.QToolButton(self)
        self.fnsbutton.setGeometry(QtCore.QRect(600, 550, 250, 35))


        self.egrbutton = QtWidgets.QToolButton(self)
        self.egrbutton .setGeometry(QtCore.QRect(600, 610, 250, 35))



        self.calcbutton.setText("Калькулятор УСН")
        self.statusbutton.setText("Статус платежа")
        self.linkbutton.setText("Декларация УСН")
        self.fnsbutton.setText("ФНС")
        self.egrbutton .setText("ЕГРЮЛ/ЕГРИП")




        oImage = QImage("pic/background.jpg")
        sImage = oImage.scaled(QSize(900,800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)



    def initSignals(self):
        self.calcbutton.clicked.connect(self.openCalc)
        self.statusbutton.clicked.connect(self.openStat)
        self.linkbutton.clicked.connect(self.declar)
        self.fnsbutton.clicked.connect(self.open1)
        self.egrbutton.clicked.connect(self.open2)


    def declar(self):
        f = requests.get("https://www.nalog.ru/html/sites/www.new.nalog.ru/doc/pril1_fns99_260216.pdf")
        with open("declaracia.pdf", "wb") as dec:
            dec.write(f.content)
            os.startfile("declaracia.pdf")


    def openStat(self):
        if not self.secondWin:
            self.secondWin = CheckWindow(self)
        self.secondWin.show()

    def openCalc(self):
        if not self.thirdWin:
            self.thirdWin = CalcWindow(self)
        self.thirdWin.show()


    def open1(self):
            url1 ="https://www.nalog.ru/rn78/ip/"
            webbrowser.open(url1)

    def open2(self):
            url2 ="https://egrul.nalog.ru/index.html"
            webbrowser.open(url2)
