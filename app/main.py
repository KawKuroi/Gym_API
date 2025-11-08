from fastapi import FastAPI, Request
from app.core.config import settings
from app.core.logger import logger
import time

app = FastAPI(title=settings.APP_NAME,
              docs_url="/docs" if settings.DEBUG else None,
              redoc_url="/redoc" if settings.DEBUG else None,
              openapi_url="/openapi.json" if settings.DEBUG else None)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)

    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "status_code": response.status_code,
        "process_time": time.time() - start,
    }
    logger.info(log_dict)
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}