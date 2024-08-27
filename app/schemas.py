from pydantic import BaseModel

class Image(BaseModel):
    id: int
    url: str

    class Config:
        orm_mode = True

class VoteCreate(BaseModel):
    image_id: int
    user_vote: bool

    class Config:
        orm_mode = True