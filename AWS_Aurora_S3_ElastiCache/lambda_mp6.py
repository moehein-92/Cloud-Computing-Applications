import json
import pymysql
import redis


class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)
        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def record(self, sql, values):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchone()

    def save(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return self.mysql.commit()

    def clear(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            self.mysql.commit()

# Time to live for cached data
TTL = 10

REDIS_URL = "redis://mp6redis.867rmj.ng.0001.use1.cache.amazonaws.com:6379"

DB_HOST = "auroradb.cluster-cmvcbkjoqwgx.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "Dsy663548"
DB_NAME = "MP6DB"

Db = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
Cache = redis.Redis.from_url(REDIS_URL) 

def read(id, usecache):
    key = f'mp6table:{id}'
    res = Cache.hgetall(key)
    if (res != {}) & usecache:
        return res
    else:
        sql = "SELECT id, hero, power, name, xp, color FROM mp6table WHERE id=%s"
        res = Db.record(sql, (id,))
        if res:
            if usecache:
                Cache.hmset(key, res)
                Cache.expire(key, TTL)
            return res

def write(value, id, usecache):
    hero = value['hero']
    power = value['power']
    name = value['name']
    xp = int(value['xp'])
    color = value['color']
    sql = f"INSERT INTO mp6table (id, hero, power, name, xp, color) VALUES ({id}, '{hero}', '{power}', '{name}', {xp}, '{color}')"
    Db.save(sql)
    if usecache:
        key = f'mp6table:{id}'
        res2 = {}
        res2['id'] = id
        res2.update(value)
        Cache.hmset(key, res2)
        Cache.expire(key, TTL)

def clearDB():
    sql = "DELETE FROM mp6table WHERE id>25"
    res = Db.clear(sql)
    return res

def lambda_handler(event, context):
    clearDB()
    USE_CACHE = event['USE_CACHE']
    SQLS = event['SQLS']
    REQUEST = event['REQUEST']
    usecache = (USE_CACHE == 'True')
    result = []
    if REQUEST == 'read':
        for id in SQLS:
            result.append(read(id, usecache))
        return {
            "statusCode": 200,
            "body": result
        }
    if REQUEST == 'write':
        count = Db.query("SELECT MAX(id) AS max_id FROM mp6table")[0]["max_id"]
        for value in SQLS:
            count += 1
            write(value, count, usecache)
        return {
            "statusCode": 200,
            "body": "write success"
        }


