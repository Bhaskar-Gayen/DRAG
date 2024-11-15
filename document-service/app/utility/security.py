from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from core.config import settings
from fastapi import Request

security = HTTPBearer()


def verify_jwt(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401, detail="Authorization token is missing")

    token = auth_header.split("Bearer ")[1]
    try:
        print(f"Token received: {token}")
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        print(f"Payload decoded: {payload}")
        return payload
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise HTTPException(status_code=401, detail="Invalid token")
