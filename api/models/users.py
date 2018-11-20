from api.models.db_controller import Dbcontroller
from api.models.models import User

class UserDb(Dbcontroller):

    def __init__(self):
        super().__init__()

    def add_user(self,new_user):
        self.cursor.execute("INSERT INTO users(username,email,password,role) VALUES\
        (%s, %s, %s, %s);",(new_user.name,new_user.email,new_user.password,new_user.role))

    def fetch_user(self,user):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM users WHERE username=%s"
        self.cursor.execute(query, (user.name,))
        user = self.cursor.fetchone()
        return user

    def fetch_all_users(self):
        return self.fetch_all_entries('users')
