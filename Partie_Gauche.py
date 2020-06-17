from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit,QFileDialog
import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy as np
from PySide2 import QtCore,QtGui
from PySide2.QtGui import QFont

import math
class Widget_Gauche(QWidget) :
    ''' Class portant la partie gauche de l'IHM

=> Le calcul des caracteristiques s'éffectue à chaque rotation ou translation du .stl
=> Les surfaces considéré imergé sont s'elles dont le point Z du baricentre est inferieur à 0
=> Permet le changement de fichier STL


    '''

    def __init__(self,lien):
        QWidget.__init__(self)
        self.setFixedWidth(340)
        self.__layout=QGridLayout()
        self.__lien=lien

        fichier=mesh.Mesh.from_file(self.__lien)
        vecteurs=(fichier.vectors)
        self.button_load=QPushButton('Load')
        self.button_load.setFixedHeight(60)
        self.__caracteristiques=QLabel()
        self.calcul_caracteristiques(vecteurs)
        A=QFont("DIN Condensed", 45)
        self.__title=QLabel('Gestion des Fichiers')
        self.__title.setFont(A)
        self.__title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__title.setFixedHeight(100)

        A=QFont("DIN Condensed", 20)
        self.__title_caracteristiques=QLabel('Caractéristiques')
        self.__title_caracteristiques.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.__title_caracteristiques.setFont(A)
        self.__title_caracteristiques.setFixedHeight(80)
        self.__load_object=QLabel('Objet : '+self.__lien)
        self.__load_object.setFixedHeight(60)

        self.button_save=QPushButton('Save')
        self.button_save.setFixedHeight(60)
        # self.__img=QLabel()
        # self.__img.setPixmap(QtGui.QPixmap('anchor.png'))
        # self.__img.setScaledContents(True)
        # self.__img.setFixedHeight(300)
        '''Association Layout'''
        self.__layout.addWidget(self.__title,0,0)
        self.__layout.addWidget(self.__load_object)
        self.__layout.addWidget(self.button_load)
        self.__layout.addWidget(self.button_save)
        self.__layout.addWidget(self.__title_caracteristiques)
        self.__layout.addWidget(self.__caracteristiques)
        #self.__layout.addWidget(self.__img)
        self.setLayout(self.__layout)


    def calcul_caracteristiques(self,vecteurs):

        Stot=0 # Surface totale du .stl
        Stot_dans_eau=0 # Surface totale imergé
        Nb_facettes_dans_eau=0# Nombre de facettes immergés

        for n in range(0,len(vecteurs)): #parcour de la totalité des facettes

            """Calcule de la surface total et de chaque facette"""
            V=(vecteurs[n][1][0]-vecteurs[n][0][0],vecteurs[n][1][1]-vecteurs[n][0][1],vecteurs[n][1][2]-vecteurs[n][0][2])
            W=(vecteurs[n][2][0]-vecteurs[n][0][0],vecteurs[n][2][1]-vecteurs[n][0][1],vecteurs[n][2][2]-vecteurs[n][0][2])
            Ds=np.linalg.norm(np.cross(V,W))/2
            Stot+=Ds

            """Calcule de la hauteur d'une facette """
            Zfk=(vecteurs[n][0][2]+vecteurs[n][1][2]+vecteurs[n][2][2])/3

            """Calcule facette immergé"""
            if Zfk <0:
                Stot_dans_eau+=Ds
                Nb_facettes_dans_eau+=1
        self.__caracteristiques.setText ('Surface : '+str(signif(Stot,4))+' m2\nSurface immergé : '+str(signif(Stot_dans_eau,4))+' m2\nNombre de facette : '
                                         +str(len(vecteurs))+'\nNombre de facette immergé : '+str(Nb_facettes_dans_eau)) #Mise en place IHM



def signif(x, digit):
    ''' Permet de retourné un digit avec un nombre de chiffre significatif defini par digit

=> Source : http://www.python-simple.com/python-langage/operations.php

    '''

    if x == 0:
        return 0
    return round(x, digit - int(math.floor(math.log10(abs(x)))) - 1)


if __name__ == '__main__' :
    app=QApplication([])
    window=Widget_Gauche('V_HULL.STL')
    window.show()
    app.exec_()
