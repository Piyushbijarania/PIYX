import os 
import subprocess
import uuid
from pathlib import Path
from typing import Tuple
import time

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
        
        # Validate the code before saving
        self.validate_python_code(clean_code)

        file_path = self.scenes_dir / f"scene_{scene_id}.py"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_code)

        return scene_id, file_path
    
    def run_manim(self, scene_file: Path, scene_id: str) -> Path:
        max_retries = 2
        
        for attempt in range(max_retries):
            try:
                cmd = [ 
                    "manim",
                    f"-q{self._get_quality_flag()}",
                    str(scene_file),
                    "GeneratedScene",
                    "-o", f"{scene_id}.mp4"
                ]

                # Run the command
                result = subprocess.run(
                    cmd,
                    cwd=str(self.base_dir),
                    capture_output=True,
                    text=True,
                    timeout=600
                )

                # Small delay to let Manim finish writing files
                time.sleep(2)
                
                # Check for video file regardless of return code
                video_path = self._find_video_file(scene_id)
                
                if video_path:
                    return video_path
                
                # If first attempt failed and no video, retry
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                
                # Final attempt - raise error
                if result.returncode != 0:
                    error_msg = result.stderr if result.stderr else result.stdout
                    raise Exception(f"Manim failed. Error: {error_msg[-500:]}")
                
                raise Exception("Video file not found after rendering")
            
            except subprocess.TimeoutExpired:
                video_path = self._find_video_file(scene_id)
                if video_path:
                    return video_path
                if attempt < max_retries - 1:
                    continue
                raise Exception("Manim rendering timed out")
            
            except Exception as e:
                # On any error, try to find the video file first
                video_path = self._find_video_file(scene_id)
                if video_path:
                    return video_path
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                raise Exception(f"Error running Manim: {str(e)}")
        
        raise Exception("Failed to generate video after retries")
    
    def _get_quality_flag(self) -> str:
        quality_map = {
            "low_quality": "l",
            "medium_quality": "m",
            "high_quality": "h",
            "production_quality": "k"
        }
        return quality_map.get(self.quality, "m")
    
    def _find_video_file(self, scene_id: str) -> Path:
        """
        Find the generated video file in Manim's output directory.
        
        Args:
            scene_id: The scene ID to search for
            
        Returns:
            Path to the video file
        """
        # Manim default output structure: media/videos/<filename>/<quality>/
        media_dir = self.base_dir / "media" / "videos"
        
        # Search recursively for the video file
        if media_dir.exists():
            for video_file in media_dir.rglob(f"{scene_id}.mp4"):
                # Copy to our videos directory
                target_path = self.videos_dir / f"{scene_id}.mp4"
                import shutil
                shutil.copy2(video_file, target_path)
                return target_path
        
        # If not found, check if it was created in the base directory
        direct_path = self.base_dir / f"{scene_id}.mp4"
        if direct_path.exists():
            target_path = self.videos_dir / f"{scene_id}.mp4"
            import shutil
            shutil.copy2(direct_path, target_path)
            return target_path
        
        return None
    
    def generate_video(self, code: str, scene_id: str = None) -> dict:
        scene_id, scene_file = self.save_scene(code, scene_id)

        video_path = self.run_manim(scene_file, scene_id)
        return {
            "scene_id" : scene_id,
            "scene_file": str(scene_file),
            "video_path": str(video_path)
        }
    
    def validate_python_code(self, code: str) -> bool:
        """
        Check if the generated Python code has syntax errors.
        
        Args:
            code: Python code to validate
            
        Returns:
            True if valid, raises exception if invalid
        """
        try:
            compile(code, '<string>', 'exec')
            return True
        except SyntaxError as e:
            raise Exception(f"Generated code has syntax error: {str(e)}")
