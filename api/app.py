from fastapi import FastAPI

import api.elf as elf
import api.package as package
from api.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(elf.router)
app.include_router(package.router)
