import postgre_model
from playhouse.migrate import *

database = MySQLDatabase('geniousoft_members', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': 'root'})
migrator = MySQLMigrator(database)
email = CharField(unique=True, null=True)

# migrate(
#     migrator.add_column('members', 'email_temp', email)
# )
#
# migrate(
#     migrator.rename_column('members', 'email', 'email_old')
# )
#

# migrate(
#     migrator.rename_column('members', 'email_old', 'email')
# )





