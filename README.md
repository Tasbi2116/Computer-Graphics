# **Computer Graphics (CSE-4104) - Laboratory Work**  

## **Course Overview**  
This repository contains lab work for the course **CSE-4104: Computer Graphics Laboratory**. It includes various practical implementations of **computer graphics concepts**, such as **line drawing algorithms, transformations, 3D graphics, and more**.  

Each lab work is implemented using **Python** with libraries like **Matplotlib, NumPy, and OpenGL** (as needed). More details will be added as new lab exercises are completed.  

---

## **Lab Work 1: Random Line Generator**  

### **Overview**  
This program generates **N random straight lines**, calculates their **slopes** and **angles** with the x-axis, and visualizes them using **Matplotlib**.  

### **Features**  
✔ Random generation of **N lines** with unique start and end points  
✔ Computation of **slope** and **angle** for each line  
✔ Visualization with **color-coded plots**  
✔ **Coordinate labels** for all key points  

### **Installation**  
To run this script, install the required libraries:  
```bash
pip install matplotlib numpy
```

### **Usage**  
1. Run the script:  
   ```bash
   python line.py
   ```
2. Enter the number of lines to generate.  
3. The script prints details of each line and displays a **graph** with plotted lines.  

### **Example Output**  
```
Enter the number of lines to draw: 3  

Line 1:  
  Start Point: (2,4)  
  End Point: (7,9)  
  Slope: 1.00  
  Angle with positive x-axis: 45.00°  
```
**Graph Output:**  
A plot with **3 randomly generated lines**, each labeled with its coordinates.

---

## **Lab Work 2: Circle Drawing**  

### **Overview**  
This program generates **N random circles**, computes their **center points and radii**, and visualizes them using **Matplotlib**.  

### **Features**  
✔ Random generation of **N circles** with unique centers and radii  
✔ Computation and visualization of each circle's **boundary points**  
✔ Marks the **center point** and points at **45-degree intervals**  
✔ Displays **coordinate labels** for key points  

### **Installation**  
To run this script, install the required libraries:  
```bash
pip install matplotlib numpy
```

### **Usage**  
1. Run the script:  
   ```bash
   python Circle.py
   ```
2. Enter the number of circles to generate.  
3. The script prints details of each circle and displays a **graph** with the plotted circles.  

### **Example Output**  
```
Enter the number of circles to draw: 2  

Circle 1:  
  Center: (4,6)  
  Radius: 5  
```
**Graph Output:**  
A plot with **2 randomly generated circles**, each labeled with its **center and 45-degree interval points**.

---

## **Lab Work 3: Line and Circle Drawing Algorithms**

### **Overview**  
This lab focuses on implementing **classic line and circle drawing algorithms** used in computer graphics. It includes three programs demonstrating:

- **DDA (Digital Differential Analyzer) Line Drawing**
- **Bresenham’s Line Drawing Algorithm**
- **Midpoint Circle Drawing Algorithm**

All implementations use **Matplotlib** and **NumPy** for visualization.

### **Features**  
✔ Accurate rendering of **lines and circles** based on pixel-level plotting  
✔ Clear comparison of different **line drawing techniques**  
✔ Visualization of **key points and pixel paths**  
✔ Well-commented code for **easy understanding**  

### **Files Included**
- `line_using_DDA.py` - Implements the **DDA line algorithm**  
- `bresenham_line.py` - Implements **Bresenham’s line algorithm**  
- `Circle_using_midpoint.py` - Implements **Midpoint circle algorithm**  

### **Installation**  
Make sure the required libraries are installed:  
```bash
pip install matplotlib numpy
```

### **Usage**  
Run any script from the terminal:  
```bash
python line_using_DDA.py  
python bresenham_line.py  
python Circle_using_midpoint.py
```

Each script will prompt for input (like coordinates or radius) and display the result using a plotted graph.

### **Example Output**  

**DDA Line Output**  
```
Enter start point (x1, y1): 2 3  
Enter end point (x2, y2): 10 8  
Line drawn using DDA Algorithm  
```

**Bresenham Line Output**  
```
Enter start point (x1, y1): 1 1  
Enter end point (x2, y2): 8 5  
Line drawn using Bresenham’s Algorithm  
```

**Midpoint Circle Output**  
```
Enter center (x, y): 5 5  
Enter radius: 4  
Circle drawn using Midpoint Circle Algorithm  
```

**Graph Output:**  
Each algorithm visualizes the respective **line or circle**, showing the plotted points/pixels clearly.

---

Let me know if you'd like me to add visuals, code snippets, or more advanced formatting to each section!
  
Stay tuned for updates! 🚀  

## **Contributing**  
Feel free to **fork this repository** and contribute. If you find issues or have suggestions, open an **issue** or submit a **pull request**.  

## **License**  
This project is open-source under the **MIT License**.  

---

This version keeps your repository **structured and expandable** for future lab exercises. Let me know if you need any further modifications! 🚀
