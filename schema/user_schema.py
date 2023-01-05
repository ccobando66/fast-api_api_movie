from pydantic import(
    BaseModel,Field,EmailStr
)

class User(BaseModel):
    email:EmailStr = Field(
        ...
    )
    passwd:str = Field(
        ...,
        min_length=8
    )