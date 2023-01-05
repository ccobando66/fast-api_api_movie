from typing import List
from Models.movie import Movie as MovieModel
from schema.movie_schema import Movie

class MovieService():
     def __init__(self, seccion) -> None:
        self.seccion = seccion
    
     def get_all_data(self) -> List[object]:
        return self.seccion.query(MovieModel).all()
    
     def get_data(self, id:int) -> object:
        return self.seccion.query(MovieModel).get(id)
     
     def create_movie(self,movie:Movie):
         movie_reciver = MovieModel(**movie.dict())
         self.seccion.add(movie_reciver)
         self.seccion.commit()
         self.seccion.close()
         return
         
     def update_movie(self,id:int,movie:Movie):
         data_model = self.get_data(id)
         data_model.title = movie.title.strip()
         data_model.overview = movie.overview.strip()
         data_model.year = movie.year   
         data_model.rating = movie.rating      
         data_model.category = movie.category.title().strip()  
         self.seccion.commit()  
         return
      
     def delete_movie(self, id:int):
         data_model = self.get_data(id)
         self.seccion.delete(data_model)
         self.seccion.commit()
         return
