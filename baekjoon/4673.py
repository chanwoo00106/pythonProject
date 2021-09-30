num = 1

l = [i for i in range(1, 10001)]


while num <= 10000:
    temp = 0
    temp += num
    Tnum = num
    while Tnum > 0:
        temp = temp + (Tnum % 10)
        Tnum = int(Tnum / 10)
    try:
        l.remove(temp)
    except ValueError:
        pass
    num += 1

for i in range(9):
    print(l[i])
print(" |\n |\n |")

for i in range(-10, 0):
    print(l[i])
