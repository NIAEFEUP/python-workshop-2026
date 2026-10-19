# Exercise 19: deriv(f)
# Return a function that numerically approximates the derivative of f using
# df(x) = (f(x + h) - f(x)) / h with h = 0.001, rounded to 3 decimals.
#
# Example tests:
#   f(x) = x*x + 2*x + 2           -> deriv(f)(3)    = 8.001
#   g(x) = sin(x) / x               -> deriv(g)(3.14) = -0.319
#   f(x) = log(x + 10)              -> deriv(f)(-5)   = 0.2
#   f(x) = 3/x + 5                  -> deriv(f)(55.231) = -0.001
