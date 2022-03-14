from app import createApp
from app.extensions import db


app = createApp('prod')
db.app = app
try:
    db.create_all()
except e:
    print("[Error] db", e)

if __name__ == "__main__":
    app.run(host='192.168.43.231')
