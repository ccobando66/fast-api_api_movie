

from fastapi import(
    FastAPI
) 


from middlewares.error_handler import ErrorHandler

from routers import(
    movies,user
)


app = FastAPI()
app.title = 'my aplicacion con fast api'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)


app.include_router(movies.movies)
app.include_router(user.users)








