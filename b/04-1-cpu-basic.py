import time
import os
import threading

nums = [30]*100



# cpu bound func : 굳이 동시성이 필요없다.
def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for k in numbers :
            for j in numbers:
                total *= i * k * j
    return total



def main():
    for num in nums:
        cpu_bound_func(num) #26.18
                            #17.01


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)