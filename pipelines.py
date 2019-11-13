# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import spider_tools as t

Auto_insert_indb = True
Auto_insert_sinsert = False


class ScrapyFramePipeline(object):
    def __init__(self):
        if Auto_insert_indb:
            self.in_db = t.Auto_indb(host='192.168.4.201', username='root', password='mysql', db="storm", table_name='',
                              comment='表注释', create_tables=True)
        elif Auto_insert_sinsert:
            self.sinsert = t.Auto_sinsert(host='192.168.4.201', username='root', password='mysql', db='zhijianju',
                                   drop_column=["id", "jid", "update", "entid"])
        else:
            raise ValueError("please chose a insert way")


    def process_item(self, item, spider):
        if Auto_insert_indb:
            self.in_db.insert_data(item)
        elif Auto_insert_sinsert:
            self.sinsert.insert_data(item,table_name='')
        else:
            raise ValueError("please chose a insert way")

        return item
