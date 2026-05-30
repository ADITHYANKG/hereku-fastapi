#1 get all users

from fastapi import APIRouter,status,HTTPException,Response,Depends
import time
from typing import Optional,List
from random import randrange
from ..database import engine,get_db
from ..import schemas
from ..import models
from sqlalchemy.orm import Session
from  ..utils import hash



router=APIRouter(
    prefix="/users",
    tags=['Users']
)



# get all users
@router.get("/",response_model=List[schemas.UserResponse])
def get_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    # print(posts)
    return users


# 2 get one single user
@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    return user

#3 create a user
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_users(user:schemas.UserCreate,db:Session=Depends(get_db)):
    ##hash the password- user.password
    print(user.password)
    print(len(user.password.encode("utf-8")))
    
    
    hashed_password=hash(user.password)
    # if not verify(user.password,hashed_password):
    #     raise HTTPException(status_code=403, detail="Invalid credentials")
    user.password=hashed_password
    
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#4 delete user
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id)
    if user.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id :{id} does not found")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#update user
@router.put("/{id}",response_model=schemas.UserResponse)
def update_user(id:int ,updated_user:schemas.UserUpdate,db:Session=Depends(get_db)):
    user_query=db.query(models.User).filter(models.User.id==id)
    user=user_query.first()

    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with {id} does not exists")
    user_query.update(updated_user.dict(),synchronize_session=False)
    db.commit()
    return user_query.first()