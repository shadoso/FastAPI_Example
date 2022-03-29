from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
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
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Yor status in the college is disabled"
        )

    result = data.query(models.Users).filter_by(role=role).all()

    return result
