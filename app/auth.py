from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from app import config
from app.models.jwt import *
from app.config import Settings, get_settings


# auth scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=get_settings().api_jwt_login_url)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    settings: Settings = Depends(get_settings),
):
    # generate exteption to re-use
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    # verify user credentials
    try:
        payload = jwt.decode(token, settings.api_secret_key, algorithms=[settings.api_jwt_algorithm])
        username: str = payload.get('sub')
        user_id: str = payload.get('user_id')
        if username is None or user_id is None:
            raise credentials_exception
        
        return JWTokenData(username=username, user_id=user_id)
    except JWTError:
        raise credentials_exception
    
    # finally (this part of the code should be unreachable)
    raise credentials_exception
