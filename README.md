[![Build Status](https://travis-ci.org/geekofalltrades/FizzBuzz.png?branch=master)](https://travis-ci.org/geekofalltrades/FizzBuzz)

Approach:
I implemented fizzbuzz as a function that takes the integer as a
positional argument, and the tests as an ambiguous list of keyword
arguments. No tests are supplied by default, so for classic FizzBuzz,
the arguments Fizz=3 and Buzz=5 must be supplied.

Thoughts:
The problem was pretty straightforward, although Python's ability to
take an arbitrary number of arguments combined with its ability to
decipher keyword arguments made the solution particularly elegant. Perl
also takes an arbitrary number of arguments for functions, but I would
have had to implement a parser to pass in keyword arguments or first
populated a Perl hash (associative array) with String->Int key-value
pairs and then passed it as the argument. Both were immediately possible
in Python with no hassle on my part.