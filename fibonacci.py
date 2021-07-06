def recur_fib(fib_num):
    if fib_num <= 1:
        return fib_num
    else:
        return(recur_fib(fib_num-1) + recur_fib(fib_num-2))

fib_length = input ("Enter number of fibonacci: ")
fib_length = int(fib_length)

print(recur_fib(fib_length))
