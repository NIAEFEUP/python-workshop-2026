## 1. n + nn + nnn

Write a Python program that asks the user to input a digit `n` (0-9), calculates the expression `n + nn + nnn` and prints its value.

For example: for a user input `5`, the output must be `615` (5 + 55 + 555).

> Note: Submit a file named `exercise1.py`.

**Example input/output:**

| Input | Output |
| ----- | ------ |
| 0     | 0      |
| 3     | 369    |
| 5     | 615    |
| 9     | 1107   |

---

## 2. Expanded Form of a 4-Digit Number

Write a Python program that asks the user to input a positive 4-digit number `n` and prints the numbers that compose its expanded form.

For example, the expanded form of `1543` is 1000+500+40+3. The expected output for a user input of 1543 is:

```
1000
500
40
3
```

**Example input/output:**

| Input | Output                 |
| ----- | ---------------------- |
| 1543  | 1000<br>500<br>40<br>3 |
| 2123  | 2000<br>100<br>20<br>3 |
| 5000  | 5000<br>0<br>0<br>0    |
| 4765  | 4000<br>700<br>60<br>5 |

---

## 3. Convert Diagram to Code (Expression Tree)

Convert the following diagram to computer code in Python.

The operations should be done sequentially. Be aware of the precedence of the operations and that operands higher up in the diagram have precedence over operands lower down.

Diagram:

```
int(input()) --(*)--> 3 --(-)--> 5  --\
                                      (+) --> print
int(input()) --(+)--> 6 --(//)--> 4 --/
                                      \
                                      (-) --> print
int(input()) --(**)-> 2 --------------/
```

**Example input/output:**

| Input             | Output           |
| ----------------- | ---------------- |
| 0<br>1<br>2       | -4<br>-3         |
| 56<br>12<br>49    | 167<br>-2397     |
| -43<br>24<br>-10  | -127<br>-93      |
| 7653<br>21<br>432 | 22960<br>-186618 |

---

## 4. Cheesecake Sentence — String Chunks

Consider the sentence: _"I ate half of the cheesecake my two roommates made."_.

1. Write a Python program that stores the sentence in the following chunks in different variables, as follows:
   - `"I ate"`
   - `"half"`
   - `"of the cheesecake my"`
   - `"two"`
   - `"roommates made."`
2. Now, print the full sentence using the concatenation of those variables.
3. Next, reassign the variable containing string `"half"` with float value `0.5` and the variable containing string `"two"` with integer value `2`.
4. You will get an error message if you try to rerun the program. Read the error message carefully, fix the problem _without_ using the strings `"0.5"` or `"2"` and submit the fixed program.

**Example output:**

| Output                                           |
| ------------------------------------------------ |
| I ate 0.5 of the cheesecake my 2 roommates made. |

---

## 5. Compound Interest

The formula for computing the final amount if one is earning compound interest is given on Wikipedia as:

**A = P(1 + r/n)^(nt)**

where:

- `P` = principal amount (the amount that the interest is provided on)
- `r` = the interest rate
- `n` = the frequency that the interest is paid out (per year)
- `t` = the number of years that the interest is calculated for

Write a Python program that replaces these letters with something a bit more human-readable and calculate the final amount (A) at the end of the second year, for some varying amounts of money (P) and payment frequency (n) at some interest rate (r).

Please round the result for 3 digits using `round()`.

For example:

- for P = 1000, r = 1% and n = 2 the result is 1020.151
- for P = 650, r = -0.05% and n = 1 and the result is 649.35

**Example input/output:**

| Input               | Output   |
| ------------------- | -------- |
| 1000<br>0.01<br>2   | 1020.151 |
| 650<br>-0.0005<br>1 | 649.35   |
| 100<br>0.1<br>10    | 122.019  |
| 1000<br>0.05<br>20  | 1105.033 |

---

## 6. Staircase Steps

Write a Python program that takes an integer provided by the user, `steps`, representing the number of steps in a staircase. For each step, the program should print the following format:

```
Step: X
```

where `X` is the current step. After finishing, the program prints: `On the ground!`.

For example for `steps = 5` the output is:

```
Step: 5
Step: 4
Step: 3
Step: 2
Step: 1
On the ground!
```

**Example input/output:**

