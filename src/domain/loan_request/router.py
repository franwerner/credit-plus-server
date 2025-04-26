from fastapi import APIRouter

router = APIRouter(prefix="/loan_request", tags=["loan request"])


@router.get("/")
def get():
    return ""
