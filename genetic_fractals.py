from tkinter import *
from tkinter.ttk import Combobox, Progressbar, Spinbox
from tkinter import messagebox, colorchooser
from config_for_genetic_fractals import covid_alpha, covid_omicron, flu, cholera, hiv, ebola, chuma, vispa
from itertools import product
from random import randrange
from math import sqrt, ceil
from numpy import unique

root = Tk()
canvas = Canvas(root, width = 1000, height = 700)
root.title('Applications of Fractals in Genetics')
root.resizable(0, 0)
canvas.pack()


deep = IntVar()
amount_of_dots = IntVar()
drawing = True
drawing2 = True
array_rgb = [0, 0, 0]
side_big_square = 650
color = 'black'
tag = 'a' # tag for elements which will be destroyed

coordinates_atcg = {'T' : [0, 0], 'C' : [side_big_square, 0], 'A' : [side_big_square, side_big_square], 'G' : [0, side_big_square]}
genetic_names = ['Коронавірус альфа', 'Коронавірус омікрон',  'грип', 'Ебола', 'Холера', 'ВІЛ', 'Чума', 'Віспа']
genetic_codes = {'Коронавірус альфа' : covid_alpha, 'Віспа' : vispa,
                 'Коронавірус омікрон' : covid_omicron,
                 'Ебола' : ebola, 'Холера' : cholera,
                 'ВІЛ' : hiv, 'Чума' : chuma, 'грип' : flu}

deep.set(4)
amount_of_dots.set(10000)
general_amount_of_pairs = []

def find_distance(code1, code2):
    amount_of_pairs1 = []
    amount_of_pairs2 = []
    summ = 0
    for d in range(1, 7):
        array = [''.join(x) for x in product('TACG', repeat = d)]
        for i in array:
            amount_of_pairs1.append(code1.count(i))
            amount_of_pairs2.append(code2.count(i))
        sum1 = sum(amount_of_pairs1)
        sum2 = sum(amount_of_pairs2)
        for i in range(len(amount_of_pairs1)):
            amount_of_pairs1[i] = amount_of_pairs1[i] / sum1
            amount_of_pairs2[i] = amount_of_pairs2[i] / sum2
        
        for i in range(len(amount_of_pairs1)):
            summ +=  1 / (2 ** d) * abs((amount_of_pairs1[i] - amount_of_pairs2[i]))

        amount_of_pairs1 = amount_of_pairs2 = []
    summ = summ * 100 / 2
    return str(round(summ, 2)) + "%"


def get_percents(genetic_code):
    stop_drawing()
    progress_bar.place_forget()
    canvas.delete(tag)
    canvas.create_rectangle(0, 0, 800, 700, fill = 'white', outline = 'white')
    coordinates = (180, 30, 530, 380)
    colors = ['red', 'orange', 'green', 'blue']
    amount_each_element = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
    
    for i in range(len(genetic_code)):
        amount_each_element[genetic_code[i]] += 1

    nucleotids = ['A', 'T', 'C', 'G']
    start, j = 0, 0
    for i in nucleotids:
        canvas.create_arc(coordinates, tag = tag, start = start, extent = round(amount_each_element[i] / len(genetic_code) * 360, 1), fill = colors[j], outline = colors[j])
        canvas.create_rectangle(50, 440 + 60 * j, 70, 460 + 60 * j, tag = tag, fill = colors[j], outline = colors[j])
        j += 1
        start += round(amount_each_element[i] / len(genetic_code) * 360, 1)

    canvas.create_text(175, 450, tag = tag, font = ('Arial', 18, 'bold'), text = 'Adenine - ' + str(round(amount_each_element['A'] / len(genetic_code) * 100, 1)) + '%')
    canvas.create_text(167, 510, tag = tag, font = ('Arial', 18, 'bold'), text = 'Thymine - ' + str(round(amount_each_element['T'] / len(genetic_code) * 100, 1)) + '%')
    canvas.create_text(185, 570, tag = tag, font = ('Arial', 18, 'bold'), text = 'Cytosine - ' + str(round(amount_each_element['C'] / len(genetic_code) * 100, 1)) + '%')
    canvas.create_text(170, 630, tag = tag, font = ('Arial', 18, 'bold'), text = 'Guanine - ' + str(round(amount_each_element['G'] / len(genetic_code) * 100, 1)) + '%')

    

