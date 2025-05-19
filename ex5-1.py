def calc_sum_diff(a,b):
    return a+b, a-b

print(calc_sum_diff(1,2))


def greet(name,time):
    if time == "morming":
        return name+"さん、" + 'おはようございます。'
    elif time == "noon":
        return name+"さん、" + 'こんにちは。'
    elif time == "evening":
        return name+"さん、" + 'こんばんわ。'

print(greet('たろう','noon'))


#l = [10,30,20]
#max = l[0]
#for i in l:
#    if max <= i:
#        max = i

def get_max(*args):
    if len(args) == 0:
        return 0
    max = args[0]
    for i in args:
        if max < i:
            max = i
    return max

print(get_max())