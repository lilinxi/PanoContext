import imageio as im
import numpy as np
import open3d
import CoordsTransfrom

img = im.imread('../images/360_1.jpg')
img = np.array(img)
print(img.shape)

points = []
colors = []
for i in range(0, img.shape[0], 10):
    for j in range(0, img.shape[1], 10):
        u = i / img.shape[0]
        v = j / img.shape[1]
        rgb = img[i][j] / 255
        x, y, z = CoordsTransfrom.uv2xyz(u, v)
        xyzs = CoordsTransfrom.sphere2cube(x, y, z)
        points.extend(xyzs)
        colors.extend([rgb] * len(xyzs))

points = np.array(points)
colors = np.array(colors)
print(points.shape)
print(colors.shape)

pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(points)
pcd.colors = open3d.utility.Vector3dVector(colors)
open3d.visualization.draw_geometries([pcd])
