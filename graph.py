import outil
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit,QToolBar
import numpy as np


class Widget_Graph(QWidget) :
    def __init__(self,lien,precision,rho,masse,translation,potentiometre) :
        QWidget.__init__(self)
        self.fig = pyplot.figure()
        self.canvas = FigureCanvas(self.fig)
        axes=pyplot.axes()

        a=(lien.vectors)
        normale=(lien.normals)



        """baisser la présicion"""

        hauteur,nb_rep,liste=outil.Dichotomie(translation,-translation,precision,a,normale,rho,masse,float(potentiometre))
        self.hauteur=hauteur

        x=np.linspace(0,nb_rep,nb_rep)
        axes.plot(x,liste)
        pyplot.style.use(pyplot.style.available[1])
        pyplot.suptitle('Dichotomie')
        pyplot.xlabel('nombre de répetition')
        pyplot.ylabel('''valeur tirant d'eau''')
        #pyplot.show()
        self.canvas.draw()
        layout = QGridLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

if __name__ == '__main__' :
    app=QApplication([])
    window=Widget_Graph('V_HULL_Normals_Outward.stl')
    window.show()
    app.exec_()
