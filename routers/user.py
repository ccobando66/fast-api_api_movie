from fastapi import(
    APIRouter,HTTPException,status,
    Body
)



from Config.database import (
    conection,Base,Seccion
)


from middlewares.jwt_bearer import create_token
from schema.user_schema import User
from Services.user_services import UserService
from passlib.hash import bcrypt

users = APIRouter()

Base.metadata.create_all(conection)
session = Seccion()

@users.post(
    path='/user/create',
    tags=['Auth'],
    status_code=status.HTTP_200_OK,
    response_model=object
)
def create_user(user_out:User = Body(...)):
     UserService(session).create_user(user_out)
     return {'sms':'user created'}

@users.post(
    path='/user/login',
    tags=['Auth']
)
def login_user(user_out:User = Body(...)):
    
     get_user = list(filter(lambda data: data.email == user_out.email and bcrypt.verify(user_out.passwd,data.passwd), UserService(session).get_all_users()))
     if len(get_user) == 0:
         raise HTTPException(
             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
             detail="email or password invalid"
         )
     payload = {
         'id':get_user[0].id,
         'email':get_user[0].email,
         'passwd':get_user[0].passwd
     }
    
     return create_token(payload)


     
