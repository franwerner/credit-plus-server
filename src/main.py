from fastapi import FastAPI
from config.router import create_routes
from middleware.custom_error_handler import custom_error_handler
from middleware.all_excepction_handler import all_excepction_handler

app = FastAPI()
create_routes(app)
custom_error_handler(app)
all_excepction_handler(app)
