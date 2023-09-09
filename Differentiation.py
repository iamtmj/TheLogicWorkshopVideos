from manim import *
class Scene1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0.1, 8],
            y_range=[-5, 5],
            axis_config={"include_numbers":True,"color":BLUE}
        )
        graph = axes.plot(lambda x: np.sin(x) * np.log(x), color=WHITE,use_smoothing=True)
        self.add(axes)
        self.play(Create(graph))
class Scene2(Scene):
    def construct(self):
        axes=Axes(
            x_range=[0,3],
            y_range=[0,3],
            axis_config={"include_numbers":True,"color":BLUE}
        )
        self.add(axes)
        dot1=Dot(color=WHITE).move_to((LEFT*6+DOWN*3)+(RIGHT*4+UP*2))
        dot2=Dot(color=WHITE).move_to((LEFT*6+DOWN*3)+(RIGHT*8+UP*4))
        dot3=Dot(color=WHITE).move_to((LEFT*6+DOWN*3)+(RIGHT*8+UP*2))
        tex1=Text("1").move_to((LEFT*6+DOWN*3)+(RIGHT*8+UP*2)+UP*1+RIGHT*0.5)
        tex2=Text("1").move_to((LEFT*6+DOWN*3)+(RIGHT*8+UP*2)+DOWN*0.5+LEFT*2)
        self.add(dot1,dot2)
        line = DashedLine(dot1.get_center(),dot3.get_center(), color=WHITE)
        line2 = DashedLine(dot2.get_center(),dot3.get_center(), color=WHITE)
        line3 = DashedLine(dot1.get_center(),dot2.get_center(), color=RED)
        self.play(Create(line))
        self.wait()
        self.play(Create(line2))
        self.wait()
        self.play(Create(line3))
        self.wait()
        self.play(Write(tex1))
        self.play(Write(tex2))
        self.wait()
class Scene3(Scene):
    def construct(self):
        
        ax = Axes(y_range=[-1, 7],x_range=[0.1,3])
        graph = ax.plot(lambda x: np.sin(x) * np.log(x), color=BLUE)

        # Initial value for 'dx'
        initial_dx = 2.0

        # Create a ValueTracker for 'dx' and set its initial value
        dx_tracker = ValueTracker(initial_dx)

        # Function to update the secant slope group
        def update_slope_group(group):
            x_value = ax.x_axis.p2n(group[0].get_start())
            dx_value = dx_tracker.get_value()
            new_slope_group = ax.get_secant_slope_group(
                x=x_value,
                graph=graph,
                dx=dx_value,
                
                dx_line_color=GREEN_B,
                secant_line_length=4,
                secant_line_color=RED_D,
            )
            group.become(new_slope_group)

        # Create the secant slope group and update it initially
        slopes = ax.get_secant_slope_group(
            x=2,  # Initial 'x' value
            graph=graph,
            dx=initial_dx,
            
            dx_line_color=GREEN_B,
            secant_line_length=4,
            secant_line_color=RED_D,
        )

        # Add the axes, graph, and slopes to the scene
        self.add(ax, graph, slopes)

        # Animation to change 'dx'
        self.play(
            dx_tracker.animate.set_value(0.5),  # Change 'dx' to 2.0
            UpdateFromFunc(slopes, update_slope_group),  # Update the slope group
            run_time=3,  # Animation duration
        )

        self.wait(1)  # Wahe animationr a moment after the animation
class Scene4(Scene):
    def construct(self):
          # Create the axes and graph
        ax = Axes(y_range=[-1, 7],x_range=[0.1,10])
        graph = ax.plot(lambda x:np.sin(x)*np.log(x), color=BLUE)

        # Create the secant slope group
        slopes = ax.get_secant_slope_group(
            x=2.0,
            graph=graph,
            dx=0.2,
           
            secant_line_length=4,
            secant_line_color=RED_D,
        )

        # Add the axes, graph, and slopes to the scene
        self.add(ax, graph, slopes)

        # Create a ValueTracker for 'x' and set its initial value
        x_tracker = ValueTracker(2.0)

        # Update the 'x' value and animate the secant slope group
        self.play(
            x_tracker.animate.set_value(8.0),  # Change 'x' to 5.0
            UpdateFromFunc(
                slopes,
                lambda m: m.become(ax.get_secant_slope_group(
                    x=x_tracker.get_value(),  # Get the current 'x' value
                    graph=graph,
                    dx=0.2,
                    
                    dx_line_color=GREEN_B,
                    secant_line_length=4,
                    secant_line_color=RED_D,
                )),
            ),
            run_time=2,  # Animation duration
        )

        self.wait(1)