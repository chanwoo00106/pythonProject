# 정답은 나오나 너무 오래 걸림

s = input().split()
userS = input()
position = 1
posList = []
result = 0


def comparison(a, b):  # 두 문자열 비교 함수
    if a == b:
        posList.append(position)
        return True
    return False


for i in s:
    for num in range(0, len(i)):
        compareString = i[num:num + len(userS)]
        if len(compareString) < len(userS):  # 비교하는 두 문자열중 입력된 문자열이 더 클 시
            position += len(compareString) + 1
            break
        if comparison(compareString, userS):
            result += 1
        position += 1


print(result)
for i in posList:
    print(f"{i} ", end="")
