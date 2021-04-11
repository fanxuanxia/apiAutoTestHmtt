import api
from tools.get_log import GetLog
log = GetLog.get_logger()
class Tools:
    @classmethod
    def common_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        log.info("正在提取token，提取到的信息为：{}".format(token))
        # 追加请求信息头
        api.headers['Authorization'] = "Bearer " + token
        log.info("正在向headers添加token，添加后的headers为：{}".format(api.headers))

    @classmethod
    def common_assert(cls, response, statues_code=201):
        # 断言状态码
        #assert statues_code == response.statues_code
        # # 断言响应信息
        log.info("正在调用公共断言方法。。。。。。")
        assert "OK" == response.json().get("message")
