from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta
from .tasks.inserta_on_db import insertDataOnDb

def start_scheduler():
    scheduler = AsyncIOScheduler()
    run_time = datetime.now() + timedelta(seconds=10)  

    scheduler.add_job(insertDataOnDb, DateTrigger(run_date=run_time)) 
    scheduler.start()