def create_frequency_fractal(string, color):
    side_mini_square = round(side_big_square / (2 ** deep.get()))
    trace_x = trace_y = side_big_square / 2
    for i in string:
        trace_x = (trace_x + coordinates_atcg[i][0]) / 2
        trace_y = (trace_y + coordinates_atcg[i][1]) / 2
    canvas.create_rectangle(trace_x - side_mini_square / 2, trace_y - side_mini_square / 2,
                        trace_x + side_mini_square / 2, trace_y + side_mini_square / 2, fill = color, outline = color, tag = tag)


def main_func(genetic_code,  colors):
    progress_bar.place_forget()
    stop_drawing()
    array = [''.join(x) for x in product('TACG', repeat = deep.get())]
    canvas.delete(tag)
    for i in array:
        general_amount_of_pairs.append(genetic_code.count(i))

    if unique(colors).size == 1:
        for i in array:
            rgb = round(sqrt(genetic_code.count(i) / max(general_amount_of_pairs)) * 255)
            if rgb > 255:
                create_frequency_fractal(i, 'black')
            else:
                create_frequency_fractal(i, '#%02x%02x%02x' % (255 - rgb,  255 - rgb, 255 - rgb))
    else:
        for i in array:
            r = round(sqrt(genetic_code.count(i) / max(general_amount_of_pairs))  * colors[0])
            g = round(sqrt(genetic_code.count(i) / max(general_amount_of_pairs))  * colors[1])
            b = round(sqrt(genetic_code.count(i) / max(general_amount_of_pairs))  * colors[2])
            create_frequency_fractal(i, '#%02x%02x%02x' % (colors[0] - r,  colors[1] - g, colors[2] - b))


def create_genetic_fractal(genetic_code):
    progress_bar.place(x = 745, y = 240)
    global drawing
    drawing = True
    progress_bar.configure(maximum = len(genetic_code))
    trace_x = trace_y = side_big_square / 2 # placing the initial coordinates in the middle of a large square
    canvas.delete(tag)
    j = 0
    for i in genetic_code:
        if not(drawing):
            break
        trace_x = (trace_x + coordinates_atcg[i][0]) / 2
        trace_y = (trace_y + coordinates_atcg[i][1]) / 2
        canvas.create_oval(trace_x, trace_y, trace_x + 3.5, trace_y + 3.5, fill = color, outline = color, tag = tag)
        if j % 100 == 0:
            root.update()
            progress_bar.configure(value = j)
        j += 1


class Fractals_with_ChaosGame:
    def __init__(self):
        self.array_x_for_triangle = [350, 680, 20]
        self.array_y_for_triangle = [20, 600, 600]
        self.array_x_for_square = [0, 700, 700, 0, 350, 700, 350, 0]
        self.array_y_for_square = [0, 0, 700, 700, 0, 350, 700, 350]
        self.trace_x = 350
        self.trace_y = 20

    def create_triangle(self, color):
        canvas.delete(tag)
        progress_bar.place(x = 745, y = 240)
        progress_bar.configure(maximum = amount_of_dots.get())
        for i in range(amount_of_dots.get()):
            if not(drawing2):
                break
            progress_bar.configure(value = i)
            random = randrange(3)
            self.trace_x = (self.trace_x + self.array_x_for_triangle[random]) / 2
            self.trace_y = (self.trace_y + self.array_y_for_triangle[random]) / 2
            canvas.create_oval(self.trace_x, self.trace_y, self.trace_x + 3.5, self.trace_y + 3.5, fill = color, outline = color, tag = tag)
            if i % 100 == 0:
                root.update()


    def create_square(self, color):
        canvas.delete(tag)
        progress_bar.place(x = 745, y = 240)
        progress_bar.configure(maximum = amount_of_dots.get())
        for i in range(amount_of_dots.get()):
            if not(drawing2):
                break
            random = randrange(8)
            self.trace_x = (self.trace_x + 2 * self.array_x_for_square[random]) / 3
            self.trace_y = (self.trace_y + 2 * self.array_y_for_square[random]) / 3
            canvas.create_oval(self.trace_x, self.trace_y, self.trace_x + 3.5, self.trace_y + 3.5, fill = color, outline = color, tag = tag)
            if i % 100 == 0:
                progress_bar.configure(value = i)
                root.update()

chaos_game = Fractals_with_ChaosGame()

