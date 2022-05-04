from fastapi import FastAPI, File, UploadFile, HTTPException
from ocr import image_to_string

app = FastAPI()

app = FastAPI(title="OCR Image to Text", docs_url="/docs")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
  try:
    image = await image_to_string(file)
  except:
    raise HTTPException(
                status_code=422, detail="Unable to process file")
  return image
