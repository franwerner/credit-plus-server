from fastapi import APIRouter

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/")
def create_client():
    return {"mensaje": "Cliente creado correctamente"}
