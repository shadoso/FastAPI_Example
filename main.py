from fastapi import FastAPI
from Routers import create, login, show, delete
from SQL.session import Base, engine


PATH = [create, login, show, delete]

Base.metadata.create_all(bind=engine)
app = FastAPI()

for rout in PATH:
    app.include_router(router=rout.router)
