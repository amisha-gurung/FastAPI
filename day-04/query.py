from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/check-age")
def get_age(age: int = Query(..., ge=1, le=120)):
    if age >= 18:
        return {"Status": "Adult"}
    else:
        return {"Status": "Minor"}
    