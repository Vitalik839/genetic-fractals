from tkinter import *

root = Tk()
canvas = Canvas(root, width = 1000, height = 700)
canvas.pack()


cx = [50, 650, 650, 50]
cy = [50, 50, 650, 650]
string = "agttcag"
string = string.lower()
canvas.create_rectangle(50, 50, 650, 650)
canvas.create_text(60, 25, font = ("Arial", 18, "bold"), text = "T (50, 50)")
canvas.create_text(660, 25, font = ("Arial", 18, "bold"), text = "C (650, 50)")
canvas.create_text(665, 680, font = ("Arial", 18, "bold"), text = "A (650, 650)")
canvas.create_text(65, 680, font = ("Arial", 18, "bold"), text = "G (50, 650)")
canvas.create_oval(346, 346, 354, 354, fill = 'black')
for i in range(len(cx)):
    canvas.create_oval(cx[i] - 5, cy[i] - 5, cx[i] + 10, cy[i] + 10, fill = 'black')

def create_genetic_fractal(genetic_code):
    trace_x = 350
    trace_y = 350
    canvas.create_text(350, 330, font = ("Arial", 16, "bold"), text = (str(trace_x) + "; " + str(trace_y)))
    y = 90
    try:
        for i in range(len(genetic_code)):
            trace_x0 = trace_x
            trace_y0 = trace_y
            if genetic_code[i] == 't':
                trace_x = (trace_x + cx[0]) / 2
                trace_y = (trace_y + cy[0]) / 2
            elif genetic_code[i] == 'c':
                trace_x = (trace_x + cx[1]) / 2
                trace_y = (trace_y + cy[1]) / 2
            elif genetic_code[i] == 'a':
                trace_x = (trace_x + cx[2]) / 2
                trace_y = (trace_y + cy[2]) / 2
            else:
                trace_x = (trace_x + cx[3]) / 2
                trace_y = (trace_y + cy[3]) / 2
            #canvas.create_line(trace_x0, trace_y0, trace_x, trace_y)
            canvas.create_oval(trace_x, trace_y, trace_x + 3.5, trace_y + 3.5, fill = 'black')
            text = str(i + 1) + ":  (x = " + str(round(trace_x, 1)) + ";  y = " + str(round(trace_y, 1)) + ")"
            canvas.create_text(800, y, font = ("Arial", 15, "bold"), text = text)
            canvas.create_text(trace_x, trace_y - 10, font = ("Arial", 16, "bold"), text = str(i + 1))
            y += 45
            root.update()
    except TclError:
        pass


create_genetic_fractal(string)
