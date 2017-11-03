# Log_Analysis
My solution to a Udacity assignment to demonstrate my knowledge of Python DB-API and SQL.

## Table of Contents
1. [Implementation](#implementation)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Quick Start Guide](#quick_start_guide)
2. [Contributing](#contributing)

## Implementation

### Dependencies

####  PostgreSQL
Log_Analysis was built for usage with a PostgreSQL database.

##### The News Database
Download the file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it.

##### SQL Views
###### article_views
```
create view article_views as select t2.author, t2.title, count(t1.path) as views
from log t1, articles t2
where t1.path like '%' || t2.slug
group by t1.path, t2.author, t2.title;
```

###### request_stat
```
create view request_stat as select to_char(time, 'Mon dd, yyyy') as log_date, status, count(status) as status_cnt
from log
group by log_date, status;
```

#### Python
Log_Analysis was built using Python 3. Notice it may not work on older versions of Python.

### Installation
* Download and install PostgreSQL for your operating system <a>https://www.postgresql.org/download/</a>
* Install Python3 per the instructions provided <a>https://wiki.python.org/moin/BeginnersGuide/Download</a>
* Clone the repository

### Quick Start Guide
* Open terminal
* Execute the command `psql -d news -f newsdata.sql`
* Connect to database with `psql -d news`
* Execute the article_views and request_stat statements
* Exit the database with `\q`
* `cd` to the (cloned repository)/src directory
* Execute `python3 news.py`

## Contributing
Open an issue first to discuss potential changes/additions.
