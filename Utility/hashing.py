from passlib.context import CryptContext

hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed(password: str):
    return hash_context.hash(password)


def verify(password, hashs):
    return hash_context.verify(password, hashs)
