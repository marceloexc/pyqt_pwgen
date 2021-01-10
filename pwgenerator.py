import string
import random
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi('MainWindow.ui', self)
        self.show()
        self.horizontalSlider.setValue(25)
        self.horizontalSlider.valueChanged.connect(self.changeLength)
        self.dict = {
            'upper' : string.ascii_lowercase,
            'lower': string.ascii_uppercase,
            'digits': string.digits,
            'special': string.punctuation
        } #remove this 
        print(self.checkBox.isChecked())
        self.variationList = []


    def changeLength(self):
        self.label_6.clear()
        self.label_6.setText(str(self.horizontalSlider.value()))
        self.amount = self.horizontalSlider.value()
        self.pw = ''
        if self.checkBox.isChecked():
            self.variationList.append(string.ascii_uppercase)
            print('lower')
        if self.checkBox_2.isChecked():
            self.variationList.append(string.ascii_lowercase)
            print('upper')
        for i in range(self.amount):
            key=random.choice(list(self.dict))
            self.pw += str(random.choice(self.dict[key]))
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(self.pw)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    app.exec_()