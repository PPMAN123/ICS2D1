# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-27

a = int(input("First number: "))
b = int(input("Second number: "))
gcf = 0

if a > b:
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
else:
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
print(gcf)