from app.main import create_app
import os

config_name = os.getenv('ENV', 'dev')
app = create_app(config_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
