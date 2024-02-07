from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.routes import root
from src.logs import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Server started. See docs on {app.docs_url}")
    yield
    logger.info(f"Server stopped")


app = FastAPI(lifespan=lifespan)
app.include_router(router=root)
