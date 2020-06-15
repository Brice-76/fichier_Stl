import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
def affichage_fichier_stl(lien) :
    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()

affichage_fichier_stl('support_casque.stl')
