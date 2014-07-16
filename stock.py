#! /bin/python
# coding="utf-8"

import urllib,time
from datetime import datetime
import sys
s=''
p=0
monitorid='cn_600609'
##         0        1       2       3     4     5    6      7       8       9     10     11     12      13   
##int u"股票代码 股票名称 当前价 涨跌幅 涨跌额 总手 现手 成交金额 换手率 最高价 最低价 市盈率 昨收盘 今开盘"
print u"\n股票代码\t股票名称\t当前价\t涨跌幅\t换手率"
print  "----------------------------------------------------------------------"
while True:
    f=urllib.urlopen("http://hq.stock.sohu.com/viewMyStockListq?cn_600609")
    buf=f.read()
    f.close()
    stock=eval(buf[buf.index(',[')+1:buf.index('])')])

    sys.stdout.write('\r'+stock[0]+'\t'+stock[1]+'\t'+stock[2]+'\t'+stock[3]+'\t'+stock[8]+" %d:%d:%d       " % (datetime.now().hour,datetime.now().minute,datetime.now().second))
#        if stock[0]==monitorid:
#            oldp=p
#            p=float(stock[2])
#            if oldp>p:
#                s +='_'
#            elif oldp<p:
#                s +='~'
#            else:
#                s +='-'
#            print s[-60:]
#    print
    time.sleep(20)