| Input | Output                                                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 3     | Step: 3<br>Step: 2<br>Step: 1<br>On the ground!                                                                                           |
| 5     | Step: 5<br>Step: 4<br>Step: 3<br>Step: 2<br>Step: 1<br>On the ground!                                                                     |
| 6     | Step: 6<br>Step: 5<br>Step: 4<br>Step: 3<br>Step: 2<br>Step: 1<br>On the ground!                                                          |
| 11    | Step: 11<br>Step: 10<br>Step: 9<br>Step: 8<br>Step: 7<br>Step: 6<br>Step: 5<br>Step: 4<br>Step: 3<br>Step: 2<br>Step: 1<br>On the ground! |

---

## 7. Multiplication Table with Early Square Stop

Write a Python program that takes an integer `num`, provided by the user, and outputs the multiplication table with lines: `num x index = res`, where `res = num * index` and `index` is a number that goes from 1 to a maximum of 10.

When the number is multiplied by itself, the displayed format should be `num ^ 2 = res` and the table is finished immediately.

For example for `num = 5` the output is:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 ^ 2 = 25
```

**Example input/output:**

| Input | Output                                                                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3     | 3 x 1 = 3<br>3 x 2 = 6<br>3 ^ 2 = 9                                                                                                                  |
| 5     | 5 x 1 = 5<br>5 x 2 = 10<br>5 x 3 = 15<br>5 x 4 = 20<br>5 ^ 2 = 25                                                                                    |
| 0     | 0 x 1 = 0<br>0 x 2 = 0<br>0 x 3 = 0<br>0 x 4 = 0<br>0 x 5 = 0<br>0 x 6 = 0<br>0 x 7 = 0<br>0 x 8 = 0<br>0 x 9 = 0<br>0 x 10 = 0                      |
| 11    | 11 x 1 = 11<br>11 x 2 = 22<br>11 x 3 = 33<br>11 x 4 = 44<br>11 x 5 = 55<br>11 x 6 = 66<br>11 x 7 = 77<br>11 x 8 = 88<br>11 x 9 = 99<br>11 x 10 = 110 |

---

## 8. 24-Hour to 12-Hour Clock Conversion

Write a Python program that reads two integers, representing the hours (in the interval [0, 24]) and minutes (in the interval [0, 60[), using the 24-hour format and prints the equivalent hour in the 12-hour format.

The 12-hour clock is a time convention in which the 24 hours of the day are divided into two periods, "am" and "pm", each of 12 hours, numbered: 12 (acting as 0), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11 (https://en.wikipedia.org/wiki/12-hour_clock).

The minutes are always represented with two digits and, if the minutes' value is zero, it should not appear in the output (see the examples available in the public tests).

If the hours and minutes values are incorrect, the program must print the message "INVALID DATE FORMAT".

_Hint:_ you can try to use formatted string literals (f-strings) to correctly print leading zeros.

**Example input/output:**

| Input   | Output              |
| ------- | ------------------- |
| 0<br>0  | 12 am               |
| 12<br>0 | 12 pm               |
| 17<br>8 | 5:08 pm             |
| 24<br>0 | INVALID DATE FORMAT |

---

## 9. Reverse a Number (No String Manipulation)

Write a Python program that, given a positive integer `num` by user input, computes its reverse (the number with the digits by the reverse order) and prints it.

You are **not allowed** to use string manipulation (for example string concatenation).

For example:

- for num=766, the output is 667
- for num=789, the output is 987
- for num=45654, the output is 45654

**Example input/output:**

| Input | Output |
| ----- | ------ |
| 766   | 667    |
| 789   | 987    |
| 45654 | 45654  |
| 190   | 91     |

---

## 10. Square of `#` with Zero Center

Write a Python program that prints a square filled with the `#` character for a given dimension, greater or equal to 3.

The square centre must be filled with either one or four zeros (`0`), depending on whether the dimension is odd or even.

For example for dimension 4, the output is:

```
####
#00#
#00#
####
```

and for dimension 5, the output is:

```
#####
#####
##0##
#####
#####
```

**Example input/output:**

| Input | Output                                                                                       |
| ----- | -------------------------------------------------------------------------------------------- |
| 3     | ###<br>#0#<br>###                                                                            |
| 4     | ####<br>#00#<br>#00#<br>####                                                                 |
| 5     | #####<br>#####<br>##0##<br>#####<br>#####                                                    |
| 8     | ########<br>########<br>########<br>###00###<br>###00###<br>########<br>########<br>######## |

