#coding:utf-8
import requests,json,traceback
from common.logger import *

class HTTP:

    def __init__(self,writer):
        self.session=requests.session()
        self.results=''
        self.jsonres={}
        #定义关联参数字典
        self.parameter={}
        self.url=''
        self.writer=writer

    def seturl(self,u):
        """
        设置请求的urlhost信息
        :param u:
        :return: 无
        """
        if u.startswith('http') or u.startswith('https'):
            self.url=u
            self.writer.write(self.writer.row,7,'PASS')

        else:
            logger.error('url格式错误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'error:url格式错误')

    #post接口方法（url，参数（data，json），编码方式）
    def post(self,url,d=None,j=None):
        """

        :param url: 接口地址
        :param d: 字典格式字符串
        :param j: json格式字符串
        :param en:
        :return:无
        """
        #如果传入的d的值是一个字典格式的字符串，则把他转化为json格式
        if  not(url.startswith('http') or url.startswith('https')):
            self.url=self.url+'/'+url


        if d==None or d=='':
            pass
        else:
            d=self.__get_param(d)
            d=self.__get_data(d)


        res=self.session.post(self.url,d,j)
        self.results=res.content.decode('utf8')

        try:
            self.jsonres=json.loads(self.results)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
        except Exception as e:
            self.jsonres={}
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.results))
            logger.info(str(self.results))
            logger.exception(e)

    #添加头
    def addheader(self,key,value):
        """
        添加头
        :param key: 键
        :param value: 值
        :return: 无
        """
        value =self.__get_param(value)
        self.session.headers[key]=value
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.session.headers))

    #从头里面删除一个键值对

    def removeheader(self,key):
        """
        在header中删除一个值
        :param key:
        :return: 无
        """
        try:
            self.session.headers.pop[key]
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
        except Exception as e:
            logger.error('不存在'+key+'这个键')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))

    #断言
    def assertequals(self,key,value):
        """
        断言
        :param key: 实际结果的key值
        :param value: 预期结果
        :return:
        """
        res=str(self.results)
        try:
            res = str(self.jsonres[key])

        except Exception as e:

            pass

        if res==str(value):
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres[key]))
        else:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.results))
            logger.info(str(self.results))

    #把需要关联的参数保存在parameter字典中
    def insertpar(self,key1,key2):
        try:
            self.parameter[key1]=self.jsonres[key2]
            logger.info(self.jsonres)
        except Exception as e:
            logger.warn('保存参数失败，jsonres中没有'+key2+'这个键')



    #按规则获取关联的参数
    def __get_param(self,s):
        #遍历已经保存的参数，并将传入字符串里面，满足{key}所有的字符串用key的值来替换
        for key in self.parameter:
            s= s.replace('{'+key+'}',self.parameter[key])

        return s

    #获取把传入的data转化为正确的字典格式
    def __get_data(self,s):
        #传入的就是一个字典格式的字符串
        try:
            s=eval(s)
        except Exception as e:

            logger.warn('参数格式为非可转字典的字符串格式')
            print(traceback.format_exc())
            s={}
        return s

        #传入的是url参数格式：username=chf&password=123456
        # par={}
        # s=s.split('&')
        # for p in s:
        #     pp=p.split('=')
        #     par[pp[0]]=pp[1]
        # return par

    # #获取关联参数字典中对应的data，将其转化为字典格式的字符串
    # def get_dumppar(self,key):
    #     p={}
    #     try:
    #         p[key]=self.parameter[key]
    #     except Exception as  e:
    #         print("warning:"+str(e))
    #         print(traceback.format_exc())
    #         p[key]=''
    #     s = json.dumps(p)
    #     return s



