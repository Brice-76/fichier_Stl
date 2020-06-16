from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit
from PySide2.QtGui import QIntValidator,QDoubleValidator
from PySide2 import QtCore
class Potentiometre(QWidget) :

    def __init__(self):
        '''
        Class d'initialisation des 3 potentiometres
        Les fonctions à la fin (knob1,2,3 et ligne1,2,3) permettent de synchroniser la valeur du potentiometre avec le lineEdit
        '''
        QWidget.__init__(self)
        self.__restriction1=QIntValidator(-180,180)
        self.__restriction2=QDoubleValidator(-10,10,2)
        self.dial1=QDial()
        self.dial1.setValue(0)
        self.dial1.setMaximum(100)
        self.dial1.setMinimum(-100)
        self.dial1.valueChanged.connect(self.knob1)
        self.dial2=QDial()
        self.dial2.valueChanged.connect(self.knob2)
        self.dial2.setMinimum(-180)
        self.dial2.setMaximum(180)
        self.dial2.setValue(0)
        self.dial3=QDial()
        self.dial3.setMinimum(-180)
        self.dial3.setMaximum(180)
        self.dial3.setValue(0)
        self.dial3.valueChanged.connect(self.knob3)
        self.layout=QGridLayout()
        self.__lab1=QLabel('Translation Z (m)')
        self.__lab1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__lab2=QLabel('Rotation Y (deg)')
        self.__lab2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__lab3=QLabel('Rotation X (deg)')
        self.__lab3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.line1=QLineEdit()
        self.line1.setValidator(self.__restriction2)
        self.line1.editingFinished.connect(self.ligne1)
        self.line1.setText('0')
        self.line2=QLineEdit()
        self.line2.setValidator(self.__restriction1)
        self.line2.editingFinished.connect(self.ligne2)
        self.line2.setText('0')
        self.line3=QLineEdit()
        self.line3.setValidator(self.__restriction1)
        self.line3.setText('0')
        self.line3.editingFinished.connect(self.ligne3)
        self.layout.addWidget(self.dial1,0,0)
        self.layout.addWidget(self.dial2,0,1)
        self.layout.addWidget(self.dial3,0,2)
        self.layout.addWidget(self.__lab1,1,0)
        self.layout.addWidget(self.__lab2,1,1)
        self.layout.addWidget(self.__lab3,1,2)
        self.layout.addWidget(self.line1,2,0)
        self.layout.addWidget(self.line2,2,1)
        self.layout.addWidget(self.line3,2,2)
        self.setLayout(self.layout)
        self.show()

    def knob1(self):
        self.line1.setText(str(self.dial1.value()/10))

    def knob2(self):
        self.line2.setText(str(self.dial2.value()))

    def knob3(self):
        self.line3.setText(str(self.dial3.value()))

    def ligne1(self):
        #self.dial1.setValue(int(self.line1.text()))
        a=self.line1.text()
        #a=str(a.replace(',','.'))
        print(a)
        self.dial1.setValue(float(a)*10)


    def ligne2(self):
        self.dial2.setValue(float(self.line2.text()))

    def ligne3(self):
        self.dial2.setValue(float(self.line3.text()))


if __name__ == '__main__' :
    app=QApplication([])

    window=Potentiometre()
    window.show()
    app.exec_()

