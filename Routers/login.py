from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from SQL.models import Users
from SQL.schemas import Token
from SQL.session import database
from sqlalchemy.orm import Session
from Utility import hashing, oauth2

router = APIRouter(
    prefix="/ChimeraCore",
    tags=["Login"]
)


@router.post("/login", response_model=Token)
async def login(
        credential: OAuth2PasswordRequestForm = Depends(),
        data: Session = Depends(database)
):
    # Query for an email in the database
    user_info = data.query(Users).filter(Users.username == credential.username).first()

    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )

    if not hashing.decrypt(credential.password, user_info.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )

    access_token = oauth2.generate_token(
        data={
            "uuid": user_info.uuid,
            "fullname": user_info.fullname,
            "role": user_info.role.value
        }
    )

    return {"access_token": access_token,
            "token_type": "bearer"}
