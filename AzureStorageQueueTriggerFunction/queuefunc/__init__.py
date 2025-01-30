import azure.functions as func
import logging
from azure.data.tables import TableServiceClient
from azure.identity import DefaultAzureCredential
import datetime
import json

def main(msg: func.QueueMessage) -> None:
    logging.info("Queue trigger function started.")
    message = msg.get_body().decode('utf-8')
    logging.info(f"Queue trigger function processed message: {message}")
    
    try:
        # Parse the message
        data = json.loads(message)
        row_key = data.get("row_key", str(datetime.datetime.utcnow().timestamp()))
        partition_key = data.get("partition_key", "default_partition")
        additional_data = data.get("data", {})
        
        # Use Managed Identity to authenticate
        credential = DefaultAzureCredential()
        table_service_client = TableServiceClient(
            endpoint="https://costoptimizationsas.table.core.windows.net",
            credential=credential
        )
        
        # Access the table
        table_client = table_service_client.get_table_client("testtabledemo")
        
        # Insert data into the table
        entity = {
            "PartitionKey": partition_key,
            "RowKey": row_key,
            **additional_data
        }
        table_client.create_entity(entity)
        logging.info(f"Entity inserted: {entity}")
    except Exception as e:
        logging.error(f"Error processing queue message: {e}")
