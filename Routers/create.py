from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException, status
from SQL import models
from SQL import schemas
from SQL.models import Exchange, Role
from SQL.session import database
from sqlalchemy.orm import Session
from Utility.hashing import encrypt
from Utility.many_checks import valid_name, valid_pass

PAYMENT_TYPE = {
    Role.student: Exchange.tuition,
    Role.guest: Exchange.lecture,
    Role.admin: Exchange.salary,
    Role.coordinator: Exchange.salary,
    Role.teacher: Exchange.salary,
    Role.staff: Exchange.salary,
}
DETAIL = 1

router = APIRouter(
    prefix="/ChimeraCore",
    tags=["Create"]
)


@router.post("/create/{role}",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser
             )
async def create_user(
        post: schemas.CreateUser,
        role: Role,
        data: Session = Depends(database)
):
    usr_name = valid_name(post.name, post.surname)
    usr_pass = valid_pass(post.password)

    if "Successful" not in usr_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=usr_name[DETAIL]
        )

    if "Successful" not in usr_pass:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=usr_pass[DETAIL]
        )

    post.name = usr_name[0]["Name"]
    post.surname = usr_name[0]["Surname"]
    post.password = encrypt(post.password)

    new_user = models.Users(
        **post.dict(),
        role=role,
        fullname=usr_name[0]["Fullname"]
    )

    new_user.context.append(models.Monetary(
        category=PAYMENT_TYPE[role],
        payment=0.00,
        status=False
    ))
    data.add(new_user)
    data.commit()
    data.refresh(new_user)

    return new_user
