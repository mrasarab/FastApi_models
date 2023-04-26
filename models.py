from pydantic import BaseModel,HttpUrl,EmailStr
from typing import Union,List,Set
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import Body

class Image(BaseModel):
    url:HttpUrl
    name:str


class Item(BaseModel):
    item_id: UUID
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]

class time_read(BaseModel):
    item_id: UUID
    start_datetime: Union[datetime, None] = Body(default=None)
    end_datetime: Union[datetime, None] = Body(default=None)
    repeat_at: Union[time, None] = Body(default=None)
    process_after: Union[timedelta, None] = Body(default=None)


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
