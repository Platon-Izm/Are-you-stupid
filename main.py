from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from random import randint
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 230, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 181, 61))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Yes"))
        self.pushButton_2.setText(_translate("Dialog", "No"))
        self.lineEdit.setText(_translate("Dialog", "Are you stupid?"))

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#function of "no"
def no():
    ui.pushButton_2.setGeometry(QtCore.QRect(randint(0, 290), randint(110, 260), 111, 41))
#function of "yes"
def yes():
    ui.lineEdit.setText("I knew it")
#detect clicked
ui.pushButton_2.clicked.connect(no)
ui.pushButton.clicked.connect(yes)

sys.exit(app.exec())