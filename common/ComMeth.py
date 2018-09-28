#  coding: utf-8
#  @author: zhoulidun

import unittest
from service import ServiceUser
from common import Utils
from common import Common


class ComMeth(unittest.TestCase):

    SUCCESS_RESULT = "'code': 0"

    # 登录
    def login(self):
        try:
            response = ServiceUser.ServiceAUser().login(Common.phone, Common.pwdOne)
            token = response['data']['token']
            Utils.Utils.headers['headerToken'] = token
            print(token)
            return response
        except Exception as ex:
            raise ex
