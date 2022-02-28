from fastapi import APIRouter, Depends, HTTPException, status
from Utility import hashing
from SQL.session import database
from SQL.models import Users
from SQL.schemas import Login
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/ChimeraCore",
    tags=["Access"]
)


@router.post("/login")
async def login(
        credential: Login,
        data: Session = Depends(database)
):
    email = data.query(Users).filter(Users.email == credential.email).first()
    if not email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    if not hashing.verify(credential.password, email.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )

    return email.email
