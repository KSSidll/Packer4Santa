from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix='/package',
    tags=['package'],
)


class PackageBase(BaseModel):
    description: str | None = None


class PackageAdd(PackageBase):
    pass


class PackageUpdate(PackageAdd):
    pass


class Package(PackageUpdate):
    id: int

    class Config:
        orm_mode = True
