from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import gpt


app = FastAPI()

with open('./data.json') as f:
    data = json.load(f)




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel): # kế thừa từ class Basemodel và khai báo các biến
    name : str
    country : str

@app.get("/get")
async def read_user():
    return data

itema = []
@app.post("/items/")
async def create_item(item: Item): # khai báo dưới dạng parameter
    itema.append(item)
    return itema

@app.get("/showitems/")
async def read_user():
    return itema




class Gpt(BaseModel):
    input: str
reactinput= None
@app.post("/gpt/")
async def gptinput(input: Gpt):
    global reactinput
    reactinput = input.input  
    return reactinput





@app.get("/showgpt/")
async def read_input():
    global reactinput
    gpt.execute_data(reactinput)
    response_gpt = gpt.get_response()  # Lấy giá trị response từ tệp gpt.py
    return response_gpt