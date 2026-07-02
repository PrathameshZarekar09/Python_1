#Write a program which accepts marks and Displays grade. condition example: >= 75 Distinction >= 60 First class  >=50 second class  <50 fail

def grade_(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail Pls try again"


def main():
    marks = int(input("Enter marks: "))

    grade = grade_(marks)

    print("Grade:", grade)


if __name__ == "__main__":
    main()