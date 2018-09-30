# -*- coding:utf-8 -*-
import re

import arrow
import requests
from lxml import etree

from DataChange import DataOptimization


TargetUrldic = {
    'alldata':
    'http://items.aiyangniu.cn/items/list?sortType=ITEM_SALES_DOWN&offset=0&limit=1000',
    'fuleiTest':
    'http://http://www.aiyangniu.cn/dist/views/index/index.html#/search?searchMode=1'
}


headerdic = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def GetAllData():
    GetCommend = requests.session()
    htmlTree = GetCommend.get(TargetUrldic['alldata'], headers=headerdic).text
    opResult = DataOptimization(htmlTree)
    return opResult


def Spmain():
    data = GetAllData()
