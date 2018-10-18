import requests
from fance.fangfa.HS import *
import unittest
class DZ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        sql = 'select distinct user_id from nf_user where user_name like"用户1%";'
        shujus=fangf.lianjiesql(sql)
        for i in shujus:
            params={
                'user_id':i,
                'ul_type':'1'
            }
            url='http://dev.fensixingqiu.com/v1.0/users/login_test'
            re=requests.get(url,params=params)
            result=re.json()
            print(result)
            token=result['']['']