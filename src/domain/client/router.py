from fastapi import APIRouter

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get("/{client_id}")
async def get(client_id: int):
    return "fdfd"


@router.get("/")
async def gets():
    return "fdfd"


@router.post("/")
async def post():
    return "fdfd"


@router.delete("/{client_id}")
async def post():
    return "fdfd"


@router.patch("/{client_id}")
async def patch():
    return "fdfd"
