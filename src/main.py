from fastapi import FastAPI

from common.custom_error_handler.create_error_handlers import create_error_handlers
from config.router import create_routes

app = FastAPI()
create_routes(app)
create_error_handlers(app)
