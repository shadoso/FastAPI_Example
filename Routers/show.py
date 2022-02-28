from fastapi import Depends
from fastapi import APIRouter
from SQL.session import database
from SQL import models
from SQL.models import Role
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/ChimeraCore",
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


@router.get("/show/all/{role}")
async def show_users(
        data: Session = Depends(database),
        role: Role = str
):
    return data.query(models.Users).filter_by(role=role).all()


# @router.get("/show/{role}")
# async def show_users(
#         data: Session = Depends(database),
#         role: Role = str
# ):
#     return data.query(TABLE[role]).filter_by(role=role).all()
