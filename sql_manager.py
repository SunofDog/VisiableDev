import MySQLdb
import sys
import os
import re

class mysql(object):
    def __init__(self, url, usr, pwd, dbname):
        self.db = MySQLdb.connect(url, usr, pwd, dbname)
        self.cur = self.db.cursor()
        print(self.cur)

    def load_report(self, file_name):
        f = open(file_name)
        grade = file_name[:-4]
        iter_f = iter(f)
        for line in iter_f:
            num, name, obj, score = line.split(" ")
            if score:
                score = score.strip(":")
                sql = "insert into report(grade, num, name, %s) values('%s', %d, '%s', %f)" %(obj, grade, int(num), name, int(score))
                print sql
                self.cur.execute(sql)
    def db_close(self):
        self.cur.close()
        self.db.commit()
        self.db.close()

    def db_show(self):
        sql = "select * from report"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        for i in result:
            print i 

    def db_update(self, classes, num, obj, value):
        sql = "update report set %s  = %d where grade = %s and num = %d" %(obj, value, classes, num)
        self.cur.execute(sql)

    def db_del(self):
        sql = "delete from report"
        self.cur.execute(sql)

if __name__ == '__main__':
    sql = mysql("localhost", "root", "011235", "testdb")
    sql.db_del()
    sql.load_report(sys.argv[1])
    sql.db_show()
    sql.db_show("2005-1-3-2", 39, "math", 99)
