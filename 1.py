def sort(l, x):
    if x.lower() == 'asc':
        l.sort()

    elif x.lower() == 'desc':
        l.sort(reverse = True)

    else:
        pass

    return l

if __name__ == '__main__':
    arr = eval(input("Enter the list: "))
    z = input("Task: ")

    a = sort(arr, z)

    print("New list:", a)
