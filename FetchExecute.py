from manim import *
class Scene1(Scene):
    def construct(self):
        loc=["Grey Rock","Black Water","Red Sky"]
        gold=[20,10,80]
        head1="Location"
        head2="Gold"
        rect=Rectangle(width=4,height=6)
        t1=Text(head1).scale(0.6).move_to(UP*2.7+LEFT*1)
        t2=Text(head2).scale(0.6).move_to(UP*2.7+RIGHT*1.3)
        v=UP*2.7+LEFT*1
        v1=1
        self.add(rect)
        self.add(t1,t2)
        for e in range(0,len(loc)):
            self.add(Text(loc[e]).scale(0.6).move_to(UP*2.7+LEFT*0.76+DOWN*v1))
            v1+=2
        v1=1
        for e in range(0,len(gold)):
            self.add(Text(str(gold[e])).scale(0.6).move_to(UP*2.7+RIGHT*1.2+DOWN*v1))
            v1+=2
class Scene2(Scene):
    def construct(self):
        rect1=Rectangle(width=5,height=5).move_to(LEFT*3)
        rect2=Rectangle(width=4,height=6).move_to(RIGHT*3)
        ar=Arrow(tip_length=0,color=BLUE).move_to(RIGHT*0.235).scale(1)
        self.add(rect1,rect2,ar)
        loc=["0","1","2"]
        val=["1","Load 2","3"]
        v=0.2
        for e in range(0,len(loc)):
            self.add(Text(loc[e]).scale(0.8).move_to(RIGHT*2+UP*1.8+DOWN*v))
            self.add(Text(val[e],color=RED).scale(0.8).move_to(RIGHT*4+UP*1.8+DOWN*v))
            v+=1.8
        v=0
        val2=["Counter :","Register :","Accumulator :"]
        value1=[]
        for e in range(0,len(val2)):
            self.add(Text(val2[e]).scale(0.5).move_to(LEFT*4.2+UP*1.4+DOWN*v))
            v+=1.1
        t1=Text("0").scale(0.7).move_to(LEFT*3+UP*1.4+DOWN*0)
        t2=Text("1").scale(0.7).move_to(LEFT*3+UP*1.4+DOWN*1.1)
        t3=Text("0").scale(0.7).move_to(LEFT*2.8+UP*1.4+DOWN*2.2)
        t4=Text("1").scale(0.7).move_to(LEFT*3+UP*1.4+DOWN*0)
        t5=Text("Load 2").scale(0.5).move_to(LEFT*2.7+UP*1.4+DOWN*1.1)
        t6=Text("1").scale(0.7).move_to(LEFT*2.8+UP*1.4+DOWN*2.2)
        t7=Text("2").scale(0.7).move_to(LEFT*2.8+UP*1.4+DOWN*1.1)
        t8=Text("3").scale(0.7).move_to(LEFT*2.8+UP*1.4+DOWN*2.2)
        t9=Text("2").scale(0.7).move_to(LEFT*3+UP*1.4+DOWN*0)
        t10=Text("5").scale(0.7).move_to(LEFT*2.8+UP*1.4+DOWN*2.2)
        self.add(t1,t2,t3)
        self.wait()
        self.play(FadeOut(t1),FadeOut(t2),FadeOut(t3))
        self.add(t4,t5,t6)
        self.wait()
        self.play(FadeOut(t5),FadeOut(t6))
        self.wait()
        self.add(t7,t8)
        self.wait()
        self.play(FadeOut(t4),FadeOut(t8))
        self.wait()
        self.add(t9,t10)
        self.wait()