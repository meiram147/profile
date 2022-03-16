from PySide2 import QtCore, QtGui, QtWidgets
from form import Ui_Form
import sys


app = QtWidgets.QApplication(sys.argv)


Form = QtWidgets.QDialog
ui = Ui_Form()
ui.setupUi(Dialog)
Dialog.show()



sys.exit(app.exec())