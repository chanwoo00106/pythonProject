testCase = int(input())
topN = []
topP = []


for i in range(0, testCase):
    case = int(input())
    for j in range(0, case):
        name, price = input().split()
        price = int(price)

        try:
            if topP[i] < price:
                topN[i] = name
                topP[i] = price
        except IndexError:
            topN.append(name)
            topP.append(price)

for i in topN:
    print(i)
