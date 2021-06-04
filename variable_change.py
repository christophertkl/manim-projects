from manim import *

class variableChange(Scene):
    def createAnimatedTitle(self,text):
        title = Tex(text)
        self.play(Write(title))
        self.play(title.animate.scale(0.5))
        self.play(title.animate.shift(3 * UP + 4.5 * LEFT))

    def construct(self):
        self.createAnimatedTitle("Illustration of moving variables")

        # LateX object need not be broken into their individual elements 
        first = MathTex("y*t=2\\cdot x\\times i^{2 \\relax}")
        second = MathTex("\\frac{1}{2}y*t= x\\times i^{3 \\relax}")

        self.play(Write(first))
        self.play(*[
            # Transform all common parts to their new locations in equation b
            Transform(
                first.get_part_by_tex(tex),
                second.get_part_by_tex(tex),
            )
            for tex in ("y", "*t", "=", "x","\\times","i")
        ] + [
            # Transform the different parts
            Transform(
                first.get_part_by_tex(texPair[0]),
                second.get_part_by_tex(texPair[1]),
            )
            for texPair in [["2\\cdot","\\frac{1}{2}"],["2 \\relax","3 \\relax"]]
        ])
        self.wait(2)