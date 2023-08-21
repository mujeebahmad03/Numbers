def fibonacci_sequence(n):
    sequence = [1,1]

    if n == 1:
            return sequence[0]

    while n > len(sequence):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return sequence


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Enter the number of sequence you wish to generate: '))
            if num < 1:
                print('Invalid number, please enter a valid number of sequence')
            else:
                break
        except ValueError:
            print('Invalid Input, please enter a valid number of sequence')
    
    fib_sequence = fibonacci_sequence(num)
    print(fib_sequence)