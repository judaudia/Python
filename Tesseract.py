# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:03:18 2025

@author: judau
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_tesseract():
    vertices = np.array([[x, y, z, w] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] for w in [-1, 1]])
    edges = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if np.sum(np.abs(vertices[i] - vertices[j])) == 2:
                edges.append((i, j))
    return vertices, edges

def project_to_3d(vertices, angle1, angle2):
    rotation_matrix1 = np.array([[np.cos(angle1), -np.sin(angle1), 0, 0],
                                 [np.sin(angle1), np.cos(angle1), 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]])
    rotation_matrix2 = np.array([[1, 0, 0, 0],
                                 [0, np.cos(angle2), -np.sin(angle2), 0],
                                 [0, np.sin(angle2), np.cos(angle2), 0],
                                 [0, 0, 0, 1]])
    rotated_vertices = vertices @ rotation_matrix1.T @ rotation_matrix2.T
    return rotated_vertices[:, :3]

def plot_tesseract(vertices, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for edge in edges:
        points = vertices[list(edge)]
        ax.plot3D(*zip(*points), color='b')
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='r')
    plt.show()

vertices, edges = generate_tesseract()
vertices_3d = project_to_3d(vertices, np.pi/4, np.pi/4)
plot_tesseract(vertices_3d, edges)
