from fastapi import FastAPI,APIRouter,Response,HTTPException,status,Depends
from .. import models,schemas,database,oauth2
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/vote",
    tags=["votes"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:int=Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no such post found")
    vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    vote_found=vote_query.first()



    if (vote.dir==1):
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user.id} has alreday voted")
        else:
            new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
            db.add(new_vote)
            db.commit()
            db.refresh(new_vote)
            return {"vote succesfully addded"}
        
    else:
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No vote found to dete for this post ->{post.title}")    
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"sucessfully votes deleted"}
