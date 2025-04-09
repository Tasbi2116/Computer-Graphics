import os

def show_menu():
    print("\n===== GRAPHICS PROGRAMS MENU =====")
    print("1. Line using DDA Algorithm")
    print("2. Line using Bresenham Algorithm")
    print("3. Circle using Midpoint Algorithm")
    print("4. Draw Random Circles")
    print("5. Draw Random Lines with Slope and Angle")
    print("0. Exit")
    print("===================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            os.system("python line_using_DDA.py")
        elif choice == '2':
            os.system("python bresenham_line.py")
        elif choice == '3':
            os.system("python Circle_using_midpoint.py")
        elif choice == '4':
            os.system("python Circle.py")
        elif choice == '5':
            os.system("python line.py")
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()