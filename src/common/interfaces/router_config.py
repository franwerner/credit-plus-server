from typing import List, TypedDict
from fastapi import FastAPI


class RouterConfing(TypedDict):
    prefix: str
    tags: List[str]
    router: FastAPI
