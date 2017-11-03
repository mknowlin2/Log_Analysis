#!/usr/bin/env python3
#
# A log web service for the 'news' database.

from flask import Flask
from newsdb import get_top_three_articles, get_most_pop_author

app = Flask(__name__)

# HTML template for an individual comment
LOG_TMPLT = '''\
    <div class=logs>{} — {} views</div>
'''


@app.route('/', methods=['GET'])
def main():
    """Main news log page."""

    # Set homePage file variable
    homePage = open('index.html', 'r')

    # Store homePage file data in data
    data = homePage.read()

    # Retrieve data from database
    logs = "".join(LOG_TMPLT.format(title, view_cnt) \
           for title, view_cnt in get_top_three_articles())
    logs = logs + "".join(LOG_TMPLT.format(title, view_cnt) \
           for title, view_cnt in get_most_pop_author())

    html = data % logs
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
