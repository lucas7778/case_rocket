from fastapi import FastAPI
from application.controllers.pokemon_controller import router as pokemon_router
from application.jobs.schedulers import start_scheduler
from contextlib import asynccontextmanager
from infra.data.model.model import init_db
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    start_scheduler()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(pokemon_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
