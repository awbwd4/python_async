import time
import os
import threading
# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

nums = [30]*100



# cpu bound func : 굳이 동시성이 필요없다.
def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for k in numbers :
            for j in numbers:
                total *= i * k * j
    return total



def main():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums)) #21.09 #3
    # print(results)
    # for num in nums:
    #     cpu_bound_func(num)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)