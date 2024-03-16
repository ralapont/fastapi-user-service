from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@cosasdedevs.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyTypicalUsername"
    )


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Rafael"
    )
    lastname: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Alapont"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        example="strongpass"
    )
    activo: Optional[bool]  = Field(
        default=True,
        example="true"
    )    
    phone: Optional[str] = Field(
        default=None,
        max_length=9,
        example="910876543"
    )
    address: Optional[str] = Field(
        default=None,
        max_length=250,
        example="c/Eduardo Requenas, 10, 3ºE"
    )

