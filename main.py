from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#static endpoint
@app.get("/hello")
def root():
    return {
        "name": "Ann",
        "age": 12,
        "country": "USA"
    }

#dynamic endpoint with path parameter
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"the requested information {user_id}"
    }
    
#multiple path parameter
@app.get("/product/{product_id}/review/{review_id}")
def get_mul(product_id: int, review_id: int):
    return{
        "product_id" : f"This is product id {product_id}",
        "review_id": f"This is review id {review_id}"
    }
  
#query parameters  
@app.get("/products")
def desc(prod_id: int, prod_name: str):
    return {
        "prod_id": prod_id,
        "prod_name": prod_name,
        "message": f"The product id is {prod_id} and the product name is {prod_name}"
    }

#using optional     
@app.get("/search")
def searchh(query: str, limit: Optional[int] = 11):
    return {
        "search_query": query,
        "limit": limit,
        "message": f"Searching for '{query}' with limit {limit}"
    }

#combining path and query parameters
@app.get("/user/{id}/post")
def get_user_info(id: int, label: str,lim: Optional[int] = None):
    return{
        "id": id,
        "label": label,
        "limit": lim,
        "message": f"The id is: {id}, The lable is {label}, the limit is {lim}"
    }