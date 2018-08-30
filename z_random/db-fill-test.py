from pony.orm import *
from db-test import Technology
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

result = select(i.name for i in Technology)
result.show()
