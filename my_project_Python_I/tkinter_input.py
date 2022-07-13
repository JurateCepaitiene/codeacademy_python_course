import string
from tkinter import *
import math
import colorsys
import idtranscoder

def color_hex(x : float):
    return format(max(0, min(255, int(x * 255.0))), "02x")

class Colorama:
    def __init__(self, window, window_width, window_height):
        self.window = window
        # self.canvas = None
        self.window_width = window_width
        self.window_height = window_height
        self.rect1_dim = 200
        self.rect1_x0 = (self.window_width - self.rect1_dim) / 2
        self.rect1_y0 = (self.window_height - self.rect1_dim) / 2
        self.rect1_x1 = (self.window_width + self.rect1_dim) / 2
        self.rect1_y1 = (self.window_height + self.rect1_dim) / 2
        self.dt = 1/60
        self.t = 0
        self.is_running = False

    def colorama_loop(self):
        r = 0.5 + 0.5 * math.sin(2.0 * math.pi * self.t)
        g = 0.5 - 0.5 * math.cos(2.0 * math.pi * 0.85 * self.t)
        b = 0.5 - 0.5 * math.sin(2.0 * math.pi * 1.1 * self.t)
        self.canvas.itemconfig(self.rect0, state="normal", fill=f"#{color_hex(r)}{color_hex(g)}{color_hex(b)}")
        self.canvas.itemconfig(self.rect1, state="normal", fill=f"#{color_hex(1.0-r)}{color_hex(1.0-g)}{color_hex(1.0-b)}")
        self.canvas.pack()
        self.t += self.dt
        if self.is_running:
            self.window.after(int(self.dt * 1000), self.colorama_loop)
        else:
            self.canvas.destroy()

    def colorama_start(self):
        if self.is_running == False:
            personal_color.personal_color_end()
            self.canvas = Canvas(self.window, width=self.window_width, height=self.window_height)
            self.rect0 = self.canvas.create_rectangle(0, 0, self.window_width, self.window_height)
            self.rect1 = self.canvas.create_rectangle(self.rect1_x0, self.rect1_y0, self.rect1_x1, self.rect1_y1)    
            self.is_running = True
            self.window.after(0, self.colorama_loop)

    def colorama_end(self):
        if self.is_running == True:
            self.is_running = False


class PersonalColor:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.canvas = None
        self.window_width = window_width
        self.window_height = window_height
        self.color_rect_dim = (200, 150)
        self.rect_x0 = (self.window_width - self.color_rect_dim[0]) / 2
        self.rect_y0 = 50
        self.rect_x1 = (self.window_width + self.color_rect_dim[0]) / 2
        self.rect_y1 = 50 + self.color_rect_dim[1]
        self.label = Label(self.window, text="Enter your personal ID:")
        self.entry = Entry(self.window)
        self.button = Button(self.window, text="Calculate color", command=self.personal_color_calculate)
        self.error = Label(self.window, text = "")
        self.is_showing = False

    def personal_color_calculate(self, event=None):
        id = self.entry.get()
        is_valid, year, month, day, digits = idtranscoder.is_id_valid(id)
        if is_valid == True:
            self.error.config(text="The personal ID is correct! Your color can be seen below.", fg="green")
            h = (year % 100.0 + month / 12.0) / 100.0
            s = (0.5 + (digits[10] + 1) / 20.0)
            v = 1.0
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            self.canvas.itemconfig(self.color_rect, state="normal", fill=f"#{color_hex(r)}{color_hex(g)}{color_hex(b)}")
        else:
            self.error.config(text="The personal ID is incorrect!", fg="red")
            self.canvas.itemconfig(self.color_rect, state="hidden")
        self.canvas.pack()

    def personal_color_start(self):
        if self.is_showing == False:
            colorama.colorama_end()
            self.canvas = Canvas(self.window, width=self.window_width, height=self.window_height)
            self.color_rect = self.canvas.create_rectangle(self.rect_x0, self.rect_y0, self.rect_x1, self.rect_y1, state="hidden")    
            self.error.config(text="")
            self.entry.delete(0, END)
            self.entry.bind("<Return>", self.personal_color_calculate)
            self.label.pack()
            self.entry.pack()
            self.button.pack()
            self.error.pack()
            self.canvas.pack()
            self.is_showing = True

    def personal_color_end(self):
        if self.is_showing == True:
            self.entry.unbind("<Return>")
            self.label.pack_forget()
            self.entry.pack_forget()
            self.button.pack_forget()
            self.error.pack_forget()
            self.canvas.destroy()
            self.is_showing = False

window_width = 900
window_height = 500

main_page = Tk()
main_page.minsize(window_width, window_height)
main_page.maxsize(window_width, window_height)
main_page.title("Python Course Project 1")

meniu = Menu(main_page)
main_page.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)

colorama = Colorama(main_page, window_width, window_height)
personal_color = PersonalColor(main_page, window_width, window_height)

submeniu.add_command(label="Colorama", command = colorama.colorama_start)
submeniu.add_command(label="Your Personal Color", command = personal_color.personal_color_start)
submeniu.add_separator()
submeniu.add_command(label="Exit", command = exit)

main_page.mainloop()