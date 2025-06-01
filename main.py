from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

class DownloadRequest(BaseModel):
    url: str

@app.post("/download")
def download_video(request: DownloadRequest):
    url = request.url
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    try:
        result = subprocess.run([
            "yt-dlp", url, "-o", f"{output_dir}/%(title)s.%(ext)s"
        ], capture_output=True, text=True, check=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)
