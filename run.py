import os

from sqlalchemy.exc import IntegrityError
from app import create_app
from app.models.user import User
from app.data_models.user import UserData
from app.extensions import db

app = create_app('prod')
db.app = app

db.create_all()
db.session.commit()

try:
    user = User(UserData(os.getenv('USERNAME') or 'admin', os.getenv('PASSWORD') or 'admin', os.getenv('EMAIL') or 'admin', True))
    user.add(user)
except IntegrityError:
    print("[Error] Account already exists")
except AttributeError:
    print("[Error] No config vars")

if __name__ == "__main__":
    app.run()
