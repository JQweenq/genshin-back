from flask_script import Manager
from flask_migrate import Migrate
from run import app
from app.models.utils import db

migrate = Migrate(app, db)

manager = Manager(app)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
