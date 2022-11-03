from fastapi import APIRouter

from lms.settings import settings

router = APIRouter()


@router.get("/")
def read_root():
    return {
        "author": "@christhoval",
        "name": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
    }


@router.get("/health_check")
def health_check() -> str:
    return "ok"
