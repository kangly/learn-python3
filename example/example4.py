"""
抓取指定小说的内容
安装requests库 'pip3 install requests'
安装beautifulsoup4库 'pip3 install beautifulsoup4'
"""

import requests
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    # 要下载的网页
    url = 'https://www.xsbiquge.com/90_90418/'
    # 网站根网址
    root_url = 'https://www.xsbiquge.com'
    # 保存本地路径
    path = 'file'

    # 解析网址
    req = requests.get(url)

    # 设置编码，浏览器查看网站源代码
    req.encoding = 'utf-8'

    # 获取网页所有内容
    soup = BeautifulSoup(req.text, 'html.parser')

    # 查找网页中div的id为main的标签
    list_tag = soup.div(id="list")

    # 查看div内所有dd标签
    dd = list_tag[0](['dd'])

    # 循环遍历
    for i in dd:
        # 停顿3秒
        time.sleep(3)

        # 获取到a标签间的内容---章节名称
        chapter_name = i.a.string
        # 获取a标签的href地址值---章节网址

        chapter_url = (i(['a'])[0].get('href'))
        complete_chapter_url = root_url + chapter_url

        # 获取网页设置网页编码
        req = requests.get(complete_chapter_url)
        req.encoding = 'utf-8'

        print("章节名：{} ".format(chapter_name))
        print("章节地址：{} ".format(complete_chapter_url))

        # 解析网页
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.div.find(id="content")
        # 转为string类型
        content = str(text)

        # 写入文件操作'a'追加
        with open(path + "/" + chapter_name + ".txt", 'a') as f:
            f.write(chapter_name)
            f.write('\n' + '\n')
            f.write(content)
            print("{}------>写入完毕".format(chapter_name))
            # 直接退出，仅抓取一章做测试用
            exit()