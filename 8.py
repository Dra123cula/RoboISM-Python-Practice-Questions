def sum_of_int(s):
    ans = 0
    
    for i in s:
        if i.isdigit():
            ans += int(i)

    return ans

if __name__ == '__main__':
    string = input("Enter the string: ")
    
    int_sum = sum_of_int(string)
    
    print("Sum of integers in the string:", int_sum)
