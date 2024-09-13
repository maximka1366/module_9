def is_prime(func):
    def wrapper(*args):
        a = 0
        summa_ = func(*args)
        for i in range(1, summa_ + 1):
            if summa_ % i == 0:
                a += 1
        if a == 2:
            print("Простое")
        elif a > 2:
            print("Составное")
        return summa_
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c



result = sum_three(2, 3, 6)
print(result)