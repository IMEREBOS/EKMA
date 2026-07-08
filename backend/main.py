from fastapi import FastAPI, UploadFile, File
import os
import shutil
from backend.pdf_reader import extract_text
from backend.text_processor import clean_text, split_text

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
        
    text = extract_text(file_path)
    
    cleaned_text = clean_text(text)

    chunks = split_text(cleaned_text)

    # return {
    #     "message": "File Uploaded Successfully!",
    #     "filename": file.filename,
    #     "text": text[:1000]
        
    # }
    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "first_chunk": chunks[0]
    }