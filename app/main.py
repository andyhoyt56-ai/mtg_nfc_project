from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os, uuid, shutil

app = FastAPI(title="MTG NFC Scanner API")

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "MTG NFC Scanner backend - healthy"}

@app.post("/api/identify")
async def identify_card(file: UploadFile = File(...)):
    """
    Temporary endpoint: saves the uploaded image and returns a filename.
    We'll replace body with OCR/image-matching later.
    """
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    fname = f"{uuid.uuid4().hex}{ext}"
    dest = os.path.join(UPLOAD_DIR, fname)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"status": "saved", "file": fname}
