from api.models.db_controller import Dbcontroller

class UserDb(Dbcontroller):

    def __init__(self,database_url):
        super().__init__(database_url)

    def add_user(self,new_user):
        self.cursor.execute("INSERT INTO users(username,email,password,role) VALUES\
        (%s, %s, %s, %s);",(new_user.name,new_user.email,new_user.password,new_user.role))

    def fetch_user_id(self,name):
        query = ("SELECT * FROM users WHERE username = %s";)%(name)
        self.cursor.execute(query)
        return self.cursor.fetchone()
