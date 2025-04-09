from fastapi import APIRouter

router = APIRouter(prefix="/providers", tags=["providers"])


@router.get("/")
def create_provider():
    return {"mensaje": "Proveedor creado correctamente"}
