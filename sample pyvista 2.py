import numpy as np
from matplotlib import pyplot as plt
from stl import mesh
import pyvista as pv



my_mesh = pv.read('./models/nut.stl')
centers = my_mesh.cell_centers()
print(len(centers.points))
z_size = my_mesh.bounds[-1] - my_mesh.bounds[-2]
thickness = 400  # micrometer
slices = my_mesh.slice_along_axis(n=int(z_size * 1000/thickness), axis="z")


p = pv.Plotter()
p.add_mesh(my_mesh.outline(), color="k")
p.add_mesh(slices)
p.show()
