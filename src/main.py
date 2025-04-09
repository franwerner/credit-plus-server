from fastapi import FastAPI
from src.routes.clients_routes import router as clients_router
from src.routes.providers_routes import router as providers_router

app = FastAPI()

app.include_router(clients_router)
app.include_router(providers_router)
