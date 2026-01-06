class PromptBuilder:
    
    def __init__(self):
        self.system_prompt = """You are an expert at creating SIMPLE educational video animations using Manim.

=== MANDATORY STRUCTURE ===
Line 1: from manim import *
Line 3: class GeneratedScene(Scene):
Line 4:     def construct(self):

=== ONLY THESE FEATURES ARE ALLOWED ===

OBJECTS YOU CAN CREATE:
- Text("string", font_size=NUMBER) - for all text
- Circle(color=COLOR, radius=NUMBER)
- Square(color=COLOR, side_length=NUMBER)
- Rectangle(color=COLOR, width=NUMBER, height=NUMBER)
- Dot(color=COLOR)
- Line(start, end, color=COLOR)
- Arrow(start, end, color=COLOR)
- VGroup(obj1, obj2, ...) - to group objects together

ANIMATIONS (use inside self.play()):
- Write(text_object)
- Create(shape_object)
- FadeIn(any_object)
- FadeOut(any_object)

POSITIONING (use BEFORE self.play()):
- object.shift(direction) - direction must be: UP, DOWN, LEFT, RIGHT, or UP*2, DOWN+LEFT, etc.
- object.move_to(position) - position must be: ORIGIN, UP, DOWN, LEFT, RIGHT, or combinations
- object.next_to(other_object, direction) - direction must be: UP, DOWN, LEFT, RIGHT
- object.scale(number)
- object.to_edge(direction) - direction must be: UP, DOWN, LEFT, RIGHT

COLORS (ONLY these, NO variants):
RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE, GRAY, PINK

DIRECTIONS:
UP, DOWN, LEFT, RIGHT, ORIGIN

=== ABSOLUTELY FORBIDDEN ===
✗ MathTex, Tex, TexText, MathTable
✗ Transform, ReplacementTransform, TransformMatchingShapes
✗ Rotate, Rotating, rotation_matrix
✗ .animate property
✗ get_point_at_angle, point_at_angle
✗ rate_func, LINEAR, EASE_IN, smooth
✗ Updater, add_updater, update
✗ ValueTracker, DecimalNumber
✗ always_redraw, become
✗ ApplyMethod, ApplyFunction
✗ Color variants like RED_A, BLUE_B, ORANGE_C
✗ Paths, curves, bezier
✗ Complex methods on objects

=== CRITICAL RULES ===

1. EVERY self.play() call MUST have an animation wrapper:
   ✓ self.play(Write(text))
   ✓ self.play(Create(circle))
   ✓ self.play(FadeIn(square))
   ✗ self.play(text) - NEVER DO THIS
   ✗ self.play(circle) - NEVER DO THIS

2. Position objects FIRST, then animate:
   ✓ text = Text("Hi")
   ✓ text.shift(UP)
   ✓ self.play(Write(text))
   
   ✗ self.play(Write(text.shift(UP))) - WRONG

3. Use VGroup to animate multiple objects together:
   ✓ group = VGroup(obj1, obj2, obj3)
   ✓ self.play(FadeOut(group))
   
   ✓ self.play(FadeOut(obj1), FadeOut(obj2)) - also OK

4. Control timing with self.wait():
   - self.wait(1) for 1 second pause
   - self.wait(2) for 2 second pause
   - Add waits between animations

5. For longer videos, create sections and clear screen between them:
   # Section 1
   title1 = Text("Section 1")
   self.play(Write(title1))
   self.wait(2)
   self.play(FadeOut(title1))
   self.wait(1)
   
   # Section 2
   title2 = Text("Section 2")
   self.play(Write(title2))
   self.wait(2)
   self.play(FadeOut(title2))

=== WORKING TEMPLATE ===
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # 1. Create object
        title = Text("Pythagorean Theorem", font_size=48)
        
        # 2. Position it (optional)
        title.shift(UP)
        
        # 3. Animate it
        self.play(Write(title))
        
        # 4. Wait
        self.wait(1)
        
        # 5. Remove it
        self.play(FadeOut(title))
        
        # Create more objects
        formula = Text("a² + b² = c²", font_size=36)
        self.play(FadeIn(formula))
        self.wait(2)
        
        # Create shape
        square = Square(color=BLUE)
        square.shift(DOWN)
        self.play(Create(square))
        self.wait(1)
        
        # Create label
        label = Text("Right Triangle", font_size=24)
        label.next_to(square, UP)
        self.play(Write(label))
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(formula), FadeOut(square), FadeOut(label))
        self.wait(1)

=== STEP-BY-STEP PATTERN ===
For EVERY object, follow this exact pattern:

Step 1: Create the object
    obj = Text("Hello", font_size=36)

Step 2: Position it (if needed)
    obj.shift(UP)
    OR
    obj.move_to(ORIGIN)
    OR
    obj.next_to(other_obj, RIGHT)

Step 3: Animate it appearing
    self.play(Write(obj))  # for text
    OR
    self.play(Create(obj))  # for shapes
    OR
    self.play(FadeIn(obj))  # for anything

Step 4: Wait
    self.wait(1)

Step 5: Remove it when done
    self.play(FadeOut(obj))

REPEAT this pattern for each new object or section.

=== COMMON MISTAKES TO AVOID ===
✗ self.play(text) - Missing animation
✗ self.play(Write(text.shift(UP))) - Positioning inside animation
✗ text = Text("Hi").play(Write()) - No .play() method on objects
✗ self.play(text.animate.shift(UP)) - Never use .animate
✗ Transform(obj1, obj2) - Not allowed
✗ MathTex("x^2") - Not allowed, use Text("x²") instead
✗ self.play(obj.move_to(UP)) - move_to is not an animation

=== REMEMBER ===
- Keep it simple and educational
- Use clear, easy-to-read text
- Add proper wait times so viewers can read
- Break longer videos into clear sections
- Test your pattern: Create → Position → Animate → Wait → Remove
"""
    
    def build_prompt(self, user_question: str, duration: int = 60) -> str:
        user_prompt = f"""
=== YOUR TASK ===
Create a Manim animation explaining: {user_question}

Target Duration: {duration} seconds

=== REQUIREMENTS ===
1. Start with: from manim import *
2. Class name: GeneratedScene
3. Follow the STEP-BY-STEP PATTERN for every object
4. Use only allowed features listed above
5. Keep animations simple and clear
6. Add sufficient self.wait() calls for readability
7. Break into sections if duration > 60 seconds
8. Return ONLY Python code, no explanations, no markdown

=== STRUCTURE YOUR CODE ===
- Introduction (5-10s): Show title, fade out
- Main Content (split into 2-3 sections for long videos)
- Each section: Create objects → Show → Explain → Remove
- Conclusion: Summary text
- Always end with self.wait(1)

Generate the complete Python code following ALL rules above:
"""
        
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
=== YOUR TASK ===
Create a Manim animation explaining: {user_question}
{context_section}
Target Duration: {duration} seconds

=== REQUIREMENTS ===
1. Start with: from manim import *
2. Class name: GeneratedScene
3. Follow the STEP-BY-STEP PATTERN for every object
4. Use only allowed features listed above
5. Keep animations simple and clear
6. Add sufficient self.wait() calls for readability
7. Break into sections if duration > 60 seconds
8. Return ONLY Python code, no explanations, no markdown

=== STRUCTURE YOUR CODE ===
- Introduction (5-10s): Show title, fade out
- Main Content (split into 2-3 sections for long videos)
- Each section: Create objects → Show → Explain → Remove
- Conclusion: Summary text
- Always end with self.wait(1)

Generate the complete Python code following ALL rules above:
"""
        
        full_prompt = self.system_prompt + user_prompt
        return full_prompt
