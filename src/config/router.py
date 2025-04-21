from fastapi import FastAPI
from domain.provider.router import router as router_provider
from domain.client.router import router as router_client

routes = [
    router_provider,
    router_client
]


def create_routes(app: FastAPI):
    for route in routes:
        app.include_router(route)
