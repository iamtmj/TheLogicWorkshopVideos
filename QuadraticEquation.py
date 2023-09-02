from manim import *
class Scene1(Scene):
    def construct(self):
        equation=MathTex("3x^2+2x+5=0")
        self.play(Write(equation))
        rect=Rectangle(color=YELLOW,fill_opacity=0.6,width=0.3,height=0.33)
        rect2=Rectangle(color=YELLOW,fill_opacity=0.6,width=0.4,height=0.4)
        rect.move_to(LEFT*1.2+UP*0.148)
        rect2.move_to(RIGHT*1.25+DOWN*0.05)
        self.play(FadeIn(rect))
        self.play(FadeIn(rect2))
class Scene2(Scene):
    def construct(self):
        ax=Axes(x_range=[-5,5,1],
        y_range=[-5,5,1],
        tips=False,
        axis_config={"include_numbers": True})
        graph=ax.plot(lambda x:(x+2)*(x-2),use_smoothing=True,color=BLUE)
        self.add(ax)
        self.play(Create(graph))
        self.wait()
class Scene3(Scene):
    def construct(self):
        eq1=MathTex("x^2",color=BLUE)
        eq2=MathTex("x^2+2",color=YELLOW)
        eq3=MathTex("x^2-4",color=RED)
        eq1.move_to(LEFT*3+DOWN*3)
        eq2.move_to(LEFT*3+DOWN*3)
        eq3.move_to(LEFT*3+DOWN*3)
        ax=Axes(x_range=[-5,5,1],
        y_range=[-5,5,1],
        tips=False,
        axis_config={"include_numbers": True})
        graph=ax.plot(lambda x:x*x,use_smoothing=True,color=BLUE)
        graph2=ax.plot(lambda x:(x*x)+2,use_smoothing=True,color=YELLOW)
        graph3=ax.plot(lambda x:(x*x)-4,use_smoothing=True,color=RED)
        self.add(ax)
        self.play(Create(graph),Write(eq1))
        self.wait()
        # Animate the changes in the graph
        self.play(FadeOut(eq1),Transform(graph, graph2),Write(eq2))
        self.wait()
        self.play(FadeOut(eq2),Transform(graph2,graph3),FadeOut(graph),Write(eq3))
        
        self.wait()
class Scene4(Scene):
    def construct(self):
        eq=MathTex("x^2",color=BLUE)
        eq2=MathTex("-x^2",color=YELLOW)
        eq.move_to(LEFT*3+DOWN*3)
        eq2.move_to(LEFT*3+DOWN*3)
        ax=Axes(x_range=[-5,5,1],
        y_range=[-5,5,1],
        tips=False,
        axis_config={"include_numbers": True})
        graph=ax.plot(lambda x:x*x,use_smoothing=True,color=BLUE)
        graph2=ax.plot(lambda x:(x*x)*-1,use_smoothing=True,color=YELLOW)
        self.add(ax)
        self.play(Create(graph),Write(eq))
        self.wait()
        self.play(FadeOut(eq),Transform(graph,graph2),Write(eq2))
        self.wait()
class Scene5(Scene):
    def construct(self):
        eq = MathTex("ax^2+bx+c")
        eq2 = MathTex("x^2 + \\frac{b}{a}x + \\frac{c}{a} = 0")
        eq3 = MathTex("2x? = \\frac{b}{a}x")
        eq4 = MathTex("? = \\frac{b}{2a}")
        eq5 = MathTex("(x+\\frac{b}{2a})^2 + \\frac{c}{a} - \\frac{b^2}{2a^2} = 0")
        eq6 = MathTex("(x+\\frac{b}{2a})^2 = \\frac{b^2 - 4ac}{2a^2}")
        eq7 = MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")

        self.play(Write(eq))
        self.wait(1)
        self.play(FadeOut(eq), Write(eq2))
        self.wait(1)
        self.play(FadeOut(eq2), Write(eq3))
        self.wait(1)
        self.play(FadeOut(eq3), Write(eq4))
        self.wait(1)
        self.play(FadeOut(eq4), Write(eq5))
        self.wait(1)
        self.play(FadeOut(eq5), Write(eq6))
        self.wait(1)
        self.play(FadeOut(eq6), Write(eq7))
        self.wait(1)

class Scene6(Scene):
    def construct(self):
        ax=Axes(x_range=[-10,10,2],
        y_range=[-10,10,2],
        tips=False,
        axis_config={"include_numbers": True})
        graph=ax.plot(lambda x:(x+2)*(x-4),use_smoothing=True,color=BLUE)
        point = Dot(ax.c2p(1,-9), color=RED,radius=0.1)
        dotted_line = DashedLine(ax.c2p(1,-10), ax.c2p(1,10), color=YELLOW)
        self.play(Create(ax), Create(graph), Create(point),Create(dotted_line))
        self.wait(2)
class Test(Scene):
    def construct(self):
        self.add(MathTex("ax^2+bx+c"))
        