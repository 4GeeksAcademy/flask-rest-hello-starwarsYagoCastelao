from models import User

class UserService:
    def get_list(self):
        user = User.query.filter_by(email="h@h.com", password="1234").first()
        return[]