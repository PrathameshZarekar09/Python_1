# Write a program which accepts radius of circle and prints area of circle
def circle(radius):
    pi = 3.14
    return pi * radius * radius


def main():
    radius = int(input("Enter radius: "))

    area = circle(radius)

    print("Area of Circle:", area)


if __name__ == "__main__":
    main()