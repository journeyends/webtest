from bs4 import BeautifulSoup


forbiddenTag = {'script', 'style'}


def filterContent(content):
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.find_all():
        if tag.name in forbiddenTag:
            tag.hidden = True
            tag.clear()
    ret = soup.decode()
    return ret
