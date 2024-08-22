from django.db import connections
from django.conf import settings

class Portal():

    def __init__(self):
        self.env = settings.ENVIR
        self.db_cursor = connections['portal'].cursor()

    def check_employee(self,employee_id):
        sql = "SELECT * FROM employees WHERE id= %s"
        self.db_cursor.execute(sql, (employee_id,))
        row = self.db_cursor.fetchall()
        data_set = {}
        if row:
            data_set['data'] = row
            data_set['titles'] = self.db_cursor.column_names
        return data_set

    def insert_employee_data(self,id, name, position, salary):
        try:
            sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
            self.db_cursor.execute(sql, (id, name, position, salary))
            row = self.db_cursor.fetchall()
            data_set = {}
            if row:
                data_set['data'] = row
                data_set['titles'] = self.db_cursor.column_names
            return data_set
        except Exception as e:
            str(e)

    def delete_employee_data(self, id):
        try:
            sql = 'DELETE FROM employees WHERE id=%s'
            self.db_cursor.execute(sql, (id))
        except Exception as e:
            str(e)

    def check_current_salary(self,employee_id):
        sql = "SELECT salary FROM employees WHERE id=%s"
        self.db_cursor.execute(sql, (employee_id,))
        row = self.db_cursor.fetchOne()
        return row

    def update_new_salary(self,new_salary,Id):
        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        self.db_cursor.execute(sql_update, (new_salary, Id))

    def display_employees(self,):
        sql = "SELECT * FROM employees order by id desc"
        self.db_cursor.execute(sql,)
        row = self.db_cursor.fetchall()
        return row

