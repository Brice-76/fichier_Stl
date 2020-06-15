import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
def affichage_fichier_stl(lien) :
    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    fichier.translate()
    print(a)
    print(a[1])
    print(len(a))
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()


class Window(QWidget) :
    def __init__(self,lien=''):
        QWidget.__init__(self)
        self.__layout=QBoxLayout
        graph=Widget_Matplotlib(lien)
        self.__layout.addWidget(graph)
        self.setLayout(self.__layout)
        self.__show()

class Widget_Matplotlib(QWidget) :
    def __init__(self,lien='') :
        QWidget.__init__(self)
        self.box=QVBoxLayout()
        figure= pyplot.Figure()
        self.canvas = FigureCanvas(figure)
        axes=mplot3d.Axes3D(figure)
        fichier=mesh.Mesh.from_file(lien)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
        scale = fichier.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        self.box.addWidget(self.canvas)
        self.setLayout(self.box)

class STL() :
    def __init__(self,lien):
        self.__lien=lien
        fichier=mesh.Mesh.from_file(lien)
        a=(fichier.vectors).




if __name__ == '__main__' :
    app=QApplication([])
    #win=Widget_Matplotlib('V_HULL.stl')
    #win.show()
    window=Window('V_HULL.stl')
    window.show()
    app.exec_()


