import os 
import subprocess
import uuid
from pathlib import Path
from typing import Tuple

class ManimRunner:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.scenes_dir = self.base_dir / "generated" / "scenes"
        self.videos_dir = self.base_dir / "generated" / "videos"

        self.scenes_dir.mkdir(parents=True, exist_ok=True)
        self.videos_dir.mkdir(parents=True, exist_ok=True)

        self.quality = os.getenv("MANIM_QUALITY", "medium_quality")
    
    def clean_generated_code(self, code: str) -> str:
        if code.startswith("```python"):
            code = code[9:]
        elif code.startswith("```"):
            code = code[3:]  # Remove ```
        
        if code.endswith("```"):
            code = code[:-3]  # Remove trailing ```
        
        return code.strip()
    
    def save_scene(self, code: str, scene_id: str = None) -> Tuple[str, Path]:
        if not scene_id:
            scene_id = str(uuid.uuid4())

        clean_code = self.clean_generated_code(code)

        file_path = self.scenes_dir / f"scene_{scene_id}.py"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_code)

        return scene_id, file_path
    
    def run_manim(self, scene_file: Path, scene_id: str) -> Path:
        try:
            cmd = [ 
                "manim",
                f"-q{self._get_quality_flag()}",
                str(scene_file),
                "GeneratedScene",
                "-o", f"{scene_id}.mp4"
            ]

            result = subprocess.run(
                cmd,
                cwd=str(self.base_dir),
                capture_output=True,
                text=True,
                timeout=300
            )

            if reult.returncode != 0:
                raise Exception(f"Manim execution failed: {result.stderr}")
            
            video_path = self._find_video_file(scene_id)

            if not video_path:
                raise Exception("Video filenot found after rendering")
            return video_path
        
        except subprocess.TimeoutExpired:
            raise Exception("Manim rendering timed out (max 5 minutes)")
        except Exception as e:
            raise Exception(f"Error running Manim: {str(e)}")
        
    def _get_quality_flag(self) -> str:
        quality_map = {
            "low_quality": "l",
            "medium_quality": "m",
            "high_quality": "h",
            "production_quality": "k"
        }
        return quality_map.get(self.quality, "m")
    
    def _find_video_file(self, scene_id: str) -> Path:
        media_dir = self.base_dir / "media" / "videos" / "scenes"

        for quality_dir in media_dir.glob("*"):
            if quality_dir.is_dir():
                video_file = quality_dir / f"{scene_id}.mp4"
                if video_file.exists():
                    target_path = self.videos_dir / f"{scene_id}.mp4"
                    import shutil
                    shutil.copy2(video_file, target_path)
                    return target_path
        return None
    
    def generate_video(self, code: str, scene_id: str = None) -> dict:
        scene_id, scene_file = self.save_scene(code, scene_file, scene_id)

        video_path = self.run_manim(scene_file, scene_id)
        return {
            "scene_id" : scene_id,
            "scene_file": str(scene_file),
            "video_path": str(video_path)
        }