#!/usr/bin/env python3
#
# A log web service for the 'news' database.

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    """Main news log page."""

    # Set homePage file variable
    homePage = open('index.html', 'r')

    # Store homePage file data in data
    data = homePage.read()

    html = data % 'logs'
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
