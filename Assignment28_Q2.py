# Count Words in file

def main():
    file = str(input("Enter File Name: "))

    word = input("Enter The Word you want to search: ")

    fobj = open(file,"r")

    Data = fobj.read()

    count = Data.count(word)

    print("The Word ",word," appears for ",count," times")

    fobj.close()

if __name__ == "__main__":
    main()