import requests
zc='http://testa.fensixingqiu.com/v1.2/auth/login/register'
a=0
for i in range(13547881123,18895703642):
    a=a+1
    if a==700:
        break
    else:
        data={
            'mobile':i,
            'passwd':'123456',
            'ul_type':'4'
        }
        re=requests.post(url=zc,data=data)
        result=re.json()
        print(result)