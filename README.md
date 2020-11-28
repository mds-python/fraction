# Fractions

Write a complete fraction class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined (`+`, `-`, `*`, `/`);

- elegant conversion to string in the form '3/2';

- simplification and clean-up on construction:
  - both attribute divided by the greatest common divisor,
  - denominator not zero (`ValueError` should be raised in such case),
  - sign in the nominator (i.e. denominator is always positive),
  - both attributes must be integers (`TypeError` if not) — you may use Python function `type` or `isinstance` for this check;

- method `decimal` returning the decimal value of the fraction (the nominator divided by the denominator).