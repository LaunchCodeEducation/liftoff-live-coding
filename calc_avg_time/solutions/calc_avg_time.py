"""
A train is travelling at x miles per hour.

The train must travel a total of y miles.

Calculate how long it will take the train to complete the trip.

You will be given 3 time's to calculate, you need to also calculate the average time of the three trials

trial 1:
x = 20
y = 150

time = 7.5

trial 2:
x = 25
y = 155

time = 6.2

trial 3:
x = 32
y = 162

time = 5.0625 


average time = 6.25416
"""

def calculate_time(mph, distance):
    time = distance / mph
    return time

def calculate_avg(trials):
    sum = 0
    for trial in trials:
        sum += trial
    avg = sum / len(trials)
    return avg

trials = []
trials.append(calculate_time(20, 150))
trials.append(calculate_time(25, 155))
trials.append(calculate_time(32, 162))

for t in trials:
    print(t)

print(calculate_avg(trials))