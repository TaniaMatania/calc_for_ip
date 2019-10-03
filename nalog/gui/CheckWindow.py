import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,QSettings


CONFIG_FILE_NAME = 'config3.ini'

class CheckWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(
        """

           QTabBar::tab {
                width: 150px;

            }
           QTabBar::tab:selected {
                font-size: 23px;

                color: #2F4F4F;

                background: #FFE4B5;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                border:2px;
                padding: 12px 50px 10px 24px;

           }

           QTabBar::tab:!selected{

                font-size: 23px;
                color: #2F4F4F;
                background: #BDB76B;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;

                border-top-style: solid;
                padding: 12px 50px 10px 24px;
            }

        """)



    def setupUi(self, Check):
        Check.resize(900, 800)
        Check.setMinimumSize(QtCore.QSize(900, 800))
        Check.setMaximumSize(QtCore.QSize(900, 800))
        oImage = QImage("pic/fon.jpg")
        sImage = oImage.scaled(QSize(900,800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.setWindowIcon(QIcon('pic/moneyjar.png'))
        Check.setWindowTitle("Check")
        #вкладка 2018
        self.checkBox1 = QCheckBox("Оплата УСН за первый квартал 2018                               Срок  до 25.04.2018")
        self.checkBox2 = QCheckBox("Оплата УСН за полугодие 2018                                       Срок  до 25.07.2018")
        self.checkBox3 = QCheckBox("Оплата УСН за девять месяцев 2018                                Срок  до 25.10.2018")
        self.checkBox4 = QCheckBox("Оплата УСН за 2017 год                                                  Срок  до 27.04.2018")
        self.checkBox5 = QCheckBox("Подача налоговой декларации за 2017 год                       Срок  до 27.04.2018")
        self.checkBox6 = QCheckBox("Оплата фиксированных взносов за 2018 год                      Срок  до 31.12.2018")
        self.checkBox7 = QCheckBox("Оплата пенсионных взносов (свыше 1% за 2017 год)         Срок  до 02.07.2018")
        #вкладка 2019
        self.checkBox = QCheckBox("Оплата УСН за первый квартал 2019                               Срок  до 25.04.2019")
        self.checkBox_2 = QCheckBox("Оплата УСН за полугодие 2019                                      Срок  до 25.07.2019")
        self.checkBox_3 = QCheckBox("Оплата УСН за девять месяцев 2019                               Срок  до 25.09.2019")
        self.checkBox_4 = QCheckBox("Оплата УСН за 2018 год                                                 Срок  до 30.04.2019")
        self.checkBox_5 = QCheckBox("Подача налоговой  декларации за 2018 год                     Срок  до 30.04.2019")
        self.checkBox_6 = QCheckBox("Оплата фиксированных взносов за 2019 год                     Срок  до 31.12.2019")
        self.checkBox_7 = QCheckBox("Оплата пенсионных взносов (свыше 1% за 2018 год)        Срок  до 01.07.2019")
        #вкладка 2020
        self.checkBox__1 = QCheckBox("Оплата УСН за первый квартал 2020                             Срок  до 25.04.2020")
        self.checkBox__2 = QCheckBox("Оплата УСН за полугодие 2020                                     Срок  до 25.07.2020")
        self.checkBox__3 = QCheckBox("Оплата УСН за девять месяцев 2020                              Срок  до 25.10.2020")
        self.checkBox__4 = QCheckBox("Оплата УСН за 2019 год                                                Срок  до 25.04.2020")
        self.checkBox__5 = QCheckBox("Подача налоговой декларации за 2019 год                     Срок  до 25.04.2020")
        self.checkBox__6 = QCheckBox("Оплата фиксированных взносов за 2019 год                    Срок  до 31.12.2020")
        self.checkBox__7 = QCheckBox("Оплата пенсионных взносов (свыше 1% за 2019 год)       Срок  до 02.07.2020")

        # наполнение вкладки 2018
        tab_1 = QFrame()
        layout_tab_1 = QVBoxLayout()
        layout_tab_1.addWidget(self.checkBox1)
        layout_tab_1.addWidget(self.checkBox2)
        layout_tab_1.addWidget(self.checkBox3)
        layout_tab_1.addWidget(self.checkBox4)
        layout_tab_1.addWidget(self.checkBox5)
        layout_tab_1.addWidget(self.checkBox6)
        layout_tab_1.addWidget(self.checkBox7)
        tab_1.setLayout(layout_tab_1)
        # наполнение вкладки 2019
        tab_2 = QFrame()
        layout_tab_2 = QVBoxLayout()
        layout_tab_2.addWidget(self.checkBox)
        layout_tab_2.addWidget(self.checkBox_2)
        layout_tab_2.addWidget(self.checkBox_3)
        layout_tab_2.addWidget(self.checkBox_4)
        layout_tab_2.addWidget(self.checkBox_5)
        layout_tab_2.addWidget(self.checkBox_6)
        layout_tab_2.addWidget(self.checkBox_7)
        tab_2.setLayout(layout_tab_2)
        # наполнение вкладки 2020
        tab_3 = QFrame()
        layout_tab_3 = QVBoxLayout()
        layout_tab_3.addWidget(self.checkBox__1)
        layout_tab_3.addWidget(self.checkBox__2)
        layout_tab_3.addWidget(self.checkBox__3)
        layout_tab_3.addWidget(self.checkBox__4)
        layout_tab_3.addWidget(self.checkBox__5)
        layout_tab_3.addWidget(self.checkBox__6)
        layout_tab_3.addWidget(self.checkBox__7)
        tab_3.setLayout(layout_tab_3)

        self.tab = QTabWidget()
        self.tab.addTab(tab_1, "2018")
        self.tab.addTab(tab_2, "2019")
        self.tab.addTab(tab_3, "2020")


        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)
        self.load_settings()


    def save_settings(self):
        settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)

        settings.setValue('BoolValue1', int(self.checkBox1.isChecked()))
        settings.setValue('BoolValue2', int(self.checkBox2.isChecked()))
        settings.setValue('BoolValue3', int(self.checkBox3.isChecked()))
        settings.setValue('BoolValue4', int(self.checkBox4.isChecked()))
        settings.setValue('BoolValue5', int(self.checkBox5.isChecked()))
        settings.setValue('BoolValue6', int(self.checkBox6.isChecked()))
        settings.setValue('BoolValue7', int(self.checkBox7.isChecked()))

        settings.setValue('BoolValue_1', int(self.checkBox.isChecked()))
        settings.setValue('BoolValue_2', int(self.checkBox_2.isChecked()))
        settings.setValue('BoolValue_3', int(self.checkBox_3.isChecked()))
        settings.setValue('BoolValue_4', int(self.checkBox_4.isChecked()))
        settings.setValue('BoolValue_5', int(self.checkBox_5.isChecked()))
        settings.setValue('BoolValue_6', int(self.checkBox_6.isChecked()))
        settings.setValue('BoolValue_7', int(self.checkBox_7.isChecked()))

        settings.setValue('BoolValue__1', int(self.checkBox__1.isChecked()))
        settings.setValue('BoolValue__2', int(self.checkBox__2.isChecked()))
        settings.setValue('BoolValue__3', int(self.checkBox__3.isChecked()))
        settings.setValue('BoolValue__4', int(self.checkBox__4.isChecked()))
        settings.setValue('BoolValue__5', int(self.checkBox__5.isChecked()))
        settings.setValue('BoolValue__6', int(self.checkBox__6.isChecked()))
        settings.setValue('BoolValue__7', int(self.checkBox__7.isChecked()))




        # settings.setValue('BoolValue', 'true' if self.cb_flag.isChecked() else 'false')

    def load_settings(self):
        settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)
        self.checkBox1.setChecked(bool(int(settings.value('BoolValue1', 0))))
        self.checkBox2.setChecked(bool(int(settings.value('BoolValue2', 0))))
        self.checkBox3.setChecked(bool(int(settings.value('BoolValue3', 0))))
        self.checkBox4.setChecked(bool(int(settings.value('BoolValue4', 0))))
        self.checkBox5.setChecked(bool(int(settings.value('BoolValue5', 0))))
        self.checkBox6.setChecked(bool(int(settings.value('BoolValue6', 0))))
        self.checkBox7.setChecked(bool(int(settings.value('BoolValue7', 0))))

        self.checkBox.setChecked(bool(int(settings.value('BoolValue_1', 0))))
        self.checkBox_2.setChecked(bool(int(settings.value('BoolValue_2', 0))))
        self.checkBox_3.setChecked(bool(int(settings.value('BoolValue_3', 0))))
        self.checkBox_4.setChecked(bool(int(settings.value('BoolValue_4', 0))))
        self.checkBox_5.setChecked(bool(int(settings.value('BoolValue_5', 0))))
        self.checkBox_6.setChecked(bool(int(settings.value('BoolValue_6', 0))))
        self.checkBox_7.setChecked(bool(int(settings.value('BoolValue_7', 0))))

        self.checkBox__1.setChecked(bool(int(settings.value('BoolValue__1', 0))))
        self.checkBox__2.setChecked(bool(int(settings.value('BoolValue__2', 0))))
        self.checkBox__3.setChecked(bool(int(settings.value('BoolValue__3', 0))))
        self.checkBox__4.setChecked(bool(int(settings.value('BoolValue__4', 0))))
        self.checkBox__5.setChecked(bool(int(settings.value('BoolValue__5', 0))))
        self.checkBox__6.setChecked(bool(int(settings.value('BoolValue__6', 0))))
        self.checkBox__7.setChecked(bool(int(settings.value('BoolValue__7', 0))))




        # self.cb_flag.setChecked(settings.value('BoolValue', 'false') == 'true')

    def closeEvent(self, e):
        self.save_settings()
        super().closeEvent(e)
