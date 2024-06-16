from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from run_pipeline import run_pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def schedule_pipeline():
    scheduler = BlockingScheduler()

    # Schedule the pipeline to run daily at midnight
    trigger = CronTrigger(hour=0, minute=0)

    scheduler.add_job(run_pipeline, trigger)

    logging.info("Pipeline scheduling started. Pipeline will run daily at midnight.")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == "__main__":
    schedule_pipeline()
