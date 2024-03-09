from peewee import *

database = PostgresqlDatabase('geniousoft_members', **{'host': 'localhost', 'port': 5432, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Members_postgres(BaseModel):
    age = IntegerField(null=True)
    email = CharField(null=True)
    name = CharField(null=True)
    position = CharField(null=True)
    start_date = DateField(null=True)

    class Meta:
        table_name = 'members'

