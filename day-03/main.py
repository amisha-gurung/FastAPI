#Basic Path Validation
from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()

class VehicleType(str, Enum):
    car = "car"
    bike = "bike"
    bus = "bus"

@app.get("/age/{age}")
def get_age(age: int = Path(..., ge=1, le=120)):
    return {"age": age}

@app.get("/product/{product_id}")
def get_prodid(product_id: int = Path(..., gt=1000, lt=9999)):
    return {"product id": product_id}

@app.get("/user/{username}")
def get_username(username: str = Path(..., min_length=4, max_length=12, regex="^[a-zA-Z]+$")):
    return {"Username": username}

@app.get("/country/{code}")
def get_code(code: str = Path(..., regex="^[A-Z]{2}$")):
    return {"code": code}

@app.get("/book/{book_id}")
def get_bookid(book_id: int = Path(..., ge=1, description="Book ID must be a positive integer used for identifying books.")):
    return {"book_id": book_id}

#a grouped validation
@app.get("/vehicle/{type}/{id}")
def get_info(type: VehicleType, id: int= Path(..., ge=100, le=999)):
    return {"type": type, "id": id}