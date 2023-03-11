from pydantic import BaseModel, Field, EmailStr, validator, ValidationError, IntegerError
from hw_6_1 import *


class StatusAdd(BaseModel):
    id: int = Field(gt=1)
    name: str = Field(max_length=10)

    @validator('name')
    def validate_email(cls, value):
        obj = Statuses()
        data = []
        res = obj.select()
        for row in res:
            data.append(row.dict().get('name'))

        if value in data:
            raise ValueError('name is not unique')
        return value


class UserAdd(BaseModel):
    # id: int = Field(gt=1)
    name: str = Field(max_length=24)
    email: EmailStr

    @validator('name')
    def name_must_contain_space(cls, value):
        if ' ' in value:
            raise ValueError('must contain a space')
        return value.title()

    @validator('name')
    def username_alpha(cls, value):
        assert value.isalpha(), 'must be alpha'
        return value

    @validator('email', pre=True)
    def validate_email(cls, value):
        obj = Users()
        data = []
        res = obj.select()
        for row in res:
            data.append(row.dict().get('email'))

        if value in data:
            raise ValueError('email is not unique')
        return value


class CategoryAdd(BaseModel):
    # id: int = Field(gt=1)
    name: str = Field(max_length=24)

    @validator('name')
    def validate_email(cls, value):
        obj = Categories()
        data = []
        res = obj.select()
        for row in res:
            data.append(row.dict().get('name'))

        if value in data:
            raise ValueError('name is not unique')
        return value


class ProductAdd(BaseModel):
    # id: int = Field(gt=1)
    title: str = Field(max_length=36)
    description: str = Field(max_length=36)
