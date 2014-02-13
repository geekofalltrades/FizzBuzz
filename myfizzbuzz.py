def fizzbuzz(n, **kwargs):
    """Extensible fizzbuzz function, passed a number and a list of
       kwargs, where keys are strings to be printed and values are
       numbers by which n must be divisible to print the key string.
    """
    pass

def oldfizzbuzz(n):
    """Classic fizzbuzz solution: prints Fizz if n divisible by 3, Buzz
       if divisible by 5, FizzBuzz if divisible by both, returns the
       number if divisible by neither.
    """

    solution = ''
    if not n % 3:
        solution += 'Fizz'
    if not n % 5:
        solution += 'Buzz'
    return solution if solution else n

if __name__ == '__main__':
    num = int(input("Enter an integer.\n"))
    print(fizzbuzz(num))