def decorator_func1(original_func1):
    def wrapper1():
        print("--------------------------")
        original_func1()
        print("**************************")
    return wrapper1

@decorator_func1
def abc():
    print("Helloo!")
abc()