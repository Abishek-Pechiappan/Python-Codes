name = "ABCDEFGHIJ"
names = list(name)
salary = [10000,10000,1200000,55000,45000,20000,26000,20000,17000,25000]
memo = [0,1,1,1,2,3,2,0,0,2,2]

a=list(zip(names, salary, memo))
removed = [i for i in a if i[1]>40000]
bal=[i for i in a if i[1]<=40000]
bal.sort(key=lambda x: x[2], reverse=True)
to_remove = []
for i in bal:
    if(i[2] > 0):
        to_remove.append(i)
    if(len(to_remove) == 3):
        break
final=removed + to_remove
for i in final:
    print("{} has been removed with salary {} and memo {}.".format(i[0], i[1], i[2]))
print("Total number of employees removed: {}".format(len(final)))   