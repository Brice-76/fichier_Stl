from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Potentiometre import *
import math

class Widget_Matplotlib(QWidget) :
    def __init__(self,lien='') :
        QWidget.__init__(self)
        self.setFixedSize(1000,500)
        self.lien=lien
        self.fichier=mesh.Mesh.from_file(self.lien)
        self.fichierr=self.fichier

        self.box=QVBoxLayout()
        self.figure= pyplot.figure()
        self.fichier=mesh.Mesh.from_file(self.lien)
        scale = self.fichier.points.flatten()
        self.axes=mplot3d.Axes3D(self.figure)
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.init_widget(self.fichier)

        self.potentiometre=Potentiometre()
        self.potentiometre.dial1.valueChanged.connect(self.d1)
        self.potentiometre.dial2.valueChanged.connect(self.d2)
        self.box.addWidget(QLabel('Bienvenue'))
        self.box.addWidget(self.potentiometre)
        self.box.addWidget(self.canvas)
        self.setLayout(self.box)

    def init_widget(self,fichier):

        self.figure= pyplot.figure()
        scale = self.fichier.points.flatten()
        self.axes.clear()

        self.axes=mplot3d.Axes3D(self.figure)

        self.axes.auto_scale_xyz(scale, scale, scale)
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
        self.canvas = FigureCanvas(self.figure)
        self.box.addWidget(self.canvas)
        print('ok')




        print('ok')
    def d1(self):


        self.fichier.translate([0,0,self.potentiometre.dial1.value()])
        print([0,0,self.potentiometre.dial1.value()])
        print(self.fichier.vectors)
        self.init_widget()

    def d2(self):


        self.fichier.rotate([0.5, 0.0, 0.0],math.radians(self.potentiometre.dial2.value()))
        print(self.fichier.vectors[1])
        self.box.removeWidget(self.canvas)

        self.init_widget(self.fichier)
        self.hide()
        self.show()


if __name__ == '__main__' :
    app=QApplication([])

    window=Widget_Matplotlib('Rectangular_HULL.stl')
    window.show()
    app.exec_()
