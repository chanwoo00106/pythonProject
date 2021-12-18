from requests import get
from bs4 import BeautifulSoup
import json
import os



def commitNum(name):
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

    return [num, f'https://github.com/{name}']