from fastapi import Depends
from fastapi import HTTPException, status
from fastapi import APIRouter
from Utility import hashing
from uuid import uuid4
from SQL import schemas
from SQL.session import database
from SQL import models
from SQL.models import Role, Payment
from sqlalchemy.orm import Session

PAYMENT_TYPE = {
    Role.student: Payment.tuition,
    Role.guest: Payment.lecture
}

router = APIRouter(
    prefix="/ChimeraCore",
    tags=["Create"]
)

COLLEGE_EMAIL = "@ChimeraCore.com"


@router.post("/create/{role}",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser
             )
async def create_user(
        post: schemas.Post,
        role: Role,
        data: Session = Depends(database)
):
    hashed = hashing.encrypt("test123")
    fullname = post.name + post.surname
    unique = str(uuid4())[11::5]
    college_email = post.name + role.value + unique + COLLEGE_EMAIL

    new_user = models.Users(
        **post.dict(),
        fullname=fullname,
        role=role,
        email=college_email,
        password=hashed
    )

    data.add(new_user)
    data.commit()
    data.refresh(new_user)

    return new_user
