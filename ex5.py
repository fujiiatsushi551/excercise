#問題1
def square(x):
    return x**2

print(square(2))
print(square(3))

#問題2
def mul(y, *args):
    result = y
    for z in args:
        result *= z
    return result

print(mul(1,2))
print(mul(2,4,6))
print(mul(3,5,7,11))

#問題3
def power(p):
    def inner(t):
        return t ** p
    return inner

power3 = power(3)
power4 = power(4)

print(power3(2))
print(power4(3))

#問題4
sum = 0
while True:
    try:
        s = input('Please input number:')
        num = int(s)
        tmp = sum
        sum = sum+num
        print(str(num)+'+'+str(tmp)+'=>'+str(sum))

    except ValueError as ex:
        print('Not a number is inputted.Program exit')
        break
