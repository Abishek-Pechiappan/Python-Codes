def a():
    yield 10
    yield 20
    yield 30

gen=a()
print(next(gen))
print(next(gen))