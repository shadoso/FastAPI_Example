from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi import status as error
from SQL import models
from SQL.models import Role
from SQL.session import database
from sqlalchemy.orm import Session
from Utility import oauth2

router = APIRouter(
    prefix="/ChimeraCore/delete",
    tags=["Delete"]
)


@router.delete("/user/{uuid}")
async def delete_user(
        data: Session = Depends(database),
        token: object = Depends(oauth2.current_user),
        uuid=str
):

    if token.status is False:
        raise HTTPException(
            status_code=error.HTTP_401_UNAUTHORIZED,
            detail="Yor status in the college is disabled"
        )

    if token.role != Role.admin:
        raise HTTPException(
            status_code=error.HTTP_401_UNAUTHORIZED,
            detail="You are not an admin"
        )

    user = data.query(models.Users).filter(models.Users.uuid == uuid).first()

    if not user:
        raise HTTPException(
            status_code=error.HTTP_404_NOT_FOUND,
            detail=f"The uuid:{uuid} doesn't belong to any User"
        )

    user_out = user.__dict__.copy()

    data.delete(user)
    data.commit()

    return user_out
