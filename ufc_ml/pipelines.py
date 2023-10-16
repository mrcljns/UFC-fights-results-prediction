# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3
from .items import UfcMlItem


class UfcMlPipeline:
    def __init__(self):
            self.con = sqlite3.connect('ufc.db')
            self.cur = self.con.cursor()
            self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS fights(
            event TEXT,
            winner TEXT,
            loser TEXT,
            UNIQUE(event, winner, loser)
        )""")
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS fighters(
            name TEXT NOT NULL,
            height TEXT,
            weight TEXT,
            reach TEXT,
            birth_date TEXT,
            PRIMARY KEY(name)
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        if isinstance(item, UfcMlItem):
            self.cur.execute("""INSERT OR IGNORE INTO fights VALUES (?, ?, ?)""", 
            (item['event'], item['winner'], item['loser']))
        else:
            self.cur.execute("""INSERT OR IGNORE INTO fighters VALUES (?, ?, ?, ?, ?)""", 
            (item['name'], item['height'], item['weight'], item['reach'], item['birth_date']))
        self.con.commit()

