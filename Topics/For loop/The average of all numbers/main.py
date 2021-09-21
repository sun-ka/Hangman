# put your python code here
a = int(input())
b = int(input())
addition = 0
counter = 0

for i in range(a, b + 1, 1):
    if i % 3 == 0:
        addition += i
        counter += 1
print(addition / counter)
