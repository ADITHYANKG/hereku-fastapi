from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
app = FastAPI()


class Post(BaseModel):
    title:str 
    content:str
    published:bool= True # default is True


while True:

    try:
        conn=psycopg2.connect(host="localhost",database='fastapi',user='postgres',password='Admin123',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connecting to database failed ")
        print("Error was ",error)
        time.sleep(2)



#0 root end point
@app.get("/") # decorator
def root(): #function
    return { "message": "Hello ! Adithyan"}

#1 get all post
@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM POSTS""")
    posts=cursor.fetchall()
    # print(posts)
    return {"posts":posts}





# 2 get one single post
@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id))) 
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
    return {"post details":post}


#3 create a post
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"post":new_post}




# 4 delete a post
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE from posts WHERE id = %s returning *""",(str(id)))
    post=cursor.fetchone()
    conn.commit()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} does not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#update post
@app.put("/posts/{id}")
def update_post(id:int ,post:Post):
    cursor.execute("""UPDATE posts set title= %s , content= %s ,published =%s where id= %s  returning *""",(post.title,post.content,post.published,str(id)))
    updated_post=cursor.fetchone()
    conn.commit()
    if updated_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} does not exists")
    
    return {"post updated" :updated_post}

#4:16 video 