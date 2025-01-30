import azure.functions as func
import logging
import datetime
from typing import Optional, Dict, Any

def main(msg: func.QueueMessage) -> None:
    message = msg.get_body().decode('utf-8')
    print(f"Queue trigger function processed message: {message}")
