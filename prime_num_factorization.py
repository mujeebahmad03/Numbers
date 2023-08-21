def prime_factor(num):
    '''
    A function that returns the prime factors of the given number
    '''
    factors = []
    divisor = 2 

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    
    return factors


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Enter a number to get its prime factors: '))
            if num < 0:
                print('Invalid input, please enter a positive number')
            else:
                break
        except ValueError:
            print('Invalid input, please enter a valid number')
    
    prime_factors = prime_factor(num)
    print(f'Prime factors of {num} are : {prime_factors}')