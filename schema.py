from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id : Optional[int]
    username : str
    email : str
    password : str
    is_active : Optional[bool]
    is_staff : Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com.com",
                "password": "password",
                "is_active": True,
                "is_staff": False
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '27794c9bf148787969926fe54ddf41c27a7d634d5b1f4708f5d5ffe9cf0882f0'


class LoginModel(BaseModel):
    username : str
    password : str