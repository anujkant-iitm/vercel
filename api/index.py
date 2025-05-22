from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open(os.path.join(os.path.dirname(__file__), "../students.json")) as f:
    students_data = json.load(f)

# Create a lookup dictionary
marks_dict = {entry["name"]: entry["marks"] for entry in students_data}

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [marks_dict.get(name, None) for name in names]
    return JSONResponse(content={"marks": marks})
