#! /usr/bin/python
# coding="utf-8"

import urllib
f=urllib.urlopen("http://hq.stock.sohu.com/viewMyStockListq?cn_000028,cn_600609")
buf=f.read()
f.close()
stocklist=eval(buf[buf.index(',[')+1:buf.index('])')])
print u"股票代码 股票名称 当前价 涨跌幅 涨跌额 总手 现手 成交金额 换手率 最高价 最低价 市盈率 昨收盘 今开盘"
for stock in stocklist:
    for stockitem in stock:
        print stockitem,
    print
    
print stocklist[0][2]+chr(9),13.05,chr(9),float(stocklist[0][2])/13.05
print stocklist[1][2]+chr(9),3.94,chr(9),float(stocklist[1][2])/3.94
print 600,'==>',int(600*float(stocklist[0][2])/float(stocklist[1][2]))
print 2000,'==>',int(2000*float(stocklist[1][2])/float(stocklist[0][2]))
