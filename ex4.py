#問題1
prob = 30
money = 4000

if prob >= 80:
    print('天気が悪いので今日は家で過ごしましょう')
elif prob >= 40 and money >= 5000:
    print('雨が降りそうなので今日は映画を見に行きましょう')
elif prob < 40 and money >= 5000:
    print('天気がいいので今日は遠出しましょう')
elif prob < 40 and money <= 5000:
    print('今日は近場で遊びましょう')

#問題2
n = 1
s = 0
while n <= 100:
    s += n
    n += 2
print(s)

#問題3
l = 0
for i in range(1,101,2):
    l += i
print(l)

#問題4
[i for i in range(1,11) if i % 2 == 0]
print(i)