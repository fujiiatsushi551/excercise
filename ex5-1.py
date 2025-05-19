def calc_sum_diff(a,b):
    return a+b, a-b

print(calc_sum_diff(1,2))


def greet(name,time):
    return name+'おはようございます。'

    if time == "morming":
        return name + 'おはようございます。'
    elif time == "noon":
        return name + 'こんにちは。'
    elif time == "evening":
        return name + 'こんばんわ。'

print(greet('a','noon'))