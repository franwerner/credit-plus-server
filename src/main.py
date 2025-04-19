from fastapi import FastAPI
from config.router import create_routes
from middleware.custom_error_handler import custom_error_handler
from middleware.verify_response import verify_response

app = FastAPI()
create_routes(app)
verify_response(app)
custom_error_handler(app)
