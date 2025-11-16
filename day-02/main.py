from fastapi import FastAPI, HTTPException
from database import Human
from typing import Optional

app = FastAPI()

humans = [
    Human(name="Zen", age=19, home="Middle East", study="Bachelors undergrad", salary=45598.6532),
    Human(name="Zayn", age=21, home="West Coast", study="CS Major", salary=70000.59258)
]

@app.get("/humans")
def get_all_human():
    return humans

@app.get("/humans/{names}", response_model=Human)
def user_info(names: str):
    for human in humans:
        if human.name == names:
            return human
    raise HTTPException(status_code=404,  detail=f"no humans named {names}")