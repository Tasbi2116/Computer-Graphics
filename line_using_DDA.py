import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    x_values = []
    y_values = []

    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if(dy > dx):
        dx, dy = dy, dx
        x1, y1 = y1, x1
        x2, y2 = y2, x2


    if(dx > 0):
        m = dy / dx
    else:
        m = float('inf')
    

    if(m <= 1):
        steps = dx
        x = x1
        y = y1

        x_values.append(x)
        y_values.append(y)
        
        for i in range(0, steps):
            x = 1 + x
            y = m + y         
            x_values.append(x)
            y_values.append(y)

    elif(m>1):
        x = x1
        y = y1

        x_values.append(x)
        y_values.append(y)
        steps = dy

        for i in range(0, steps):
            x = 1/m + x
            y = 1 + y
            x_values.append(x)
            y_values.append(y)

    else:
        x = x1
        y = y1

        x_values.append(x)
        y_values.append(y)
        steps = dy
        for i in range(0, steps):
            y = 1 + y
            x_values.append(x)
            y_values.append(y)




    plt.plot(x_values, y_values, 'ro-', label='Line')
    plt.plot(x1, y1, 'go', label='Start Point')
    plt.plot(x2, y2, 'bo', label='End Point')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line plot using DDA')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    print(x1, " ", y1, " ", x2, " ", y2)

    DDA(x1, y1, x2, y2)