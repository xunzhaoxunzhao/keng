# coding=gbk
from fance.fangfa.HS import fangf
import requests
import time
'''
1����ȡ����������Ա��id
2�����н���
3��ͨ��idȥ���ݿ��ҵ���Ӧ�����ݣ��޸�valid_time���ĳɼ��������ʱ�䣩���������ѣ�
input���Ƿ����ѣ�1�ǵģ�2���ǣ�
4��ͨ������������ҵ����ѽ��˵�ʱ�䣬��input��1.android 2.ios������Ϊ�������������ǰ����׿����iOS�ĵ�����ǰ
'''
login='http://testa.fensixingqiu.com/v1.0/users/app_login'
data = {
            'unionid': 'ofQWl1A_nOac1Wr674DT2kK51pW8',
            'ul_type': '1',
            'openid': 'o8afQ0sWMOWc7WclUhRJQyT4nttc',
            'nickname': '����'
        }

re = requests.post(url=login, json=data)

result = re.json()

token = result['info']['token']

xingqi='http://testa.fensixingqiu.com/v1.2/groups/3181285325'#����
print('����Ϊ����')
header={
    'token':token
}
data={
    'refresh':'true'
}
re1=requests.get(xingqi,params=data,headers=header)
result1=re1.json()
xingqiID=result1['info']['id']
userid=result1['info']['current_user']
USERID=userid['id']
shijian=userid['member_info']['join_time']
print('ajoin:%s'%shijian)
id_list=[xingqiID,USERID]
canshuhua=[]
jiajiemi = 'http://dev.fensixingqiu.com/test/get_decode_id'
for i in id_list:
    data1 = {
        'id': '101',
        'encodeId':i,
    }
    header = {
        'auth': 'DaFa88..'
    }
    re2=requests.get(url=jiajiemi,params=data1,headers=header)
    result2=re2.json()
    id=result2['info'][i]
    canshuhua.append(id)
xq=canshuhua[0]
auser=canshuhua[1]
sql="update nf_group_user set valid_time='%s' where group_id='%s' and user_id='%s';"%(shijian,xq,auser)
print(sql)
s=fangf().newlianjiesql(sql)