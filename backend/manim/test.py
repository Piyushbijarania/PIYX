from manim import *

class Test(Scene):
    def construct(self):
        text = Text("Hello PIYXsdfgfdggdsgfdsgdgDS")
        self.play(Write(text))
        self.wait(2)
