from manim import *

class CustomGraphScene(GraphScene):
    def createAnimatedTitle(self,text):
        title = Tex(text)
        self.play(Write(title))
        self.play(title.animate.scale(0.5))
        self.play(title.animate.shift(3 * UP + 4.5 * LEFT))

    # Create function to automate transformation of objects.
    def autoAnimate(self,objects):
        self.play(
            *[Create(itemGroup[0]) for itemGroup in objects],run_time=1.5
        )
        # self.play(Create(graphs[0]),Create(points[0]),Create(pointLabels[0]), run_time=1.5)
        # self.play(Create(graphLabels[0]))
        for idx in range(len(objects[0])-1):
            for itemGroup in objects:
                self.play(ReplacementTransform(itemGroup[idx],itemGroup[idx + 1]),run_time = 1.5)
        # for idx in range(len(graphs) - 1):
        #     self.wait(1)
        #     self.play(Transform(graphLabels[idx],graphLabels[idx + 1]))
        #     self.play(Transform(graphs[idx],graphs[idx + 1]))
        #     self.play(Transform(points[idx],points[idx + 1]),Transform(pointLabels[idx],pointLabels[idx + 1]))
        self.wait(2)
        

AxesParams = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -7,
    "y_max": 7,
    "graph_origin":[0,2,0.0],
    "include_tip": True,
    "y_axis_height": 3.5,
    "y_axis_config":{"tick_frequency": 50},
    "x_axis_config":{"tick_frequency": 50}, 
}

def polyFunc(x):
        return 3/((x-1)*(x+2)) - 2




