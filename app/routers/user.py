from fastapi import APIRouter, Depends, Path, Query, status
from sqlalchemy.orm import Session
from schemas import user as UserSchemas
from utils.dependencies import get_db


router = APIRouter()

@router.post('/api/v1/users/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchemas.UserIn, db: Session = Depends(get_db)):
    
    return user
