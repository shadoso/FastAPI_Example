from passlib.context import CryptContext

hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt(password: str):
    return hash_context.hash(password)


def decrypt(password: str, secret: str):
    return hash_context.verify(password, secret)
