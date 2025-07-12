from jose import JWTError, jwt
from datetime import datetime, timedelta
from config.env import Env

SECRET_KEY = Env.SECRET_KEY
ALGORITHM = Env.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = Env.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        print("Token decoding failed", e)
        return None
