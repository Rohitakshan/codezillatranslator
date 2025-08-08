from fastapi import FastAPI
from pydantic import BaseModel
from translator import translate_text

app = FastAPI()

class TranslateRequest(BaseModel):
    input_text: str
    target_language: str
    style: str
    tone: str

@app.post("/translate")
async def translate(req: TranslateRequest):
    result = translate_text(
        input_text=req.input_text,
        target_language=req.target_language,
        style=req.style,
        tone=req.tone
    )
    return {"translated_text": result}

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("frontend", "index.html"))


