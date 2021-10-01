from requests import get
from bs4 import BeautifulSoup
import json


def commitNum(name):
    data = json.load(open('./ranking.json', 'r', encoding='utf-8'))

    for i in range(1, 19):
        if data.get(f'{i}')[0]['name'] == name:
            name = data[f'{i}'][0]['id']

    html = get(f'https://github.com/{name}')

    soup = BeautifulSoup(html.text, 'html.parser')

    num = 0

    if soup.select(".filter-list.small li") == []:
        return None

    for i in soup.select(".filter-list.small li"):
        html = get(
            f'https://github.com/users/{name}/contributions?tab=overview&from={int(i.get_text())}-01-01&to={int(i.get_text())}-12-31')
        soup = BeautifulSoup(html.text, 'html.parser')
        commit = soup.select_one(".f4.text-normal.mb-2").get_text()
        list = str(commit).split(' ')

        for i in range(0, len(list)):
            try:
                num += int(list[i].replace(',', ''))
                break

            except ValueError:
                pass

    if name == 'baekteun':
        num -= 1000

    for i in range(1, 19):
        user = data.get(str(i))[0]
        if user.get("id") == name:

            data.get(f"{i}")[0]["commit"] = num

            with open('./ranking.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
    return [num, f'https://github.com/{name}']


def ranking():
    data = json.load(open('./ranking.json', 'r', encoding='utf-8'))
    rankingDic = {}
    for i in range(0, 5):
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
                topCommitUser[1] = user.get("name")
        data.pop(f"{tempJ}")
        rankingDic[topCommitUser[1]] = topCommitUser[0]

    return rankingDic


def rankingNum(top):
    data = json.load(open('./ranking.json', 'r', encoding='utf-8'))
    rankingDic = {}
    for i in range(0, top):
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
                topCommitUser[1] = user.get("name")
        data.pop(f"{tempJ}")
        rankingDic[topCommitUser[1]] = topCommitUser[0]

    return rankingDic