---

## 11. Interleave Digits of Two Numbers

Write a Python program that, given two numbers `n1` and `n2` provided by the user, produces a new number `result` by joining the last digit of `n1` (i.e. the least significant) with the last digit of `n2`, and so on for the other digits.

The number of digits of `n1` and `n2` is the same.

You are **not allowed** to use string manipulation (for example string concatenation).

For example:

- if the numbers given are n1=123 and n2=456, the resulting number is 362514.

**Example input/output:**

| Input        | Output   |
| ------------ | -------- |
| 123<br>456   | 362514   |
| 45<br>54     | 5445     |
| 30<br>50     | 35       |
| 1278<br>6431 | 81732416 |

---

## 12. adigits(a, b, c)

Write a Python function `adigits(a, b, c)` that receives three integers, each one with a single decimal digit and returns the lowest integer number that can be assembled with the three digits given as parameters.

**Example tests:**

| Teste                     | Output |
| ------------------------- | ------ |
| `print(adigits(1, 2, 3))` | 123    |
| `print(adigits(9, 1, 9))` | 199    |
| `print(adigits(9, 1, 8))` | 189    |
| `print(adigits(0, 1, 0))` | 1      |

---

## 13. is_perfect(n)

Write a Python boolean function `is_perfect(n)` to check whether a number `n` is perfect or not.

In number theory, **a perfect number** is a positive integer that is equal to the sum of its proper positive divisors, except itself.

For example:

- for n=6, the function returns `True` (because 1+2+3 = 6)
- for n=12, the function returns `False` (because 1+2+3+4+6 = 16 != 12)
- for n=28, the function returns `True` (because 1+2+4+7+14 = 28)

**Example tests:**

| Teste                   | Output |
| ----------------------- | ------ |
| `print(is_perfect(6))`  | True   |
| `print(is_perfect(12))` | False  |
| `print(is_perfect(28))` | True   |
| `print(is_perfect(60))` | False  |

---

## 14. var_numbers(number, precision)

Write a Python function `var_numbers(number, precision)` that returns the variance of all positive integers up to and including `number`. The second parameter defines the precision of the result and has the default value of 2. Use `round` to approximate the result to the given precision.

Remember the formula of variance:

**σ(x) = Σᵢ₌₁..ₙ (xᵢ − x̄)² / N**

where xᵢ is the i-th element of the sequence 1, 2, …, `number`, and x̄ is the average of all those values.

Hint: It is easier if you write an additional function `avg_numbers(number)` that returns the average of all positive integers up to and including `number` and then use this function in the `var_numbers` function.

**Example tests:**

| Teste                       | Output |
| --------------------------- | ------ |
| `print(var_numbers(3))`     | 0.67   |
| `print(var_numbers(10, 1))` | 8.2    |
| `print(var_numbers(15, 3))` | 18.667 |
| `print(var_numbers(7))`     | 4.0    |

---

## 15. reuse(number)

Write a function `reuse(number)` that, given a positive integer `number`, will calculate and return another integer using the following rules:

- Iterate over all numbers between 1 and `number` (inclusive);
- If the current number is odd, calculate its **triangular number** (i.e., if the number is n, calculate the nᵗʰ triangular number, Tₙ);
- If the current number is even, calculate its **factorial**;
- Return the sum of all calculations.

For calculating the triangular number, you can use the following Python function:

```python
def calc_triangular(n):
    triangular = 0
    for x in range(1, n+1):
        triangular += x
    return triangular
```

You must implement a function for calculating the factorial. Recall that the factorial of a number n is the product of all natural numbers between 1 and n. It is defined by the following equation:

**n! = n × (n − 1) × (n − 2) × … × 1**

For example, for `number = 3`, `reuse` should sum T₁ (1 is odd), 2! (2 is even), and T₃ (3 is odd), adding up to 9.

**Example tests:**

| Teste              | Output  |
| ------------------ | ------- |
| `print(reuse(1))`  | 1       |
| `print(reuse(3))`  | 9       |
| `print(reuse(6))`  | 768     |
| `print(reuse(10))` | 3669961 |

---

## 16. rm_letter_rev(ch, s)

Write a Python function `rm_letter_rev(ch, s)` that removes all occurrences of a given character `ch` (case sensitive) from the given string `s` (case sensitive) and returns the resulting string with its characters in the reverse order.

