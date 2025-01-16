import logging
import time
import azure.functions as func
import uuid
import json

import azure.functions as func


app = func.FunctionApp()

@app.route(route="AddSubtitle", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
@app.table_output(
    arg_name="table",
    connection="AzureWebJobsStorage",
    table_name="AcmeTranslations",
    partition_key=""
)
def HttpEndpoint(req: func.HttpRequest, table: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    subtitle = req_body.get("subtitle")

    rowKey = str(uuid.uuid4())

    data = {
        "Name": "Output binding message",
        "PartitionKey": "message",
        "RowKey": rowKey,
        "Subtitle": subtitle
    }

    table.set(json.dumps(data))
    return func.HttpResponse(
        f"Message created with the rowKey: {rowKey} Translation is: {subtitle}",
        status_code=200
    )