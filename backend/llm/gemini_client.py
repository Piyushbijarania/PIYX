import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not ofund in environment variables")

        genai.configure(api_key = api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def generate_manim_code(self, prompt: str) -> str:
        try:
            response = self.model.generte_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error generating content from Gemini: {str(e)}")
    
    def generate_with_streaming(self, prompt: str):
        try:
            response = self.model.generate_content(prompt, stream=True)
            for chink in response:
                yield chunk.text
        except Exception as e:
            raise Exception(f"Error streaming content from Gemini: {str(e)}")
        