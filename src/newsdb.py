# Data acces layer for the "news" database

import datetime
import psycopg2

DBNAME = "news"


def get_top_three_articles():
    """Return most popular articles of all times in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select 2 + 2, 3 + 3")

    return c.fetchall()
    db.close()


def get_most_pop_author():
    """Return most popular author of all times in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select 2 + 3, 3 + 4")

    return c.fetchall()
    db.close()
