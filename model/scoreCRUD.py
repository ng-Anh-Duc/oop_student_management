import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError
import model.mvc_exceptions as mvc_exc

DB_name = 'myDB'

def connect_to_db(db=None):
    """Connect to a sqlite DB. Create the database if there isn't one yet.

    Open a connection to a SQLite DB (either a DB file or an in-memory DB).
    When a database is accessed by multiple connections, and one of the
    processes modifies the database, the SQLite database is locked until that
    transaction is committed.

    Parameters
    ----------
    db : str
        database name (without .db extension). If None, create an In-Memory DB.

    Returns
    -------
    connection : sqlite3.Connection
        connection object
    """
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = '{}.db'.format(db)
        print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection

# TODO: use this decorator to wrap commit/rollback in a try/except block ?
# see https://www.kylev.com/2009/05/22/python-decorators-and-database-idioms/
def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when we want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Parameters
    ----------
    func : function
        function which performs the database query

    Returns
    -------
    inner func : function
    """
    def inner_func(conn, *args, **kwargs):
        try:
            conn.execute(
                'SELECT name FROM sqlite_temp_master WHERE type="table";')
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
def create_score_relationship_table(conn, table_name):
    sql = 'CREATE TABLE {} (student_id INTEGER NOT NULL REFERENCES students(student_id), course_id INTEGER NOT NULL REFERENCES courses(course_id), score REAL, PRIMARY KEY (student_id, course_id))'.format(table_name)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)

@connect
def insert_one(conn, studentID, courseID, score, table_name):
    sql = "INSERT INTO {} ('student_id', 'course_id', 'score') VALUES (?, ?, ?)".format(table_name)
    try:
        conn.execute(sql, (studentID, courseID, score))
        conn.commit()
    except IntegrityError:
        raise mvc_exc.ItemAlreadyStored()

# def tuple_to_object(mytuple):
#     course = Course(mytuple[0], mytuple[1], mytuple[2])
#     return course

# @connect
# def select_all(conn, table_name):
#     sql = 'SELECT * FROM {}'.format(table_name)
#     c = conn.execute(sql)
#     results = c.fetchall()
#     return list(map(lambda x: tuple_to_object(x), results))

@connect
def update_one(conn, studentID, courseID, score, table_name):
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE (student_id, course_id)=(?,?) LIMIT 1)'.format(table_name)
    sql_update = 'UPDATE {} SET score=? WHERE (student_id, course_id)=(?,?)'.format(table_name)
    c = conn.execute(sql_check, (studentID, courseID,))
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