from fastapi import FastAPI
from routes.clients import router as clients_router
from routes.providers import router as providers_router

app = FastAPI()
app.include_router(clients_router)
app.include_router(providers_router)
