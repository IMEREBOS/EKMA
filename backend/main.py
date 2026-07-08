from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI(
    title="Enterprise Knowledge Management Assistant",
    version="1.0"
)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Backend is Running Successfully!"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File Uploaded Successfully!",
        "filename": file.filename
    }