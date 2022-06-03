def hide(num):
    length = len(num) - 4
    
    for i in range(length):
        num[i] = '*'

    num = "".join(num)

    return num

if __name__ == '__main__':
    credit = input("Credit Card Number: ")
    
    credit_code = hide(list(credit))
    
    print("Encoded Credit Card Number:", credit_code)
