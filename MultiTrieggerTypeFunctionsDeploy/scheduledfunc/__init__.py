import datetime
import azure.functions as func
import logging
import datetime
from typing import Optional, Dict, Any

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().isoformat()
    if mytimer.past_due:
        print("The scheduled function is running late!")
    print(f"Scheduled function ran at {utc_timestamp}")
