from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    print("Startup: Database tables created")
    yield
    print("Shutdown: Application is closing")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello Worldd"}
