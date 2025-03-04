import numpy as np
import matplotlib.pyplot as plt
import random
import math

N = int(input("Enter the number of lines to draw: "))


plt.figure(figsize=(12, 9))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i in range(N):

    x1, y1 = random.randint(0, 10), random.randint(0, 10)
    x2, y2 = random.randint(0, 10), random.randint(0, 10)
    
    while x1 == x2:
        x2 = random.randint(0, 10)

    m = (y2 - y1) / (x2 - x1)
    theta = math.degrees(math.atan(m))


    print(f"Line {i+1}:")
    print(f"  Start Point: ({x1},{y1})")
    print(f"  End Point: ({x2},{y2})")
    print(f"  Slope: {m:.2f}")
    print(f"  Angle with positive x-axis: {theta:.2f}°\n")

    x_values = []
    y_values = []
    x, y = x1, y1
    step = 1 if x1 < x2 else -1
    while (step > 0 and x <= x2) or (step < 0 and x >= x2):
        x_values.append(x)
        y_values.append(y)
        x += step
        y += m * step
    

    plt.plot(x_values, y_values, label=f"Line {i+1}", color=colors[i % len(colors)])
    plt.scatter(x_values, y_values, color='red', s=10) 
    plt.scatter([x1, x2], [y1, y2], color='black')  
    

    for x, y in zip(x_values, y_values):
        plt.text(x, y, f"({int(x)},{int(y)})", fontsize=8, ha='left', va='top')
    
    plt.text(x1, y1, f"({x1},{y1})", fontsize=10, ha='left', va='top')
    plt.text(x2, y2, f"({x2},{y2})", fontsize=10, ha='right', va='bottom')


plt.xlabel("x")
plt.ylabel("y")
plt.title(f"{N} Random Straight Lines with Slopes and Angles")
plt.legend()
plt.grid(True)
plt.show()