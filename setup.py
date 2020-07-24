from app import db, User, md5encode
import os

if os.path.exists('data.db'):
    os.remove('data.db')

db.create_all()

users = [
    User(username='ckonz', password=md5encode('tomato juice'), privilege=0),
    User(username='admin', password=md5encode('hunter1'), privilege=1)
]

for user in users:
    db.session.add(user)
db.session.commit()