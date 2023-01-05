from jwt import encode,decode
from fastapi.security import HTTPBearer
from fastapi import Request, status, HTTPException
from Services.user_services import UserService

from Config.database import (
    conection,Base,Seccion
)

Base.metadata.create_all(conection)
session = Seccion()

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = verify_token(auth.credentials)
        if UserService(session).get_user_by_email(data['email']) is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="invalid credentials"
            )

def verify_token(token:str)-> dict:
    data = decode(token, key="pkBQsEUs`F&Qv*a,[E2x[#,F}/I.W3",  algorithms='HS256')
    return data

def create_token(token:dict)-> str:
    token = encode(payload=token, key="pkBQsEUs`F&Qv*a,[E2x[#,F}/I.W3", algorithm='HS256')
    return token