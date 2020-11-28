"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the numerator, denumerator not zero (ValueError should be raised in such case), both attributes
  must be integers (TypeError if not),
- method `decimal` returning the decimal value of the fraction.
"""
from math import gcd


class Fraction:
    """
    Fraction class.
    """

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom
