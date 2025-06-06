import time 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time Taken : {} Sec".format(end-start))
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(5)
    print("Finished")
slow_function()