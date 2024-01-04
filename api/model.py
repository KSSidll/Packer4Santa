from pydantic import BaseModel


class PackageBase(BaseModel):
    description: str | None = None


class Package(PackageBase):
    id: int

    class Config:
        orm_mode = True


class PackageAdd(PackageBase):
    pass
