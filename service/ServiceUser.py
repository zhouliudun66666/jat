#  coding: utf-8
#  @author: zhoulidun

from common import Utils


class ServiceAUser:
    # 登录
    def login(self, user, password):
        params = {
            'loginName': user,
            'password': password,
            'udesk': False,
            'sig': '',
            'token': '',
            'scene': '',
            'sso': '',
            'return_to': ''
        }
        url = '/api/v2/inner/user/weblogin'
        return Utils.Utils().http_post_request(params, url)

    # 退出登录
    def login_out(self):
        params = {
        }
        url = '/api/v2/inner/user/logout'
        return Utils.Utils().http_post_request(params, url)

    # 用户个人信息
    def user_account(self):
        params = {
        }
        url = '/api/v2/inner/user/account'
        return Utils.Utils().http_get_request(params, url)