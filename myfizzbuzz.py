def fizzbuzz(n, **kwargs):
    """Extensible fizzbuzz function, passed a number and a list of
kwargs, where keys are strings to be printed and values are
numbers by which n must be divisible to print the key string.
"""
    tests = sorted(kwargs.iteritems(), key=lambda x: x[1])

    solution = ''
    for string, num in tests:
        if not n % num:
            solution += string

    return solution if solution else n

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


#TEST CODE: Tests fizzbuzz() by prompting the user for an integer and a
#list of tests.
if __name__ == '__main__':
    num = int(input("Enter an integer.\n"))
    tests = {}
    userin = 'blargh'
    while(userin):
        userin = raw_input(
"""Enter tests, where term and integer to be divided by are separated by
whitespace (as in 'Fizz 3' or 'Buzz   5'). Submit a blank line when finished.\n""")
        if not userin:
            break
        terms = userin.split()
        tests[terms[0]] = int(terms[1])

    print(fizzbuzz(num, **tests))