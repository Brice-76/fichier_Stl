from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit,QLCDNumber,QRadioButton,QFileDialog
from PySide2 import QtCore
from PySide2.QtGui import QFont,QIntValidator
from PySide2 import QtGui
import math
class Widget_Droit(QWidget) :
    def __init__(self,obj):
        QWidget.__init__(self)
        self.setFixedWidth(315)
        self.__restriction=QIntValidator()
        self.__precision=0,1
        self.__valeur_z=0
        self.__poids=0
        self.__rho=1250
        self.__label_title=QLabel('''Tirant d'Eau''')
        self.__label_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        A=QFont("DIN Condensed", 45)
        self.__label_title.setFont(A)
        self.__layout=QGridLayout()
        self.__button_compute=QPushButton('Compute')
        self.__button_compute.sizeHint()
        self.__button_compute.clicked.connect(self.push_compute)
        self.__label_precision=QLabel('Tolérance')
        self.__label_precision.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__text_precision=QLineEdit()
        self.__text_precision.setValidator(self.__restriction)
        self.__label_valeur_z=QLabel('Valeur Z (m)')
        self.__label_valeur_z.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__text_valeur_z=QLineEdit()
        self.__text_valeur_z.setValidator(self.__restriction)
        self.__label_poids=QLabel('Cas de Masse (kg)')
        self.__label_poids.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__text_poids=QLineEdit()
        self.__text_poids.setValidator(self.__restriction)

        self.__text_precision.textChanged.connect(self.l1)
        self.__text_poids.textChanged.connect(self.l2)
        self.__text_valeur_z.textChanged.connect(self.l3)

        self.__eau_de_mer=QRadioButton('''Eau De Mer''')
        self.__eau_de_mer.setChecked(True)
        self.__eau_douce=QRadioButton('''Eau Douce''')



        A=QFont("DIN Condensed", 20)
        self.__label_LCD=QLabel('''Tirant d'eau (m)''')
        self.__label_LCD.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__label_LCD.setFont(A)
        self.__LCD=QLCDNumber()

        self.__layout.addWidget(self.__label_title,0,0,1,0)
        self.__layout.addWidget(self.__label_precision,2,0,1,0)
        self.__layout.addWidget(self.__text_precision,3,0,1,0)
        self.__layout.addWidget(self.__label_poids,4,0,1,0)
        self.__layout.addWidget(self.__text_poids,5,0,1,0)
        self.__layout.addWidget(self.__label_valeur_z,6,0,1,0)
        self.__layout.addWidget(self.__text_valeur_z,7,0,1,0)
        self.__layout.addWidget(self.__eau_de_mer,8,0)
        self.__layout.addWidget(self.__eau_douce,8,1)
        self.__layout.addWidget(self.__button_compute,9,0,1,0)
        self.__layout.addWidget(self.__label_LCD,11,0,1,0)
        self.__layout.addWidget(self.__LCD,12,0,1,0)
        self.setLayout(self.__layout)

    def l1(self):
        self.__precision=int(self.__text_precision.text())
    def l2(self):
        self.__poids=int(self.__text_poids.text())
    def l3(self):
        self.__valeur_z=int(self.__text_valeur_z.text())

    def push_compute(self):
        if self.__eau_de_mer.isChecked() == True :
            self.__rho=1250
        else :
            self.__rho=1000
        print('precision :',self.__precision,' -|- poids : ',self.__poids,' -|- valeur z :',self.__valeur_z,' -|- valeur rho :',self.__rho)
        Ouverture = QFileDialog.getOpenFileName(self,
                "Ouvrir un fichier",
                "../Documents",
                "STL (*.stl);; TIFF (*.tif);; All files (*.*)")
        print(Ouverture[0])





if __name__ == '__main__' :
    app=QApplication([])
    window=Widget_Droit('V_HULL.STL')
    window.show()
    app.exec_()
