from decimal import Decimal, getcontext

def calc_pi():
    """
    A function that calculates pi to a given decimal point value.
    Using the Gauss-Legendre algorithm

    a[0] = 1
    b[0] = 1 / √(2)
    t[0] = 1 / 4
    p[0] = 1

    a[n+1] = (a[n] + b[n]) / 2
    b[n+1] = √(a[n] * b[n])
    t[n+1] = t[n] - p[n] * (a[n] - a[n+1]) ** 2
    p[n+1] = 2 * p[n]

    π ≈ (a[n+1] + b[n+1]) ** 2 / (4 * t[n+1])

    """
    while True:
        try:
            num = int(input('Enter the number of decimal places (1 - 1000) you want the value of pi: ' ))
            if num <= 0 or num > 1000:
                print('Invalid num. Please enter a number between 1 and 1000')
            else:
                break
        except ValueError:
            print('Invalid input, please enter a valid number')

    getcontext().prec = num + 2   # Set the precision of the final value of pi
    
    a = Decimal(1)
    b = Decimal(1)/Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    
    for _ in range(num):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t = t - p * (a - a_next) ** 2
        a = a_next
        p *= 2
    return str((a + b)**2 / (4 * t))[:-1]


if __name__ == "__main__":
    pi = calc_pi()
    print(pi)
