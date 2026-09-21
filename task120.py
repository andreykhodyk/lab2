distance = float(input())
time_min = float(input())

hours = time_min / 60
speed = distance / hours

if speed <= 60:
    print("Traffic rules are executed.")
else:
    print("Traffic rules are not met.")
    