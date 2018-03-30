# coding=utf-8
import requests
from bs4 import BeautifulSoup
import csv
from importlib import reload

import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")




# План
# 1. Выяснить количество страниц
# 2. Сформировать список урлов на страницы выдачи
# 3. Собрать данные


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')
    return int(total_pages[1].split('&')[0])


def write_csv(data):
    with open('teleram-parse-multi12.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((
            data['url'],
            data['descr'],
        ))
    # pass



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('ol', id='b_results').find_all('li', class_='b_algo')
    # ads = soup.find('ol', id='b_results')
    # print(ads)

    for ad in ads:
        # recieve title price url date
        print(ad)
        # try:
        #     title = ad.find('h3').text.strip()
        # except:
        #     title = ''
        try:
            url = ad.find('a').get('href')
        except:
            url = ''
        try:
            descr = ad.find('p').text.strip()
        except:
            descr = ''

        data = {
            # 'title': title,
            'url': url,
            'descr': descr,
        }

        print (data)
        write_csv(data)




# https://www.bing.com/search?q=site%3at.me+join&qs=n&sp=-1&pq=site%3at.me+join&sc=0-0&sk=&cvid=BC8BC2714C3F47C6A9D9025EE41E9707&first=11&FORM=PERE
def main():
    # https://www.avito.ru/ryazan?p=1&s=101&sgtd=1&view=gallery&q=iphone+6
    url = 'https://www.bing.com/search?q=site%3At.me+join&qs=n&form=QBLH&sp=-1&pq=site%3At.me+join&sc=0-0&sk=&cvid=BC8BC2714C3F47C6A9D9025EE41E9707'

    base_url = 'https://www.bing.com/search?q=site%3at.me+join&qs=n&sp=-1&pq=site%3at.me+join&sc=0-0&sk=&cvid=BC8BC2714C3F47C6A9D9025EE41E9707'

    page_part1 = '&first='
    page_part2 = '&FORM=PERE'


    # total_pages = get_total_pages(get_html(url))
    total_pages = 117272
    # total_pagesExample = 3   # тестовые две страницы



    for i in range(110000,120000):
        if i == 1:
            mnog = str(11)
        else:
            mnog = str(i*11 -1)
        url_gen = base_url + page_part1 + mnog   + page_part2 + str(i)
        print('Cтраница' + str(i))
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)




if __name__ == '__main__':
    main()