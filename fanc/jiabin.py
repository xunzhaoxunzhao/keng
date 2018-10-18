# coding=gbk
import requests
import time
huoqu='http://testa.fensixingqiu.com/v1.2/auth/login/mobile'
huoqujiabin='http://testa.fensixingqiu.com/v1.2/groups/3181986425/invite'
jieshouyaoqing='http://testa.fensixingqiu.com/v1.2/groups/3181986425/join_with_guest'
host = 'http://testa.fensixingqiu.com'
# url=host+'/v1.0/users/app_login'
# data={
#                 'unionid': 'ofQWl1A_nOac1Wr674DT2kK51pW8',
#                 'ul_type': '1',
#                 'openid': 'o8afQ0sWMOWc7WclUhRJQyT4nttc',
#                 'nickname': '你麦哥'
#             }
#
#
# re=requests.post(url,json=data)
# result=re.json()
# token=result['info']['token']
# hea={
#             'token':token
#         }
# re1=requests.get(huoqujiabin,headers=hea)
# result1=re1.json()
# print(result1)
# id=result1['info']['guest_id']
a=0
for i in range(13546881123,18895703642):
    a=a+1
    if a==300:
        break
    else:
        url = host + '/v1.0/users/app_login'
        data = {
            'unionid': 'ofQWl1EAMCCaJdwCu2tniVU8lkAY',
            'ul_type': '1',
            'openid': 'o8afQ0tg3jz_b_VLGqRR3ZeRciMA',
            'nickname': '点点点王国'
        }

        re = requests.post(url, json=data)
        result = re.json()
        token = result['info']['token']
        hea = {
            'token': token
        }
        re1 = requests.get(huoqujiabin, headers=hea)
        result1 = re1.json()
        print(result1)
        id = result1['info']['guest_id']
        data={
            'mobile':i,
            'passwd':'123456',
            'ul_type':'4'
        }
        re=requests.post(url=huoqu,data=data)
        resl=re.json()
        print(resl)
        token=resl['info']['token']
        header={
            'token':token
        }
    datra={
        'guest_id':id
    }
    re2=requests.post(jieshouyaoqing,data=datra,headers=header)
    time.sleep(1)
    result2=re2.json()
    print(result2)