def double(s):
    for i in range(len(s)):
        s[i] = 2 * s[i]

    s = "".join(s)

    return s

if __name__ == '__main__':
    string = input("Enter the string: ")
    
    updated_string = double(list(string))
    
    print("New string:", updated_string)
