# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
from toscrape_book.settings import MYSQL_DB_NAME as mysql_name
from toscrape_book.settings import MYSQL_HOST as mysql_host
from toscrape_book.settings import MYSQL_PORT as mysql_port
from toscrape_book.settings import MYSQL_USER as mysql_user
from toscrape_book.settings import MYSQL_PASSWORD as mysql_password

class MySQLAsyncPipeline(object):
    def open_spider(self, spider):
        #同步操作数据库
        #self.db_conn = MySQLdb.connect(host=mysql_host,port=mysql_port,db=mysql_name,user=mysql_user,passwd=mysql_password,charset='utf8')
        #self.db_cur = self.db_conn.cursor()

        #异步操作数据库
        self.dbpool = adbapi.ConnectionPool('MySQLdb',host=mysql_host,port=mysql_port,db=mysql_name,user=mysql_user,passwd=mysql_password,charset='utf8')


    def close_spider(self, spider):
        # self.db_conn.commit()
        # self.db_conn.close()
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db,item)
        return item

    def insert_db(self, tx, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )

        sql = 'INSERT INTO books VALUES(%s,%s,%s,%s,%s,%s)'
        tx.execute(sql,values)
