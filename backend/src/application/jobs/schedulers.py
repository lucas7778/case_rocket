from apscheduler.schedulers.asyncio import AsyncIOScheduler
from application.jobs.tasks.inserta_on_db import insertDataOnDb

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(insertDataOnDb, 'interval', seconds=30)  # Exemplo: rodar a cada 30 segundos
    scheduler.start()