def genetic_fractal():
    global drawing
    drawing = True
    create_genetic_fractal(genetic_codes[combobox.get()])


def create_color_palette():
    array_rgb.clear()
    selected_color = colorchooser.askcolor()[0]
    for i in range(3):
        array_rgb.append(int(selected_color[i]))
    global color
    color = '#%02x%02x%02x' % (array_rgb[0], array_rgb[1], array_rgb[2])
    canvas.delete('temp')
    canvas.create_rectangle(940, 15, 955, 30, fill = color, outline = color, tag = 'temp')


def stop_drawing():
    global drawing, drawing2
    drawing = False
    drawing2 = False


def find_difference():
    if combobox2.get() == combobox3.get():
        messagebox.showwarning('Warning', 'You chose 2 the same viruses')
    else:
        messagebox.showinfo('Information', 'Difference between ' + combobox2.get()+ ' and ' + combobox3.get() + ': ' +
                            str(find_distance(genetic_codes[combobox2.get()], genetic_codes[combobox3.get()])))

def sierp_triangle():
    global drawing2
    drawing2 = True
    chaos_game.create_triangle(color)


def sierp_carpet():
    global drawing2
    drawing2 = True
    chaos_game.create_square(color)



choose_color = Button(root, text = 'Choose color', width = 25, command = create_color_palette)
choose_color.place(x = 745, y = 10)
canvas.create_rectangle(940, 15, 955, 30, fill = 'black', tag = 'temp')
canvas.create_text(855, 50, font = ('Arial', 11, 'bold'), text = 'Depth of frequency portrait')

spinbox = Spinbox(root, width = 30, textvariable = deep, justify = CENTER, from_ = 1, to = 7, state = 'readonly')
spinbox.place(x = 745, y = 65)
combobox = Combobox(root, values = genetic_names, width = 35, state = 'readonly', justify = CENTER)
combobox.current(0)
combobox.place(x = 745, y = 100)

button_omicron = Button(root, text = 'Fractal portrait', width = 17, command = genetic_fractal)
button_omicron.place(x = 745, y = 135)
button_percent_covid = Button(root, text = 'Frequency fractal portrait', width = 30, command = lambda: main_func(genetic_codes[combobox.get()], array_rgb))
button_percent_covid.place(x = 745, y = 170)
button_percent_omicron = Button(root, text = 'Amount of nitrogenous bases', width = 30, command = lambda: get_percents(genetic_codes[combobox.get()]))
button_percent_omicron.place(x = 745, y = 205)
button_finish = Button(root, text = 'Stop', width = 9, command = stop_drawing)
button_finish.place(x = 890, y = 135)
progress_bar = Progressbar(root, length = 240)

canvas.create_line(710, 0, 710, 700, width = 7, fill = 'green')
canvas.create_line(710, 270, 1000, 270, width = 7, fill = 'green')
canvas.create_line(710, 435, 1000, 435, width = 7, fill = 'green')

canvas.create_text(855, 290, font = ('Arial', 11, 'bold'), text = 'Difference between 2 sequences')
combobox2 = Combobox(root, values = genetic_names, width = 35, state = 'readonly', justify = CENTER)
combobox2.place(x = 745, y = 315)
combobox2.current(0)
combobox3 = Combobox(root, values = genetic_names, width = 35, state = 'readonly', justify = CENTER)
combobox3.place(x = 745, y = 345)
combobox3.current(1)
button_find_difference = Button(root, text = 'Find difference', width = 30, command = find_difference)
button_find_difference.place(x = 745, y = 375)

canvas.create_text(855, 455, font = ('Arial', 11, 'bold'), text = 'Fractals with Chaos Game')
canvas.create_text(765, 480, font = ('Arial', 9, 'bold'), text = 'Amount of dots: ')
spinbox = Spinbox(root, width = 30, justify = CENTER, from_ = 8000, to = 20000, increment = 500, state = 'readonly', textvariable = amount_of_dots)
spinbox.place(x = 810, y = 472)
button_triangle_sierpinskiy = Button(root, width = 30, text = 'Sierpinski triangle', command = sierp_triangle)
button_triangle_sierpinskiy.place(x = 745, y = 505)
button_square_sierpinskiy = Button(root, width = 30, text = 'Sierpinski carpet', command = sierp_carpet)
button_square_sierpinskiy.place(x = 745, y = 540)




