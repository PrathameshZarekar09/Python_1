# Search a word in file

def main():

    file = input("Enter file :")

    word = input("Enter word: ")

    fobj = open(file,"r")

    Data = fobj.read()

    if word in Data:
        print("word ",word," exists")
    else:
        print("not found")

if __name__ == "__main__":
    main()