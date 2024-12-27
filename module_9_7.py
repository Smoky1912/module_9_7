# ф-я декоратор, кот. проверяет простой ли рез-т
def is_prime(func):
    # внутр. ф-я wrapper
    def wrapper(*args, **kwargs):
        # вызов ф-и func с передан. аргументами и сохр. рез-т
        result = func(*args, **kwargs)
        # явл. ли рез-т простым числом
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else: # иначе вывод сообщ.
                print("Простое")
        else: # иначе вывод сообщ.
            print("Составное")
        return result
    return wrapper

# ф-я sum_three складывает 3 числа
@is_prime  # декоратор для ф-и sum_three
def sum_three(a, b, c):
    # возврат суммы 3 чисел
    return a + b + c

# пример
result = sum_three(2, 3, 6)
print(result)