from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic import conint




class PostBase(BaseModel):
    title:str 
    content:str
    published:bool= True # default is True
    
class PostCreate(PostBase):
    title:str 
    content:str
    published:bool= True # default is True
    
class PostUpdate(PostBase):
    title:str 
    content:str
    published:bool=True

class UserBase(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode=True      




class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)
    

class PostResponse(PostBase):
    id:int
    created_at:datetime
    user_id:int
    owner:UserResponse
    
    class Config:
        orm_mode=True

class PostVoteResponse(BaseModel):
    Post:PostResponse
    votes:int
    class Config:
        orm_mode=True





class UserCreate(UserBase):
    email:EmailStr
    password:str    
    
class UserUpdate(UserBase):
    email:EmailStr
    password:str        
    


class UserLogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[int]=None


