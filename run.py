from app import createApp
from app.extensions import db
from app.tables import Users, Characters, Dictionary, Gebets

app = createApp('dev')
db.app = app
db.create_all()
Users.add(Users('admin', 'admin', 'admin@example.com', True))
Characters.add(Characters('Josty'))
Dictionary.add(Dictionary('Josty', 'Джости', 'no name', 'Josty'))
Gebets.add(Gebets('Josty', '1.0'))

if __name__ == "__main__":
    app.run(host='api-genshin-journey.herokuapp.com')
