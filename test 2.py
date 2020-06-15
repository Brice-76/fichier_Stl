import vtkplotlib as vpl
from stl.mesh import Mesh

path = "V_HULL.stl"

# Read the STL using numpy-stl
mesh = Mesh.from_file(path)

# Plot the mesh
vpl.mesh_plot(mesh, color='red')

# Show the figure
vpl.show()

