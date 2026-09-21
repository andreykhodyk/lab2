num = input()

d1 = int(num[0])
d2 = int(num[1])
d3 = int(num[2])
d4 = int(num[3])

sum_first = d1 + d2
sum_last = d3 + d4

if sum_first == sum_last:
    print("True")
else:
    print("False")