from fastapi import(
    APIRouter,HTTPException,status,
    Depends,Path,Query,Body
)


from Config.database import (
    conection,Base,Seccion
)

from Services.movie_service import MovieService
from middlewares.jwt_bearer import JWTBearer
from typing import List
from schema.movie_schema import Movie

movies = APIRouter()

Base.metadata.create_all(conection)
session = Seccion()

@movies.get(
    path='/movies',
    tags=['Movies'],
    dependencies=[Depends(JWTBearer())]
)
def get_all_movies():
    show_all_data = MovieService(session).get_all_data()
    return 'movies not found' if len(show_all_data) == 0  else show_all_data

@movies.get(
    path='/movies/{id_movie}',
    tags=['Movies'],
    response_model=object
)
def get_movie_by_id(id_movie:int = Path(..., lg=0)):
    # get_movie = list(filter(lambda data: data['id'] == id_movie, movies))
    get_movie =  MovieService(session).get_data(id_movie)
    
    if get_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='movie not found'
        ) 
    return get_movie

@movies.get(
    path='/movies/',
    tags=['Movies'],
    status_code=status.HTTP_200_OK,
    response_model=List[object],
    dependencies=[Depends(JWTBearer())]
    )
def get_movie_by_category(
      category:str = Query(..., min_length=1)
    ):
    get_movie = list(filter(lambda data: data.category == category.title(),MovieService(session).get_all_data()))
    if len(get_movie) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='category not found'
        ) 
    return get_movie

@movies.post(
    path='/movies',
    tags=['Movies'],
)
def create_movies(get_data:Movie):
   
    """
     # get_movie = list(filter(lambda data: data['id'] == get_data.id, movies))
     get_movie = get_data()
     if len(get_movie) > 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='this number is register a movie'
        ) 
    """
    
    MovieService(session).create_movie(get_data)
    return {'sms':'movie register'}

@movies.put(
    path='/movies/{id_movie}',
    tags=['Movies']
)
def update_movies_by_id(id_movie:int = Path(..., lg=0), get_out_data:Movie = Body()):
    #get_movie = list(filter(lambda data: data['id'] == id_movie, movies))
    get_movie = MovieService(session).get_data(id_movie)
    if get_movie is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='movie not found'
        ) 
    MovieService(session).update_movie(id_movie,get_out_data)
    return {'sms':'movie update'}

@movies.delete(
    path='/movies/{id_movie}',
    tags=['Movies']
)
def delete_movies_by_id(id_movie:int = Path(..., lg=0)):
    get_movie = MovieService(session).get_data(id_movie)
    if get_movie is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='movie not found'
        ) 
    MovieService(session).delete_movie(id_movie)
    return {'sms':'movie deleted'}
