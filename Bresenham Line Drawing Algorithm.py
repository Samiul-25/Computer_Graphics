import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0,0], [4,6]])

del_x = points[-1][0] - points[0][0]
del_y = points[-1][1] - points[0][1]

p = 2*del_y - del_x
x = points[0][0]
y = points[0][1]

resulted_points = [[x,y]]

while True:
    x += 1
    if p < 0:
        p = p + 2*del_y
    else:
        y += 1
        p = p + 2*del_y - 2*del_x

    if abs(x) > abs(points[-1][0]) or abs(y) > abs(points[-1][1]):
        break 

    resulted_points.append([x, y])

resulted_points = np.array(resulted_points)
resulted_points = resulted_points.astype(np.int32)
plt.plot(resulted_points[:,0], resulted_points[:,1])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Line Drawing Algorithm')
plt.grid()
plt.show()