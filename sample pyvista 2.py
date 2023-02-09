import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

my_mesh = pv.read('./models/cone.stl')
centers = my_mesh.cell_centers()
print(len(centers.points))
z_size = my_mesh.bounds[-1] - my_mesh.bounds[-2]
print(my_mesh.bounds)
thickness = 1000  # micrometer
# slices = my_mesh.slice_along_axis(n=int(z_size * 1000/thickness), axis="y")
slices = my_mesh.slice_along_axis(n=1, axis="y")
data_list = []
# slices = my_mesh.slice(normal='y', generate_triangles=False, origin=(0, 1, 0))


combined = slices.combine()
slice_points = combined.points


print(len(slice_points.points))
print(slice_points.points)

# for z in range(1, int(z_size)):
#     # slices += my_mesh.slice(normal='z', generate_triangles=False, origin=(0, 0, z))
#     slices += my_mesh.slice_along_axis(n=int(z_size * 1000/thickness), axis="z")
#     data_list.append(my_mesh.slice_along_axis(n=int(z_size * 1000/thickness), axis="z"))
# print(data_list[0])




# slices = my_mesh.slice_orthogonal(x=10, y=10, z=10)
# data = pv.PolyData(data_list[3])
# data.plot()

p = pv.Plotter()
p.add_mesh(slices, color="w")
# p.add_mesh_slice(my_mesh,normal='z',generate_triangles=True)

# p.add_mesh(slices, style='points')

p.show()
