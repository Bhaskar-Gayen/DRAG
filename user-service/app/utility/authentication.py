from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from core.config import settings


# Create access token
def create_access_token(data: dict, expires_in: timedelta = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_in
    to_encode.update({"exp": expire})  # Set expiration time
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

# Decode access token and get the payload


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY,
                             algorithms=[settings.JWT_ALGORITHM])
        return payload if payload["exp"] >= datetime.now(timezone.utc) else None
    except JWTError:
        return None
