from app import createApp
from app.extensions import db


app = createApp('prod')
db.app = app
try:
    db.create_all()
except:
    print("[Error] db")

if __name__ == "__main__":
    app.run()
