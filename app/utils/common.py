from json import JSONEncoder
from pydantic import BaseModel
from typing import List


class CustomModel(BaseModel):
    class Config:
        orm_mode = True

class Encoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
    

class CustomException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

def divide_chunks(data, n):
    for i in range(0, len(data), n):
        yield data[i:i + n]


def modify_error_index(errors: List, chunk_size, index):
    key_to_modify_in_response = 'path'
    for i in range(len(errors)):
        if key_to_modify_in_response in errors[i]:
            path_index = int(errors[i][key_to_modify_in_response].split("[")[-1].split("]")[0])
            path_index += chunk_size*index
            path = 'body.domains[' + str(path_index) + ']'
            errors[i][key_to_modify_in_response] = path
    
    return errors
