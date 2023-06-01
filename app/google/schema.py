from typing import List
from app.utils.common import CustomModel


class OrganicResultInterface(CustomModel):
    snippet: str
    title: str
    link: str


class GoogleSearchInterface(CustomModel):
    organic: List[List[OrganicResultInterface]]
