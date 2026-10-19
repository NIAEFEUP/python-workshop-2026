# Exercise 19: deriv(f)
# Return a function that numerically approximates the derivative of f using
# df(x) = (f(x + h) - f(x)) / h with h = 0.001, rounded to 3 decimals.
#
# Example tests:
#   f(x) = x*x + 2*x + 2           -> deriv(f)(3)    = 8.001
#   g(x) = sin(x) / x               -> deriv(g)(3.14) = -0.319
#   f(x) = log(x + 10)              -> deriv(f)(-5)   = 0.2
#   f(x) = 3/x + 5                  -> deriv(f)(55.231) = -0.001

def deriv(f):
    h = 0.001

    def df(x):
        return round((f(x + h) - f(x)) / h, 3)

    return df


if __name__ == "__main__":
    def f1(x):
        return x * x + 2 * x + 2
    print(deriv(f1)(3))

    import math

    def g(x):
        return math.sin(x) / x
    print(deriv(g)(3.14))

    def f2(x):
        return math.log(x + 10)
    print(deriv(f2)(-5))

    def f3(x):
        return 3 / x + 5
    print(deriv(f3)(55.231))
