# Data acces layer for the "news" database

import datetime
import psycopg2

DBNAME = "news"


def get_top_three_articles():
    """Return most popular articles of all times in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select t2.title, count(t1.path) as view_cnt \
               from log t1, articles t2 \
               where t1.path like '%' || t2.slug \
               group by t1.path, t2.title \
               order by view_cnt desc \
               limit 3")

    return c.fetchall()
    db.close()


def get_most_pop_author():
    """Return most popular author of all times in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select t1.name, count(*) view_cnt \
               from authors t1, articles t2, log t3 \
               where t1.id = t2.author \
               and t3.path like '%' || t2.slug \
               group by t1.name \
               order by view_cnt desc")

    return c.fetchall()
    db.close()


def get_request_error_log():
    """Return a list of all days where more than '1%' of requests lead to
       errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select 2 + 4, 3 + 5")

    return c.fetchall()
    db.close()
