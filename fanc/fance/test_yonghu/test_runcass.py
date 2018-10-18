import unittest
import requests
from fance.fangfa.HS import *
host = 'http://testa.fensixingqiu.com'
import time
class fc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url=host+'/v1.0/users/app_login'
        Log('登录中..')
        data = {
            'unionid': 'ofQWl1A_nOac1Wr674DT2kK51pW8',
            'ul_type': '1',
            'openid': 'o8afQ0sWMOWc7WclUhRJQyT4nttc',
            'nickname': '点点点'
        }
        Log('参数是%s'%data)
        re=requests.post(url,json=data)
        Log('已进行请求等待相应')
        result=re.json()
        Log('等待json解析')
        token=result['info']['token']
        Log('获取token%s'%token)
        with open(r'C:\Users\yz\Desktop\token.txt', 'w') as e:
            e.write(token)
            Log('写入token')
    @classmethod
    def tearDownClass(cls):
        pass
    @unittest.skip(u'1')
    def test_zhuti(self):

        for i in range(200):
            url = host + '/v1.2/groups/3181346525/topics'
            token = fangf.read_token(self)
            headers = {
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
            'token': token,
            'Content-Length': '57',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
            data = {
                'topic_text': '123456新的数据，只是看星球外面有显示数据不%s'%time.time(),
            }
            re = requests.post(url, json=data, headers=headers)
            result = re.json()
        print(result)

    def test_start(self):
        sql="select comment_id from nf_topic_comment where user_id='4549' and topic_id='15121';"
        start=fangf()
        result=start.daoxuchaxun(sql)
        sql2="select hashtag_id from nf_hashtag_default where group_id='256' and user_id='4549';"
        huati_ids=start.daoxuchaxun(sql2)
        for i in result:
            id=i[0]
        jiami_id=fangf().jiajiemi(id)
        start.write_excel(17,3,jiami_id)
        for i in huati_ids:
            huati_id=i[0]
        jiami_huati=start.jiajiemi(huati_id)
        start.write_excel(32,3,jiami_huati)
        start.read_excel()
if __name__=='__main__':
    unittest.main()