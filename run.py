import os

from sqlalchemy.exc import IntegrityError
from app import createApp
from app.tables import User
from app.data import UserData
from app.extensions import db

app = createApp('prod')
db.app = app

try:
    db.create_all()
    db.session.commit()
except:
    print("[Error] db")

try:
    user = User(UserData(os.getenv('USERNAME'), os.getenv('PASSWORD'), os.getenv('EMAIL'),  True))
    user.add(user)
except IntegrityError:
    print("[Error] Account already exists")
except AttributeError:
    print("[Error] No config vars")

if __name__ == "__main__":
    app.run()
