def duplicate(l):
    for num in l:
        count = l.count(num)

        if count == 2:
            return num

if __name__ == '__main__':
    array = eval(input("Enter the array: "))
    
    duplicate_num = duplicate(array)
    
    print("Duplicate Number:", duplicate_num)
