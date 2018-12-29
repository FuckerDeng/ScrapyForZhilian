# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import zhilian.settings
import pymysql
import logging
from zhilian.sqlError import SaveLog

class ZhiLianPipeline(object):
	def __init__(self):
		self.MYSQL = zhilian.settings.MYSQL
		self.con = pymysql.connect(
			host = self.MYSQL["MYSQL_HOST"],
			db = self.MYSQL["MYSQL_DBNAME"],
			user = self.MYSQL["MYSQL_USER"],
			passwd = self.MYSQL["MYSQL_PASSWD"],
			charset='utf8',
			use_unicode=True
		)
		#self.logFile = SaveLog()
		self.cursor = self.con.cursor()

	def close_spider(self,spider):
		print("数据库连接被关闭！")
		self.con.close()
		SaveLog.closeFile()

	def process_item(self, item, spider):

		try:
			#print("开始插入数据")
			self.cursor.execute(
				'insert into zhilian (number,jobname,company,position,size,edulevel,salary,workexp,workcontent) values("%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(item["number"],item["jobname"],item["company"],item["position"],item["size"],item["edulevel"],item["salary"],item["workexp"],item["workcontent"])
				)
			self.con.commit()
			#print("数据插入成功")
		except Exception as e:
			self.con.rollback()
			SaveLog.saveLog(repr(e))
			print(e)
		return item
