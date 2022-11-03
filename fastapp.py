from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from chat import get_response


class Item(BaseModel):
    message: str
    
app = FastAPI()


@app.post("/items/")
async def predict(item: Item):
    response = get_response(item.message)
    return { "message":response }


