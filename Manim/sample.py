from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle(radius=2.5, color=GREEN)


        self.play(Create(circle))


