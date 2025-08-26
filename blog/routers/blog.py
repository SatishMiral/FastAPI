# This file contains all the routes for the blog 

from typing import List
from fastapi import APIRouter, Depends
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

# Get all blogs
@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

# Create a blog
@router.post("/", tags=["blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

# Get a blog with id
@router.get("/{id}", response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.show(id, db)

# Update a blog with id
@router.put("/{id}")
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

# Delete a blog with id
@router.delete("/{id}")
def destroy(id, db: Session = Depends(get_db)):
    return blog.destroy(id, db)
