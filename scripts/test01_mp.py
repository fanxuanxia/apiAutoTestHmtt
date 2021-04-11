from api.api_mp import ApiMp
import pytest
from tools.tool import Tools
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
import api

log = GetLog.get_logger()

class TestMp:
    #  初始化
    def setup_class(self):
        self.mp = ApiMp()

    # 测试登录接口
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, mobile, code):
        r = self.mp.api_mp_login(mobile, code)
        print("登录接口返回的信息为：", r.json())
        try:
            Tools.common_token(r)
            Tools.common_assert(response=r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 发布文章接口测试
    def test02_article(self, title=api.title, content=api.content, channel_id=api.channel_id):
         r = self.mp.api_mp_article(title, content, channel_id)
         print("获取的响应信息为：", r.json())
         # 获取文章id
         api.article_id = r.json().get("data").get("id")
         # 断言
         try:
            Tools.common_assert(response=r)
         except Exception as e:
             log.error(e)
             raise

