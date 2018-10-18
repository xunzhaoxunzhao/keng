# coding=gbk
from fance.fangfa.HS import *
sql = 'select distinct user_mobile from nf_user where user_name like"用户96%";'
zhanghao=fangf().lianjiesql(sql)
for i in zhanghao:
    zh=i[0]
    with open(r'C:\Users\yz\Desktop\yonghushuju.txt','a') as f:
        f.write(zh+','+'123456'+'\n')