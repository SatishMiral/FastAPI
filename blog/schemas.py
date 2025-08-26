from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    # body: str

    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True