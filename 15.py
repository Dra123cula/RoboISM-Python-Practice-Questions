if __name__ == '__main__':
    string = input("Enter the string: ")
    
    alphabets, digits, characters = 0, 0, 0

    for i in string:
        if i.isalpha():
            alphabets += 1

        elif i.isdigit():
            digits += 1

        else:
            characters += 1

    print("Number of Alphabets:", alphabets)
    print("Number of Digits:", digits)
    print("Number of Special Characters:", characters)
