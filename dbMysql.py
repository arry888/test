import pymysql


def db_excute(sql):
    db = pymysql.connect("172.16.143.164", "root", "!1232456", "test")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print('数据库请求异常:' + e)
        db.rollback()
    db.close()


def select_user():
    sql = "select * from image;"
    return db_excute(sql)


def add_image(url, name):
    sql = "insert into image(url,name) value('%s','%s')" % (url, name)
    return db_excute(sql)
