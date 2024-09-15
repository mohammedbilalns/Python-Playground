from manim import *

class Errors(Scene):
    def construct(self):
        
        ax = Axes(x_range=[-2,5], y_range=[-5,100],x_length=10)

        self.play(Create(ax))
    

        
       