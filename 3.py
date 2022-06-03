def operation(x, op, y):
    if op == '+':
        ans = x + y
        
    elif op == '-':
        ans = x - y

    elif op == '/':
        ans = x / y

    else:
        ans = x * y

    return ans

if __name__ == '__main__':
    int1 = int(input("Enter the first integer: "))
    operator = input("Enter the operator: ")
    int2 = int(input("Enter the second operator: "))

    answer = operation(int1, operator, int2)

    print("Answer:", answer)
