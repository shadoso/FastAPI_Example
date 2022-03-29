from Config.config import settings as env
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi import status as error
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from SQL.schemas import Role, TokenData


OAUTH_SCHEME = OAuth2PasswordBearer(tokenUrl="/ChimeraCore/login")


def generate_token(data: dict):
    # We make a copy to assure the data will be safe
    to_encrypt = data.copy()

    # How long the token will last
    expire = datetime.utcnow() + timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encrypt.update({"exp": expire})

    # Token
    jwt_token = jwt.encode(claims=to_encrypt, key=env.OATH_SECRET_KEY, algorithm=env.ALGORITHM)

    return jwt_token


def check_login_token(token: str, credentials_exception):
    try:

        info = jwt.decode(token=token, key=env.OATH_SECRET_KEY, algorithms=[env.ALGORITHM])

        uuid: str = info.get("uuid")
        status: bool = info.get("status")
        fullname: str = info.get("fullname")
        role: Role = info.get("role")

        if uuid is None or role is None or fullname is None:
            return credentials_exception

        token_data = TokenData(uuid=uuid, status=status, fullname=fullname, role=role)

    except JWTError:
        raise credentials_exception

    return token_data


def current_user(token: str = Depends(OAUTH_SCHEME)):
    credentials_exception = HTTPException(
        status_code=error.HTTP_401_UNAUTHORIZED,
        detail="Can't validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return check_login_token(token=token, credentials_exception=credentials_exception)
