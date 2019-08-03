
from com.eurekamw_mg.model import JSONCostants as JSC

class User:
    def __init__(self, loginid, username, password):
        self.loginid = loginid
        self.username = username
        self.password = password

    def get_dict(self):
        data={}
        data[JSC.ID]=self.loginid
        data[JSC.LOGINID]=self.loginid
        data[JSC.USERNAME] = self.username
        data[JSC.PASSWORD] = self.password
        return data