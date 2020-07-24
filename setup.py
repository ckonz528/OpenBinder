from app import db, User
import os

if os.path.exists('data.db'):
    os.remove('data.db')

db.create_all()

users = [
    User(username='ckonz', password='tomato juice', privilege=0),
    User(username='admin', password='hunter1', privilege=1)
]

for user in users:
    db.session.add(user)
db.session.commit()