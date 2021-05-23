from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm

from crud import create_user
from jwt import Token, authenticate_user, create_access_token, get_current_active_user, get_admin_active_user
from models import User
from schemas import UserCreateSerializer, UserSerializer, AdminUserCreateSerializer
from settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_ADMIN_KEY

app = FastAPI()


@app.get("/profile/")
async def profile(current_user: User = Depends(get_current_active_user)):
    return {'result': UserCreateSerializer(
        email=current_user.email,
        password=current_user.hashed_password,
        age=current_user.age,
        first_name=current_user.first_name,
        patronymic=current_user.patronymic,
        surname=current_user.surname,
    )}


@app.get("/user/profile_info/{user_id}/")
async def profile_id(user_id: int, current_user: User = Depends(get_current_active_user)):
    user = User.get_user_by_id(user_id)
    return {'result': UserSerializer.from_orm(user)}


@app.get("/admin_secret_key/")
async def admin_secret_key(current_user: User = Depends(get_admin_active_user)):
    return {'result': {
        'secret_admin_key': SECRET_ADMIN_KEY
    }}


@app.post("/create-admin/")
async def create_admin(data: AdminUserCreateSerializer):
    user = create_user(user=data, is_admin=True)
    return {'result': UserSerializer.from_orm(user)}


@app.post("/register/")
async def register(data: UserCreateSerializer):
    user = create_user(user=data, is_admin=False)
    return {'result': UserSerializer.from_orm(user)}


@app.post("/login/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
