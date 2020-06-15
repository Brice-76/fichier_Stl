import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math
import time
def affichage_fichier_stl(lien) :
    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    fichier.rotate([0.5, 0.0, 0.0],math.radians(180))

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
    time.sleep(2)
    print('ok')
    fichier.rotate([0.5, 0.0, 0.0],math.radians(180))
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))


affichage_fichier_stl('Mini650_HULL.stl')
