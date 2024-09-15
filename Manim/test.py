from manim import *

class WriteText(Scene):
    def construct(self):
        text = Text("This is a just a text")
        self.play(Write(text))
        self.wait(3)