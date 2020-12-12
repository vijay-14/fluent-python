def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        # print(average)
        term = yield average
        total += term
        count += 1
        average = total/count

avg = averager()
avg
next(avg)
avg.send(0)
import random
for i in range(10**2):
    avg.send(random.randint(1,10**8))