**Example tests:**

| Teste                                                                                 | Output                                                  |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `print(rm_letter_rev("s", "A style guide is about consistency"))`                     | ycnetinoc tuoba i ediug elyt A                          |
| `print(rm_letter_rev(" ", "a nut for a jar of tuna"))`                                | anutforajaroftuna                                       |
| `print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters"))` | srettel evomer ot deed on htiw ecnetnes doog yltcefrepP |
| `print(rm_letter_rev("l", "Please let me keep my letters!"))`                         | !srette ym peek em te esaeP                             |

---

## 17. camel_case(phrase)

Write a Python function `camel_case(phrase)` to convert a given string `phrase` to the camelCase format.

Note that:

- `phrase` may include punctuation or whitespace at the beginning or end.
- `phrase` does not contain digits.
- Words can be separated by whitespaces or punctuation marks (e.g., commas, periods, hyphens, underscores, etc.).

Camel case (sometimes stylized as camelCase or CamelCase, also known as camel caps or more formally as medial capitals) is the practice of writing phrases without spaces or punctuation, indicating the separation of words with a single "uppercase" (capital) letter, and the first letter always "lowercase" (minuscule).

Hint: Have a look at the common string operations at https://docs.python.org/3/library/string.html and the string methods at https://docs.python.org/3.8/library/stdtypes.html#string-methods

**Example tests:**

| Teste                                    | Output       |
| ---------------------------------------- | ------------ |
| `print(camel_case("-Testing"))`          | testing      |
| `print(camel_case("One_more_test  "))`   | oneMoreTest  |
| `print(camel_case("  NumberOne"))`       | numberone    |
| `print(camel_case(",!What about Now?"))` | whatAboutNow |

---

## 18. mask_data(data, n_characters, position)

Write a Python function `mask_data(data, n_characters, position)` that receives a string `data` and returns the masked string in which the first or last `n_characters` characters are masked as an asterisk, according to `position`.

The `position` admits two values: `'begin'` — indicating that masking must consider the first `n_characters` characters of the original string — and `'end'` — indicating that masking must consider the last `n_characters` of the original string.

If `n_characters` is zero then the function must return the original string. If `n_characters` is greater than the total of characters of the string or less than zero then the function must return all the characters masked by asterisks.

**Example tests:**

| Teste                                       | Output        |
| ------------------------------------------- | ------------- |
| `print(mask_data("764987002", 4, "begin"))` | \*\*\*\*87002 |
| `print(mask_data("John Wick", 0, "begin"))` | John Wick     |
| `print(mask_data("202101298", 5, "end"))`   | 2021**\***    |
| `print(mask_data("910432409", 4, "end"))`   | 91043\*\*\*\* |

---

## 19. deriv(f)

Write a Python function `deriv(f)` that receives a function `f` and returns a new function that computes df(x) numerically using the approximation below. Use `round` to approximate the result to 3 decimal places.

Recall that the derivative df(x) of a real function f(x) is defined as a limit:

**df(x) = limₕ→₀ [ f(x+h) − f(x) ] / h**

For a small h, we can numerically compute the derivative using the equation:

**df(x) = [ f(x+h) − f(x) ] / h**

For the sake of simplicity, consider h = 0.001.

**Example tests:**

| Teste                                                                          | Output |
| ------------------------------------------------------------------------------ | ------ |
| `def f(x): return x*x + 2*x + 2`<br>`print(deriv(f)(3))`                       | 8.001  |
| `import math`<br>`def g(x): return math.sin(x) / x`<br>`print(deriv(g)(3.14))` | -0.319 |
| `import math`<br>`def f(x): return math.log(x+10)`<br>`print(deriv(f)(-5))`    | 0.2    |
| `def f(x): return 3/x + 5`<br>`print(deriv(f)(55.231))`                        | -0.001 |

---

## 20. find_highest_paid_employee(database)

Write a Python function `find_highest_paid_employee(database)` that receives a tuple of employee records (`database`), where each record is a tuple in the form `(id, name, department, salary)`.

The function should return the tuple corresponding to the employee with the highest salary. If the database is empty, the function should return the empty tuple. **You can assume that no two salaries are the same.**

For example, if:

```python
database = (
    (1, "Alice", "Engineering", 5500),
    (2, "Bob", "HR", 6200),
    (3, "Charlie", "Engineering", 6100)
)
```

