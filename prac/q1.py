# create a local db
import sqlite3
import os

# create database and tables


def init_db():
    conn = sqlite3.connect('storage.db')
    # create table
    conn.execute(
        "CREATE TABLE RESULTS(USERID INT PRIMARY KEY,USERNAME CHAR(50),PASSWORD CHAR(50),REGION CHAR(50));")
    print("database created successfully")
    conn.commit()
    conn.close()


def get_region():
    conn = sqlite3.connect('storage.db')
    # get results
    x = conn.execute("SELECT * FROM RESULTS")
    d = {}
    for i in x:
        if(i[3] in d.keys()):
            d[i[3]] = d[i[3]]+1
        else:
            d[i[3]] = 1
    conn.close()
    return d


def get_region_group():
    conn = sqlite3.connect('storage.db')
    x = conn.execute(
        "SELECT COUNT(USERID),REGION FROM RESULTS GROUP BY REGION;")
    print("Region\t", "Users")
    for i in x:
        print(i[1], " ", i[0])
    conn.close()
# check for user id


def check(id):
    conn = sqlite3.connect('storage.db')
    x = conn.execute('SELECT COUNT(USERID) FROM RESULTS WHERE userid='+id)
    for i in x:
        if(i[0] > 0):
            conn.close()
            return True
        else:
            conn.close()
            return False
# print to file


def write_to_file(data):
    filepath = "output.txt"
    f = open(filepath, 'w', encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.flush()
    f.close()
# login and print details to file


def login():
    userid = input("Enter userid:\n")
    if(check(userid)):
        print("User exists")
        conn = sqlite3.connect('storage.db')
        query = "SELECT * FROM RESULTS WHERE userid="+userid
        data = conn.execute(query)
        for i in data:
            print(i[0], " ", i[1], " ", i[2], " ", i[3])
            write_to_file(str(i[0])+" "+i[1]+" "+i[2]+" "+i[3])
        conn.close()
    else:
        print("user does not exist")


def show_all():
    conn = sqlite3.connect('storage.db')
    x = conn.execute('SELECT * FROM RESULTS')
    for i in x:
        print(i[0], i[1], i[2], [3])
    conn.close()


init_db()
c = sqlite3.connect('storage.db')
n = int(input("Enter number of users"))
for i in range(n):
    userid = input("Enter userid: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    region = input("Enter region: ")
    exp = "INSERT INTO RESULTS(USERID,USERNAME,PASSWORD,REGION)VALUES(" + \
        userid+",\""+username+"\",\""+password+"\",\""+region+"\");"
    print(exp)
    c.execute(exp)
    c.commit()

c.close()
get_region_group()
login()
show_all()