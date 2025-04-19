from fastapi import FastAPI
from domain.provider.router import router as router_provider

routes = [
    router_provider
]


def create_routes(app: FastAPI):
    for route in routes:
        app.include_router(route)
