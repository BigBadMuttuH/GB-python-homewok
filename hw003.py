import math

# 1. Найти НОК двух чисел
# Классический вариант нахождения НОК
def get_least_common_multiple(a, b):
    if a == 0 or b == 0: return 0
    lcm = min(a, b)
    # print(f"{a=}, {b=}, {lcm=}")
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
            print(f"{a=}, {b=}, {lcm=}")
        lcm += 1
    return lcm

# 1. Найти НОК двух чисел
# Вариант через math.gcd() находим общий делитель
# далее по формуле lcm(a, b) = (a * b) // math.gcd(a, b)
def glcm_math(a, b):
    return ((a * b) // math.gcd(a, b))

a, b = map(int, input("Введите два числа (через пробел): ").strip().split())
print(f"НОК чисел {a=} и {b=} = {get_least_common_multiple(a, b)}")
print(f"НОК чисел {a=} и {b=} = {glcm_math(a, b)}\n")


# 2. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
def get_PI(d):
    num = len("".join(str(d).split(".")[1]))
    return "{:1.{poins}f}".format(math.pi, poins=num)

a = input("Введите точность для PI (пример 0.001): ")
print(get_PI(a))
