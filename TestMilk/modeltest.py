# -*- coding:utf-8 -*-

import requests
import lxml
import arrow
import re

from re import S
from openpyxl import load_workbook


class dataOpfunction():
	'''
	数据获取
	数据处理
	数据存储
	'''
	def __init__(self):
		pass

	def getData(self):
		data = requests.get(self.url, headers = header)
		resultHtml = data.text
		self.data = resultHtml


	def DataOptimization(self):
		htmlTree = self.data
		itemId = 0
		datalist = re.findall('"itemSpuSummary":(.*?)},{', htmlTree, re.S)
		for info in datalist:
			resultList = []
			resultList.append(re.search('name":"(.*?)","remark', info).group(1))
			resultList.append(re.search('"secondName":"(.*?)","shop', info).group(1))
			resultList.append(int(round(float(re.search('spuSales":(.*?),"spuVisits', info).group(1)), 0)))
			resultList.append(int(re.search('"spuComments":(.*?),"spuSales', info).group(1)))
			resultList.append(re.search('"company":"(.*?)","contactCell', info).group(1))
			resultList.append(re.search('contactName":"(.*?)","id":', info).group(1))
			resultList.append(re.search('"contactCell":"(.*?)","contactName', info).group(1))
			self.Dic[itemId] = resultList
			itemId += 1


class getHtmltree(dataOpfunction):
	'''
	初始化请求对象
	继承父类所有处理方法。
	'''
	def __init__(self, url, header):
		self.url = url
		self.herders = header
		self.dic = {}



if __name__ == '__main__':

	url = "http://items.aiyangniu.cn/items/list?sortType=ITEM_SALES_DOWN&offset=0&limit=10"

	header = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
	}

	fileName = 'dataExcel.xlsx'
    saveName = 'dataExcel/newExcel/dataExcel.xlsx'

	mainObject = getHtmltree(url, header)
	mainObject.getData()
	mainObject.printData()
	