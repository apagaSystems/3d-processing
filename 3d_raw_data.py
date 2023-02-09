import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

my_mesh = pv.read('./models/cone.stl')
centers = my_mesh.cell_centers()
print(len(centers.points))
z_size = my_mesh.bounds[-1] - my_mesh.bounds[-2]
thickness = 400  # micrometer

slices = my_mesh.slice(normal='y', generate_triangles=False, origin=(0, 1, 0))
for y in range(1, int(z_size)):
    slices += my_mesh.slice(normal='y', generate_triangles=False, origin=(0, y, 0))
print(slices.points)
x_cord = []
z_cord = []
for item in slices.points:
    if item[1] == slices.points[0][1]:
        x_cord.append(item[0])
        z_cord.append(item[2])
print(x_cord)
print(z_cord)
# blocks = pv.MultiBlock(slices_z)
# obj = blocks.triangulate()

# print(blocks.triangulate)
xx, yy = np.meshgrid(x_cord, z_cord)
f = (xx ** 2 + yy ** 2 < 1)
#
# points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
# cloud = pv.PolyData(points)
# surf = cloud.delaunay_2d()
# surf.plot(show_edges=True)

p = pv.Plotter()
p.add_mesh(slices)
p.show()

plt.pcolormesh(xx, yy, f)
plt.show()
