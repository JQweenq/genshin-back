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

if __name__ == "__main__":
    app.run()
