num = int(input())
result = 0
trashList = []

while(num > 0):
    s = input()
    for i in s:
        try:
            trashList.index(i)
            if trashList[-1] != i:
                result -= 1
                break
        except ValueError:
            trashList.append(i)
            pass

    trashList = []
    result += 1
    num -= 1
print(result)
