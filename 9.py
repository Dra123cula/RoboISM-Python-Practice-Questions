if __name__ == '__main__':
    string = input("Enter the string: ")
    
    l = list(string)
    l.sort()

    new_string = "".join(l)
    
    print("Sorted string:", new_string)
