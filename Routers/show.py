from typing import List
from fastapi import APIRouter
from fastapi import Depends
from SQL.schemas import ShowUser
from SQL import models
from SQL.models import Role
from SQL.session import database
from sqlalchemy.orm import Session
from Utility import oauth2

router = APIRouter(
    prefix="/ChimeraCore/show",
    tags=["Show"]
)

# EMPLOYEE = models.Employee
# STUDENT = models.Student
# GUEST = models.Guest
#
# TABLE = {
#     Role.admin: EMPLOYEE,
#     Role.staff: EMPLOYEE,
#     Role.coordinator: EMPLOYEE,
#     Role.teacher: EMPLOYEE,
#     Role.student: STUDENT,
#     Role.guest: GUEST
# }


@router.get("/all/{role}", response_model=List[ShowUser])
async def show_users(
        data: Session = Depends(database),
        token: str = Depends(oauth2.current_user),
        role: Role = str
):

    return data.query(models.Users).filter_by(role=role).all()


# @router.get("/show/{role}")
# async def show_users(
#         data: Session = Depends(database),
#         role: Role = str
# ):
#     return data.query(TABLE[role]).filter_by(role=role).all()
