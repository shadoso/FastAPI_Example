from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi import status as error
from SQL.schemas import ShowUser, SecretShow
from SQL import models
from SQL.models import Role
from SQL.session import database
from sqlalchemy.orm import Session
from Utility import oauth2

router = APIRouter(
    prefix="/ChimeraCore/show",
    tags=["Show"]
)


@router.get("/all/{role}", response_model=List[ShowUser])
async def show_users(
        data: Session = Depends(database),
        token: object = Depends(oauth2.current_user),
        role: Role = str
):
    if token.status is False:
        raise HTTPException(
            status_code=error.HTTP_401_UNAUTHORIZED,
            detail="Your status in the college is disabled"
        )

    result = data.query(models.Users).filter_by(role=role).all()

    return result


@router.get("/find/{uuid}", response_model=ShowUser)
async def show_user(
        data: Session = Depends(database),
        token: object = Depends(oauth2.current_user),
        uuid=str
):
    if token.status is False:
        raise HTTPException(
            status_code=error.HTTP_401_UNAUTHORIZED,
            detail="Your status in the college is disabled"
        )

    result = data.query(models.Users).filter(models.Users.uuid == uuid).first()

    if not result:
        raise HTTPException(
            status_code=error.HTTP_404_NOT_FOUND,
            detail=f"The uuid:{uuid} doesn't belong to any User"
        )

    return result
