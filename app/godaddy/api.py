import os
import json
import requests
from typing import List
from . import schema
from app.utils.common import divide_chunks, Encoder, modify_error_index
from fastapi import APIRouter, Request


router = APIRouter(prefix="/godaddy", tags=["Godaddy"])

# , response_model=schema.ResponseSchema, response_model_exclude_none=True
@router.post("")
async def domains(request: Request, data: List[str]):
    domain_list = []
    error_list = []
    misc_list = []
    status_code_set = set()
    url = 'https://api.godaddy.com/v1/domains/available?checkType=FAST'
    result = {'status': ''}
    headers = {"Content-Type": "application/json", 'Authorization': 'sso-key {}:{}'.format(os.environ["NEXT_PUBLIC_GODADDY_KEY"], os.environ["NEXT_PUBLIC_GODADDY_SECRET"])}
    try:
        chunk_size = 500
        data_chunks = list(divide_chunks(data, chunk_size))
        for i in range(len(data_chunks)):
            chunk = data_chunks[i]
            response = requests.post(url, json=chunk, headers=headers)
            status_code = response.status_code
            response = response.json()
            print(response)
            if status_code == 203 and response['domains'] is None and response['errors'] != []:
                status_code = 422
            status_code_set.add(status_code)
            domains = errors = []
            if 'domains' in response and response['domains'] != None:
                domains = response['domains']
            if 'errors' in response and response['errors'] != None:
                errors = modify_error_index(response['errors'], chunk_size, i)
            if (domains == [] or domains is None) and errors == [] and misc_list == []:
                misc_list.extend(response)
            
            domain_list.extend(domains)
            error_list.extend(errors)
    except Exception:
        result['status'] = 503
        result['message'] = "Connection failed"

    if (domain_list == [] or domains is None) and error_list == []:
        data = schema.ResponseSchema(**misc_list[0])
        result.update(misc=json.loads(json.dumps(data, cls=Encoder)))
    elif error_list == []:
        data = schema.ResponseSchema(domains=domain_list).domains
        result.update(domains=json.loads(json.dumps(data, cls=Encoder)))
    elif domain_list == []:
        data = schema.ResponseSchema(errors=error_list).errors
        result.update(errors=json.loads(json.dumps(data, cls=Encoder)))
    else:
        data = schema.ResponseSchema(domains=domain_list, errors=error_list)
        result.update(domains=json.loads(json.dumps(data.domains, cls=Encoder)))
        result.update(errors=json.loads(json.dumps(data.errors, cls=Encoder)))

    status_code_list = list(status_code_set)
    if len(status_code_list) == 1:
        result['status'] = status_code_list[0]
    elif status_code_list != []:
        result['status'] = status_code_list

    return result
