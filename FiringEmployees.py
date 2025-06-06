name = "ABCDEFGHIJ"
names = list(name)
salary = [100000,200000,1200000,55000,45000,20000,26000,60000,17000,25000]
memo = [0,1,1,1,2,3,2,0,0,2,2]

filtered = [(n, s, m) for n, s, m in zip(names, salary, memo) if s <= 50000]

names, salary, memo = zip(*filtered)
names = list(names)
salary = list(salary)
memo = list(memo)
print("Names:", names)
print("Salary:", salary)    