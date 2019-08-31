#requests爬去豆瓣TOP250电影

from lxml import etree
import requests
import time
import csv


def data_writer(item):
    with open('doubanTop250.csv', 'a', encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(item)

def spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    pre_url = 'https://movie.douban.com/top250?start='
    for i in range(0, 250, 25):
        response = requests.get(url = pre_url + str(i), headers=headers)
        time.sleep(2)
        selector = etree.HTML(response.text)

        move_list = selector.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for move in move_list:
            title = move.xpath('div/div[2]/div[1]/a/span[1]/text()')[0]
            grade = move.xpath('div/div[2]/div[2]/div/span[2]/text()')[0]
            comment_number = move.xpath('div/div[2]/div[2]/div/span[4]')[0]
            content = move.xpath('div/div[2]/div[2]/p[2]/span/text()')[0]
            item = [title, grade, comment_number, content]
            data_writer(item)
            print('正在抓取...', title)

if __name__ == '__main__':
    spider()



