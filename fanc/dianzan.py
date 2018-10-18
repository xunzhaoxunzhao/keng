# coding=gbk
import requests
import pymysql as pq
from fance.log.longger import *

# dengru='http://testa.fensixingqiu.com/v1.2/auth/login/register'
huoqu='http://testa.fensixingqiu.com/v1.2/auth/login/mobile'
jr='http://testa.fensixingqiu.com/v1.0/groups/3181299825/join'
dz='http://testa.fensixingqiu.com/v1.2/groups/3181299825/topics/9353765425/set_like'
a=0
for i in range(13546881123,18895703642):
    a=a+1
    if a==400:
        break
    else:
        data={
            'mobile':i,
            'passwd':'123456',
            'ul_type':'4'
        }
        re=requests.post(url=huoqu,data=data)
        resl=re.json()
        token=resl['info']['token']
        hea={
            'token':token
        }
        headers = {
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
            'token': token,
            'Content-Length': '57',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body={
            'supportcache':'false'
        }
        rens=requests.post(url=jr,data=body,headers=headers)
        re2=rens.json()
        print(re2)
        re1=requests.put(url=dz,data=body,headers=headers)
        result1=re1.json()
        print(result1)

# def lianjiesql(sql):
#     config = {
#         'host': '193.112.125.61',
#         'port': 3307,
#         'user': 'root',
#         'password': '123456',
#         'database': 'fsxq_pub',
#         'charset': 'utf8'
#     }
#     Log('数据库参数配置%s' % config)
#     cnn = pq.connect(**config)
#     Log('已连接数据库')
#     cursor = cnn.cursor()
#     Log('获取游标')
#     cursor.execute(sql)
#     Log('执行sql语句')
#     results = cursor.fetchall()
#    # Log('结果:%s' % results)
#    #  for reult in results:
#    #       pass
#     cursor.close()
#     cnn.close()
#     Log('关闭数据库')
#     return results
#
# sql ='select distinct user_id from nf_user where user_name like"用户1%";'
# shuju=lianjiesql(sql)
# # print(shuju)
# dengur='http://dev.fensixingqiu.com/v1.0/users/login_test'
# for i in shuju:
#     reult=i[0]
#     # print(reult)
#     data={
#         'user_id':reult,
#         'ul_type':'1'
#     }
#     re=requests.get(url=dengur,params=data)
#     res=re.text
# print(res)