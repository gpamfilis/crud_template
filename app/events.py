from app.models import User
from app import db

@db.event.listens_for(User, "after_insert")
def insert_order_to_printer(mapper, connection, target):
    print('New User', target.username)


#lk
