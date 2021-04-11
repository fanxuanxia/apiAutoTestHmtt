from api.api_mis import ApiMis
from tools.tool import Tools
from tools.get_log import GetLog
import pytest
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestMis:
    def setup_class(self):
        self.mis = ApiMis()

    @pytest.mark.parametrize("account, pwd",read_yaml("mis_login.yaml"))
    def test01_mis_login(self, account, pwd):
        r = self.mis.mis_login(account, pwd)
        Tools.common_token(r)
        try:
            Tools.common_assert(r)
        except Exception as e:
            log.error(e)
            raise


    def test02_mis_search_article(self):
        r = self.mis.mis_search_article()
        try:
            Tools.common_assert(r, statues_code=200)
        except Exception as e:
            log.error(e)
            raise

    def test03_mis_audit_article(self):
        r = self.mis.mis_article_audit()
        #print(r.json())
        try:
            Tools.common_assert(r)
        except Exception as e:
            log.error(e)
            raise