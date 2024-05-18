# -*- coding: utf-8 -*-

"""
蒙特卡罗法

随机抽样、统计试验
    当无法求得精确解时，进行随机抽样，根据统计试验求近似解。
"""

import matplotlib.pyplot as plt
import numpy as np

radius = 1

num_points = 100000
points = np.random.rand(num_points, 2) * 2 - 1
inside_circle = points[np.linalg.norm(points, axis=1) < radius]
estimated_area = len(inside_circle) / num_points * 4

print(estimated_area)

plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], color='blue', s=1)
plt.scatter(inside_circle[:, 0], inside_circle[:, 1], color='red', s=1)
circle = plt.Circle((0, 0), radius, color='green', fill=False)
plt.gca().add_artist(circle)
plt.axis('equal')
plt.title(f"Estimated Area: {estimated_area}")
plt.show()

