from decimal import Decimal, getcontext

def calc_euler_const():
    """
    A function that calculates the euler's constant value
    Using the Taylor series expansion of the exponential function. 
            
    """    
    while True:
        try:
            num = int(input('Enter the number of decimal places (1 - 1000) you want the value of e: ' ))
            if num <= 0 or num > 1000:
                print('Invalid num. Please enter a number between 1 and 1000')
            else:
                break
        except ValueError:
            print('Invalid input, please enter a valid number')
    
    getcontext().prec = num + 1

    e = Decimal(1)
    factorial = Decimal(1)

    for n in range(1, num + 1):
        factorial *= n
        e += Decimal(1)/factorial

    return str(e)


if __name__ == '__main__':
    euler_const = calc_euler_const()
    print(euler_const)