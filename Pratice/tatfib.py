num = 10
lst = []
fib = 0
for i in range(0, num):
    if i>=2:
        fib = lst[i-1] + lst[i-2]
        lst.append(fib)
    else:
        fib = fib + i
        lst.append(fib)

print(lst)

def fibonacci(num):
    n1, n2 = 0, 1
    sum = 0
    lst = []
    for i in range(0,num):
        lst.append(sum)
        n1 = n2
        n2 = sum
        sum = n1+n2

    print(lst)
fibonacci(10)
