#  coding: utf-8
#  @author: zhoulidun

import unittest
import time
from service import ServiceUser
from common import Common, ComMeth


class TestCaseAUser(unittest.TestCase):
    SUCCESS_RESULT = "'code': 0"

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    # 使用手机登录
    def test1_login_by_phone(self):
        '''使用手机登录'''
        try:
            print('test_login_by_phone')
            response = ComMeth.ComMeth().login()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    # 测试退出登录
    def test3_loginout(self):
        '''退出登录'''
        try:
            print('test_loginout')
            response = ServiceUser.ServiceAUser().login_out()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    # 用户个人信息
    def test2_user_info(self):   
        '''用户个人信息'''
        print('user_info')
        try:
            response = ServiceUser.ServiceAUser().user_account()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex
