from tkinter import *

root = Tk()
canvas = Canvas(root, width = 1000, height = 700)
canvas.pack()

cx = [0, 700, 700, 0]
cy = [0, 0, 700, 700]
codons = StringVar()


number_pairs_covid = {}
number_pairs_omicron = {}
result_pairs = {}

for i in array:
    number_pairs_covid[i] = covid_19.count(i)
    number_pairs_omicron[i] = covid_omicron.count(i)

def create_genetic_fractal():
    trace_x = 350
    trace_y = 350
    a, t, c, g = 0, 0, 0, 0
    genetic_code2 = str(codons.get())
    genetic_code2 = ''.join(filter(str.isalpha, genetic_code2))
    if genetic_code2:
        for i in range(len(genetic_code2)):
            if genetic_code2[i] == 't':
                trace_x = (trace_x + cx[0]) / 2
                trace_y = (trace_y + cy[0]) / 2
                t += 1
            elif genetic_code2[i] == 'c':
                trace_x = (trace_x + cx[1]) / 2
                trace_y = (trace_y + cy[1]) / 2
                c += 1
            elif genetic_code2[i] == 'a':
                trace_x = (trace_x + cx[2]) / 2
                trace_y = (trace_y + cy[2]) / 2
                a += 1
            elif genetic_code2[i] == 'g':
                trace_x = (trace_x + cx[3]) / 2
                trace_y = (trace_y + cy[3]) / 2
                g += 1
            else:
                label1 = Label(root, text = "Стрічка містить некоректні букви!", font = 'Times 25', fg = 'red').place(x = 250, y = 250)
                break
            canvas.create_oval(trace_x, trace_y, trace_x + 2.5, trace_y + 2.5, fill = 'black')
            root.update()

label1 = Label(root, width = 30, text = "Введіть генетичний код: ", font = 'Times 13').place(x = 690, y = 15)
entry = Entry(root, width = 28, textvariable = codons).place(x = 735, y = 45)
button1 = Button(root, text = "Зобразити фрактал", width = 30, command = create_genetic_fractal).place(x = 735, y = 75)
result_pairs[i] = number_pairs_covid[i] - number_pairs_omicron[i]
