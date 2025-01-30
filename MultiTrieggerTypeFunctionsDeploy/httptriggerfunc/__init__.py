import azure.functions as func
import json
import logging
import datetime
from typing import Optional, Dict, Any

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        return func.HttpResponse(json.dumps({"message": f"Hello, {name}!"}), mimetype="application/json")
    else:
        return func.HttpResponse(
            json.dumps({"error": "Please pass a name in the query string or in the request body 000000000"}),
            status_code=400,
            mimetype="application/json"
        )
