s = input()
num = 0

for i in range(0, len(s)):
    if s[i] == '=':
        if s[i - 2: i] == 'dz':
            num -= 1
            continue
        elif s[i - 1] == 'c' or s[i - 1] == 's' or s[i - 1] == 'z':
            continue

    elif s[i] == '-':
        if s[i - 1] == 'c' or s[i - 1] == 'd' or s[i - 1]:
            continue

    elif s[i] == 'j':
        if s[i - 1] == 'l' or s[i - 1] == 'n':
            continue

    num += 1

print(num)
