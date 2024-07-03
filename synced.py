import time

def factorize(*numbers):
    def inner(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    results = []
    for number in numbers:
        results.append(inner(number))
    return results

if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(end_time - start_time)
    print(a)
    print(b)
    print(c)
    print(d)