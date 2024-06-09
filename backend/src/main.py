from fastapi import FastAPI
from .application.controllers.pokemon_controller import app
from core import Routes
from .application.jobs.schedulers import start_scheduler

app = FastAPI()

app.include_router(app, prefix=Routes.QUERY)
