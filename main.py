from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("ml_model.pkl")

@app.get("/")
def root():
    return {"message": "AI Healthcare Tool API is running"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    predictions = model.predict(df)
    return {"predictions": predictions.tolist()}
