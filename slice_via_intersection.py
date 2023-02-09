import numpy as np
import pyvista as pv

my_mesh = pv.read('./models/nut.stl')
x_bound = np.abs(np.abs(my_mesh.bounds[1]) - np.abs(my_mesh.bounds[0]))
y_bound = np.abs(np.abs(my_mesh.bounds[3]) - np.abs(my_mesh.bounds[2]))
z_bound = np.abs(np.abs(my_mesh.bounds[5]) - np.abs(my_mesh.bounds[4]) - 10)
print(x_bound,y_bound,z_bound )
mesh_cube = pv.Cube(center=(0.0, 0.0, 0.0), x_length=x_bound, y_length=y_bound, z_length=z_bound).triangulate()
result = my_mesh.boolean_intersection(mesh_cube)

pl = pv.Plotter()

_ = pl.add_mesh(result, color='tan')
pl.camera_position = 'xz'
pl.show()
