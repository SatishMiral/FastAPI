from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user

app = FastAPI()

# Whenever we find a new model, we need to create the tables in the database
models.Base.metadata.create_all(bind=engine)

# Include the routers in main.py
app.include_router(blog.router)
app.include_router(user.router)