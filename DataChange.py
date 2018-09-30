# -*- coding:utf-8 -*-
import re

def DataOptimization(htmlTree):
    datalist = re.findall('"itemSpuSummary":(.*?)},{', htmlTree, re.S)
    for info in datalist:
        commentCount = int(re.search('"spuComments":(.*?),"spuSales', info).group(1))
        saleCount = int(re.search('spuSales":(.*?),"spuVisits', info).group(1))
        
    return 1