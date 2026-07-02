# Write a program which accepts one character and checks whether it is vowel or consonant

def vowel(ch):
    ch = ch.lower()

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else:
        return False


def main():
    char = input("Enter a character: ")

    if vowel(char):
        print("Vowel")
    else:
        print("Consonant")


if __name__ == "__main__":
    main()