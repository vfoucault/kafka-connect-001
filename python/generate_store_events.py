#!/usr/bin/env python
from datetime import timedelta, datetime

import sys
from faker import Faker
from random import choice, random
from random import randint
import mysql.connector
import time

class VideoStoreGenerator(object):

    def __init__(self, dbconfig,):
        self.dbconfig = dbconfig
        self.cnx = mysql.connector.connect(**dbconfig)
        self.random_event_types = ['generate_customers'] + ['generate_videos'] * 2 + ['generate_rental'] * 10
        self.event_types = ['customers'] + ['videos'] + ['rentals']
        self.video_cat = ['romantic', 'scifi', 'action', 'kidz']
        self.faker = Faker()
        self.sql_statments = {"add_customer": ("INSERT INTO customers "
                                               "(firstname, lastname, address, zipcode, city) "
                                               "VALUES (%s, %s, %s, %s, %s)"),
                              "add_video": ("INSERT INTO videos "
                                            "(name, year, genre, synopsis) "
                                            "VALUES (%s, %s, %s, %s)"),
                              "add_rental": ("INSERT INTO rentals "
                                             "(id_video, id_customer, start, stop) "
                                             "VALUES (%s, %s, %s, %s)"),
                              "truncate": ("TRUNCATE TABLE %s")
                              }

    def get_cursor(self):
       return self.cnx.cursor()

    def commit(self):
        self.cnx.commit()

    def close_cursor(self, cursor):
        cursor.close()

    def generate_random(self):
        cursor = self.get_cursor()
        evt_type = choice(self.random_event_types)
        func = getattr(self,evt_type)
        print "Generating {}".format(func.__name__)
        func()

    def generate_customers(self):
        cursor = self.get_cursor()
        data = (self.faker.first_name(), self.faker.last_name(), self.faker.street_address(), self.faker.zipcode(), self.faker.city())
        cursor.execute(self.sql_statments['add_customer'], data)
        self.commit()
        self.close_cursor(cursor)

    def generate_videos(self):
        cursor = self.get_cursor()
        data = (self.faker.bs(), self.faker.year(), choice(self.video_cat), self.faker.text(max_nb_chars=1000, ext_word_list=None))
        cursor.execute(self.sql_statments['add_video'], data)
        self.commit()
        self.close_cursor(cursor)

    def get_random_customer_id(self):
        query = ("SELECT id FROM customers "
                 "ORDER BY RAND() LIMIT 1")
        cursor = self.get_cursor()
        cursor.execute(query)
        id = [x for x in cursor][0]
        self.close_cursor(cursor)
        return id[0]

    def truncate_db(self):
        cursor = self.get_cursor()
        for evt in self.event_types:
            query = self.sql_statments['truncate'] % evt
            cursor.execute(query)
            self.cnx.commit()
        self.close_cursor(cursor)


    def get_random_video_id(self):
        query = ("SELECT id FROM videos "
                 "ORDER BY RAND() LIMIT 1")
        cursor = self.get_cursor()
        cursor.execute(query)
        id = [x for x in cursor][0]
        self.close_cursor(cursor)
        return id[0]

    def generate_rental(self):
        customer_id = self.get_random_customer_id()
        video_id = self.get_random_video_id()
        cursor = self.get_cursor()
        days = choice(range(0,1460))
        start = self.faker.past_datetime(start_date="-{}d".format(days), tzinfo=None)
        stop = None
        if start < datetime.now() - timedelta(days=10):
            stop = self.faker.date_time_between_dates(datetime_start=start, datetime_end=start+timedelta(days=10), tzinfo=None)
        data = (video_id, customer_id, start, stop)
        cursor.execute(self.sql_statments['add_rental'], data)
        self.commit()
        self.close_cursor(cursor)

def main():
    dbconfig = {
        'user': 'root',
        'password': 'abcd1234',
        'host': '127.0.0.1',
        'database': 'demodb_1',
        'raise_on_warnings': True,
    }
    video_shop = VideoStoreGenerator(dbconfig)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'base':
            print "genrating base customers...(2000)"
            for x in range(0, 2000):
                video_shop.generate_customers()
            print "generating base videos...(4000)"
            for x in range(0, 4000):
                video_shop.generate_videos()
            print "generating base rentals...(1000)"
            for x in range(0, 1000):
                video_shop.generate_rental()
        elif sys.argv[1] == 'truncate':
            video_shop.truncate_db()
    else:
        while True:
            video_shop.generate_random()
            n = random()
            print "Sleeping for {}".format(n)
            time.sleep(n)


if __name__ == '__main__':
    main()
