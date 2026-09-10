from fastapi import FastAPI
from app.database import init_db
from contextlib import asynccontextmanager


# initialisation de la BDD au démarrage
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # tout ce qui est avant yield s'éxecute au démarrage, tout ce qui est après s'execute à l'arrêt de l'API


app = FastAPI(title="Demo postgre", lifespan=lifespan)
