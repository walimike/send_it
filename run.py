from api import app
from api.views.utilities import user_db
from api.models.models import User

if __name__ == '__main__':
    admin_user = User('admin_user','admin@gmail.com','@H@nN@H92','admin')
    user_db.drop_tables()
    user_db.create_tables()
    user_db.add_user(admin_user)
    app.run()
