import numpy as np
from matplotlib import pyplot as plt
from stl import mesh
import pyvista as pv
from pyvista import examples


# mesh = examples.load_channels()
my_mesh = pv.read('./models/nut.stl')
# define a categorical colormap
# cmap = plt.cm.get_cmap("viridis", 4)

slices = my_mesh.slice_along_axis(n=60, axis="z",tolerance=1.0)
clips=my_mesh.clip(normal="z")
elevation=my_mesh.elevation()
# slices = my_mesh.slice((1,0,0))

for item in slices.keys():

    print(np.array(slices["slice0"]))





pl = pv.Plotter()
# centers = my_mesh.cell_centers()
# pl.add_mesh(my_mesh, show_edges=True, opacity=0.5, line_width=1)
# pl.add_mesh(centers, color="r", point_size=4.0, render_points_as_spheres=True)
# voxels = pv.voxelize(my_mesh, density=my_mesh.length / 200)
# pl.add_mesh(voxels, show_edges=True, opacity=0.5, line_width=1)
# pl.add_mesh(slices, show_scalar_bar=False,show_edges=True, opacity=1, line_width=1)
pl.add_mesh(elevation, show_scalar_bar=False,show_edges=True, opacity=1, line_width=1)
pl.show()
# slices.plot()
