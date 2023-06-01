from typing import List, Optional, Dict
from app.utils.common import CustomModel


class DomainSchema(CustomModel):
    available: bool
    currency: Optional[str]
    definitive: bool
    domain: str
    period: Optional[int]
    price: Optional[int]


class ResponseSchema(CustomModel):
    domains: Optional[List[Dict]]
    errors: Optional[List[Dict]]
    code: Optional[str]
    fields: Optional[List[Dict]]
    message: Optional[str]
