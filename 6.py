def prime_check(num):
    check = 1
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            check = 0
            break

    return check

def prime(r):
    if r > 1:
        l = [2]

        for n in range(3, r+1, 2):
            if prime_check(n):
                l.append(n)

        return l

    else:
        return []

if __name__ == '__main__':
    prime_range = int(input("Enter the range: "))
    
    prime_array = prime(prime_range)
    
    print("Array of prime numbers in the given range:", prime_array)
