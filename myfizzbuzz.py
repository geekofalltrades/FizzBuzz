def fizzbuzz(n):
    solution = ''
    if not n % 3:
        solution += 'Fizz'
    if not n % 5:
        solution += 'Buzz'
    return solution

if __name__ == '__main__':
    num = int(input("Enter an integer."))
    print(fizzbuzz(num))