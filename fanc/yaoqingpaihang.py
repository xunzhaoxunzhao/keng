# coding=gbk
from fance.fangfa.HS import fangf
import requests
huoqu='http://testa.fensixingqiu.com/v1.2/auth/login/mobile'
jinruxingqiu=' http://testa.fensixingqiu.com/v1.2/groups/3181276325'
buyanzheng='http://testa.fensixingqiu.com/v1.2/groups/3181276325/join'
sql = 'select distinct user_mobile from nf_user where user_name like "用户96%";'
sql2='select distinct user_mobile from nf_user where user_name like "%962%";'
zhanghao=fangf().oldlianjiesql(sql)
a=0
id_list=[]
for i in zhanghao:

    shouji=i[0]
    data={
        'mobile':shouji,
        'passwd':'123456',
        'ul_type':'4',
    }
    re=requests.post(url=huoqu,data=data)
    resl = re.json()
    token = resl['info']['token']
    header={
        'token':token
    }
    # data2 = {
    #     'inviter_id': '9533946325',
    # }
    re2 = requests.post(buyanzheng, headers=header)
    rs = re2.json()
    print(rs)
    data3={
        'refresh':'true'
    }
    re3=requests.get(jinruxingqiu,params=data3,headers=header)
    result1=re3.json()
    userid = result1['info']['current_user']
    USERID = userid['id']
    id_list.append(USERID)
    a=a+1
    if a==44:
        zhanghao1 = fangf().oldlianjiesql(sql2)
        for i in zhanghao1:
            shouji = i[0]
            print(i)
            print(shouji)
            data = {
                'mobile': shouji,
                'passwd': '123456',
                'ul_type': '4',
            }
            re = requests.post(url=huoqu, data=data)
            resl = re.json()
            print(resl)
            token1 = resl['info']['token']
            header1 = {
                'token': token1,
            }
            for j in id_list:
                data2 = {
                     'inviter_id': j,
                 }
                print(data2)
                print(j)
                re2 = requests.post(buyanzheng, data=data2,headers=header)
                rs = re2.json()
                print(rs)