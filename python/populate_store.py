#!/usr/bin/env python
from faker import Faker
from random import choice
from random import randint
import mysql.connector


def main():

    config = {
        'user': 'root',
        'password': 'abcd1234',
        'host': '127.0.0.1',
        'database': 'demodb_1',
        'raise_on_warnings': True,
    }
    cnx = mysql.connector.connect(**config)

    print "Generating 2000 Customers..."
    generate_customer(2000, cnx)
    print "Generating 4000 Videos..."
    generate_videos(4000, cnx)
    print "Generating 1000 Rentals..."
    generate_rental(10000, cnx)
    cnx.close()
    print "Done."

def generate_rental(count, cnx):
    cursor = cnx.cursor()
    faker = Faker()
    add_rental = ("INSERT INTO rentals "
                  "(id_video, id_customer, start, stop) "
                  "VALUES (%s, %s, %s, %s)")
    while count > 0:
        client_id = randint(1, 2000)
        start = faker.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
        stop = choice([None, faker.date_time_this_century(before_now=False, after_now=True, tzinfo=None)])
        video_id = randint(1, 4000)
        data = (video_id, client_id, start, stop)
        cursor.execute(add_rental, data)
        cnx.commit()
        count -= 1
    cursor.close()



def generate_customer(count, cnx):
    faker = Faker()
    cursor = cnx.cursor()
    add_customer = ("INSERT INTO customers "
                    "(firstname, lastname, address, zipcode, city) "
                    "VALUES (%s, %s, %s, %s, %s)")
    while count > 0:
        data = (faker.first_name(), faker.last_name(), faker.street_address(), faker.zipcode(), faker.city())
        cursor.execute(add_customer, data)
        count -= 1
    cnx.commit()
    cursor.close()

def generate_videos(count, cnx):
    faker = Faker()
    cursor = cnx.cursor()
    add_video = ("INSERT INTO videos "
                 "(name, year, genre, synopsis) "
                 "VALUES (%s, %s, %s, %s)")

    list_genre = ['romantic', 'scifi', 'action', 'kidz']
    while count > 0:
        data = (faker.bs(), faker.year(), choice(list_genre), faker.text(max_nb_chars=1000, ext_word_list=None))
        cursor.execute(add_video, data)
        count -= 1
    cnx.commit()
    cursor.close()

if __name__ == '__main__':
    main()
