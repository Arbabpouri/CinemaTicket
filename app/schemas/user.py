from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    

class UserIn(UserBase):
    password: str
    password_confirm: str
    
    
class UserOut(UserBase):
    id: int
    
    class Config:
        orm_mode = True
