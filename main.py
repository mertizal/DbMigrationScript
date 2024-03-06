
from peewee import *
import mysql_model
import postgre_model
from mysql_model import Members_mysql
from postgre_model import Members_postgres


pg_query = Members_postgres.select()
mysql_query = Members_mysql.select()

if pg_query.order_by(Members_postgres.id.desc()).get() != mysql_query.order_by(Members_mysql.id.desc()).get():
    for member in mysql_query:
        Members_postgres.get_or_create(
            name=member.name,
            email=member.email,
            position=member.position,
            start_date=member.start_date,
            age=member.age
        )




# print(mysql_query[-1].id)



















