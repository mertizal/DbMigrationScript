from peewee import *

database = MySQLDatabase('geniousoft_members', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Members_mysql(BaseModel):
    age = IntegerField(null=True)
    email = CharField(unique=True, null=True)
    name = CharField(null=True)
    position = CharField(null=True)
    start_date = DateField(null=True)

    class Meta:
        table_name = 'members'

