from fastapi import Depends
from fastapi import FastAPI
from typing import Optional
from uuid import uuid4
from SQL.session import engine, database, Base
from SQL import models
from SQL.models import Role, Course, Enum
from SQL import schemas
from sqlalchemy.orm import Session

EMPLOYEE = [Role.admin, Role.coordinator, Role.staff, Role.teacher]
NOT_FOUND = 404
COLLEGE_EMAIL = "@ChimeraCore.com"

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/home")
async def home():
    return {"I'm home": "Hi"}


@app.get("/home/ChimeraCore/show/all/{role}")
async def show_users(data: Session = Depends(database),
                     role: Role = str
                     ):
    user = role

    if user == Role.student:
        student = data.query(models.Student).all()
        return {f"{user.value}s": student}

    if user in EMPLOYEE:
        employee = data.query(models.Employee).all()
        return {f"{user.value}s": employee}

    if user == Role.guest:
        guest = data.query(models.Guest).all()
        return {f"{user.value}s": guest}


@app.post("/home/ChimeraCore/create/{role}")
async def create_user(post: schemas.Post, role: Role,
                      code: str = str(uuid4())[::5],
                      data: Session = Depends(database)
                      ):
    unique = str(uuid4())[11::5]
    college_email = post.name + role.value + unique + COLLEGE_EMAIL
    user = role
    # code = password

    if user == Role.student:
        student = models.Student(**post.dict(), email=college_email, password=code, role=user)

        data.add(student)
        data.commit()
        data.refresh(student)

        return {f"{user.value}": student.email}

    if user in EMPLOYEE:
        employee = models.Employee(**post.dict(), email=college_email, password=code, role=user)

        data.add(employee)
        data.commit()
        data.refresh(employee)

        return {f"{user.value}": employee.email}

    if user == Role.guest:
        guest = models.Guest(**post.dict(), email=college_email, password=code, role=user)

        data.add(guest)
        data.commit()
        data.refresh(guest)

        return {f"{user.value}": guest.email}
