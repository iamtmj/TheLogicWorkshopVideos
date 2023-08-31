from manim import *

class Scene1(Scene):
    def construct(self):
        dotL=["C1","C2","C3"]
        ldots=[]
        rdots=[]
        numDots=len(dotL)
        sp=[-2,3,0]
        cp=-1
        for i in range(0,numDots):
            sp[1]+=cp
            dot=Dot(np.array([sp[0],sp[1],sp[2]]))
            dot2=Dot(np.array([2,sp[1],sp[2]]))
            ldots.append(dot.get_center())
            rdots.append(dot2.get_center())
            l1=Text(dotL[i])
            l2=Text(dotL[i])
            l1.move_to(LEFT*4+UP*sp[1])
            l2.move_to(RIGHT*4+UP*sp[1])
            self.add(dot,dot2,l1,l2)
        arrows=[]
        items=[]
        a=-2.3
        for i in range(0,numDots):
            for j in range(0,numDots):
                if i!=j:
                    a+=2.3
                    t=f"[{dotL[i]},{dotL[j]}]"
                    items.append(t)
                    arrow=Arrow(ldots[i],rdots[j],color=BLUE,stroke_width=2)
                    arrows.append(arrow)
                    self.play(Create(arrow))
                    #self.wait()
                    tex=Text(t,color=GREEN)
                    tex.move_to(DOWN*3+LEFT*5.5+RIGHT*a)
                    self.play(Create(tex))
                    #self.wait()
class Scene2(Scene):
    def construct(self):
        dotL=["C1","C2","C3"]
        ldots=[]
        rdots=[]
        numDots=len(dotL)
        sp=[-2,3,0]
        cp=-1
        for i in range(0,numDots):
            sp[1]+=cp
            dot=Dot(np.array([sp[0],sp[1],sp[2]]))
            dot2=Dot(np.array([2,sp[1],sp[2]]))
            ldots.append(dot.get_center())
            rdots.append(dot2.get_center())
            l1=Text(dotL[i])
            l2=Text(dotL[i])
            l1.move_to(LEFT*4+UP*sp[1])
            l2.move_to(RIGHT*4+UP*sp[1])
            self.add(dot,dot2,l1,l2)
        a=-2.3
        for i in range(0,numDots):
            for j in range(i+1,numDots):
                a+=2.3
                t=f"[{dotL[i]},{dotL[j]}]"
                arrow=Arrow(ldots[i],rdots[j],color=BLUE,stroke_width=2)
                self.play(Create(arrow))
                tex=Text(t,color=GREEN)
                tex.move_to(DOWN*3+LEFT*2+RIGHT*a)
                self.play(Create(tex))
class Scene4(Scene):
    def construct(self):
        l1="No. of candies=n"
        l2="No. of option/candy=n-1"
        l3=f"Total number of sets={l1} X {l2}"
        t1=Text(l1).move_to(LEFT*3+UP*3)
        t2=Text(l2).move_to(LEFT*3+UP*2)
        t3=Text(l3).move_to(LEFT*3+UP*1).scale(0.5)
        self.add(t1,t2,t3)
class Test(Scene):
    def construct(self):
       
        custom_dot = Dot(np.array([-2, 1, 0]))

        # Add the dots to the scene
        self.add(custom_dot)
class Scene3(Scene):
    def construct(self):
        num=[1,2,3]
        comb=[]
        for i in range(0,len(num)):
            for j in range(0,len(num)):
                if i!=j:
                    for k in range(0,len(num)):
                        if i!=k and j!=k:
                            comb.append([num[i],num[j],num[k]])
        a=0
        coord=[]
        for i in range(0,len(comb)):
            a-=1
            e=comb[i]
            t=str(e)
            tex=Text(t).move_to(LEFT*3+UP*4+UP*a)
            coord.append(tex.get_center())
            self.add(tex)
        rect=Rectangle(color=YELLOW,fill_opacity=0.5,width=1.2,height=0.7)
        rect2=Rectangle(color=BLUE,fill_opacity=0.5,width=0.6,height=0.7)
        self.play(rect.animate.shift([coord[0][0]+0.4,coord[0][1],0]))
        for i in range(0,len(coord)-1):
          self.play(rect.animate.shift(DOWN*1))
        self.play(FadeOut(rect))
        self.play(rect2.animate.shift([coord[0][0]-0.6,coord[0][1],0]))
        for i in range(0,2):
          self.play(rect2.animate.shift(DOWN*2))
        
class PermutationFormula(Scene):
    def construct(self):
        n = MathTex("n")
        r = MathTex("r")
        
        numerator = MathTex(f"n!")
        denominator = MathTex(f"(n-r)!")
        
        formula = MathTex(r"\frac{" + numerator.get_tex_string() + "}{" + denominator.get_tex_string() + "}")
        
        # Display the formula on the screen
        self.play(Write(formula))
        self.wait()  # Pause for 3 seconds
class CombinationFormula(Scene):
    def construct(self):
        n = MathTex("n")
        r = MathTex("r")
        
        numerator = MathTex(f"n!")
        denominator = MathTex(f"(n-r)!(r)!")
        
        formula = MathTex(r"\frac{" + numerator.get_tex_string() + "}{" + denominator.get_tex_string() + "}")
        
        # Display the formula on the screen
        self.play(Write(formula))
        self.wait()  # Pause for 3 seconds
