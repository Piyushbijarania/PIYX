class PromptBuilder:
    
    def __init__(self):
        self.system_prompt = """You are an expert at creating educational video animations using Manim (Mathematical Animation Engine).

Your task is to generate complete, runnable Python code using Manim that explains the given concept visually.

CRITICAL RULES:
1. Always create a class that inherits from Scene
2. The class name must be "GeneratedScene"
3. Put all animation logic inside the construct() method
4. Use clear, educational animations that explain concepts step by step
5. Add text explanations using Text() objects
6. Use self.play() for animations and self.wait() for pauses
7. Return ONLY the Python code, no explanations before or after
8. Do not include markdown code blocks (no ```python```)
9. Make animations smooth and easy to understand

AVAILABLE MANIM OBJECTS:
- Text()
- Circle(), Square(), Rectangle(), Line(), Arrow() for shapes
- VGroup() to group objects
- Write(), Create(), FadeIn(), FadeOut(), Transform() for animations
- UP, DOWN, LEFT, RIGHT for positioning

EXAMPLE OUTPUT:
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        formula = MathTex("a^2 + b^2 = c^2")
        self.play(Write(formula))
        self.wait(2)
"""
    
    def build_prompt(self, user_question: str, duration: int = 60) -> str:
        user_prompt = f"""
Generate a Manim animation that explains the following topic:

TOPIC: {user_question}

TARGET DURATION: Approximately {duration} seconds of animation

Remember:
- Class name must be "GeneratedScene"
- Use self.play() and self.wait() to control timing
- Add visual elements that make the concept clear
- Include text explanations
- Make it educational and engaging
- Return ONLY the Python code, nothing else

Generate the code now:
"""
        
        # Combine system and user prompts
        full_prompt = self.system_prompt + user_prompt
        return full_prompt
    
    def build_prompt_with_context(self, user_question: str, 
                                  context: str = None, 
                                  duration: int = 60) -> str:
        context_section = ""
        if context:
            context_section = f"""
ADDITIONAL CONTEXT:
{context}

Use this context to make your explanation more accurate and detailed.
"""
        
        user_prompt = f"""
Generate a Manim animation that explains the following topic:

TOPIC: {user_question}
{context_section}
TARGET DURATION: Approximately {duration} seconds of animation

Remember:
- Class name must be "GeneratedScene"
- Use self.play() and self.wait() to control timing
- Add visual elements that make the concept clear
- Include text explanations
- Make it educational and engaging
- Return ONLY the Python code, nothing else

Generate the code now:
"""
        
        full_prompt = self.system_prompt + user_prompt
        return full_prompt