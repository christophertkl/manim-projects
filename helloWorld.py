from manim import *

class SquareToCircle(Scene):

    # All animations must be contained within the definition of construct
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()
        square.flip(RIGHT)


        # Sequence of animations
        self.play(Create(square))
        self.play(Rotate(square,PI))
        self.wait(1)
        self.play(Transform(square,circle))
        self.play(FadeOut(square))

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        # To create the image at the start
        # self.add(numberplane, dot, arrow, origin_text, tip_text)

        self.play(Create(numberplane))
        self.wait(1)
        self.play(Create(dot))
        self.play(Create(origin_text))
        self.wait(1)
        self.play(Create(arrow))
        self.play(Create(tip_text))

amp = 5
mu = 3
sig = 1

def gaussian(x):
    return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2))

class GaussianFunctionPlot(GraphScene):
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(gaussian, x_min=-1, x_max=10)
        graph.set_stroke(width=5)
        self.add(graph)