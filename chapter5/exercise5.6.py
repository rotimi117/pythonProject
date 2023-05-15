# (Fibonacci) As seen in Exercise 3.15, the Fibonacci numbers are a sequence in which
# each number is the sum of the two preceding ones. Define a function fib that receives three
# consecutive numbers of the Fibonacci series and returns the three subsequent values. Then,
# call the function three times starting with the numbers 0, 1, and 1 and restarting the func-
# tion each time with the resulting numbers of the previous iteration.



def fib(a, b, c):
    d = a + b + c
    e = b + c + d
    f = c + d + e
    return d, e, f

a, b, c = 0, 1, 1

for _ in range(3):
    d, e, f = fib(a, b, c)
    print(d, e, f)
    a, b, c = d, e, f
