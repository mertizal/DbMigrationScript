
from peewee import *
import mysql_model
import postgre_model
from mysql_model import Members_mysql
from postgre_model import Members_postgres


mysql_query = Members_mysql.select()
pg_query = Members_postgres.select()

if pg_query.count() == 0:

    for member in mysql_query:
        Members_postgres.create(
            id=member.id,
            name=member.name,
            email=member.email,
            position=member.position,
            start_date=member.start_date,
            age=member.age
        )
    print("Satırlar eklendi..")

else:

    for member in mysql_query.where(Members_mysql.id > pg_query[-1].id):
        Members_postgres.get_or_create(
                name=member.name,
                email=member.email,
                position=member.position,
                start_date=member.start_date,
                age=member.age
            )

    print("yeni atırlar eklendi..")







# print(mysql_query[-1].id)
# if pg_query[-1].id != mysql_query[-1].id:
    #     for member in mysql_query:
    #         Members_postgres.get_or_create(
    #             id=member.id,
    #             name=member.name,
    #             email=member.email,
    #             position=member.position,
    #             start_date=member.start_date,
    #             age=member.age
    #         )



















