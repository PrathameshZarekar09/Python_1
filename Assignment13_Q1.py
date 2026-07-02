# Write a program which accepts length and width of rectangle and print area
def area_rectangle(length, width):
    return length * width


def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = area_rectangle(length, width)

    print("Area of Rectangle:", area)


if __name__ == "__main__":
    main()