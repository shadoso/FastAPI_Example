from fastapi import FastAPI
from Routers import show, create, login
from SQL.session import Base, engine


PATH = [show, create, login]

Base.metadata.create_all(bind=engine)
app = FastAPI()

for rout in PATH:
    app.include_router(router=rout.router)
