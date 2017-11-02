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

    cursor = cnx.cursor()
    for table in ['videos', 'rentals', 'customers']:
        query = ("TRUNCATE TABLE {}".format(table))
        print "Removing {}".format(table)
        cursor.execute(query)
    cnx.commit()
    cnx.close()
    print "Done."

if __name__ == '__main__':
    main()
