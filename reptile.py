import re
import lxml
import time
import requests
from bs4 import BeautifulSoup

class Air(object):
    """
    斗鱼直播
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        url = "https://www.douyu.com/g_LOL"
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 "}
        res = requests.get(url=url, headers=header)
        if res.status_code != 200:
            raise Exception("网络连接失败")
        soup = BeautifulSoup(res.text, "lxml")
        users = soup.select(".DyListCover-userName")
        users_list = []
        for user in users:
            users_list.append(user.string)
        count = soup.find_all("span", class_='DyListCover-hot')
        people_count = list(re.findall('\d+\.\d?\D', str(count)))
        f = open("douyu.txt", "a", encoding="utf-8")
        i = 0
        link = soup.find_all('a', class_="DyListCover-wrap")
        link_list = list(re.findall(r'(?<=href=")/\d*', str(link)))
        url_list = []
        for i in link_list:
            new_url = "https://www.douyu.com" + i
            url_list.append(new_url)
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "主播排名以及观看数：\n ")
        for i in range(0, len(people_count)):
            f.write(
                "当前排名第{}的主播为： {}，当前观看人数为{},直播链接：{}\n".format(str(i + 1), users_list[i], people_count[i], url_list[i]))
            f.flush()


if __name__ == "__main__":
    air = Air()

    air.get()
