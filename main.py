from fastapi import FastAPI
from news import News
import json
app = FastAPI()

@app.get("/data")
def data():
    s = News()
    # data = json.dumps(s.items, indent=4)
    return s.items

