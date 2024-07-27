import logging
from fastapi import FastAPI
from app.middlewares import ErrorHandlerMiddleware
from app.views import router as views_router

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

app.add_middleware(ErrorHandlerMiddleware)
app.include_router(views_router, prefix="/auth")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up application")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application")
    
