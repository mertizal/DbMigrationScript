import postgre_model
from playhouse.migrate import *

database = PostgresqlDatabase('geniousoft_members', **{'host': 'localhost', 'port': 5432, 'user': 'root', 'password': 'root'})
migrator = PostgresqlMigrator(database)
email = CharField(unique=True, null=True)

# migrate(
#     migrator.rename_column('members', 'email_old', 'email')
# )



