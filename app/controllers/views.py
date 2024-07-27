from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_active_user_role
from app.models import Token, User, UserInDB
from app.db import fake_users_db, get_password_hash

router = APIRouter()

@router.post("/register/", response_model=UserInDB)
async def register_user(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(username=user.username, hashed_password=hashed_password, role="user")
    fake_users_db[user.username] = user_in_db
    return user_in_db

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/admin/")
async def read_admin_data(current_user_role: str = Depends(get_current_active_user_role)):
    if current_user_role != "admin":
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return {"message": "This is an admin endpoint"}
