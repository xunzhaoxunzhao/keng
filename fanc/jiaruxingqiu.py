# coding=gbk
from fance.fangfa.HS import fangf
import requests
huoqu='http://testa.fensixingqiu.com/v1.2/auth/login/mobile'
jrxq='http://testa.fensixingqiu.com/v1.2/groups/3181519125/examine'
buyanzheng='http://testa.fensixingqiu.com/v1.2/groups/3181518125/join'
sql = 'select distinct user_mobile from nf_user where user_name like"用户96%";'
zhanghao=fangf().oldlianjiesql(sql)
print(zhanghao)
a=0
for i in zhanghao:
    shouji=i[0]
    data={
        'mobile':shouji,
        'passwd':'123456',
        'ul_type':'4',
    }
    re=requests.post(url=huoqu,data=data)
    resl = re.json()
    print(resl)
    token = resl['info']['token']
    header={
        'token':token,
    }
    '''需要验证'''
    data2={
         'answer':'通过',
     }
    re2=requests.post(jrxq,json=data2,headers=header)
    rs=re2.json()
    print(rs)
    # '''邀请'''
    # # data2 = {
    # #     'inviter_id': '9533946325',
    # # }
    # re2 = requests.post(buyanzheng, headers=header)
    # rs = re2.json()
    # print(rs)
    a=a+1
    if a==160:
        break
    print(a)