# encoding:utf8
from inter.interface import *
import inspect

# http=HTTP()
#
# http.post('http://www.testingedu.com.cn:8081/inter/HTTP/auth')
# http.assertequals('status','200')
# #将token写入到关联字典中
# http.insertpar('token','token')
#
# http.addheader('token','token')
#
# http.post('http://www.testingedu.com.cn:8081/inter/HTTP/login',"{'username':'chf1','password':'123456'}")
#
# http.assertequals('status','200')
#
# #将userid添加到关联字典中
# http.insertpar('id','userid')
# print(http.parameter)
# #
# #查询用户接口
# http.post('http://www.testingedu.com.cn:8081/inter/HTTP/getUserInfo', d=http.get_dumppar('id'))
# # #
# http.assertequals('status','200')
# #
# http.post('http://www.testingedu.com.cn:8081/inter/HTTP/logout')


#反射
# http=HTTP()
# func=getattr(http,'post')
# func('http://www.testingedu.com.cn:8081/inter/HTTP/auth')
# #获取到反射后函数的参数个数
# args=inspect.getfullargspec(func).__str__()
# print(args)
# args=args[args.find('args=')+5:args.rfind(', varargs=Non')]
# print(args)
# args=eval(args)
# args.remove('self')
# print(args)

data=['username=123456','name=123456']
p={}
for d in data:
    key=d[0:d.find('=')]
    value= d[d.find('=')+1:len(d)]
    p[key]=value
print(p)