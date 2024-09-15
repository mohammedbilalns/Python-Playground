from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(GREEN, opacity=0.7)


        square = Square()
        square.set_fill(GREEN, opacity=0.7)



        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))