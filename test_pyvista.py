import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

my_mesh = pv.read('./models/cone.stl')
centers = my_mesh.cell_centers()
print(len(centers.points))
z_size = my_mesh.bounds[-1] - my_mesh.bounds[-2]
thickness = 1400  # micrometer

slices = my_mesh.slice(normal='y', generate_triangles=False, origin=(0, 0, 10))
for z in range(1, int(z_size)):
    slices+= my_mesh.slice_along_axis(n=int(z_size * 1000/thickness), axis="y")
# print(slices_z.points)

# blocks = pv.MultiBlock(slices_z)
# obj = blocks.triangulate()

# print(blocks.triangulate)
# xx, yy, zz = np.meshgrid(slices_z.points[0], slices_z.points[1], slices_z.points[2])
#
# points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
# cloud = pv.PolyData(points)
# surf = cloud.delaunay_2d()
# surf.plot(show_edges=True)

p = pv.Plotter()
p.add_mesh(slices)
p.show()
