# python -m manim my_test.py Graphing -pl

from manimlib.imports import *
import math

class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Geometría Analítica")
        second_line = TextMobject("1. Línea Recta ")
        second_line_main = TextMobject("1. Línea Recta ")
        final_line = TextMobject("Noe A. Eseiza", color=PURPLE)
        eq_line = TextMobject("$ y = mx + b $", color=BLUE)
        eq_example1 = TextMobject("$ y = 3x + 2 $", color=TEAL)

        #Coloring
        #color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)
        final_line.next_to(second_line, DOWN)
        eq_line.shift(DOWN)
        eq_example1.shift(DOWN)
        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        #self.play(Write(final_line))
        self.wait(2)
        self.play(Write(final_line))
        self.wait(5)
        
        self.play(FadeOut(first_line) )
        self.play(ReplacementTransform( second_line, second_line_main), ReplacementTransform(final_line, eq_line))
        self.wait(3)
        self.play(ReplacementTransform(eq_line, eq_example1))
        self.wait(2)
        #self.play(FadeOut(final_line), ReplacementTransform(first_line, second_line))
        #self.wait(2)
        #self.play(Transform(final_line, color_final_line))
        #self.wait(2)

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -8,
        "x_max": 8,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def func_to_graph(self, x):
        return 0.5*(x-1) +2

    def func_ex_1(self,x):
        return 0.12*(x-1) +2

    def func_ex_2(self,x):
        return 0.6*(x-1) +2

    def func_ex_3(self,x):
        return -1*(x-1) +2

    def func_ex_4(self,x):
        return -3*(x-1) +2

    def construct(self):
        #Make graph
        self.setup_axes(animate=False)
        loc_func = lambda self, x: 0.5*(x-1) +2 
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "y = 0.5(x-1)+2", direction=BOTTOM)

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        func_ex_1=self.get_graph(self.func_ex_1, YELLOW)
        func_ex_2=self.get_graph(self.func_ex_2, PURPLE)
        func_ex_3=self.get_graph(self.func_ex_3, TEAL)
        func_ex_4=self.get_graph(self.func_ex_4, MAROON)

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(2,3))
        point1 = Dot(self.coords_to_point(1,2))
        point2 = Dot(self.coords_to_point(5,4))
        #Display graph
        #self.play(ShowCreation(func_graph), Write(graph_lab))
        #self.wait(1)
        self.play(ShowCreation(point1))
        self.wait(1)
        self.play(ShowCreation(func_ex_1))
        self.wait(1)
        self.play(ShowCreation(func_ex_2))
        self.wait(1)
        self.play(ShowCreation(func_ex_3))
        self.wait(1)
        self.play(ShowCreation(func_ex_4))
        self.wait(1)
        self.play(ShowCreation(point2))
        self.wait(1)

        self.play(ReplacementTransform(func_ex_2, func_ex_1), ReplacementTransform(func_ex_4, func_ex_3))
        self.wait(1)
        #self.play(ShowCreation(func_graph))
        self.play(ReplacementTransform(func_ex_1, func_graph), ReplacementTransform(func_ex_3, func_graph))
        #self.play(ShowCreation(func_graph), Write(graph_lab))
        #self.add(point1)
        #self.add(point2)
        #self.play(ShowCreation(vert_line))
        #self.play(ShowCreation(horz_line))
        #self.add(point)
        #self.wait(1)
        #self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)
        self.play(Write(TextMobject("Geometría Analítica")))

    def func_to_graph_2(self, x):
        return(x**3)

class EquationDeduction(Scene):
    def construct(self):
        defini = TextMobject("Tenemos dos puntos: $ P_1 = (1,2) $ y $ P_2 = (5,4) $")
        #defini = TextMobject("$m=\\frac{y_2 - y_1}{x_2 - x_1}$")
        defini.to_edge(UP)
        defini.shift(DOWN)

        pendiente = TextMobject("$m=\\frac{y_2 - y_1}{x_2 - x_1}$", color=LIGHT_PINK)
        pendiente.next_to(defini,3*DOWN)

        pendiente_1 = TexMobject(r"m=\frac{4-2}{5-1} ")
        pendiente_1.next_to(pendiente,2*DOWN)

        pendiente_2 = TexMobject(r"m=\frac{2}{4} = 0.5")
        pendiente_2.next_to(pendiente_1,2*DOWN)

        definicion_2 = TextMobject("Entonces $ m = 0.5 $")
        definicion_2.next_to(defini, DOWN)

        definicion_3 = TextMobject("$ y = y_0 + m(x - x_0) $", color=LIGHT_PINK)
        definicion_3.next_to(definicion_2, 2*DOWN)

        sust = TexMobject("\\text{Sustituimos: } m \\text{ y } (x_0,y_0) ")
        sust.next_to(definicion_3, 2*DOWN)

        sust_1 = TexMobject("y = 2 + 0.5(x-1) ", color=GREEN)
        sust_1_1 = TexMobject("y = 2 + 0.5(1-1) = 2", color=GREEN)
        sust_1.next_to(sust, 2*DOWN)
        sust_1_1.next_to(sust, 2*DOWN)

        sust_2 = TexMobject("y = 4 + 0.5(x-5) ", color=RED)
        sust_2_2 = TexMobject("y = 4 + 0.5(1-5) =  2", color=RED)
        sust_2.next_to(sust_1, 2*DOWN) 
        sust_2_2.next_to(sust_1, 2*DOWN) 

        self.add(defini)
        self.wait(1)
        self.play(Write(pendiente))
        self.wait(1)
        self.play(Write(pendiente_1))
        self.wait(1)
        self.play(Write(pendiente_2))
        self.play(FadeOut(pendiente), FadeOut(pendiente_1), FadeOut(pendiente_2))
        self.play(Write(definicion_2))
        self.wait(1)
        self.play(Write(definicion_3))
        self.wait(1)
        self.play(Write(sust))
        self.wait(1)
        self.play(Write(sust_1))
        self.wait(1)
        self.play(Write(sust_2))
        self.wait(1)
        self.play(Transform(sust_1, sust_1_1), Transform(sust_2,sust_2_2))

        self.wait(2)

