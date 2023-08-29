from manim import *
class Scene1(Scene):
    def construct(self):
        #Logo
        logo=ImageMobject("Logo.jpg")
        logo.scale(0.5)
        self.play(FadeIn(logo))
        self.wait(1)
        self.play(FadeOut(logo))
        self.wait(1)
        label1=Text("Set A")
        label2=Text("Set B")
        self.play(FadeIn(label1))
        r1=Rectangle(width=3,height=3,color=BLUE,fill_opacity=0.7)
        self.play(label1.animate.shift(LEFT*4+UP*2))
        self.play(Create(r1))
        self.play(r1.animate.shift(LEFT*4+UP*0))
        
        self.wait()
        cent=r1.get_center()
        xcor=cent[0]
        ycor=cent[1]
        heightR=r1.height
        num=["1","2"]
        lnum=len(num)
        a=heightR/lnum
        counter=(heightR/2)+ycor+a
        for i in num:
            counter-=a
            v=RIGHT*xcor+UP*counter+DOWN*0.5
            t=Text(i)
            t.move_to(v)
            self.play(FadeIn(t))
            self.wait()
        self.play(FadeIn(label2))
        r2=Rectangle(width=3,height=3,color=BLUE,fill_opacity=0.7)
        self.play(label2.animate.shift(RIGHT*4+UP*2))
        self.play(Create(r2))
        self.play(r2.animate.shift(RIGHT*4+UP*0))
        
        self.wait()
        cent=r2.get_center()
        xcor=cent[0]
        ycor=cent[1]
        heightR=r2.height
        num=["4","5"]
        lnum=len(num)
        a=heightR/lnum
        counter=(heightR/2)+ycor+a
        for i in num:
            counter-=a
            v=RIGHT*xcor+UP*counter+DOWN*0.5
            t=Text(i)
            t.move_to(v)
            self.play(FadeIn(t))
            self.wait()
        l1=[1,2]
        l2=[4,5]
        l3=[]
        for i in range(len(l1)):
            for j in range(len(l2)):
                o=f"[{l1[i]},{l2[j]}]"
                l3.append(o)
            j=0
        c=RIGHT*1.2
        sv=DOWN*3+LEFT*3
        for i in range(len(l3)):
            sv+=c
            t=Text(str(l3[i])).scale(0.7)
            t.move_to(sv)
            self.play(FadeIn(t))
            self.wait()
        
class Scene2(Scene):
    def construct(self):
        set1=[1,2]
        set2=[4,5]
        set3=[]
        coord=[]
        for i in range(len(set1)):
            for j in range(len(set2)):
                a=str(set1[i])
                b=str(set2[j])
                c=f"[{a},{b}]"
                set3.append(c)
        l=len(set3)
        print(l)
        c1=RIGHT*2.5
        v1=LEFT*1.5+UP*2-c1
        v2=LEFT*2-c1
        v3=LEFT*1.5-c1+DOWN*2
        for i in range(0,2):
            v1+=c1
            coord.append(v1)
            tex=Text(set3[i])
            tex.move_to(v1)
            self.play(FadeIn(tex))
            self.wait()
        for i in range(2,4):
            v3+=c1
            coord.append(v3)
            tex=Text(set3[i])
            tex.move_to(v3)
            self.play(FadeIn(tex))
            self.wait()
        r=Rectangle(color=YELLOW,width=2,height=2,fill_opacity=0.4)
        r2=Rectangle(color=YELLOW,width=2,height=2,fill_opacity=0.4)
        r.move_to(coord[1])
        r2.move_to(coord[3])
        self.wait(2)
        self.play(FadeIn(r),FadeIn(r2))
        self.wait()
class Scene3(Scene):
    def construct(self):
     ax=Axes(   x_range=[0,5,1],
        y_range=[-5,5,1],
        tips=False,
        axis_config={"include_numbers": True})
        
     graph=ax.plot(lambda x:x**0.5,use_smoothing=True,color=BLUE)
     graph2=ax.plot(lambda x:-1*x**0.5,use_smoothing=True,color=BLUE)
     label = ax.get_graph_label(graph, label="y^2 = x", direction=RIGHT)
     label.move_to(UP*3+RIGHT*3)
     self.add(ax)
     self.play(Create(graph),Create(graph2),FadeIn(label))
     self.wait()
class Scene4(Scene):
    def construct(self):
     ax=Axes(   x_range=[0,5,1],
        y_range=[-5,5,1],
        tips=False,
        axis_config={"include_numbers": True})
        
     graph=ax.plot(lambda x:x**0.5,use_smoothing=True,color=BLUE)
     label = ax.get_graph_label(graph, label="y = \\sqrt(x)", direction=RIGHT)
     label.move_to(UP*3+RIGHT*3)
     self.add(ax)
     self.play(Create(graph),FadeIn(label))
     self.wait()


        