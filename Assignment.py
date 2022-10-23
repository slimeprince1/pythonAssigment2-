# Even numbers
for i in range(1, 30+1):
    if i % 2 == 0:
        print(i)

a = 2
while a <= 30:
    print(a)
    a = a + 2

# odd numbers
for i in range(1, 30+1):
    if i % 2 == 1:
        print(i)

b = 1
while b <= 30:
    if (b % 2 != 0):
        print(b)

capstoneAmount = 50000
print("Marketing:", capstoneAmount * 0.25)
print("Operation:", capstoneAmount * 0.5)
print("Customer acquisition:", capstoneAmount * 0.25)
print("Number of customer:", (capstoneAmount * 0.25) / 5)
