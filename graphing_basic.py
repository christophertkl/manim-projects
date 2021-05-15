from manim import *

class CustomGraphScene(GraphScene):
    def createAnimatedTitle(self,text):
        title = Tex(text)
        self.play(Write(title))
        self.play(title.animate.scale(0.5))
        self.play(title.animate.shift(3 * UP + 4.5 * LEFT))

    def autoAnimate(self,graphs,graphLabels,points,pointLabels):
        self.play(Create(graphs[0]),Create(points[0]),Create(pointLabels[0]), run_time=1.5)
        self.play(Write(graphLabels[0]))
        for idx in range(len(graphs) - 1):
            self.wait(1)
            self.play(Transform(graphLabels[idx],graphLabels[idx + 1]))
            self.play(Transform(graphs[idx],graphs[idx + 1]))
            self.play(Transform(points[idx],points[idx + 1]),Transform(pointLabels[idx],pointLabels[idx + 1]))
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

AxesParams = {
    "x_min": -12,
    "x_max": 12,
    "y_min": -22,
    "y_max": 22,
    "graph_origin":[0,0,0.0],
    "include_tip": True,
    "y_axis_height": 6,
    "y_axis_config":{"tick_frequency": 50},
    "x_axis_config":{"tick_frequency": 50}, 
}
class TranslationX(CustomGraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        self.createAnimatedTitle("Translation parallel to the x-axis")
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: 1-x+ 0.5 * x**2, x_min = -6, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(2,1))
        pointLabel1 = MathTex('A(2,1)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: 1-(x+2)+ 0.5 * (x+2)**2, x_min = -8, x_max = 6)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=f(x+2)")
        point2 = Dot().move_to(self.coords_to_point(0,1))
        pointLabel2 = MathTex('A\'(0,1)').next_to(point2,RIGHT)

        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])
        # self.play(Create(func_graph),Create(point1),Create(pointLabel1), run_time=1.5)
        # self.play(Write(graphLabel1))
        # self.wait(1)
        # self.play(Transform(graphLabel1,graphLabel2))
        # self.play(Transform(func_graph,func_graph2))
        # self.play(Transform(point1,point2),Transform(pointLabel1,pointLabel2))
        # self.wait(2)
        # self.play(
        #     *[FadeOut(mob) for mob in self.mobjects]
        # )

class TranslationY(CustomGraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        self.createAnimatedTitle("Translation parallel to the y-axis")
    
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: 1-x+ 0.5 * x**2, x_min = -6, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(2,1))
        pointLabel1 = MathTex('A(2,1)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: 1-(x)+ 0.5 * (x)**2-3, x_min = -6, x_max = 8)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=f(x)-3")
        point2 = Dot().move_to(self.coords_to_point(2,-2))
        pointLabel2 = MathTex('A\'(2,-2)').next_to(point2,RIGHT)


        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])


