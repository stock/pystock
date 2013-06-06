#! /bin/python
# coding="utf-8"

import urllib
f=urllib.urlopen("http://hq.stock.sohu.com/viewMyStockListq?cn_000028,cn_600609")
buf=f.read()
f.close()
stocklist=eval(buf[buf.index(',[')+1:buf.index('])')])
##         0        1       2       3     4     5    6      7       8       9     10     11     12      13   
##int u"股票代码 股票名称 当前价 涨跌幅 涨跌额 总手 现手 成交金额 换手率 最高价 最低价 市盈率 昨收盘 今开盘"
print u"\n股票代码\t股票名称\t当前价\t涨跌幅\t换手率"
print  "------------------------------------------------------"
for stock in stocklist:
    print stock[0],'\t',stock[1].decode('gbk').encode('utf8'),'\t',stock[2],'\t',stock[3],'\t',stock[8]

print
    
