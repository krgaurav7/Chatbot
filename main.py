from fastapi import FastAPI
import uvicorn
from src.routes.chat_route import router 
from contextlib import asynccontextmanager
from src.services.database_service import db_manager
from dotenv import load_dotenv
import os

load_dotenv(override=True)

@asynccontextmanager
async def lifespan(app : FastAPI):
    db_manager.initialize(connection_string=os.getenv("DB_URI"))
    print("Database Initialized")

    yield

    db_manager.close()
    print("Db connection closed")

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)