class ScalingX(CustomGraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        self.createAnimatedTitle("Scaling parallel to the x-axis")
    
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: 1-x+ 0.5 * x**2, x_min = -6, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(2,1))
        pointLabel1 = MathTex('A(2,1)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: 1-2*x+ 0.5 * (2*x)**2, x_min = -3, x_max = 5)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=f(2x)")
        point2 = Dot().move_to(self.coords_to_point(1,1))
        pointLabel2 = MathTex('A\'(1,1)').next_to(point2,RIGHT)


        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class ScalingY(CustomGraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        # title = Text("Translation parallel to the y-axis")
        # self.play(Write(title))
        # self.play(title.animate.scale(0.3))
        # self.play(title.animate.shift(3 * UP + 4 * LEFT))
        self.createAnimatedTitle("Scaling parallel to the y-axis")
    
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: 1-x+ 0.5 * x**2, x_min = -6, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(2,1))
        pointLabel1 = MathTex('A(2,1)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: 0.5 * (1-x+ 0.5 * x**2), x_min = -6, x_max = 8)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=0.5f(x)")
        point2 = Dot().move_to(self.coords_to_point(2,0.5))
        pointLabel2 = MathTex('A\'(2,0.5)').next_to(point2,RIGHT)


        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class ModY(CustomGraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        # title = Text("Translation parallel to the y-axis")
        # self.play(Write(title))
        # self.play(title.animate.scale(0.3))
        # self.play(title.animate.shift(3 * UP + 4 * LEFT))
        self.createAnimatedTitle(r"Modulus transformation $|f(x)|$")
    
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: x + 2, x_min = -8, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(-4,-2))
        pointLabel1 = MathTex('A(-4,-2)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: np.abs(x + 2), x_min = -8, x_max = 8)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=|f(x)|")
        point2 = Dot().move_to(self.coords_to_point(-4,2))
        pointLabel2 = MathTex('A\'(-4,2)').next_to(point2,RIGHT)


        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class ModX(CustomGraphScene):
   
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )


    def construct(self):
        # title = Text("Translation parallel to the y-axis")
        # self.play(Write(title))
        # self.play(title.animate.scale(0.3))
        # self.play(title.animate.shift(3 * UP + 4 * LEFT))
        self.createAnimatedTitle(r"Modulus transformation $f(|x|)$")
    
        self.setup_axes(animate=True)

        func_graph = self.get_graph(lambda x: x + 2, x_min = -8, x_max = 8)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(-4,-2))
        pointLabel1 = MathTex('A(-4,-2)').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: np.abs(x) + 2, x_min = -8, x_max = 8)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=f(|x|)")
        point2 = Dot().move_to(self.coords_to_point(-4,6))
        pointLabel2 = MathTex('A\'(-4,6)').next_to(point2,RIGHT)

        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class ReflectionY(CustomGraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )
    def construct(self):
        def f(x):
            return x ** 2
        
        self.createAnimatedTitle(r"Reflection about the $x$-axis")
    
        self.setup_axes(animate=True)
        
        func_graph = self.get_graph(lambda x: f(x+1), x_min = -6, x_max = 6)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(-4,f(-4+1)))
        pointLabel1 = MathTex(f'A(-4,{f(-4+1)})').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: -f(x+1), x_min = -6, x_max = 6)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=-f(x)")
        point2 = Dot().move_to(self.coords_to_point(-4,-f(-4+1)))
        pointLabel2 = MathTex(f'A\'(-4,{-f(-4+1)})').next_to(point2,RIGHT)

        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class ReflectionX(CustomGraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )
    def construct(self):
        def f(x):
            return (x+1) ** 2
        
        self.createAnimatedTitle(r"Reflection about the $y$-axis")
    
        self.setup_axes(animate=True)
        
        func_graph = self.get_graph(lambda x: f(x), x_min = -6, x_max = 6)
        graphLabel1 = self.get_graph_label(func_graph,label = "y=f(x)")
        point1 = Dot().move_to(self.coords_to_point(2,f(2)))
        pointLabel1 = MathTex(f'A(2,{f(2)})').next_to(point1,RIGHT)

        func_graph2 = self.get_graph(lambda x: f(-x), x_min = -6, x_max = 6)
        graphLabel2 = self.get_graph_label(func_graph2,label = "y=f(-x)")
        point2 = Dot().move_to(self.coords_to_point(-2,f(2)))
        pointLabel2 = MathTex(f'A\'(-2,{f(2)})').next_to(point2,RIGHT)

        self.autoAnimate([func_graph,func_graph2],[graphLabel1,graphLabel2],[point1,point2],[pointLabel1,pointLabel2])

class allScenes(CustomGraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )
    def construct(self):
        TranslationX.construct(self)
        TranslationY.construct(self)
        ScalingX.construct(self)
        ScalingY.construct(self)
        ReflectionX.construct(self)
        ReflectionY.construct(self)
        ModX.construct(self)
        ModY.construct(self)