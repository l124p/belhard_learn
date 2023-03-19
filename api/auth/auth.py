from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from jose import jwt, JWTError

from core.models import User
from core.schemas import UserInfo, RegisterForm, LoginForm, TokenSchema
from core.settings import SECRET_KEY, EXPIRE_JWT_TOKEN, ALGORITHM, TOKEN_TYPE

router = APIRouter()


@router.post('/register', response_model=UserInfo, response_model_exclude={'password', 'hashed_password', 'pk'},
             status_code=status.HTTP_201_CREATED
             )
async def register_user(register_form: RegisterForm):
    user_info = UserInfo(**register_form.dict())
    user = User(**user_info.dict(exclude={'pk', 'password'}))
    try:
        await user.save()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='email or user not unique')
    else:
        return user_info


@router.post(
    '/login', response_model=TokenSchema
)
async def login(login_form: LoginForm):
    user = await User.select(
        User.email == login_form.email
    )
    if user:
        user = user[0]
        try:
            user_info = UserInfo(**login_form.dict() | {
                'hashed_password': user.hashed_password,
                'username': user.username
            }
                                 )
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='incorect password')
        else:
            data = {
                'sub': user_info.username,
                'exp': datetime.utcnow() + timedelta(minutes=EXPIRE_JWT_TOKEN)
            }
            token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
            return TokenSchema(access_token=token, token_type=TOKEN_TYPE)
         #   return TokenSchema(access_token=token, token_type=TOKEN_TYPE)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
