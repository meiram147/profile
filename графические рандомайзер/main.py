import string
import pyperclip
from randomgui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import randm as genrand
from PyQt6.QtGui import QIcon
from datetime import datetime
import random
from random import choice
from string import ascii_letters


i = datetime.now().date()
year = i.year
month = i.month
day = i.day

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Randomizer")
        self.setWindowIcon(QIcon("car.png"))
        self.ui.lineEdit.setPlaceholderText("Login")
        self.ui.lineEdit_2.setPlaceholderText("Password")
        self.ui.lineEdit_3.setPlaceholderText("URL")
        self.ui.label.setText(f"        дата: {day}.{month}.{year}")
        g = genrand.d
        save  = self.ui.pushButton_2.clicked.connect(self.save)
        exit = self.ui.pushButton_5.clicked.connect(self.close)
        copypass = self.ui.pushButton_4.clicked.connect(self.copypass)
        copylog = self.ui.pushButton.clicked.connect(self.copylog)
        ranom = self.ui.pushButton_3.clicked.connect(self.randompass)
        paste3 = self.ui.pushButton_6.clicked.connect(self.pasteline3)
        clean = self.ui.pushButton_7.clicked.connect(self.celan)
        paste2 = self.ui.pushButton_8.clicked.connect(self.pasteline2)
        paste1 = self.ui.pushButton_9.clicked.connect(self.pasteline1)



    def celan(self):
        self.ui.lineEdit_3.setText("")

    def pasteline1(self):
        f = pyperclip.paste()
        p = self.ui.lineEdit.setText(f)

    def pasteline2(self):
        f = pyperclip.paste()
        p = self.ui.lineEdit_2.setText(f)

    def pasteline3(self):
        f = pyperclip.paste()
        p = self.ui.lineEdit_3.setText(f)

    def randompass(self):#временное решение генераций паролей надо выбрать нормальный гпсч
        f = genrand.d
        def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))
        s = random.randint(1, 4)
        i = random_char(s)
        p = random_char(s)
        l = ''.join(choice(ascii_letters) for i in range(3))
        a = random.choice(genrand.d)
        if i != f:
            f = p + a + f + l
            s = a + p + l + f
            a = s + a
            p = self.ui.lineEdit_2.setText(a)
        else:
            p = self.ui.lineEdit_2.setText(f)



    def save(self):#сохраняет все введенные данные в одну папку тхт
        login = self.ui.lineEdit.text()
        print(login)
        password = self.ui.lineEdit_2.text()
        Url = self.ui.lineEdit_3.text()
        print(f"login:{login},\npassword:{password}\nURL:{Url}")
        f = open("login and password.txt", 'a')
        f.write(f"login: {login}\npassword: {password}\nURL: {Url}\n")
        f.write("\n*********************************************************************************************************************************\n")
        f.close()

    def copypass(self):#копирует пароль в буфер обмеа
        password = self.ui.lineEdit_2.text()
        pyperclip.copy(password)
        

    def copylog(self):#копирует логин в буфер обмена
        login = self.ui.lineEdit.text()
        pyperclip.copy(login)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())