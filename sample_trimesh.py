import trimesh
import numpy as np
from shapely.geometry import LineString
import matplotlib.pyplot as plt

mesh = trimesh.load_mesh('./models/nut.stl')

# get a single cross section of the mesh
slice = mesh.section(plane_origin=(1,1,5),
                     plane_normal=[0, 0, 1])

# the section will be in the original mesh frame
# slice.show()
slice_2D, to_3D = slice.to_planar()
# slice_2D.show()


# # if we wanted to take a bunch of parallel slices, like for a 3D printer
# # we can do that easily with the section_multiplane method
# # we're going to slice the mesh into evenly spaced chunks along z
# # this takes the (2,3) bounding box and slices it into [minz, maxz]
z_extents = mesh.bounds[:,2]
# # slice every .125 model units (eg, inches)
z_levels  = np.arange(*z_extents, step=.125)
# # find a bunch of parallel cross sections
sections = mesh.section_multiplane(plane_origin=mesh.bounds[0],
                                   plane_normal=[0,0,1],
                                   heights=z_levels)
print(sections)
for polygon in slice_2D.polygons_closed:
    # trimesh.path.polygons.plot_polygon(polygon, show=True)
    print(polygon.area)
#
# # summing the array of Path2D objects will put all of the curves
# # into one Path2D object, which we can plot easily
print(len(sections))
import time
combined= np.sum(sections[0])
for i in sections:
    time.sleep(0.5)
    combined = np.sum(i)
    combined.show()

# combined = np.sum(sections[100])
# combined.show()
# # if we want to intersect a line with this 2D polygon, we can use shapely methods
# polygon = slice_2D.polygons_full[0]
# print(polygon)
#
# # # intersect line with one of the polygons
# # hits = polygon.intersection(LineString([[-4,-1], [3,0]]))
# # # check what class the intersection returned
# # print(hits.__class__)
#
# # we can plot the intersection (red) and our original geometry(black and green)
# # ax = plt.gca()
# # for h in hits.geoms:
# #     ax.plot(*h.xy, color='r')
# # slice_2D.show()
# # (slice_2D + slice_2D.medial_axis()).show()
# import pymesh
# mesh = pymesh.load_mesh('./models/nut.stl')
