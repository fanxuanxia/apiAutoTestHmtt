from tools.read_yaml import read_yaml
import data

"""以下为公共变量"""
# 1. 请求域名
host = "http://ttapi.research.itcast.cn"

# 2. 请求信息头
headers = {"Content-Type": "application/json"}

# 3. 文章ID
article_id = None

# 读取发表文章的数据
data_article = read_yaml("mp_article.yaml")
print(data_article)
title = data_article[0][0]
content = data_article[0][1]
channel_id = data_article[0][2]
channel = data_article[0][3]


