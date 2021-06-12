from datetime import timedelta

from fastapi import Depends, HTTPException, status, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from crud import create_user, get_user
from jwt import Token, authenticate_user, create_access_token, get_current_active_user
from models import User
from schemas import UserCreateSerializer, UserSerializer, LoginRequest
from settings import ACCESS_TOKEN_EXPIRE_MINUTES, ADMIN_DATA, USER_DATA

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    if not get_user(username=ADMIN_DATA.get('username')):
        create_user(UserCreateSerializer(**ADMIN_DATA), is_admin=True)
    if not get_user(username=USER_DATA.get('username')):
        create_user(UserCreateSerializer(**USER_DATA), is_admin=False)


@app.get("/profile/")
async def profile(current_user: User = Depends(get_current_active_user)):
    return {'res': UserCreateSerializer(
        username=current_user.username,
        password=current_user.hashed_password,
        address=current_user.address,
        first_name=current_user.first_name,
        patronymic=current_user.patronymic,
        surname=current_user.surname,
    )}


@app.get("/{username}/")
async def profile_id(username: str, current_user: User = Depends(get_current_active_user)):
    user = User.get_user_by_username(username)
    if user:
        data = UserSerializer.from_orm(user)
    else:
        data = {}
    return {'res': data}


@app.post("/sign-in/")
async def register(data: UserCreateSerializer):
    user = create_user(user=data, is_admin=False)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "jwt_access_token": access_token,
        "token_type": "bearer",
        "user_data": UserSerializer.from_orm(user)
    }


@app.post("/login/", response_model=Token)
async def login_for_access_token(data: LoginRequest):
    def raise_auth_error(msg, error_status):
        raise HTTPException(
            status_code=error_status,
            detail=msg,
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not data.username or not data.password:
        raise_auth_error('Укажите имя-пользователя и пароль!', status.HTTP_400_BAD_REQUEST)
    user = authenticate_user(data.username, data.password)
    if not user:
        raise_auth_error('Неверное имя пользователя или пароль', status.HTTP_401_UNAUTHORIZED)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"jwt_access_token": access_token, "token_type": "bearer"}
