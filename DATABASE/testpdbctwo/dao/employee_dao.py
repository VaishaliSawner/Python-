import mysql.connector
from config.db import pool


class EmployeeDAO:

    @staticmethod
    def save(emp):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql="insert"

    @staticmethod
    def fetch_all():
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "select * from empolyee"
                    cursor.execute(sql)
                    rows = cursor.fetchall

    @staticmethod
    def update(emp):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql="update employee set name = %s, salary = %s,department=%s where "
                    cursor.execute(sql,(emp.name,emp.salary,emp.department,emp.id))
                    conn.commit()
                    return cursor.rowcount>0

        except Error as e:
            if conn and conn.is_connected
    @staticmethod
    def delete(id):
        try:
            with pool.get_connection() as conn:
                with conn.cursor



