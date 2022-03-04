from app import createApp
from app.extensions import db
from app.tables import User, Character, Word, Wishe


app = createApp('prod')
db.app = app
try:
    db.create_all()
except:
    print("rrr")

# if (User.query.filter(User.id == 1).first() == []) or \
#         (Character.query.filter(Character.id == 1).first() == []) or \
#         (Word.query.filter(Word.id == 1).first() == []) or \
#         (Wishe.query.filter(Wishe.id == 1).first() == []):
User.add(User('admin', 'admin', 'admin@example.com', True))
Character.add(Character('Джости', 5, 'Josty', 'Josty Qweenq', ))
Word.add(Word('Josty', 'Джости',  'no name', 'Josty'))
Wishe.add(Wishe('Josty', '1.0'))

if __name__ == "__main__":
    app.run()