class Reciprocal(CustomGraphScene):
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            **AxesParams,
            **kwargs
        )
    def createPoint(self,equation,x,label,labelDirection = DOWN,labelScale = 0.5,accuracy = 0,pointColor = WHITE):
        point = Dot().move_to(self.coords_to_point(x,equation(x))).set_color(pointColor)
        pointLabel = MathTex(f"{label}({x},{round(equation(x),accuracy)})").next_to(point,labelDirection).scale(labelScale).set_color(pointColor)
        box = SurroundingRectangle(pointLabel, buff =.1)
        return [VGroup(point,pointLabel),box]

    def createVerticalLine(self,x,labelDirection = DOWN,labelScale = 0.5,lineColor = WHITE):
        vert_line = DashedLine(self.coords_to_point(x,self.y_min+1),self.coords_to_point(x,self.y_max-1),color = lineColor)
        label = MathTex(f"x={x}").next_to(vert_line,labelDirection).scale(labelScale).set_color(lineColor)
        box = SurroundingRectangle(label, buff =.1)
        return [VGroup(vert_line,label),box]

    def createHorizontalLine(self,y,labelDirection = RIGHT,labelScale = 0.5,lineColor = WHITE):
        horiz_line = DashedLine(self.coords_to_point(self.x_min + 1,y),self.coords_to_point(self.x_max - 1,y),color = lineColor)
        label = MathTex(f"y={y}").next_to(horiz_line,labelDirection).scale(labelScale).set_color(lineColor)
        box = SurroundingRectangle(label, buff =.1)
        return [VGroup(horiz_line,label),box]

    

    def construct(self):
        self.createAnimatedTitle("Reciprocal transformation")
        self.setup_axes(animate=True)

        func_graph1 = self.get_graph(polyFunc, x_min = self.x_min + 1, x_max = 1.092 * -2,color=WHITE)
        func_graph2 = self.get_graph(polyFunc, x_min = 0.85 * -2, x_max = 0.75 * 1,color=WHITE)
        func_graph3 = self.get_graph(polyFunc, x_min = 1.15 * 1, x_max = self.x_max - 1,color=WHITE)

        fullGraph = VGroup(func_graph1,func_graph2,func_graph3)
        fullGraphLabel = self.get_graph_label(func_graph3,label = "y=f(x)",direction=UP).scale(0.5)
        
        oldXInt1 = self.createPoint(polyFunc,-2.436,"A",UP)

        oldXAsym1 = self.createVerticalLine(-2,0.5 * UP,lineColor=ORANGE)
        oldXAsym2 = self.createVerticalLine(1,0.5 * UP,lineColor=ORANGE)

        oldXInt2 = self.createPoint(polyFunc,1.436,"B",UP)
        
        oldMin = self.createPoint(polyFunc,-0.5,"C",accuracy = 4,pointColor=RED)

        oldYInt = self.createPoint(polyFunc,0,"D",labelDirection = 0.5*RIGHT,accuracy = 3,pointColor=BLUE)

        oldYAsym = self.createHorizontalLine(-2,lineColor=YELLOW)
    
        self.graph_origin = 2 * DOWN

        self.setup_axes(animate=True)

        newGraph1 = self.get_graph(lambda x: 1/polyFunc(x), x_min = self.x_min + 1, x_max = 1.04 * -2.436,color=WHITE)
        newGraph2 = self.get_graph(lambda x: 1/polyFunc(x), x_min = 0.97 * -2.436, x_max = 0.97 * 1.436,color=WHITE)
        newGraph3 = self.get_graph(lambda x: 1/polyFunc(x), x_min = 1.04 * 1.436, x_max = self.x_max - 1,color=WHITE)
        fullGraph2 = VGroup(newGraph1,newGraph2,newGraph3)
        fullGraphLabel2 = self.get_graph_label(newGraph3,label = "y=\\frac{1}{f(x)}",direction=UP).scale(0.5)

        newXInt1 = self.createPoint(lambda x: 0,-2,"E",labelDirection = 0.5 * UP,pointColor=ORANGE)
        newXInt2 = self.createPoint(lambda x: 0,1,"F",labelDirection = 0.5 * UP,pointColor=ORANGE)

        newXAsym1 = self.createVerticalLine(-2.436,0.5 * DOWN)

        newMax = self.createPoint(lambda x: 1/polyFunc(x),-0.5,'C\'',labelDirection = UP,accuracy = 4,pointColor=RED)

        newXAsym2 = self.createVerticalLine(1.436,0.5 * DOWN)

        newYAsym = self.createHorizontalLine(-0.5,lineColor=YELLOW)

        newYInt = self.createPoint(lambda x: 1 / polyFunc(x),0,"D\'",labelDirection = 0.5*RIGHT, accuracy = 4,pointColor=BLUE)

        # 1. Create graph
        self.play(Create(fullGraph))
        # self.play(fullGraph.animate.fade(0.5))
        self.wait()

        # 2a. Create x-intercepts
        self.play(
            *[Create(group) for group in [oldXInt1[0],oldXInt2[0]]],run_time = 1.5
        )
        
        self.wait()

        self.play(
            *[Create(group) for group in [oldXAsym1[0],oldXAsym2[0]]],run_time = 1.5
        )
        
        self.wait()
        # 2b. Create y-intercepts
        self.play(
            *[Create(group) for group in [oldYInt[0],oldMin[0]]],run_time = 1.5
        )
        
        self.wait()
        self.play(
            Create(oldYAsym[0], run_time = 1.5)
        )

        self.wait(2)
        
        # 3a. x-intercepts -> vertical asymptote
        self.play(
            *[Circumscribe(group,fade_out=True,buff=0.05) for group in [oldXInt1[0],oldXInt2[0]]]
        )

        self.play(
            # *[Create(new) for new in [newXAsym1[0],newXAsym2[0]]]
            *[Transform(old.copy(),new) for old,new in zip([oldXInt1[0],oldXInt2[0]],[newXAsym1[0],newXAsym2[0]])]
        )
        self.wait()
        # 3b. vertical asymptotes -> x-intercepts
        self.play(
            *[Circumscribe(group,fade_out=True,buff=0.05) for group in [oldXAsym1[0],oldXAsym2[0]]]
        )
        self.play(
            # *[Create(new) for new in [newXAsym1[0],newXAsym2[0]]]
            *[Transform(old.copy(),new) for old,new in zip([oldXAsym1[0],oldXAsym2[0]],[newXInt1[0],newXInt2[0]])]
        )
        self.wait()
        # 3c. Change y-intercepts
        self.play(
            Circumscribe(oldYInt[0],fade_out=True,buff=0.05)
        )
        self.play(
            Transform(oldYInt[0].copy(),newYInt[0])
        )
        self.wait()
        # 3d. Change horizontal asymptotes.
        self.play(
            Circumscribe(oldYAsym[0],fade_out=True,buff=0.05)
        )
        self.play(
            Transform(oldYAsym[0].copy(),newYAsym[0])
        )
        self.wait()
        # 3e. Change turning point
        self.play(
            Circumscribe(oldMin[0],fade_out=True,buff=0.05)
        )
        self.play(
            Transform(oldMin[0].copy(),newMax[0])
        )
        self.wait()
        # 4. Draw new graph
        self.play(Transform(func_graph1.copy(),newGraph1),run_time = 2)
        self.play(Transform(func_graph2.copy(),newGraph2),run_time = 2)
        self.play(Transform(func_graph3.copy(),newGraph3),run_time = 2)
        # self.play(Write(fullGraphLabel2))
        # self.play(
        #     *[FadeOut(mob) for mob in self.mobjects]
        # )