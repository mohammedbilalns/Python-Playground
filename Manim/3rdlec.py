from manim import *

class Testing(Scene):
    def construct(self):

        name = Tex("$\Sigma_{n=0}^{\infty} a_n$").to_edge(UL) #shows name on the upper left edge
        sq = Square(side_length=0.5, fill_color = RED , fill_opacity = 0.75).shift(LEFT*2) #Square on the 2 points left of the centre with fill color red
        tri = Triangle().scale(0.6).to_edge(DR) # Triangle with scale 0.6 on the down right edge



        self.play(Write(name, run_time =3)) #write name with runtime 3
        self.play(DrawBorderThenFill(sq), run_time = 2) #Draw border and fill the square for 2 sec
        self.play(Create(tri)) #Create triangle 
        self.wait(100) #wait 

        self.play(name.animate.to_edge(UR), run_time = 2) #animate name into upper right edge for 2 seconds 
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time =3 ) #animate square to scale and triangle to move to down right 
        self.wait()

