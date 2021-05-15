from manim import *
class Logo(Scene):
    def construct(self):
        circle = Circle(color=RED).shift(LEFT)
        triangle = Triangle(color=GREEN).shift(UP)
        square = Square(color=BLUE).shift(RIGHT)
        text = Text("fayth.sketches",font = "Open Sans Condensed Light Italic").scale(2.5)
        self.play(Create(circle))
        self.play(ReplacementTransform(circle.copy(),triangle))
        self.play(ReplacementTransform(triangle.copy(),square))
        self.play(Write(text))