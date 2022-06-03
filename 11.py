if __name__ == '__main__':
    string = input("Enter the string: ").lower()
    
    if string == string[::-1]:
        print("The given string is a Palindrome")
        
    else:
        print("The given string is Not a Palindrome")
