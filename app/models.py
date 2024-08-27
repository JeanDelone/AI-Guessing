from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Image(Base):
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    is_ai_generated = Column(Boolean)
    prompt = Column(String)
    model = Column(Integer)
    cry_count = Column(Integer)
    laugh_count = Column(Integer)
    like_count = Column(Integer)
    heart_count = Column(Integer)
    comment_count = Column(Integer)
    size = Column(String)
    steps = Column(Integer)
    sampler = Column(String)
    cfg_scale = Column(Float)
    negative_prompt = Column(String)
    nsfw_level = Column(String)

    votes = relationship("Vote", back_populates = "image")

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key = True, index = True)
    image_id = Column(Integer, ForeignKey("images.id"))
    user_vote = Column(Boolean, index = True)
    
    image = relationship("Image", back_populates = "votes")