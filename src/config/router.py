from fastapi import FastAPI
from domain.provider.router import router_provider
from common.interfaces.router_config import RouterConfing
from typing import List

routes: List[RouterConfing] = [
    router_provider
]


def create_routes(app: FastAPI) -> None:
    for route in routes:
        app.include_router(
            route.get("router"),
            tags=route.get("tags"),
            prefix=route.get("prefix"),
        )
