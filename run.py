from dotenv import load_dotenv
from app import createApp
from app.extensions import db
from app.tables import Users, Characters, Dictionary, Wishes

load_dotenv()

app = createApp('dev')
db.app = app
db.create_all()
Users.add(Users('admin', 'admin', 'admin@example.com', True))
Characters.add(Characters('Josty'))
Dictionary.add(Dictionary('Josty', 'Джости', 'no name', 'Josty'))
Wishes.add(Wishes('Josty', '1.0'))

if __name__ == "__main__":
    app.run()
