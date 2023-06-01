import os
import json
import base64
import requests
from . import schema
from app.utils.common import Encoder
from fastapi import APIRouter, Request

router = APIRouter(prefix="/moz", tags=["Moz"])

@router.post("")
async def metrics(request: Request, targets: schema.MozRequest):
    data_list = []
    url = 'https://lsapi.seomoz.com/v2/url_metrics'
    auth = base64.b64encode('{}:{}'.format(os.environ['NEXT_PUBLIC_MOZ_ACCESS_ID'], os.environ['NEXT_PUBLIC_MOZ_SECRET_KEY']).encode('utf-8')).decode()
    result = {'status': 200}
    headers = {'Authorization': 'Basic {}'.format(auth), 'Content-Type': 'application/json'}
    try:
        targets = json.loads(json.dumps(targets, cls=Encoder))
        response = requests.post(url, json=targets, headers=headers)
        data_list = response.json()['results']
    except Exception:
        result['status'] = 503
        result['message'] = "Connection failed"

    data = schema.IMozResponse(results=data_list).results
    result.update(results=json.loads(json.dumps(data, cls=Encoder)))

    return result