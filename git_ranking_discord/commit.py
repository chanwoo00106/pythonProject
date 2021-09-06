from requests import get
from bs4 import BeautifulSoup
import json

data = json.load(open('./ranking.json', 'r', encoding='utf-8'))

def commitNum(name):

    for i in range(1, 19):
        if data.get(f'{i}')[0]['name'] == name:
            name = data[f'{i}'][0]['id']

    html = get(f'https://github.com/{name}')

    soup = BeautifulSoup(html.text, 'html.parser')

    commit = soup.select_one(
        ".js-yearly-contributions > .position-relative > .f4").get_text()
    list = str(commit).split(' ')
    a = 0

    for i in range(0, len(list)):
        try:
            num = int(list[i])
            for i in range(1, 19):
                user = data.get(f"{i}")[0]
                if user.get("id") == name:

                    data.get(f"{i}")[0]["commit"] = num

                    with open('./ranking.json', 'w', encoding='utf-8') as outfile:
                        json.dump(data, outfile, indent=4, ensure_ascii=False)
            return num
        except ValueError:
            pass


def ranking():
    rankingDic = {}
    for i in range(0, 15):
        topCommitUser = [0, ""]
        tempJ = 0

        for j in range(1, 19):
            try:
                user = data.get(f"{j}")[0]
            except TypeError:
                continue

            if topCommitUser[0] <= user.get("commit"):
                tempJ = j
                topCommitUser[0] = user.get("commit")
                topCommitUser[1] = user.get("id")
        data.pop(f"{tempJ}")
        rankingDic[topCommitUser[1]] = topCommitUser[0]

    return rankingDic
