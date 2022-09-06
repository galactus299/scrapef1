from fastapi import FastAPI
from news import News
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def data():
    s = News()
    # data = json.dumps(s.items, indent=4)
    return s.items

