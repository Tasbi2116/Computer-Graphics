import numpy as np
import matplotlib.pyplot as plt
import random

N = int(input("Enter the number of circles to draw: "))

plt.figure(figsize=(12, 9))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] 

for i in range(N):
    h, k = random.randint(0, 10), random.randint(0, 10)
    r = random.randint(1, 10)

    print(f"Circle {i+1}:")
    print(f"  Center: ({h}, {k})")
    print(f"  Radius: {r}\n")

    theta = np.linspace(0, 2 * np.pi, 300)  
    x_values = h + r * np.cos(theta)
    y_values = k + r * np.sin(theta)

    # Plot the circle
    plt.plot(x_values, y_values, label=f"Circle {i+1}", color=colors[i % len(colors)])
    plt.scatter(h, k, color='black')  # Mark the center
    plt.text(h, k - 0.4, f"({h},{k})", fontsize=10, ha='right', color='black')

    for j in range(0, 360, 45):  # Mark points at 45-degree intervals
        x_point = h + r * np.cos(np.radians(j))
        y_point = k + r * np.sin(np.radians(j))
        plt.scatter(x_point, y_point, color='red', s=10)
        plt.text(x_point, y_point, f"({int(x_point)},{int(y_point)})", fontsize=8, ha='left', va='top')

plt.legend(loc="lower right")

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"{N} Random Circles")

plt.grid(True)
plt.axis("equal")
plt.show()