from fastapi import FastAPI, Query

app = FastAPI()

#numerical validation:
@app.get("/check-age")
def get_age(age: int = Query(..., ge=1, le=120)):
    if age >= 18:
        return {"Status": "Adult"}
    else:
        return {"Status": "Minor"}

#string validation:
@app.get("/search")
def get_query(query: str = Query(..., min_length=3, max_length=50)):
    return {"query": query}

#rating API
@app.get("/rate")
def rate(value: int = Query(..., ge=1, le=5)):
    return {"rating": value}

