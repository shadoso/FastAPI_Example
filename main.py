from fastapi import FastAPI
from Routers import show, post, access
from SQL.session import Base, engine


PATH = [show, post, access]
COLLEGE_EMAIL = "@ChimeraCore.com"

Base.metadata.create_all(bind=engine)
app = FastAPI()

for rout in PATH:
    app.include_router(router=rout.router)


# @app.get("/ChimeraCore/show/all/{role}")
# async def show_users(data: Session = Depends(database),
#                      role: Role = str
#                      ):
#     user = role
#
#     if user == Role.student:
#         student = data.query(models.Student).filter_by(role=user).all()
#         return {f"{user.value}s": student}
#
#     if user in EMPLOYEE:
#         employee = data.query(models.Employee).filter_by(role=user).all()
#         return {f"{user.value}s": employee}
#
#     if user == Role.guest:
#         guest = data.query(models.Guest).filter_by(role=user).all()
#         return {f"{user.value}s": guest}
#
#
# @app.post("/ChimeraCore/create/{role}")
# async def create_user(post: schemas.Post, role: Role,
#                       code: str = str(uuid4())[::5],
#                       data: Session = Depends(database)
#                       ):
#     hashed = hashing.hashed(code)
#     code = hashed
#     unique = str(uuid4())[11::5]
#     college_email = post.name + role.value + unique + COLLEGE_EMAIL
#     user = role
#
#     if user == Role.student:
#         student = models.Student(**post.dict(), email=college_email, password=code, role=user)
#
#         data.add(student)
#         data.commit()
#         data.refresh(student)
#
#         return {f"{user.value}": student.email}
#
#     if user in EMPLOYEE:
#         employee = models.Employee(**post.dict(), email=college_email, password=code, role=user)
#
#         data.add(employee)
#         data.commit()
#         data.refresh(employee)
#
#         return {f"{user.value}": employee.email}
#
#     if user == Role.guest:
#         guest = models.Guest(**post.dict(), email=college_email, password=code, role=user)
#
#         data.add(guest)
#         data.commit()
#         data.refresh(guest)
#
#         return {f"{user.value}": guest.email}
#

# @app.delete("/ChimeraCore/delete/{role}/{user_uuid}")
# async def delete_user(data: Session = Depends(database),
#                       role: Role = str,
#                       user_uuid: UUID = str):
#     pass
