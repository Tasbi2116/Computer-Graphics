import matplotlib.pyplot as plt
import numpy as np


def circle_midpoint(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    circle_points = []
    while y >= x:
        circle_points.append((xc + x, yc + y))
        circle_points.append((xc - x, yc + y))
        circle_points.append((xc + x, yc - y))
        circle_points.append((xc - x, yc - y))
        circle_points.append((xc + y, yc + x))
        circle_points.append((xc - y, yc + x))
        circle_points.append((xc + y, yc - x))
        circle_points.append((xc - y, yc - x))
        if p >= 0:
            p = p + 2*(x - y) + 5
            y -= 1
        else:
            p = p + 2*x + 3
        x += 1

    return np.array(circle_points)


if __name__ == "__main__":
    print("Enter the center coordinates::")
    xc = int(input())
    yc = int(input())
    r = int(input("Enter the radius of the circle::"))

    circle_points = circle_midpoint(xc, yc, r)

    x = circle_points[:, 0]
    y = circle_points[:, 1]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o', color='red', linestyle = '', markersize=4)
    plt.plot(xc, yc, marker='o', color='blue', markersize=3, label='Center')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Circle using Midpoint Algorithm")
    # plt.xlim([xc - r - r // 5, xc + r + r // 5])
    # plt.ylim([yc - r - r // 5, yc + r + r // 5])
    plt.grid(True)
    plt.show()
