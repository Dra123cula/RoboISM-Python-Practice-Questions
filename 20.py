def prime_check(num):
    check = 1
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            check = 0
            break

    return check

def circular_rotation(x):
    x = list(map(str, str(x)))
    x = x[1::] + x[0:1]
    x = int("".join(x))

    return x

def circular_prime():
    count = 1

    for n in range(3, 1000000, 2):
        z = n
        flag = 1
        
        for i in range(len(str(z))):
            if prime_check(z) == 0:
                flag = 0
                break
            
            z = circular_rotation(z)

        if flag:
            count += 1

    return count

if __name__ == '__main__':
    circular_prime_count = circular_prime()
    
    print("Number of circular prime numbers below one million:", circular_prime_count)
