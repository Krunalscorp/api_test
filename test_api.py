import uvicorn
from fastapi import FastAPI
import pandas as pd
import os

# Initialize FastAPI
app = FastAPI()

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_path = os.path.join(BASE_DIR, "test.csv")

# Load CSV file
df = pd.read_csv(csv_path)

@app.get("/")
def read_root():
    return {"message": "API is running on Render!"}

@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Run the API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
