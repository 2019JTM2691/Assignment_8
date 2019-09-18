a = input("Enter the bit stream : ")
for char in a[0:1]:
    x = int(char)
    print(x)
for char in a[1:]:
    y = int(char)
    x ^= y
print(x)
a += str(x)
print(a)
a = a.replace('010', '0100'
a += '0101'
print(a)
s