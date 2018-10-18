import time

import xlrd
import os
import requests
from xlutils.copy import copy
import pymysql as pq
from fance.log.longger import Log
host = 'http://testa.fensixingqiu.com'
class fangf(object):

    def read_token(self):
        with open(r'C:\Users\yz\Desktop\token.txt','r') as e:
            token=e.read()
            Log('读取token:%s'%token)
        return token

    def read_excel(self):
        shijian = time.time()
        results = []
        msg=[]
        os.chdir(r'C:\Users\yz\Desktop')
        workbook = xlrd.open_workbook('fance.xls')
        Log('打开数据文件:%s'%workbook)
        sheet_name = workbook.sheet_by_index(0)
        Log('读取表单名:%s'%sheet_name)
        nrow = sheet_name.nrows
        Log('读取行数:%s'%nrow)
        token = fangf().read_token()
        Log('将token赋值给excel中相应的数据')
        for i in range(1, nrow):
            kws={
            'mingche' : sheet_name.cell_value(i, 0),
                'sfpj':sheet_name.cell_value(i,1),
            'url' : sheet_name.cell_value(i, 2),
               'ziduan':sheet_name.cell_value(i,3),
            'method' : sheet_name.cell_value(i, 4),
            'type':sheet_name.cell_value(i,5),
            'body' :eval(sheet_name.cell_value(i, 6)),
            'header' : eval(sheet_name.cell_value(i, 7)),
            'result':sheet_name.cell_value(i,8),
            }
            Log('读取用例名称:%s,路径:%s,请求方式:%s,请求内容 :%s,请求头:%s'%(kws['mingche'],kws['url'],kws['type'],kws['body'],kws['header']))
            Log(kws['sfpj'])
            if kws['sfpj']==0:
                url = host + kws['url']
                Log('url:%s'%url)
            else:
                url=host+kws['url']+kws['ziduan']
                Log('url:%s' % url)
            if kws['method']=='get':
                Log('请求方式为:get')
                re=requests.get(url,params=kws['body'],headers=kws['header'])
                result=re.json()
                Log('请求结果:%s'%result)
                if kws['body']==None:
                    Log('请求方式为:get')
                    re = requests.get(url, headers=kws['header'])
                    result = re.json()
                    Log('请求结果:%s' % result)

            elif kws['method']=='post':
                # Log('请求方式为:post,参数为表单形式')
                # re=requests.post(url,data=kws['body'],headers=kws['header'])
                # result=re.json()
                # Log('请求结果:%s' % result)
                if kws['type']=='body':
                    Log('请求方式为:post,参数为json')
                    re=requests.post(url,json=kws['body'],headers=kws['header'])
                    result=re.json()
                    Log('请求结果:%s' % result)
                else:
                    Log('请求方式为:post,参数为data')
                    re = requests.post(url, data=kws['body'], headers=kws['header'])
                    result = re.json()
                    Log('请求结果:%s' % result)
            elif kws['method']=='put':
                Log('请求方式为:put,参数为data')
                re=requests.put(url,data=kws['body'],headers=kws['header'])
                result = re.json()
                Log('请求结果:%s' % result)
            elif kws['method']=='delete':
                Log('请求方式为:delete')
                re = requests.delete(url,headers=kws['header'])
                result = re.json()
                Log('请求结果:%s' % result)


            if result['result']==kws['result']:
                print(type(result['result']))
                Log('预期结果为:%s'%kws['result'])
                Log('实际结果为:%s' % result['result'])
                Log('断言结果正确')
                results.append('True')
                msg.append(result['msg'])
            else:
                results.append('False')
                Log('预期结果为:%s' % kws['result'])
                Log('实际结果为:%s' % result['result'])
                Log('断言结果错误')
                msg.append(result['msg'])
                Log('写入提示信息')

            Log('共有%d个url，当前执行%d个' % ((nrow - 1), i))
        newwork = copy(workbook)
        Log('复制数据文件')
        sheet = newwork.get_sheet(0)
        Log('获取文件表单')
        Log('开始准备写入结果：....')
        for j in range(1, nrow):
            sheet.write(j, 9, results[j - 1])
            sheet.write(j, 10, msg[j - 1])

            os.remove('fance.xls')
            newwork.save('fance.xls')
       # return panduan
        Log('结果写入完毕')
    def oldlianjiesql(self,sql):
        config={
            'host':'193.112.125.61',
            'port':3307,
            'user':'root',
            'password':'123456',
            'database':'fsxq_pub',
            'charset':'utf8'
        }
        Log('数据库参数配置%s'%config)
        cnn=pq.connect(**config)
        Log('已连接数据库')
        cursor=cnn.cursor()
        Log('获取游标')
        cursor.execute(sql)
        Log('执行sql语句')
        results=cursor.fetchall()
        # for reult in results:
        #     print(reult)
        cnn.commit()
        cursor.close()
        cnn.close()
        Log('关闭数据库')
        return results
# sql = 'select distinct user_id from nf_user where user_name like"用户1%";'
# print(fangf().lianjiesql(sql))
    def newlianjiesql(self,sql):
        config={
            'host':'193.112.157.157',
            'port':3306,
            'user':'root',
            'password':'xiaoheiban123..',
            'database':'fsxq_pub',
            'charset':'utf8'
        }
        Log('数据库参数配置%s'%config)
        cnn=pq.connect(**config)
        Log('已连接数据库')
        cursor=cnn.cursor()
        Log('获取游标')
        cursor.execute(sql)
        Log('执行sql语句')
        results=cursor.fetchall()
        # for reult in results:
        #     print(reult)
        cnn.commit()
        Log('提交数据')
        cursor.close()
        cnn.close()
        Log('关闭数据库')
        return results

    def jiajiemi(self,jiami_id=None,jiemi_id=None):
        url='http://testa.fensixingqiu.com/test/get_decode_id'
        header={
            'auth':'DaFa88..'
        }
        # data={
        #     'id':jiami_id,
        #     'encodeId':jiemi_id,
        # }
        if jiami_id==None:
            data={
            'encodeId':jiemi_id,
         }
            re=requests.get(url,params=data,headers=header)
            result=re.json()
            print(result)
            __jiemi_id=result['info'][jiemi_id]
            return __jiemi_id
        else:
            data = {
                'id':jiami_id,
            }
            re = requests.get(url, params=data, headers=header)
            result = re.json()
            __jiammi_id = result['info']['%s'%jiami_id]
            return __jiammi_id
    def daoxuchaxun(self,sql):
        config={
            'host':'193.112.157.157',
            'port':3306,
            'user':'root',
            'password':'xiaoheiban123..',
            'database':'fsxq_pub',
            'charset':'utf8'
        }
        Log('数据库参数配置%s'%config)
        cnn=pq.connect(**config)
        Log('已连接数据库')
        cursor=cnn.cursor()
        Log('获取游标')
        cursor.execute(sql)
        Log('执行sql语句')
        results=cursor.fetchall()
        # for reult in results:
        #     print(reult)
        Log('提交数据')
        cursor.close()
        cnn.close()
        Log('关闭数据库')
        return results

    def write_excel(self,x,y,z):
        os.chdir(r'C:\Users\yz\Desktop')
        workbook = xlrd.open_workbook('fance.xls')
        newwork = copy(workbook)
        sheet = newwork.get_sheet(0)
        sheet.write(x, y, z)
        os.remove('fance.xls')
        newwork.save('fance.xls')
        # return panduan
        Log('结果写入完毕')