# useful to do a task together with a function
import time
import math


def elapsed_time(f):
    def wrapper(*args):
        t1 = time.time()
        f(*args)
        t2 = time.time()
        print(f"Elapsed time {(t2-t1)*1000000} ns")
    return wrapper


@elapsed_time  # the decorator
def long_task(angle):
    print(f"Cosinus of {angle} is {math.cos(angle)}")


long_task(math.pi)
