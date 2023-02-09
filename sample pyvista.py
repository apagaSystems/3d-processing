import numpy as np
import pyvista as pv

my_mesh = pv.read('./models/cone.stl')

# make sure you compute the normals before you slice it
my_mesh.compute_normals(inplace=True)  # added

centers = my_mesh.cell_centers()
print(len(centers.points))
z_size = my_mesh.bounds[-1] - my_mesh.bounds[-2]
thickness = 400  # micrometer
# slices = my_mesh.slice_along_axis(n=int(z_size * 1000 / thickness), axis="z")
slices = my_mesh.slice_along_axis(n=1, axis="y")
# print(slices.cell_centers())
###############################################################################
# This is for the original dataset

# points from a PolyData dataset
# print(my_mesh.points)

# face centers from a polydata dataset
# print(len(my_mesh.cell_centers().points))

###############################################################################

###############################################################################

# If you want to get all the points from a bunch of slices. This is probably
# what you're looking for.
# combined = slices.combine()
# slice_points = combined.points
# slice_norm = combined.point_data['Normals']
# print(len(slice_points))
# print(slice_points)
# data_slice = []
#
# for item in slice_points:
#     if slice_points[0][-1] == item[-1]:
#         data_slice.append(item)

print(len(data_slice))
print(data_slice)

blocks = pv.MultiBlock(data_slice)
obj = blocks.triangulate()
print(blocks.triangulate)


xx, yy, zz = np.meshgrid(data_slice[0], data_slice[1], data_slice[2])

points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
cloud = pv.PolyData(points)
surf = cloud.delaunay_2d()
surf.plot(show_edges=True)

# pl = pv.Plotter()
# # blocks = pv.MultiBlock(slice_points)
# pl.add_mesh(obj)
# pl.show()

# print(obj.compute_cell_sizes())
# obj.plot(show_edges=True, line_width=5)
