import cv2
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def PointCloudVisualizer(disparity, calib_path):
    # Load calibration data 
    calib_data = cv2.FileStorage(calib_path, cv2.FILE_STORAGE_READ)
    disparity = disparity[0, 0].astype(np.float32)
    Q = calib_data.getNode('Q').mat()
    
    # Calculate inferred depth
    points = cv2.reprojectImageTo3D(disparity, Q)
    # Visualize the 3D point cloud
    points = points.reshape(-1, 3)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd])
