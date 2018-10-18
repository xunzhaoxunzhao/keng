import requests
url='https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx4459a4f9da3f73cc&redirect_uri=https://w.fensixingqiu.com/dist/checkLogin?query=%257B%2522froms%2522%253A%2522%252Fdist%252Findex%252Findex%2522,%2522server%2522%253A%2522testw%2522,%2522protocol%2522%253A%2522http%2522%257D&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1&uin=Mjc5ODAxNzkwOQ%3D%3D&key=f7f328af0c621374544b7a3a9cc5103d0914f922e25c646479ff78bfefda7edf2a66bb970f7d20e6c40d0c94dcbb807d&pass_ticket=XhUNWz3QDNW7JxuEkU2N9rtqe/NeFg3HLvWkFWFdwwG87G3JLQ38wei6U1eNxGPcQqM7xzx9oNI4kLwb08XExA=='
re=requests.get(url,verify=False)
res=re.text
print(res)
