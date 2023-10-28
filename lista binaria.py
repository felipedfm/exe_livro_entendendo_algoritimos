x = int(input("digite um numero"));
y = 0;
while x != 1:
    if x%2 == 0:
        x = x/2
        y += 1
    else:
        x = x//2 + 1
        y += 1
print(y)
