# api/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import SessionLocal
from schemas.user import UserCreate, UserResponse, LoginRequest, TokenResponse
from services.user_service import create_user, get_user, get_user_by_username, get_user_by_email
from utility.hashing import verify_password
from utility.authentication import create_access_token
from core.dependencies import get_db

router = APIRouter(
    prefix="/api"
)

# Dependency to get DB session


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_200_OK)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(request: LoginRequest, db: Session = Depends(get_db)):

    db_user = get_user_by_username(
        db, request.username) or get_user_by_email(db, request.username)

    if db_user is None:
        raise HTTPException(
            status_code=400, detail="Invalid Username or Email")

    print(request.password, db_user.hashed_password)
    if not verify_password(request.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Wrong password!")

    access_token = create_access_token(data={"sub": db_user.username})

    return {
        "username": db_user.username,
        "email": db_user.email,
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout():

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "msg": "Successfully logged out. Please remove your token from local storage or cookies."}
    )