then

```python
find_highest_paid_employee(database)
```

returns

```python
(2, "Bob", "HR", 6200)
```

**Example tests:**

| Teste                                                                                                                                 | Output                            |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `print(find_highest_paid_employee(()))`                                                                                               | ()                                |
| `print(find_highest_paid_employee(((1, "Alice", "Engineering", 7500),)))`                                                             | (1, 'Alice', 'Engineering', 7500) |
| `print(find_highest_paid_employee(((1, "Alice", "Engineering", 5500), (2, "Bob", "HR", 6200), (3, "Charlie", "Engineering", 6100))))` | (2, 'Bob', 'HR', 6200)            |

---

## 21. triplet(tup)

Given a tuple of size > 3, write a Python function `triplet(tup)` that finds a triplet (a, b, c) where a, b, c are elements of `tup`, such that their sum is zero (a + b + c = 0).

In case there is more than one triplet that sums up to zero, return the first occurrence when searching by lexicographical order of indexes. In case there are none, return an empty tuple, `()`.

**Example tests:**

| Teste                                                  | Output      |
| ------------------------------------------------------ | ----------- |
| `print(triplet((-8, 0, 4, -2, -1, 1, 2)))`             | (0, -2, 2)  |
| `print(triplet((-1, 1, 1, 1)))`                        | ()          |
| `print(triplet((-4, 3, 0, -2, -1, -3)))`               | (3, 0, -3)  |
| `print(triplet((-1, 0, -5, -2, 4, 5, 15, 21, 42, 3)))` | (-1, -2, 3) |

---

## 22. multi(g)

A directed **multi-graph** is a graph in which two vertices may be connected by multiple edges, such as the graph drawn in the figure (vertices A, B, C with edges: two parallel edges A→B, one edge A→C, one edge B→C, and two edges C→B, plus one edge A→C... represented as pairs).

A possible representation of a multi-graph is as a tuple of pairs, each representing a single edge. For example, the multi-graph of the figure would be represented as `(('A','B'), ('A','C'), ('B','C'), ('C','B'), ('A','B'))`.

A more succinct representation would be as a tuple of triples, each representing a multi-edge associated with a multiplicity. The same graph would then be represented as `(('A',2,'B'), ('A',1,'C'), ('B',1,'C'), ('C',1,'B'))`.

Write a Python function `multi(g)` that given a multi-graph `g` as a tuple of pairs, returns its representation as a tuple of triples with multiplicities. The order of triples in the tuple is irrelevant.

**Note:** You cannot use lists.

**Example tests:**

