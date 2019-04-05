import tkinter as tk
from operator import add, sub, mul, truediv, pow
from math import sqrt


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("CalcPy")
        self.resizable(0, 0)
        self.equation = tk.StringVar()
        self.equation.set("0")
        self.calc_mem = tk.IntVar()
        self.calc_mem.set(0)
        self.equation_arr = []

        self.container = tk.Frame(self)
        self.container.grid(column=0, row=0, sticky="NSEW")

        self.screens = tk.Frame(self.container, bg="red")
        self.screens.grid(column=0, row=0, padx=5, pady=5, sticky="EW")
        self.screens.grid_rowconfigure(0, weight = 1)
        self.screens.grid_columnconfigure(0, weight = 1)

        self.result_box = tk.Listbox(self.screens)
        self.result_box.grid(column=0, row=0, columnspan=2, sticky="EW")

        self.entry_box = tk.Entry(self.screens, textvariable=self.equation,
                                  state="readonly", readonlybackground="white")
        self.entry_box.grid(column=0, row=1, columnspan=5, sticky="EW")

        self.buttons = tk.Frame(self.container)
        self.buttons.grid(column=0, row=1, sticky="EW")
        tk.Button(self.buttons, text="MC",
                  command=self.mem_clear).grid(column=0, row=2, padx=2.5,
                                               pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="MR",
                  command=self.mem_recall).grid(column=1, row=2, padx=2.5,
                                                pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="MS",
                  command=self.mem_store).grid(column=2, row=2, padx=2.5,
                                               pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="M+",
                  command=self.mem_plus).grid(column=3, row=2, padx=2.5,
                                              pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="M-",
                  command=self.mem_minus).grid(column=4, row=2, padx=2.5,
                                               pady=2.5, sticky="EW")

        tk.Button(self.buttons, text="C",
                  command=self.clear).grid(column=0, row=3, padx=2.5,
                                           pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="←",
                  command=self.back).grid(column=1, row=3, columnspan=2,
                                          padx=2.5, pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="±",
                  command=self.posineg).grid(column=3, row=3, padx=2.5,
                                          pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="√",
                  command=self.square_root).grid(column=4, row=3, padx=2.5,
                                                 pady=2.5, sticky="EW")

        tk.Button(self.buttons, text="7",
                  command=lambda num="7":
                  self.insert_to_entry_box(num)).grid(column=0, row=4,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="8",
                  command=lambda num="8":
                  self.insert_to_entry_box(num)).grid(column=1, row=4,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="9",
                  command=lambda num="9":
                  self.insert_to_entry_box(num)).grid(column=2, row=4,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="/",
                  command=lambda num="/":
                  self.insert_to_entry_box(num)).grid(column=3, row=4,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="%",
                  command=self.do_percent_maths).grid(column=4, row=4,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")

        tk.Button(self.buttons, text="4",
                  command=lambda num="4":
                  self.insert_to_entry_box(num)).grid(column=0, row=5,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="5",
                  command=lambda num="5":
                  self.insert_to_entry_box(num)).grid(column=1, row=5,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="6",
                  command=lambda num="6":
                  self.insert_to_entry_box(num)).grid(column=2, row=5,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="*",
                  command=lambda num="*":
                  self.insert_to_entry_box(num)).grid(column=3, row=5,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="1/n",
                  command=self.recipro).grid(column=4, row=5, padx=2.5,
                                             pady=2.5, sticky="EW")

        tk.Button(self.buttons, text="1",
                  command=lambda num="1":
                  self.insert_to_entry_box(num)).grid(column=0, row=6,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="2",
                  command=lambda num="2":
                  self.insert_to_entry_box(num)).grid(column=1, row=6,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="3",
                  command=lambda num="3":
                  self.insert_to_entry_box(num)).grid(column=2, row=6,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="-",
                  command=lambda num="-":
                  self.insert_to_entry_box(num)).grid(column=3, row=6,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")
        tk.Button(self.buttons, text="=",
                  command=self.do_maths).grid(column=4, row=6,
                                              rowspan=2, padx=2.5,
                                              pady=2.5, sticky="NSEW")

        tk.Button(self.buttons, text="0",
                  command=lambda num="0":
                  self.insert_to_entry_box(num)).grid(column=0, row=7,
                                                      columnspan=2, padx=2.5,
                                                      pady=2.5, sticky="EW")
        tk.Button(self.buttons, text=".",
                  command=lambda num=".":
                  self.insert_to_entry_box(num)).grid(column=2, row=7, padx=2.5,
                                                      pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="+",
                  command=lambda num="+":
                  self.insert_to_entry_box(num)).grid(column=3, row=7,
                                                      padx=2.5, pady=2.5,
                                                      sticky="EW")

        self.set_bindings()

    def set_bindings(self):
        self.buttons.bind_all("<Return>", self.do_maths)
        self.buttons.bind_all("<Key-+>", self.insert_to_entry_box)
        self.buttons.bind_all("<Key-->", self.insert_to_entry_box)
        self.buttons.bind_all("<Key-*>", self.insert_to_entry_box)
        self.buttons.bind_all("<Key-/>", self.insert_to_entry_box)
        self.result_box.bind("<ButtonRelease-1>", self.click_history_item)
        self.buttons.bind_all("<BackSpace>", self.back)
        for num in range(0, 9):
            self.buttons.bind_all("Key-" + str(num) + ">", self.insert_to_entry_box)

    def click_history_item(self, evt):
        if evt.widget.curselection():
            self.equation.set(evt.widget.get(evt.widget.curselection()[0]))
            self.equation_arr = self.equation.get().split(" ")

    def insert_to_history_box(self, equation):
        self.result_box.insert(tk.END, equation)

    def insert_to_entry_box(self, value):
        if hasattr(value, "char"):
            value = value.char
        if value in "+-*/":
            self.equation_arr.append(value)
        if value in "0123456789":
            if len(self.equation_arr) and self.equation_arr[-1] not in "+-*/":
                self.equation_arr[-1] += value
            else:
                self.equation_arr.append(value)
        elif value == "." and "." not in self.equation_arr[-1]:
            self.equation_arr[-1] += value
        self.equation_arr = [num if not num.startswith("0") or
                             "." in num else
                             num[1:] for num in self.equation_arr]
        self.equation.set("".join(self.equation_arr))

    def square_root(self):
        try:
            self.result = sqrt(float(self.equation.get()))
            self.insert_to_history_box("sqrt(" +
                                       str(self.equation.get()) + ")")
            self.equation.set("")
            self.insert_to_entry_box(self.result)
        except ValueError:
            self.equation.set("ERROR: Numbers only.")

    def clear(self):
        self.equation.set("")
        self.equation_arr = []

    def do_maths(self, evt=None):
        if self.equation.get():

            self.insert_to_history_box(self.equation.get())
            try:
                self.result = eval(self.equation.get(),
                                   {},
                                   {"add":add,
                                    "sub":sub,
                                    "mul":mul,
                                    "truediv":truediv,
                                    "sqrt":sqrt,
                                    "pow":pow}
                                   )
            except ZeroDivisionError:
                self.result = "ERROR: Cannot divide by zero"
            self.equation_arr = [str(self.result)]
            self.equation.set(self.result)

    def do_percent_maths(self):
        if self.equation.get():
            self.equation_arr[-1] = str(eval("(" + "".join(self.equation_arr[0:len(self.equation_arr)-2]) + ")*." + self.equation_arr[-1], {}, {"mul":mul}))
            self.do_maths()

    def mem_recall(self):
        try:
            self.equation.set(self.calc_mem.get())
        except tk.TclError:
            self.equation.set("ERROR: Could not display memory.")
            self.mem_clear()

    def mem_clear(self):
        self.calc_mem.set("0")
        self.insert_to_history_box(self.equation.get() + " no longer stored.")

    def mem_store(self):
        try:
            self.calc_mem.set(self.equation.get())
            self.insert_to_history_box(self.equation.get() + " (M)")
        except ValueError:
            self.equation.set("ERROR: Not a number.")
            self.mem_clear()

    def mem_plus(self):
        try:
            result = int(self.equation.get()) + int(self.calc_mem.get())
            self.insert_to_history_box([self.equation.get(), "+", self.calc_mem.get()])
            self.equation_arr = []
            self.equation.set("0")
            self.insert_to_entry_box(str(result))

        except ValueError:
            self.equation.set("ERROR: Not a number.")
            self.mem_clear()

    def mem_minus(self):
        try:
            self.insert_to_entry_box(str(int(self.equation.get()) -
                                     self.calc_mem.get()))
            self.insert_to_history_box([str(self.equation.get()), " - ",
                                       str(self.calc_mem.get()), " (M)"])
        except ValueError:
            self.equation.set("ERROR: Not a number.")
            self.mem_clear()

    def back(self, evt=None):
        if self.equation_arr:
            del self.equation_arr[-1]
            self.equation.set("".join(self.equation_arr))

    def posineg(self, evt=None):
        if self.equation_arr[-1].startswith("-"):
            self.equation_arr[-1] = self.equation_arr[-1][1:]
        else:
            self.equation_arr[-1] = "-" + self.equation_arr[-1]
        self.equation.set("".join(self.equation_arr))

    def recipro(self):
        self.equation.set("1/" + self.equation.get())
        self.do_maths()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
