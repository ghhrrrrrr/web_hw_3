from multiprocessing import Pool
import time

def worker(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

def factorize(*number):
    with Pool(processes=4) as pool:
        result = pool.map(worker, number)
    return result

if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(end_time - start_time)
    print(a)
    print(b)
    print(c)
    print(d)