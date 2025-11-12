from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

db = { "Amisha": {"age":22, "home":"Boston", "study":"Bachelors", "salary":450000.3657 },
    "Suraj": {"age":19, "home":"Honolulu", "study":"Bachelors", "salary":450000.3657}
}

@app.get("/user")
def get_info(name: Optional[str] = None):
    if name is None:
        return db
    elif name not in db:
        raise HTTPException(status_code=404, detail="User not found")    
    return db[name]
    
