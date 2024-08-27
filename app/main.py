from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from sqlalchemy.orm import Session
import models, schemas, database
import random

PICTURES_FOLDER = Path("../Pictures")
database.init_db()

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/images/random", response_model=schemas.Image)
def get_random_image(db: Session = Depends(get_db)):
    
    # Get all images from the database
    images = db.query(models.Image).all()
    
    # If no images are found, return an error
    if not images:
        raise HTTPException(status_code=404, detail="No images found")

    # Select a random image
    random_image = random.choice(images)
    return random_image


@app.post("/vote", response_model = schemas.VoteCreate)
async def create_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db)):

    # Check if photo exists in images
    image_exists = db.query(models.Image).filter_by(id=vote.image_id).first()
    if not image_exists:
        raise HTTPException(status_code=404, detail="Image not found")

    # If it does, then add vote to a database
    new_vote = models.Vote(
        image_id = vote.image_id,
        user_vote = vote.user_vote
    )

    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return vote

