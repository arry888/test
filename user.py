import pymysql


def select():
    # 打开数据库连接
    db = pymysql.connect("172.16.230.149", "root", "123456", "test")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from user;"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            # 打印结果
            print("id=%s,name=%s,age=%d" % \
                  (id, name, age))
    except:
        print("Error: 数据库请求异常")
    # 关闭数据库连接
    db.close()


# select()

def db_excute(sql):
    db = pymysql.connect("172.16.230.149", "root", "123456", "test")
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
    sql = "select * from user;"
    # esults = db_excute(sql)
    return db_excute(sql)

    # for row in results:
    #     id = row[0]
    #     name = row[1]
    #     email = row[2]
    #     age = row[3]

        # 打印结果
    # return ("id=%s ,name=%s , email=%s ,age=%s ," % (id, name, email, age))
    # return db_excute(sql)


def add_user(name, email, age):
    sql = "insert into user(name,emai,age) value('%s','%s',%s)" % (name, email, age)
    return db_excute(sql)


def delect_user(name):
    sql = "delete from user where name='%s'" % (name)

    db_excute(sql)
