# Найти НОК двух чисел
import math
# Класический варинат нахождения НОК
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

# Варинат чере math.gcd() находим общий делитель
# далее по формуле lcm(a, b) = (a * b) // math.gcd(a, b)
def glcm_math(a, b):
    return ((a * b) // math.gcd(a, b))

a, b = map(int, input("Введите два числа (через пробел): ").strip().split())
print(f"НОК числел {a=} и {b=} = {get_least_common_multiple(a, b)}")
print(f"НОК числел {a=} и {b=} = {glcm_math(a, b)}")