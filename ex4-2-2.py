import random

i = [random.randint(0,99) for _ in range(100)]
#print(i)

ul = []

for l in i:

    if l not in ul:
        ul.append(l)

print(sorted(ul))
