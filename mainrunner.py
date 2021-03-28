# coding：utf8
from common.Excel import *
from inter.interface import HTTP
import inspect,time
from web.Web import Browser

"""
    自动化框架主代码运行入口
    powered by chf
    at：2019/09/08

"""


def runcase(line,f):
    #接口测试用例列表中，如果第一列或者第二列有值，那么则line[3]列为空，所以可以短路

    if len(line[0])>0 or len(line[1])>0:

        return
    #反向映射
    func=getattr(f,line[3])

    #获取func的所有参数详情字符串
    args=inspect.getfullargspec(func).__str__()
    #截断获得参数
    args=args[args.find('args=')+5:args.rfind(', varargs=Non')]
    #字符串转换为列表
    args=eval(args)
    args.remove('self')
    #跟进参数数量调用相应关键字函数
    if len(args)==0:
        func()
        return
    if len(args)==1:
        func(line[4])
        return
    if len(args)==2:
        func(line[4],line[5])
        return
    if len(args)==3:
        func(line[4],line[5],line[6])
        return


reader = Reader()
casename="电商测试用例"
reader.open_excel('./conf/lib/'+ casename + '.xls' )
sheetname=reader.get_sheets()
writer = Writer()
writer.copy_open('./conf/lib/'+ casename+'.xls', './results/'+'result_'+casename+'.xls')

casetype=reader.readline()[1]
if casetype=='web':
    http=Browser(writer)
elif casetype=='HTTP':
    http=HTTP(writer)



#用for循环切换每一个sheetname中的sheet
for sheet in sheetname:
    reader.set_sheet(sheet)
    #保持读写在一个sheet页
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        writer.row=i
        line=reader.readline()
        print(line)
        runcase(line,http)
writer.save_close()

# reader.set_sheet('授权接口')
# writer.set_sheet('授权接口')
# writer.row=5
# for i in range(3,6):
#     reader.r=i
#     line=reader.readline()
#     runcase(line, http)
# writer.save_close()

