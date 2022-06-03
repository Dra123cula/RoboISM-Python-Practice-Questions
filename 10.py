def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y

    return x, y    

if __name__ == '__main__':
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    
    swap_int1, swap_int2 = swap(int1, int2)

    print("\nAfter swapping.....")
    print("First integer:", swap_int1)
    print("Second integer:", swap_int2)
