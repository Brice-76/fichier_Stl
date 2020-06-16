from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit
from PySide2.QtGui import QFont
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Potentiometre import *
from Partie_Droite import *
from Partie_Gauche import *
import math

class Widget_2(QWidget) :
    ''' Class comprenant l'affichage global de l'interface comprend également l'affichage du graph 3D MatplotLib

    lien : correspond au chemin du fichier stl par defaut ''
    d1,d2,d3 sont liés aux changements de valeur des potentiometres avec maj du graph 3D

    '''
    def __init__(self,lien='') :
        QWidget.__init__(self)
        self.setWindowTitle('STL BOAT')
        #self.setFixedSize(1000,800)
        self.box=QGridLayout()

        A=QFont("DIN Condensed", 70)
        self.titre=QLabel("S T L   B O A T")
        self.titre.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.titre.adjustSize()
        self.titre.setFont(A)
        # PLOT 3D
        self.lien=lien
        self.fichier=mesh.Mesh.from_file(self.lien)
        self.kx=0
        self.ky=0
        self.kz=0
        self.figure= pyplot.figure()
        self.fichier=mesh.Mesh.from_file(self.lien)
        self.scale = self.fichier.points.flatten()
        self.axes=mplot3d.Axes3D(self.figure)
        self.axes.auto_scale_xyz(self.scale, self.scale, self.scale)
        self.init_widget(self.fichier)

        self.potentiometre=Potentiometre()
        self.potentiometre.dial1.valueChanged.connect(self.d1)
        self.potentiometre.dial2.valueChanged.connect(self.d2)
        self.potentiometre.dial3.valueChanged.connect(self.d3)

        self.box.addWidget(self.titre,0,1)
        self.box.addWidget(self.potentiometre,1,1)
        self.box.addWidget(self.canvas,2,1)

        # partie Droite

        self.partie_droite=Widget_Droit(self.lien)
        self.box.addWidget(self.partie_droite,0,2,0,2)
        self.setLayout(self.box)

        # partie Gauche
        self.partie_gauche=Widget_Gauche(self.lien)
        self.box.addWidget(self.partie_gauche,0,0)
        self.partie_gauche.button_load.clicked.connect(self.push_load)

    def init_widget(self,fichier):
        ''' Initialisation de l'affichage 3D Matplotlib '''
        pyplot.close()

        self.figure= pyplot.figure()
        scale = self.fichier.points.flatten()
        self.axes=mplot3d.Axes3D(self.figure)
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
        self.canvas = FigureCanvas(self.figure)
        self.box.addWidget(self.canvas,2,1)
        self.axes.set_xlabel('X',fontsize=20)
        self.axes.set_ylabel('Y',fontsize=20)
        self.axes.set_zlabel('Z',fontsize=20)

    def d1(self):
        self.fichier.translate([0,0,self.potentiometre.dial1.value()-self.kx])
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
        Ouverture = QFileDialog.getOpenFileName(self,
                "Ouvrir un fichier",
                "../Documents",
                "STL (*.stl);; TIFF (*.tif);; All files (*.*)")
        print(Ouverture[0])
        self.__lien=str(Ouverture[0])
        print('ok')
        window=Widget_Matplotlib(self.__lien)
        window.show()

        #self.__load_object.setText('Object : '+self.__lien)

if __name__ == '__main__' :
    app=QApplication([])
    window=Widget_Matplotlib('V_HULL.STL')
    window.show()
    app.exec_()
