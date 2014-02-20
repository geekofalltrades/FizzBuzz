Feature: Simple FizzBuzz
    Implement a simple version of the FizzBuzz game.

    Scenario: FizzBuzz of 5
        Given the number <input>
        When I call FizzBuzz
        Then I see the output <output>

    Examples:
    | input | output  |
    | 0     | 0       |
    | 1     | 1       |
    | 3     | Fizz    |
    | 5     | Buzz    |
    | 15    | FizzBuzz|