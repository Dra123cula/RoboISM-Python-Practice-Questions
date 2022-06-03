def max_frequency(l):
    max_count = 0
    
    for i in l:
        count = l.count(i)

        if count > max_count:
            max_count = count
            x = i

    return x

if __name__ == '__main__':
    array = eval(input("Enter the array: "))
    
    z = max_frequency(array)
    
    print("Element with maximum frequency:", z)
