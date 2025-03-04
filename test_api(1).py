import uvicorn
import nest_asyncio
from fastapi import FastAPI
import pandas as pd
import os

# Allow Uvicorn to run inside Jupyter
nest_asyncio.apply()

# Initialize FastAPI
app = FastAPI()

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_path = os.path.join(BASE_DIR, "test.csv")

# Load CSV file
df = pd.read_csv(csv_path)

# Define a simple endpoint
@app.get("/")
def read_root():
    return {"message": "API is running!"}

# Define an endpoint to get data
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Run the API
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
