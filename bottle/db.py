import mysql.connector
import hashlib
import string
import random
import time

user = 'root'
password = 'Lou0073eE8'
database = 'hctf'

def md5(strings):
    strings = strings.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(strings)
    return md5.hexdigest()

def get_random():
    strings = string.ascii_letters+string.digits
    random_str = ''.join(random.sample(list(strings),8))
    return md5(random_str)[0:4]
def connect():
    conn = mysql.connector.connect(user=user,password=password,database=database)
    if(conn):
        return conn
    else:
        return 'mysql connect failed'

def register_user(username,password):
    password = md5(password)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from users where username = %s',(username,))
    value = cursor.fetchall()
    if (value) :
        return 2
    cursor.execute('insert into users(username,password) values (%s,%s)',[username,password])
    conn.commit()
    if (cursor.rowcount):
        cursor.close()
        return 1
    else :
        cursor.close()
        return 0

def login_user(username,password):
    password = md5(password)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from users where username = %s and password = %s',[username,password])
    value = cursor.fetchall()
    cursor.close()
    if (value) :
        return value[0][0]
    else:
        return 0

def find_user(userId):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from users where id = %s',(userId,))
    value = cursor.fetchall()
    cursor.close()
    if(value):
        return value[0][1]
    else:
        return 0

def is_insert_url(userId):
    conn = connect()
    cursor = conn.cirsor()
    cursor.execute('select * from url where id = %s',(userId,))
    value = cursor.fetchall()
    if value[100]:
        return 0
    else:
        return 1
def insert_url(userId,url):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('insert into url (userId,url) values (%s,%s)',[userId,url])
    conn.commit()
    if (cursor.rowcount):
        cursor.close()
        time.sleep(1)
        return 1
    else :
        cursor.clos
