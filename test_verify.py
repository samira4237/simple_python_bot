#create table help with dbhelper that has columns of verify,refcod,chat_id, first name and last name
from db_helper_test import DBHelper
db = DBHelper()
db.setup()
#db.add_item(1,2,3)
a = str('true')


print(db.get_verify('Sam'))






