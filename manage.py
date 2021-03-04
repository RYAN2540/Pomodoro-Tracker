from app import create_app, db
from flask_script import Manager,Server
<<<<<<< HEAD
from flask_migrate import Migrate, MigrateCommand
=======
from app.models import User, Task
from  flask_migrate import Migrate, MigrateCommand
>>>>>>> 3c575a9699105a90336370be2d0d4bb79b512854

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)  


@manager.shell
def make_shell_context():
<<<<<<< HEAD
    return dict(app = app, db = db)
=======
    return dict(app = app,db = db,User = User, Task=Task)
>>>>>>> 3c575a9699105a90336370be2d0d4bb79b512854

if __name__ == '__main__':
    manager.run()