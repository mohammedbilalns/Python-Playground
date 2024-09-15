from manim import *

class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5,stroke_color= GREEN, fill_color = BLUE , fill_opacity = 100)

        self.play(Create(sq), run_time = 3) #run square for 3 seconds
        self.wait(3) #wait 3 seconds after square 
        
