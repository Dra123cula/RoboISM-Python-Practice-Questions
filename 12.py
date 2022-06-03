def duplicate(l):
    x = sum(l) - 4950

    return x

if __name__ == '__main__':
    array = eval(input("Enter the array: "))
    
    duplicate_num = duplicate(array)
    
    print("Duplicate Number:", duplicate_num)
