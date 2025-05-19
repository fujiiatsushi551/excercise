students_data = [
    {"name":"A", "math":85, "english":92, "science":78},
    {"name":"B", "math":70, "english":81, "science":88},
    {"name":"C", "math":95, "english":88, "science":92},
    {"name":"D", "math":60, "english":75, "science":70},
    {"name":"E", "math":88, "english":90, "science":85},
]
sum = 0
for l in students_data:
    #print(l.get('math'))
    sum += l.get('math')
print(sum/len(students_data))
#print(students_data[0].get('math'))

x = -1
for l in students_data:
    if x <= l.get('science'):
        x = l.get('science')
print(x)

for l in students_data:
    l["total"] = l["math"] + l["english"] + l["science"]
    print(l)