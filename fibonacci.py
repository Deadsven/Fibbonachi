def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = input ("Enter number of fibonacci: ")
nterms = int(nterms)

for i in range(nterms):
    print(recur_fibo(i))