| Teste                                                                              | Output                                                       |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))` | (('A', 1, 'C'), ('A', 2, 'B'), ('B', 1, 'C'), ('C', 1, 'B')) |
| `print(tuple(sorted(multi(()))))`                                                  | ()                                                           |
| `print(tuple(sorted(multi(((1,2),(2,3),(3,4)))))`                                  | ((1, 1, 2), (2, 1, 3), (3, 1, 4))                            |
| `print(tuple(sorted(multi((('A','B'),('B','A')))))`                                | (('A', 1, 'B'), ('B', 1, 'A'))                               |

---

## 23. string_length(s)

Write a Python function `string_length(s)` that receives a string `s` and returns its length (the number of characters it contains).

**You must not use** Python's built-in `len()` function or any library that directly computes string length.

For example, if `s = "hello"` then `string_length(s)` returns 5.

**Example tests:**

| Teste                             | Output |
| --------------------------------- | ------ |
| `print(string_length("  "))`      | 2      |
| `print(string_length("a"))`       | 1      |
| `print(string_length("he llo "))` | 7      |
| `print(string_length(""))`        | 0      |

---

## 24. check_amicable(number1, number2)

Write a Python function `check_amicable(number1, number2)` that checks whether the two natural numbers greater than 1 are amicable numbers, that is, whether the sum of the proper divisors of `number1` is `number2`, and the sum of the proper divisors of `number2` returns to `number1`.

Your function should return one of the following strings:

`'same number: v1'`
where v1 is the value of any one of the numbers, if the two numbers are the same (thus not amicable).

`'sum of divisors of v1 is not v2'`
if the sum of proper divisors of v1 does not match v2. The function must always check first if `number1` leads to `number2` and, if it does not, it should immediately return the corresponding string.

`'number1 and number2 form an amicable pair'`
if both numbers' divisor sums lead back to each other.

Hint: define a function `sum_of_proper_divisors(n)` that returns the sum of proper divisors of n (excluding n itself), for n > 1.

**Example tests:**

| Teste                               | Output                              |
| ----------------------------------- | ----------------------------------- |
| `print(check_amicable(220, 284))`   | 220 and 284 form an amicable pair   |
| `print(check_amicable(1210, 1184))` | 1210 and 1184 form an amicable pair |
| `print(check_amicable(10, 10))`     | same number: 10                     |
| `print(check_amicable(10, 20))`     | sum of divisors of 10 is not 20     |

---

## 25. remove_consecutive_duplicates(str)

When processing text, it's sometimes useful to simplify repeated characters that appear consecutively.

For example, the string `"aaabbbccc"` can be reduced to `"abc"`, because each group of repeating characters is replaced by a single one.

Write a function, `remove_consecutive_duplicates(str)` that receives a string `str` and input and returns a new string where consecutive duplicate characters are removed.

**Example tests:**

| Teste                                                 | Output   |
| ----------------------------------------------------- | -------- |
| `print(remove_consecutive_duplicates("aaabbbccc"))`   | abc      |
| `print(remove_consecutive_duplicates("hellooo"))`     | helo     |
| `print(remove_consecutive_duplicates("mississippi"))` | misisipi |
| `print(remove_consecutive_duplicates("a"))`           | a        |

---

## 26. mastermind(g1, g2, g3, c1, c2, c3)

Write a function `mastermind(g1, g2, g3, c1, c2, c3)` to evaluate a single line of a mastermind game.

The function receives 6 single character strings. Each string can be `"b"` for blue, `"w"` for white and `"y"` for yellow. The first 3 arguments are the _user guess_. The last 3 arguments are the _correct key_. Argument `g1` is the user guess for the argument `c1` and so on.

You should give 3 points for each user guess that is completely correct, that is, the same color at the same position in the key and 1 point if the user guessed the color right but at the wrong position (that is, the color exists in the key but at another wrong position). See the tests for examples.

Note that **one right guess (position or color) counts only once**.

**Example tests:**

| Teste                                             | Output |
| ------------------------------------------------- | ------ |
| `print(mastermind("b", "w", "y", "b", "w", "y"))` | 9      |
| `print(mastermind("b", "b", "y", "b", "w", "b"))` | 4      |
| `print(mastermind("b", "w", "y", "w", "y", "w"))` | 2      |
| `print(mastermind("b", "b", "y", "y", "y", "b"))` | 2      |

---

## 27. analyze_text(text, keyword)

Write a function `analyze_text(text, keyword)` that analyzes a string `text` and returns a string with a summary containing:

- the number of words in text,
- the count of occurrences of the given `keyword` (case-insensitive, **without using count()** and **considering overlapping occurrences**, and,
- the same `text` but with all characters in all instances of that keyword replaced by `"*"` (a censored version) and with any leading and trailing whitespaces removed.

The function returns a string summary in the format: `"Words: X; Keyword count: Y; Censored: Z"`

See the public tests for examples.

Use string methods like `split()`, `lower()`, `find()`, `replace()`, and `strip()`.
Do not use `count()`.
Hint: You can also use the method `len()` to count the number of elements in a list.

To learn more about these methods, you should consult the Python Library Reference that is available on Moodle (and will be available during the tests).

**Example tests:**

| Teste                                                              | Output                                                                          |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| `print(analyze_text("This is a simple test sentence.", "simple"))` | Words: 6; Keyword count: 1; Censored: This is a **\*** test sentence.           |
| `print(analyze_text("Nothing to find here.", "hello"))`            | Words: 4; Keyword count: 0; Censored: Nothing to find here.                     |
| `print(analyze_text("Repeat repeat REPEAT!", "repeat"))`           | Words: 3; Keyword count: 3; Censored: **\*** **\*** **\***!                     |
| `print(analyze_text("  Spaces   and punctuation!  ", "and"))`      | Words: 3; Keyword count: 1; Censored: Spaces \*\*\* punctuation!                |
| `print(analyze_text("A Abracadabra to baabraba abrabra", "abra"))` | Words: 5; Keyword count: 5; Censored: A \***\*cad\*\*** to ba**\***ba **\***bra |
