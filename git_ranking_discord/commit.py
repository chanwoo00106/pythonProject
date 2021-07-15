from requests import get
from bs4 import BeautifulSoup


commitList = []
idList = ['git id List']

def commitNum(name):
    html = get(f'https://github.com/{name}')

    soup = BeautifulSoup(html.text, 'html.parser')

    commit = soup.select_one(".js-yearly-contributions > .position-relative > .f4").get_text()
    list = str(commit).split(' ')
    a = 0

    for i in range(0, len(list)):
        try:
            return int(list[i])
        except ValueError:
            pass

class commitsNumber():
    def __init__(self, idList):
        self.idList = idList

    def search(name):
        return commitNum(name)
    
    def main(self):
        for i in self.idList:
            if i == None:
                commitList.append(0)
                continue
            commitList.append(commitNum(i))
        return commitList