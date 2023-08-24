import math

def is_prime(num):
    '''
    A function that checks if a number is prime
    '''
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

def gen_prime_num():
    '''
    A function that generates a prime number using the "yield" keyword
    '''
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


if __name__ == '__main__':

    prime_generator = gen_prime_num()

    while True:
        user_input = input('Do you want the next prime number (y/n)? ').strip().lower()
        if user_input not in ('y', 'yes'):
            print('Goodbye')
            break
        next_prime = next(prime_generator)
        print(f'Next prime number: {next_prime}')
            