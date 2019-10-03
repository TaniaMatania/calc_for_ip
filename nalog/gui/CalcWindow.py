import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,QSettings


class CalcWindow(QWidget):
    def __init__(self, parent=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        super().__init__(parent, QtCore.Qt.Window)
        self.setStyleSheet(
        """QLabel {background-color: #FFFFE0;
                        font-size: 20px;
                        color: #2F4F4F; border-radius: 5px;}
            QDoubleSpinBox {background-color: #DCDCDC;
                            font-size: 16px;
                            color: #2F4F4F; border-radius: 3px;}
            QPushButton {background-color: #FFFFE0;
                            font-size: 40px;
                            color: #2F4F4F; border-radius: 30px;}

        """)
        self.setupUi(self)
        self.initSignals()


    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(900, 800)
        Calculator.setMinimumSize(QtCore.QSize(900, 800))
        Calculator.setMaximumSize(QtCore.QSize(900, 800))

        oImage = QImage("pic/candel.jpg")
        sImage = oImage.scaled(QSize(900,800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


        #доходы и платежи
        self.dohodinalog = QtWidgets.QLabel(self)
        self.dohodinalog.setGeometry(QtCore.QRect(200, 55,570, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.dohodinalog.setFont(font)

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 70, 900, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 900, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.kvartal1 = QtWidgets.QLabel(self)
        self.kvartal1.setGeometry(QtCore.QRect(200, 90, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kvartal1.setFont(font)

        self.kvartal2 = QtWidgets.QLabel(self)
        self.kvartal2.setGeometry(QtCore.QRect(350, 90, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kvartal2.setFont(font)

        self.kvartal3 = QtWidgets.QLabel(self)
        self.kvartal3.setGeometry(QtCore.QRect(500, 90, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kvartal3.setFont(font)

        self.kvartal4 = QtWidgets.QLabel(self)
        self.kvartal4.setGeometry(QtCore.QRect(650, 90, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kvartal4.setFont(font)

        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(0, 140, 900, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(0, 195, 900, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(0, 260, 900, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_6 = QtWidgets.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(0, 310, 900, 31))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.dohody = QtWidgets.QLabel(self)
        self.dohody.setGeometry(QtCore.QRect(5, 150, 185, 51))

        self.strahov = QtWidgets.QLabel(self)
        self.strahov.setGeometry(QtCore.QRect(5, 210, 185, 51))

        self.avans = QtWidgets.QLabel(self)
        self.avans.setGeometry(QtCore.QRect(5, 270, 185, 51))

        self.dohod1 = QtWidgets.QDoubleSpinBox(self)
        self.dohod1.setGeometry(QtCore.QRect(200, 150, 121, 51))
        self.dohod1.setMaximum(9999999.99)

        self.strah1 = QtWidgets.QDoubleSpinBox(self)
        self.strah1.setGeometry(QtCore.QRect(200, 210, 121, 51))
        self.strah1.setMaximum(9999999.99)

        self.avance1 = QtWidgets.QDoubleSpinBox(self)
        self.avance1.setGeometry(QtCore.QRect(200, 270, 121, 51))
        self.avance1.setMaximum(9999999.99)

        self.dohod2 = QtWidgets.QDoubleSpinBox(self)
        self.dohod2.setGeometry(QtCore.QRect(350, 150, 121, 51))
        self.dohod2.setMaximum(9999999.99)

        self.strah2 = QtWidgets.QDoubleSpinBox(self)
        self.strah2.setGeometry(QtCore.QRect(350, 210, 121, 51))
        self.strah2.setMaximum(9999999.99)

        self.avance2 = QtWidgets.QDoubleSpinBox(self)
        self.avance2.setGeometry(QtCore.QRect(350, 270, 121, 51))
        self.avance2.setMaximum(9999999.99)

        self.dohod3 = QtWidgets.QDoubleSpinBox(self)
        self.dohod3.setGeometry(QtCore.QRect(500, 150, 121, 51))
        self.dohod3.setMaximum(9999999.99)

        self.strah3 = QtWidgets.QDoubleSpinBox(self)
        self.strah3.setGeometry(QtCore.QRect(500, 210, 121, 51))
        self.strah3.setMaximum(9999999.99)

        self.avance3 = QtWidgets.QDoubleSpinBox(self)
        self.avance3.setGeometry(QtCore.QRect(500, 270, 121, 51))
        self.avance3.setMaximum(9999999.99)

        self.dohod4 = QtWidgets.QDoubleSpinBox(self)
        self.dohod4.setGeometry(QtCore.QRect(650, 150, 121, 51))
        self.dohod4.setMaximum(9999999.99)

        self.strah4 = QtWidgets.QDoubleSpinBox(self)
        self.strah4.setGeometry(QtCore.QRect(650, 210, 121, 51))
        self.strah4.setMaximum(9999999.99)
        #налог к упл
        self.nalogkupl = QtWidgets.QLabel(self)
        self.nalogkupl.setGeometry(QtCore.QRect(10, 390, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nalogkupl.setFont(font)
        #налог к уплат после вычета
        self.nalogposle = QtWidgets.QLabel(self)
        self.nalogposle.setGeometry(QtCore.QRect(10, 510, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nalogposle.setFont(font)
        #1 квартал лейбел
        self.line1kvartal = QtWidgets.QLineEdit(self)
        self.line1kvartal.setGeometry(QtCore.QRect(10, 550, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line1kvartal.setFont(font)
        #полгуод лейбел
        self.linePolugodie = QtWidgets.QLineEdit(self)
        self.linePolugodie.setGeometry(QtCore.QRect(170, 550, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.linePolugodie.setFont(font)
        #9 мс лейбел
        self.line9mes = QtWidgets.QLineEdit(self)
        self.line9mes.setGeometry(QtCore.QRect(330, 550, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line9mes.setFont(font)
        #год лейбел
        self.lineyear = QtWidgets.QLineEdit(self)
        self.lineyear.setGeometry(QtCore.QRect(490, 550, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineyear.setFont(font)

        self.newcalc = QtWidgets.QToolButton(self)
        self.newcalc.setGeometry(QtCore.QRect(10, 700, 300, 30))
        #ваш доход за год
        self.vashdogod = QtWidgets.QLineEdit(self)
        self.vashdogod.setGeometry(QtCore.QRect(10, 430, 191, 30))
        #налог усн
        self.nalogusn = QtWidgets.QLineEdit(self)
        self.nalogusn.setGeometry(QtCore.QRect(10, 470, 191, 30))

        #итого год выручка
        self.doubleSpinBoxyear = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBoxyear.setGeometry(QtCore.QRect(220, 430, 130, 30))
        self.doubleSpinBoxyear.setMaximum(9999999.99)
        self.doubleSpinBoxyear.setReadOnly(True)

        #6% усн
        self.doubleSpinBoxusn = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBoxusn.setGeometry(QtCore.QRect(220, 470, 130, 30))
        self.doubleSpinBoxusn.setMaximum(9999999.99)
        self.doubleSpinBoxusn.setReadOnly(True)


        #кнопка расчет налга
        self.CalcButton = QtWidgets.QPushButton(self)
        self.CalcButton.setGeometry(QtCore.QRect(250, 330, 400, 50))
        #квартал
        self.doubleSpinBoxkvartal = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBoxkvartal.setGeometry(QtCore.QRect(10, 600, 150, 40))
        self.doubleSpinBoxkvartal.setMaximum(9999999.99)
        self.doubleSpinBoxkvartal.setReadOnly(True)
        #полугодие
        self.doubleSpinBoxhalfyear = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBoxhalfyear.setGeometry(QtCore.QRect(170, 600, 150, 40))
        self.doubleSpinBoxhalfyear.setMaximum(9999999.99)
        self.doubleSpinBoxhalfyear.setReadOnly(True)
        #9мес
        self.doubleSpinBox9mes = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBox9mes.setGeometry(QtCore.QRect(330, 600, 150, 40))
        self.doubleSpinBox9mes.setMaximum(9999999.99)
        self.doubleSpinBox9mes.setReadOnly(True)
        #год
        self.doubleSpinBoxgod = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBoxgod.setGeometry(QtCore.QRect(490, 600, 150, 40))
        self.doubleSpinBoxgod.setMaximum(9999999.99)
        self.doubleSpinBoxgod.setMinimum(-99999.99)
        self.doubleSpinBoxgod.setReadOnly(True)


        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)


    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle( "Калькулятор УСН")
        self.dohodinalog.setText ("                      Укажите доходы и платежи")
        self.kvartal1.setText(" 1 квартал")
        self.kvartal2.setText(" 2 квартал")
        self.kvartal3.setText(" 3 квартал")
        self.kvartal4.setText(" 4 квартал")
        self.dohody.setText("        Доходы")
        self.strahov.setText("  Страховые взносы")
        self.avans.setText("Авансовые платежи")
        self.nalogkupl.setText("    Налог к уплате:")
        self.nalogposle.setText( "Налог к уплате после вычета страховых взносов и авансовых платежей:")
        self.line1kvartal.setText( " 1 квартал")
        self.line1kvartal.setReadOnly(True)
        self.linePolugodie.setText( " Полугодие")
        self.linePolugodie.setReadOnly(True)
        self.line9mes.setText(" 9 месяцев")
        self.line9mes.setReadOnly(True)
        self.lineyear.setText( "    Год")
        self.lineyear.setReadOnly(True)
        self.newcalc.setText("Новый расчет")
        self.vashdogod.setText("  Ваш доход за год:")
        self.vashdogod.setReadOnly(True)
        self.nalogusn.setText("  Налог УСН:")
        self.nalogusn.setReadOnly(True)
        self.CalcButton.setText("Расчет налога")


    def initSignals(self):
        self.CalcButton.clicked.connect(self.handleClick)
        self.dohod1.valueChanged.connect(self.updateConvertBtn)
        self.newcalc.clicked.connect(self.clearcalc)


    def handleClick(self):
        vald1 = self.dohod1.value()
        vald2 = self.dohod2.value()
        vald3 = self.dohod3.value()
        vald4 = self.dohod4.value()
        vals1 = self.strah1.value()
        vals2 = self.strah2.value()
        vals3 = self.strah3.value()
        vals4 = self.strah4.value()
        vala1 = self.avance1.value()
        vala2 = self.avance2.value()
        vala3 = self.avance3.value()


        self.doubleSpinBoxyear.setValue(vald1+vald2+vald3+vald4)
        self.doubleSpinBoxusn.setValue((vald1+vald2+vald3+vald4) * 0.06)
        self.doubleSpinBoxkvartal.setValue((vald1) * 0.06)
        self.doubleSpinBoxhalfyear.setValue(((vald1+vald2) * 0.06) - vala1 - vals1)
        self.doubleSpinBox9mes.setValue(((vald1+vald2+vald3) * 0.06) - vala1 - vala2 - vals1 - vals2)
        self.doubleSpinBoxgod.setValue(((vald1+vald2+vald3+vald4) * 0.06) - vala1 - vala2 - vala3 - vals1 - vals2 - vals3 - vals4)


    def clearcalc(self):
        self.doubleSpinBoxyear.setValue(0.0)
        self.doubleSpinBoxusn.setValue(0.0)
        self.doubleSpinBoxkvartal.setValue(0.0)
        self.doubleSpinBoxhalfyear.setValue(0.0)
        self.doubleSpinBox9mes.setValue(0.0)
        self.doubleSpinBoxgod.setValue(0.0)
        self.dohod1.setValue(0.0)
        self.dohod2.setValue(0.0)
        self.dohod3.setValue(0.0)
        self.dohod4.setValue(0.0)
        self.strah1.setValue(0.0)
        self.strah2.setValue(0.0)
        self.strah3.setValue(0.0)
        self.strah4.setValue(0.0)
        self.avance1.setValue(0.0)
        self.avance2.setValue(0.0)
        self.avance3.setValue(0.0)


    def updateConvertBtn(self, value):
        self.CalcButton.setEnabled(bool(value))
