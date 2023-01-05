#validation
from pydantic import(
    BaseModel,Field
)

class Movie(BaseModel):
    title:str = Field(..., min_length=1, max_length=100)
    overview:str = Field(..., min_length=1, max_length=255)
    year:int = Field(..., lg=0)
    rating:float = Field(..., lg=0)
    category:str =  Field(..., min_length=1, max_length=100)