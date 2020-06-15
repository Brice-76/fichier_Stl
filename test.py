import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
def affichage_fichier_stl(lien) :
    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    print(a)
    print(a[1])
    print(len(a))
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()


affichage_fichier_stl('V_HULL.stl')
