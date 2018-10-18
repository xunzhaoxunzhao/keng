# import xlrd
# import os
# from fance.fangfa.HS import *
# os.chdir(r'C:\Users\yz\Desktop')
# workbook=xlrd.open_workbook('fance.xls')
# sheet_name=workbook.sheet_by_index(0)
# nrow=sheet_name.nrows
# token=fangf().read_token()
# for i in range(1,nrow):
#     kws={
#     'mingche':sheet_name.cell_value(i,0),
#     'url':sheet_name.cell_value(i,1),
#     'type':sheet_name.cell_value(i,2),
#     'body':eval(sheet_name.cell_value(i,3)),
#     'header':eval(sheet_name.cell_value(i,4))
#     }
# print(kws)
#
# import requests
#
#
# host='http://testa.fensixingqiu.com'
# url=host+'/v1.2/groups/3181308025/topics'
# data={
#     'limit':'10',
#     'scope':'all'
# }
# header={
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'br, gzip, deflate',
#     'Accept-Language': 'zh-tw',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN',
#     'token':'f4ea75d5d5238e9a3093d7ef15d502c9'
#
# }
#
# re=requests.get(url,params=data,headers=header)
# result=re.json()
# print(result)
import requests
jr='http://testa.fensixingqiu.com/v1.0/groups/3181308125/join'
huoqu='http://testa.fensixingqiu.com/v1.2/auth/login/mobile'
data={
            'mobile':'13546881123',
            'passwd':'123456789',
            'ul_type':'4'
        }
re=requests.post(url=huoqu,data=data)
resl=re.json()
token=resl['info']['token']
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
rens = requests.put(url=jr, data=body, headers=headers)
re2 = rens.json()
print(re2)