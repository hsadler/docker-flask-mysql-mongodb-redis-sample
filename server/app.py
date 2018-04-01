
import time

from flask import Flask
import MySQLdb as mdb
from pymongo import MongoClient
import redis


# flask instance
app = Flask(__name__)


# METHODS

def get_mysql_data():
    # mysql instance and settings
    mysql_con = mdb.connect(
        host='mysql',
        user='root',
        passwd='example',
        db='test'
    )
    mysql_con.set_character_set('utf8')
    mysql_cur = mysql_con.cursor(mdb.cursors.DictCursor)
    mysql_cur.execute('SET NAMES utf8;')
    mysql_cur.execute('SET CHARACTER SET utf8;')
    mysql_cur.execute('SET character_set_connection=utf8;')
    with mysql_con:
        # create table if doesn't exist
        mysql_cur.execute("""
            CREATE TABLE IF NOT EXISTS
            test_table(
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL
            );
        """)
        # insert new record
        mysql_cur.execute("""
            INSERT INTO test_table
            VALUES ();
        """)
        # get all records
        mysql_cur.execute("""
            SELECT *
            FROM test_table
            ORDER BY id DESC
        """)
        rows = mysql_cur.fetchall()
        return rows

def get_mongo_data():
    # mongo instance
    mongo_client = MongoClient(
        host='mongo',
        port=27017
    )
    db = mongo_client.test_db
    collection = db.test_collection
    # insert new record
    collection.insert_one({'text': 'i\'m new!'})
    # get all records
    records = []
    for record in collection.find():
        records.append(record)
    return records

def get_hit_cache_count():
    cache = redis.Redis(
        host='redis',
        port=6379
    )
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


# ROUTES

@app.route('/get-mysql')
def get_mysql():
    mysql_data = get_mysql_data()
    return 'Insertion complete.. Here\'s the mysql datas:\n{}' \
        .format(str(mysql_data))

@app.route('/get-mongo')
def get_mongo():
    mongo_data = get_mongo_data()
    return 'Insertion complete.. Here\'s the mongo datas:\n{}' \
        .format(str(mongo_data))

@app.route('/get-redis')
def get_redis():
    count = get_hit_cache_count()
    return 'Hello World! I have been seen {} times.\n'.format(str(count))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

