from fastapi import FastAPI
from routes.clients import router as clients_router
from routes.providers.router import router as providers_router
from middleware.custom_error_handler import custom_error_handler
from middleware.verify_response import verify_response

app = FastAPI()
app.include_router(clients_router)
app.include_router(providers_router)
verify_response(app)
custom_error_handler(app)
