from fastapi import FastAPI
from .views import router as views_router
from config import config_by_name

def create_app(config_name='dev'):
    app = FastAPI()

    # Configuración de la aplicación
    app.config = config_by_name[config_name]

    # Registrar los routers
    app.include_router(views_router, prefix="/auth")

    return app
