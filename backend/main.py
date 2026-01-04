import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path

from llm.gemini_client import GeminiClient
from prompt_builder import PromptBuilder
from manim_runner import ManimRunner

load_dotenv()

app = FastAPI(
    title = "PIYX AI - Video Explanation Generator",
    description = "Generate educational video explanations from text prompts",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

videos_path = Path(__file__).parent / "generated" / "videos"
videos_path.mkdir(parents = True, exist_ok = True)
app.mount("/videos", StaticFiles(directory = str(videos_path)), name = "videos")

gemini_client = GeminiClient()
prompt_builder = PromptBuilder()
manim_runner = ManimRunner()

class VideoGenerationRequest(BaseModel):
    question: str
    duration : int = 60
    context: str = None

class VideoGenerationResponse(BaseModel):
    success: bool
    message: str
    scene_id: str = None
    video_url: str = None
    scene_file: str = None

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", response_model = HealthResponse)
async def root():
    return {
        "status": "online",
        "message": "PIYX AI API is running"
    }

@app.get("/health", response_model = HealthResponse)
async def health_check():
    return {
        "status": "healthy",
        "message": "All systems operational"
    }

@app.post("/generate-video", response_model = VideoGenerationResponse)
async def generate_video(request: VideoGenerationRequest):
    try:
        if not request.question or len(request.question.strip()) == 0:
            raise HTTPException(status_code = 400, detail = "Question cannot be empty")
        
        if request.duration < 10 or request.duration > 300:
            raise HTTPException(
                status_code = 400,
                detail = "Duration must be between 10 and 300 seconds"
            )
        
        if request.context:
            prompt = prompt_builder.build_prompt_with_context(
                request.question,
                request.context,
                request.duration
            )
        else:
            prompt = prompt_builder.build_prompt(request.question, request.duration)

        generated_code = gemini_client.generate_manim_code(prompt)
        
        result = manim_runner.generate_video(generated_code)

        video_url = f"/videos/{result['scene_id']}.mp4"

        return VideoGenerationResponse(
            success = True,
            message = "Video generated successfully",
            scene_id = result["scene_id"],
            video_url = video_url,
            scene_file = result["scene_file"]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Error generating video: { str(e)}"
        )
    
@app.get("/video/{scene_id}")
async def get_video(scene_id: str):
    video_path = videos_path / f"{scene_id}.mp4"

    if not video_path.exists():
        raise HTTPException(status_code = 404, detail = "Video not found")
    
    return FileResponse(
        video_path,
        media_type = "video/mp4",
        filename = f"{scene_id}.mp4"
    )

@app.get("/scenes/{scene_id}")
async def get_scene_code(scene_id: str):
    scene_path = Path(__file__).parent / "generated" / "scenes" / f"scene_{scene_id}.py"

    if not scene_path.exists():
        raise HTTPException(status_code = 404, detail = "Scene not found")
    
    with open(scene_path, 'r', encoding = 'utf-8') as f:
        code = f.read()

    return {"scene_id": scene_id, "code": code}

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
