import matplotlib.pyplot as plt


def bresenham_algorithm(x1, y1, x2, y2):
    x_values = []
    y_values = []
    x, y = x1, y1
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    m = dy / float(dx) if dx > 0 else float('inf')

    if(m == float('inf')):
        x = x1
        y = y1

        x_values.append(x)
        y_values.append(y)
        steps = dy
        for i in range(0, steps):
            y = 1 + y
            x_values.append(x)
            y_values.append(y)
    else:
        if (m > 1):
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2*dy - dx
        print(f"x = {x}, y = {y}")
        x_values.append(x)
        y_values.append(y)

        for k in range(2, dx+2):
            if (p > 0):
                y = y + 1 if y < y2 else y - 1
                p = p + 2*(dy-dx)
            else:
                p = p + 2*dy

            x = x + 1 if x < x2 else x - 1

            print(f"x = {x}, y = {y}")
            x_values.append(x)
            y_values.append(y)

    plt.plot(x_values, y_values, 'ro-', label='Line')
    plt.plot(x1, y1, 'go', label='Start Point')
    plt.plot(x2, y2, 'bo', label='End Point')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line plot using Bresenham Algorithm')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    print(x1, " ", y1, " ", x2, " ", y2)
    bresenham_algorithm(x1, y1, x2, y2)