class PromptBuilder:
    
    def __init__(self):
        self.system_prompt = """You are an expert at creating SIMPLE educational video animations using Manim.

CRITICAL RULES:
1. ALWAYS start with: from manim import *
2. Class name MUST be "GeneratedScene" inheriting from Scene
3. Keep animations EXTREMELY SIMPLE - only use basic features
4. Return ONLY Python code, no explanations, no markdown blocks

ALLOWED FEATURES ONLY:
- Text() for all text (font_size parameter to adjust size)
- Circle(), Square(), Rectangle(), Dot(), Line(), Arrow() for shapes
- Write(), Create(), FadeIn(), FadeOut() for animations
- self.play() and self.wait()
- .scale(), .shift(), .move_to(), .next_to() for positioning
- UP, DOWN, LEFT, RIGHT, ORIGIN
- Colors ONLY: RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE, GRAY, PINK
- DO NOT use color variants like RED_A, BLUE_B, ORANGE_C - ONLY use base colors listed above

FORBIDDEN - DO NOT USE:
- MathTex, Tex (use Text instead)
- Rotate animations
- get_point_at_angle or any curve methods
- rate_func, LINEAR, EASE_IN, etc.
- Complex orbital animations
- Updater functions
- ValueTracker or any tracking

KEEP IT SIMPLE EXAMPLE:
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("Pythagorean Theorem", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Formula
        formula = Text("a² + b² = c²", font_size=36)
        self.play(FadeIn(formula))
        self.wait(2)
        
        # Simple shape
        square = Square(color=BLUE).shift(DOWN)
        self.play(Create(square))
        self.wait(1)
        
        # Label
        label = Text("Right Triangle", font_size=24).next_to(square, UP)
        self.play(Write(label))
        self.wait(2)
        
        # Cleanup
        self.play(FadeOut(formula), FadeOut(square), FadeOut(label))
        self.wait(1)

IMPORTANT: Keep explanations simple with text, basic shapes, and fade/write animations only!
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