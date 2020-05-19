import re
lessons = {}
lines = open('06.txt').readlines()
for line in lines:
    num_sum = 0
    job, rest = line.split(':   ')
    numbers = [int(s) for s in re.findall(r'\d+', rest)]
    for number in numbers:
        num_sum += number
    lessons[job] = num_sum
print(lessons)
