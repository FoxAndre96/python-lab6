import pymysql


def add_new_task(task):

    sql = "INSERT INTO to_do_list (todo) VALUES (%s)"

    conn = pymysql.connect(user='root', password='passwordserver', host='localhost', database='tasks')
    cursor = conn.cursor()

    result = -1

    try:
        cursor.execute(sql, (task,))
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        conn.rollback()

    conn.close()

    return result


def show_tasks():

    sql = "SELECT * FROM to_do_list"

    conn = pymysql.connect(user='root', password='passwordserver', host='localhost', database='tasks')
    cursor = conn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return result


def remove_task(task):

    sql = "DELETE FROM to_do_list WHERE id_task=%s"

    conn = pymysql.connect(user='root', password='passwordserver', host='localhost', database='tasks')
    cursor = conn.cursor()

    result = -1

    try:
        cursor.execute(sql, (task,))
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        conn.rollback()

    conn.close()

    return result