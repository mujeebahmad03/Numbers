from decimal import Decimal, getcontext

def calc_pi():
    num = int(input('Enter the number of decimal places (1 - 1000) you want the value of pi: ' ))
    if num <= 0 or num >= 1000:
        return 'Invalid num. Please enter a number between 1 and 1000'
    
    getcontext().prec = num + 2
    
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
