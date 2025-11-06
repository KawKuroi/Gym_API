from fastapi import FastAPI
from app.config import config

app = FastAPI(title=config.APP_NAME,
              docs_url="/docs" if config.DEBUG else None,
              redoc_url="/redoc" if config.DEBUG else None)


@app.get("/")
async def root():
    return {"message": "Hello World"}
