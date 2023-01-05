from passlib.hash import bcrypt
from schema.user_schema import User
from Models.users import User as UserModel

class UserService:
    def __init__(self, seccion) -> None:
        self.seccion = seccion
    
    def create_user(self, user:User):
        user_reciver = UserModel(
            email=user.email,
            passwd=bcrypt.encrypt(user.passwd)
        )
        self.seccion.add(user_reciver)
        self.seccion.commit()
        self.seccion.close()
        return
    
    def get_all_users(self):
        return self.seccion.query(UserModel).all()
    
    def get_user_by_email(self, email:str):
        return self.seccion.query(UserModel).filter(UserModel.email == email).first()
    