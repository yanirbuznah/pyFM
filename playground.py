import meshplot as mp
import numpy as np
import open3d as o3d

from pyFM.mesh import TriMesh

obj = 'data/lion-00'
def plot_mesh(myMesh, cmap=None):
    mp.plot(myMesh.vertlist, myMesh.facelist, c=cmap)


def double_plot(myMesh1, myMesh2, cmap1=None, cmap2=None):
    d = mp.subplot(myMesh1.vertlist, myMesh1.facelist, c=cmap1, s=[2, 2, 0])
    mp.subplot(myMesh2.vertlist, myMesh2.facelist, c=cmap2, s=[2, 2, 1], data=d)


def visu(vertices):
    min_coord, max_coord = np.min(vertices, axis=0, keepdims=True), np.max(vertices, axis=0, keepdims=True)
    cmap = (vertices - min_coord) / (max_coord - min_coord)
    return cmap


mesh1 = TriMesh(f'{obj}.off', area_normalize=True, center=False)

# Load the mesh
mesh = o3d.io.read_triangle_mesh(f"{obj}.off")
print(mesh)
# Convert the mesh to a point cloud
pcd = mesh.sample_points_uniformly(number_of_points=10000)
print(pcd)

pcd1 = TriMesh(np.array(pcd.points))

pcd1.geod_from(1000)

# plot_mesh(pcd1, cmap=visu(np.array(pcd.points)))
# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

#save nd array to file
np.save(f'{obj}_1e4.npy', np.array(pcd.points))

#load nd array from file
pcd2 = TriMesh(np.load(f'{obj}.npy'))