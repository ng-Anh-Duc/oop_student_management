import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError
import model.mvc_exceptions as mvc_exc
from model.score import Score

DB_name = 'myDB'

def connect_to_db(db=None):
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = '{}.db'.format(db)
        print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection

def connect(func):
    def inner_func(conn, *args, **kwargs):
        try:
            conn.execute('SELECT name FROM sqlite_temp_master WHERE type="table";')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db(DB_name)
        return func(conn, *args, **kwargs)
    return inner_func

# def disconnect_from_db(db=None, conn=None):
#     if db is not DB_name:
#         print("You are trying to disconnect from a wrong DB")
#     if conn is not None:
#         conn.close()
#AUTOINCREMENT
@connect
def create_course_table(conn, table_name):
    sql = 'CREATE TABLE {} (course_id INTEGER PRIMARY KEY, courseName VARCHAR, major VARCHAR)'.format(table_name)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)

@connect
def create_score_relationship_table(conn, table_name1, table_name2, table_name3):
    sql = 'CREATE TABLE {} (student_id INTEGER NOT NULL REFERENCES {}(student_id), course_id INTEGER NOT NULL REFERENCES {}(course_id), score REAL, PRIMARY KEY (student_id, course_id))'.format(table_name1, table_name2, table_name3)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)

@connect
def insert_course(conn, courseID, courseName, major, table_name):
    # Check if the course exists; if not, insert it
    check_course_sql = 'SELECT EXISTS(SELECT 1 FROM {} WHERE course_id=? LIMIT 1)'.format(table_name)
    insert_course_sql = 'INSERT INTO {} (course_id, courseName, major) VALUES (?, ?, ?)'.format(table_name)

    c = conn.execute(check_course_sql, (courseID,))
    if not c.fetchone()[0]:
        # Course does not exist, insert it
        conn.execute(insert_course_sql, (courseID, courseName, major))
        conn.commit()

# @connect
# def insert_one(conn, studentID, courseID, score, table_name):
#     sql = "INSERT INTO {} ('student_id', 'course_id', 'score') VALUES (?, ?, ?)".format(table_name)
#     try:
#         conn.execute(sql, (studentID, courseID, score))
#         conn.commit()
#     except IntegrityError:
#         raise mvc_exc.ItemAlreadyStored()

def tuple_to_score(mytuple):
    score = Score(mytuple[0], mytuple[1], mytuple[2])
    return score

# @connect
# def select_all(conn, table_name):
#     sql = 'SELECT * FROM {}'.format(table_name)
#     c = conn.execute(sql)
#     results = c.fetchall()
#     return list(map(lambda x: tuple_to_object(x), results))
@connect
def select_scores_by_student(conn, studentID, table_name):
    sql = 'SELECT * FROM {} WHERE student_id = ?'.format(table_name)
    c = conn.execute(sql, (studentID,))
    results = c.fetchall()
    return list(map(lambda x: tuple_to_score(x), results))

@connect
def update_one(conn, studentID, courseID, score, table_name):
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE (student_id, course_id)=(?,?) LIMIT 1)'.format(table_name)
    sql_update = 'UPDATE {} SET score=? WHERE (student_id, course_id)=(?,?)'.format(table_name)
    c = conn.execute(sql_check, (studentID, courseID))
    result = c.fetchone()
    if result[0]:
        c.execute(sql_update, (score, studentID, courseID))
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored()

@connect
def delete_one(conn, studentID, courseID, table_name):
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE (student_id, course_id)=(?,?) LIMIT 1)'.format(table_name)
    sql_delete = 'DELETE FROM {} WHERE (student_id, course_id)=(?,?)'.format(table_name)
    c = conn.execute(sql_check, (studentID, courseID,))
    result = c.fetchone()
    if result[0]:
        c.execute(sql_delete, (studentID, courseID,))
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored()