from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit,QToolBar,QMessageBox
from PySide2.QtGui import QFont
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Potentiometre import *
from Partie_Droite import *
from Partie_Gauche import *
from outil import *
from graph import *
import math
import sys


class Widget_Matplotlib(QWidget) :
    ''' Class comprenant l'affichage global de l'interface comprend également l'affichage du graph 3D MatplotLib

    lien : correspond au chemin du fichier stl par defaut ''
    d1,d2,d3 sont liés aux changements de valeur des potentiometres avec maj du graph 3D

    '''
    def __init__(self,lien='') :
        QWidget.__init__(self)
        self.setWindowTitle('STL BOAT')
        #self.setFixedSize(1000,800)
        self.box=QGridLayout()
        self.lien=lien

        A=QFont("DIN Condensed", 70)
        self.titre=QLabel("S T L   B O A T")
        self.titre.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        #self.titre.adjustSize()
        self.titre.setFont(A)
        # partie Gauche
        self.partie_gauche=Widget_Gauche(self.lien)
        self.partie_gauche.button_load.clicked.connect(self.push_load)
        # partie Droite
        self.partie_droite=Widget_Droit(self.lien)
        self.partie_droite.button_compute.clicked.connect(self.push_compute)
        self.kx=0
        self.ky=0
        self.kz=0


        # PLOT 3D
        self.fichier=mesh.Mesh.from_file(self.lien)
        self.fichier2=self.fichier
        self.figure= pyplot.figure()
        self.fichier=mesh.Mesh.from_file(self.lien)
        self.init_widget(self.fichier)

        # Connexion des potentiometres
        self.potentiometre=Potentiometre()
        self.potentiometre.dial1.valueChanged.connect(self.d1)
        self.potentiometre.dial2.valueChanged.connect(self.d2)
        self.potentiometre.dial3.valueChanged.connect(self.d3)

        '''Association Layout'''
        self.box.addWidget(self.titre,0,1)
        self.box.addWidget(self.potentiometre,1,1)
        self.box.addWidget(self.canvas,2,1)
        self.box.addWidget(self.partie_gauche,0,0)
        self.box.addWidget(self.partie_droite,0,2,0,2)
        self.setLayout(self.box)
        self.show()

    def init_widget(self,fichier):
        ''' Initialisation de l'affichage 3D Matplotlib '''
        pyplot.close()

        self.figure= pyplot.figure()
        scale = self.fichier.points.flatten()
        self.axes=mplot3d.Axes3D(self.figure)
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors,color='red'))
        self.canvas = FigureCanvas(self.figure)
        self.box.addWidget(self.canvas,2,1)
        self.axes.set_xlabel('X',fontsize=20)
        self.axes.set_ylabel('Y',fontsize=20)
        self.axes.set_zlabel('Z',fontsize=20)
        self.partie_gauche.calcul_caracteristiques(fichier.vectors)
        #mer
        x=np.linspace(-5,5,5)
        y=np.linspace(-5,5,5)
        X, Y = np.meshgrid(x, y)
        z=0*X+0*Y
        self.axes.plot_wireframe(X,Y,z)
    def d1(self):
        self.fichier.translate([0,0,(self.potentiometre.dial1.value()-self.kx)/10])
        self.kx=self.potentiometre.dial1.value()
        self.box.removeWidget(self.canvas)
        self.init_widget(self.fichier)

    def d2(self):
        self.fichier.rotate([1, 0.0, 0.0],math.radians(self.potentiometre.dial2.value()-self.ky))
        self.ky=self.potentiometre.dial2.value()
        self.box.removeWidget(self.canvas)
        self.init_widget(self.fichier)

    def d3(self):
        self.fichier.rotate([0.0, 1, 0.0],math.radians(self.potentiometre.dial3.value()-self.kz))
        self.kz=self.potentiometre.dial3.value()
        self.box.removeWidget(self.canvas)
        self.init_widget(self.fichier)
    def push_load(self):
        '''
        Methode lors de l'appui du bouton 'load'

=> Permet de changer de fichier STL en ouvrant une nouvelle fenêtre

        '''

        Ouverture = QFileDialog.getOpenFileName(self,
                "Ouvrir un fichier",
                "../Documents",
                "STL (*.stl);; TIFF (*.tif);; All files (*.*)")
        print(Ouverture[0])
        self.__lien=str(Ouverture[0])
        window=Widget_Matplotlib(self.__lien)
        window.exec()
        self.close()
        #self.__load_object.setText('Object : '+self.__lien)


    def push_compute(self):
        '''
        Methode lors de l'appui du bouton 'compute'

=> Permet de lancer l'algorithme de dicotomie situé dans Calcul.py
=> Change la valeur sur l'écran LCD en affichant le Tirant d'Eau 10^-2 près
=> création du graph de dicotomie
=> Verification de la valeur de la précision/tolérance
=> oblige la translation d'être supérieur à 2
        '''

        #verif tolérance
        if float(self.partie_droite.precision) >= 1 or float(self.partie_droite.precision)<=0 :
            self.message_box_erreur('''Tolérance
Erreur : la tolérance doit être inferieur à 1 et positive
Erreur : la tolérance doit être un nombre''')
            return
        if self.partie_droite.eau_de_mer.isChecked() == True :
            self.partie_droite.rho=1025
        else :
            self.partie_droite.rho=1000

        # verification de la translation
        translation=abs(self.potentiometre.dial1.value()/10)
        if translation <=2 :
            translation=2
            self.message_box_erreur('La translation est definie à 2')


        #print((self.potentiometre.line1.text()),(self.potentiometre.line1.text()),(self.partie_droite.precision),(self.partie_droite.rho),(self.partie_droite.masse))
        a=Dichotomie(translation,-translation,float(self.partie_droite.precision),self.fichier2.vectors,self.fichier2.normals,float(self.partie_droite.rho),float(self.partie_droite.masse))
        #print('retour dico',a[0])

        self.partie_droite.LCD.display(abs(a[0]))
        self.potentiometre.dial1.setValue(a[0]*10)

        # graph

        self.graph = Widget_Graph(self.lien,float(self.partie_droite.precision),float(self.partie_droite.rho),float(self.partie_droite.masse),translation)
        self.partie_droite.layout.addWidget(self.graph,13,0,2,0)
        self.showFullScreen()



    def message_box_erreur(self,text):
        '''Fenetre Pop-Up affichant un message d'erreur'''
        message=QMessageBox()
        message.setText(text)
        message.setWindowTitle('Erreur')
        icon=(QtGui.QPixmap('091-notification.png'))
        message.setWindowIcon(icon)
        message.exec_()





if __name__ == '__main__' :
    app=QApplication([])
    window=Widget_Matplotlib('V_HULL_Normals_Outward.STL')
    window.show()
    app.exec_()
