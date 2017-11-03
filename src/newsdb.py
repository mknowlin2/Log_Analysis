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

    c.execute("select log_date, to_char(percentage, '99.9') \
               from (select t1.log_date, \
                            t1.err_cnt * 100::numeric / t2.total \
                            as percentage \
                     from (select to_char(time, 'Mon dd, yyyy') as log_date, \
                                  count(status) as err_cnt \
                           from log \
                           where status like '404 NOT FOUND' \
                           group by log_date) t1, \
                          (select log_date, count(status) as total \
                           from (select to_char(time, 'Mon dd, yyyy') \
                                        as log_date, status \
                                 from log) as nt1 \
                           group by log_date) t2 \
                     where t1.log_date = t2.log_date) as temp1 \
              where percentage > 1")

    return c.fetchall()
    db.close()
