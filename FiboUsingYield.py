def gen_fibo(x):
    a,b=0,1
    for i in range(x):
        yield a
        a,b=b,a+b

n=int(input("Enter the Number :"))
for i in gen_fibo(n):
    print(i, end=' ')