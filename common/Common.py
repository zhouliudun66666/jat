#  coding: utf-8
#  @author: zhoulidun

import re
from common import MyException

# 123456
pwdOne = 'GIsPp%2Btfp8WoMX40pkIRceEXnACxi34IU3x9RkZZjnOdBHHr0hRREdZvQXMgpXrQ%2F' \
         'CQf8nOTEgC98sgeMRAFK%2Fvq9fCy1cMboC1%2FpLbmISYAtV6%2FG%2FPsviJ3oW5mQ9' \
         '73eUqHZ%2B%2ByTIQZT%2FiFzWR7w0DBBHz%2BAicglyL2e5NcGYwfB3mHsTWtq3%2F8Z' \
         'PcVmWRHDXFULN6lczFjGsRzt%2BwcrwGU2E6ZO6fs%2F3LhagUKRNWs7Tt0HS0KQRJ9M77' \
         '4dHJ7xEhnp0N9D7PZyRtbuJN1SYpbuzcngmGYWygkIhxGfzn61TMZkC5bk5o9GM32oV4v' \
         '2WZLNNCegC1Yz7yxEiDJPQ%3D%3D'

# 18349192602
phone = '18349192602'


# 未匹配
def search_str(response, regex_list):
    try:
        for i in regex_list:
            re_com = re.compile(i)
            search_str = re_com.search(response)
            if search_str is None:
                raise MyException.NotMatchException("未匹配到预期结果")
                return False
    except Exception as e:
        print("Failed, response is : %s,%s" % (response, e))
        raise e
