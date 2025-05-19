import random

i = [random.randint(0,99) for _ in range(100)]

s = set(i)
print(s)