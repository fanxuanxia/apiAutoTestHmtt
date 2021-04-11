import api
import requests
from tools.get_log import GetLog
log = GetLog.get_logger()
class ApiMis:

    def __init__(self):
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("正在初始化后台管理系统，登录url:{}".format(self.url_login))
        self.url_search_article = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 查询文章url:{}".format(self.url_search_article))
        self.url_article_audit = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 审核文章url:{}".format(self.url_article_audit))

    def mis_login(self,account, password):
        data = {"account": account, "password": password}
        log.info("正在调用后台管理系统 登录接口，请求数据：{}，请求信息头：{}".format(data, api.headers))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    def mis_search_article(self):
        data = {"title": api.title, "channel": api.channel}
        log.info("正在调用后台管理系统 查询文章接口，请求数据：{}，请求信息头：{}".format(data, api.headers))
        return requests.get(url=self.url_search_article, params=data, headers=api.headers)

    def mis_article_audit(self):
        data = {"article_ids": [api.channel_id], "status":2} # 2为审核通过
        log.info("正在调用后台管理系统 审核文章接口，请求数据：{}，请求信息头：{}".format(data, api.headers))
        return requests.put(self.url_article_audit, json=data, headers= api.headers)