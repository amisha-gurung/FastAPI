from fastapi import FastAPI
from database import Human

app = FastAPI()

humans = [
    Human(name="Zen", age=19, home="Middle East", study="Bachelors undergrad", salary=45598.6532),
    Human(name="Zayn", age=21, home="West Coast", study="CS Major", salary=70000.59258)
]

@app.get("/humans")
def user_info():
    return humans