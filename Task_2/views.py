from django.shortcuts import render

from django.db import connection

def my_custom_sql(self):
    # import pdb;pdb.set_trace()
    with connection.cursor() as cursor:
        cursor.execute('''SELECT "Task_2_blog"."id", "Task_2_blog"."name", "Task_2_blog"."tagline" FROM "Task_2_blog"''')
        row = cursor.fetchall()
    return row