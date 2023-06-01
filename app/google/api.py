import os
import json
import requests
from . import schema
from typing import List
from app.utils.common import Encoder
from pydantic import Json
from fastapi import APIRouter, Request
from langchain.utilities import GoogleSerperAPIWrapper


router = APIRouter(prefix="/google", tags=["Google"])


@router.post("/news")
async def news(request: Request, query: str):
    result = {'status': 200}
    # query = json.loads(data)
    params = {'type': 'news', 'tbm': 'nws', 'location': 'Dallas', 'serper_api_key': os.environ['NEXT_PUBLIC_GOOGLE_NEWS_API']}
    
    try:
        search = GoogleSerperAPIWrapper(**params)
        response = search.results(query)
        result['news'] = response['news']
    
    except Exception:
        result['status'] = 400
        result['message'] = "Cannot fetch google news"

    return result


@router.post("/search")
async def search(request: Request, query: List[str]):
    data = json.loads(json.dumps([{'q': q} for q in query]))
    # data = json.loads(data)
    result = {'status': 200, 'result': []}
    url = 'https://google.serper.dev/search'
    headers = {'X-API-KEY': os.environ['NEXT_PUBLIC_GOOGLE_NEWS_API'], 'Content-Type': 'application/json'}
    # try:
    response = requests.post(url, json=data, headers=headers).json()
    result['result'] = response
    # except Exception:
        # result['status'] = 503
        # result['message'] = "Connection failed"

    return result
