from fastapi import FastAPI
from .views import router as views_router

def create_app():
    app = FastAPI()
   
    app.include_router(views_router, prefix="/auth")

    return app
