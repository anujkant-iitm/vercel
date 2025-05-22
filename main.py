from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data into a dictionary
with open("data.json", "r") as f:
    data = json.load(f)

# Convert list of dicts to name: marks dict
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_dict.get(name, None) for name in names]
    return {"marks": result}
