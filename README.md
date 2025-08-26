source :- Bitfumes on Youtube
link :- https://youtu.be/7t2alSnE2-I?si=ojDTXq_I4PpJk33e

## What is FastAPI?

FastAPI is a modern, high-performance Python web framework for building APIs — especially when speed and developer experience matter.

- Extremely fast (built on ASGI and Starlette)
- Built-in data validation using Python type hints (via Pydantic)
- Automatic Swagger UI and ReDoc for API testing
- Supports async for handling thousands of concurrent requests

## Installing FastAPI and Uvicorn
pip install fastapi
pip install uvicorn
Uvicorn is a lightning-fast ASGI(Asynchronous Server Gateway Interface) server used to run FastAPI apps. 
It supports asynchronous execution and is lightweight, making it ideal for both development and production.

## Steps to create & activate venv 
python -m venv fastapienv
-fastapienv is the name of virtual environment

fastapienv\Scripts\activate
-activate fastapienv like above

## Run Script
uvicorn blog.main:app --reload
