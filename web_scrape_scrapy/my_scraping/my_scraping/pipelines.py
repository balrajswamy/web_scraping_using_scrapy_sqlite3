# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3 as sql



class MyScrapingPipeline:
    def __init__(self):
        self.create_conn() # calling the create_conn method without self argument
        self.create_table() # calling the create_table method without self argument

    def create_conn(self):

        self.conn = sql.connect("my_scraping_database.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        try:
            self.cursor.execute(
                """
                create table if not exists mydata_tb
                (id integer primary key, book_title text, book_price float)
                """)
            self.conn.commit()

        except:
            pass


    '''
    def insert_record(self, title, price):
        self.cursor.execute("""insert into mydata_tb(book_title,book_price) values (?,?)""", (title, price))
        self.conn.commit()
    '''

    def store_db(self,item):
        item["book_price"] = float(item["book_price"][1:])
        self.cursor.execute("""insert into mydata_tb(book_title,book_price) values (?,?)""", (item["book_title"], item["book_price"]))
        self.conn.commit()

    def process_item(self, item, spider):
        #book_title = item["book_title"]
        #book_price = item["book_price"]

        self.store_db(item) # calling the store_db method without self argument
        return item
