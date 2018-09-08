import os
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app, db
from app.models import User,Article,Apply

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)
#把MigrateCommand命令添加到manager中
manager.add_command('db',MigrateCommand)

@manager.command
def deploy():
    from flask_migrate import upgrade
    from app.models import Role

    # migrate database to latest revision
    # upgrade()

    # create user roles
    Role.insert_roles()


if __name__ == '__main__':
        manager.run()
