Square = lambda No: No * No

def main():
    Data = [10, 12, 8, 9, 11, 20]

    print("Input data is :", Data)

    FData = list(map(Square, Data))

    print("Data after map (squares):", FData)


if __name__ == "__main__":
    main()