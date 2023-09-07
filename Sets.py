from manim import *

class Scene1(Scene):
    def construct(self):
        dot=Dot(color=BLUE).move_to(LEFT*2+UP*1)
        dot1=Dot(color=BLUE).move_to(RIGHT*2+DOWN*1)
        dot2=Dot(color=BLUE).move_to(DOWN*2)
        cir=Circle(radius=2.7,color=RED,fill_opacity=0.5)
        self.add(dot,dot1,dot2)
        self.wait()
        self.play(Create(cir))
        self.wait(1)
class Scene2(Scene):
    def construct(self):
        dot=Dot(color=BLUE).move_to(LEFT*2+UP*1)
        dot1=Dot(color=BLUE).move_to(RIGHT*2+DOWN*1)
        dot2=Dot(color=BLUE).move_to(DOWN*2)
        dot3=Dot(color=BLUE).move_to(DOWN*2+LEFT*4)
        cir=Circle(radius=2.7,color=RED,fill_opacity=0.5)
        self.add(dot,dot1,dot2,dot3)
        self.wait()
        self.play(Create(cir))
        self.wait(1)
        self.play(dot3.animate.set_color(YELLOW))
        self.wait(1)
class Scene3(Scene):
    def construct(self):
        text1=Text("Kingdom A")
        text2=Text("Kingdom B")
        numDotA=3
        numDotB=2
        locA=[[2,-5],[2.5,-5.2],[1.2,-5.7]]
        locB=[[2.1,4.8],[2.3,5.3]]
        dotL=[]
        for i in range(0,numDotA):
            dot=Dot(color=WHITE).move_to(UP*locA[i][0]+RIGHT*locA[i][1])
            dotL.append(dot)
            self.add(dot)
        cir1=Circle(radius=1.5,color=YELLOW,fill_opacity=0.3).move_to(LEFT*5+UP*2)
        cir2=Circle(radius=1.5,color=YELLOW,fill_opacity=0.3).move_to(RIGHT*5+UP*2)
        text1.move_to(LEFT*5)
        text2.move_to(LEFT*-5)
        self.play(Create(cir1))
        self.play(FadeIn(text1))
        dotR=[]
        for i in range(0,numDotB):
            dot=Dot(color=WHITE).move_to(UP*locB[i][0]+RIGHT*locB[i][1])
            dotR.append(dot)
            self.add(dot)
        self.play(Create(cir2))
        self.play(FadeIn(text2))
        self.wait()
        self.play(FadeOut(cir1),FadeOut(cir2),FadeOut(text1),FadeOut(text2))
        text3=Text("Union")
        text3.move_to(DOWN*1)
        for dot in dotL:
            self.play(dot.animate.shift(RIGHT*5))
        for dot in dotR:
            self.play(dot.animate.shift(RIGHT*-3.8))
        cir3=Circle(radius=2,color=BLUE,fill_opacity=0.3).move_to(UP*1.3)
        self.play(Create(cir3))
        self.play(FadeIn(text3))
class Scene4(Scene):
    def construct(self):
        text1=Text("Kingdom A")
        text2=Text("Kingdom B")
        numDotA=3
        numDotB=2
        locA=[[2,-5],[2.5,-5.2],[1.2,-5.7]]
        locB=[[2.1,4.8],[2.3,5.3]]
        dotL=[]
        for i in range(0,numDotA):
            dot=Dot(color=WHITE).move_to(UP*locA[i][0]+RIGHT*locA[i][1])
            if i==0 or i==1:
                dot.set_color(BLUE)
            dotL.append(dot)
            self.add(dot)
        cir1=Circle(radius=1.5,color=YELLOW,fill_opacity=0.3).move_to(LEFT*5+UP*2)
        cir2=Circle(radius=1.5,color=YELLOW,fill_opacity=0.3).move_to(RIGHT*5+UP*2)
        text1.move_to(LEFT*5)
        text2.move_to(LEFT*-5)
        self.add(cir1)
        self.add(text1)
        dotR=[]
        for i in range(0,numDotB):
            dot=Dot(color=WHITE).move_to(UP*locB[i][0]+RIGHT*locB[i][1])
            if i==0:
                dot.set_color(BLUE)
            dotR.append(dot)
            self.add(dot)
        self.add(cir2)
        self.add(text2)
        self.wait()
        for dot in range(0,len(dotL)):
            if dot==0 or dot==1:
                self.play(dotL[dot].animate.shift(RIGHT*5))
            else:
                self.play(FadeOut(dotL[dot]))
        for dot in range(0,len(dotR)):
            if dot==0 :
                self.play(dotR[dot].animate.shift(RIGHT*-4.5))
            else:
                self.play(FadeOut(dotR[dot]))
        self.play(FadeOut(cir1,cir2,text1,text2))
        cir3=Circle(radius=2,color=PURE_RED,fill_opacity=0.3).move_to(UP*1.3)
        self.play(Create(cir3))
        text3=Text("Intersection")
        text3.move_to(DOWN*1)
        self.play(FadeIn(text3))
class Scene5(Scene):
    def construct(self):
        tex1=Text("Intersection")
        tex2=Text("Union")
        cir1=Circle(radius=1,color=BLUE,fill_opacity=0.5)
        cir2=Circle(radius=1,color=BLUE,fill_opacity=0.5).move_to(LEFT*0.5)
        self.add(cir1,cir2)
        inter=Intersection(cir1,cir2,color=PURPLE,fill_opacity=0.2)
        union=Union(cir1,cir2,color=PURPLE,fill_opacity=0.2)
        self.wait()
        self.play(inter.animate.scale(0.5).move_to(DOWN*2+LEFT*2))
        self.wait()
        self.play(union.animate.scale(0.5).move_to(DOWN*2+RIGHT*2))
        tex1.move_to(DOWN*2+LEFT*5)
        tex2.move_to(DOWN*2+RIGHT*5)
        self.play(FadeIn(tex1,tex2))