from fastapi import APIRouter, Depends
from src.schemas import User
from src.services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/me", response_model=User, responses={401: {"description": "Unauthorized"}}
)
async def me(user: User = Depends(get_current_user)):
    return user
