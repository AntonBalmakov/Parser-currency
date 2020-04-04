import requests
from bs4 import BeautifulSoup
import time


EVRO = 'https://finance.tut.by/kurs/minsk/euro/'
DOLLAR_BEL_RUB = 'https://finance.tut.by/kurs/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
full_page = requests.get(DOLLAR_BEL_RUB, headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
def cours():
    convert = soup.find("div", {"class": "b-course"})
    convert = convert.text
    convert = convert[:7]
    a = "1 Доллар равен =" + convert + " бел.р"
    a = ' '.join(a.split())
    print(a)


    full_page2 = requests.get(EVRO, headers=headers)
    soup2 = BeautifulSoup(full_page2.content, 'html.parser')
    convert2 = soup2.find("span", {"class": "red tooltip-holder event-time past"})
    convert2 = convert2.text
    convert2 = convert2[:5]
    a2 = "1 Евро равен = " + convert2 + " бел.р"
    a2 = ' '.join(a2.split())
    print(a2)
    time.sleep(5)

if __name__ == '__main__':
    cours()