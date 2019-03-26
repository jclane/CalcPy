import tkinter as tk
import ast
import operator
from math import sqrt


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.equation = tk.StringVar()
        self.equation.set("0")
        self.calc_mem = tk.IntVar()
        self.calc_mem.set(0)
        #self.equation_arr = [] #may or may not use this to build equation string
        
        self.container = tk.Frame(self)
        self.container.grid(column=0, row=0, sticky="NSEW")
        
        self.screens = tk.Frame(self.container, bg="red")
        self.screens.grid(column=0, row=0, padx=5, pady=5, sticky="EW")
        self.screens.grid_rowconfigure(0, weight = 1)
        self.screens.grid_columnconfigure(0, weight = 1)
        
        self.result_box = tk.Listbox(self.screens)
        self.result_box.grid(column=0, row=0, columnspan=2, sticky="EW")
        self.entry_box = tk.Entry(self.screens, textvariable=self.equation)
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
        tk.Button(self.buttons, text="±").grid(column=3, row=3, padx=2.5, 
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
                  command=lambda num="%": 
                  self.insert_to_entry_box(num)).grid(column=4, row=4, 
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
        tk.Button(self.buttons, text="1/x").grid(column=4, row=5, 
                                                 padx=2.5, pady=2.5, 
                                                 sticky="EW")
        
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
        tk.Button(self.buttons, text=".").grid(column=2, row=7, padx=2.5, 
                                               pady=2.5, sticky="EW")
        tk.Button(self.buttons, text="+", 
                  command=lambda num="+": 
                  self.insert_to_entry_box(num)).grid(column=3, row=7, 
                                                      padx=2.5, pady=2.5, 
                                                      sticky="EW")
       
        self.bind("<Return>", self.do_maths)
        self.buttons.bind_all("<Key>", self.key_press)
    
    def insert_to_history_box(self, equation):
        self.result_box.insert(tk.END, equation)
    
    def insert_to_entry_box(self, value):
        if self.equation.get() == "0":
            self.equation.set("")
        self.entry_box.insert(tk.END, value)

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
        
    def do_maths(self, evt=None):
        self.insert_to_history_box(self.equation.get())        
        self.result = Calc.evaluate(self.equation.get())
        self.equation.set(self.result)
    
    def mem_recall(self):
        try:
            self.equation.set(self.calc_mem.get())
        except tk.TclError:
            self.equation.set("ERROR: Could not display memory.")
            self.mem_clear()
            
    def mem_clear(self):
        self.calc_mem.set(0)
        
    def mem_store(self):
        try:
            self.calc_mem.set(int(self.equation.get()))
        except ValueError:
            self.equation.set("ERROR: Numbers only.")
            self.mem_clear()
        
    def mem_plus(self):
        self.insert_to_entry_box(int(self.equation.get()) + 
                                 self.calc_mem.get())
        self.insert_to_history_box(self.equation.get() + " + " +
                                   str(self.calc_mem.get()) + " (M)")
        
    def mem_minus(self):
        self.insert_to_entry_box(int(self.equation.get()) - 
                                 self.calc_mem.get())
        self.insert_to_history_box(self.equation.get() + " - " + 
                                   str(self.calc_mem.get()) + " (M)")
    
    def back(self):
        self.entry_box.delete(len(self.entry_box.get()) - 1, tk.END)
    
    def add_to_equation_arr(self):
        pass
        
    def key_press(self, evt):
        key_pressed = evt.char
        if key_pressed in "1234567890+-*/":
            self.insert_to_entry_box(key_pressed)

            
class Calc(ast.NodeVisitor):
    """ 
    Evaluates string equation and adheres to order of operations.
    
    Stolen from:  
    https://stackoverflow.com/questions/33029168/how-to-calculate-an-equation-in-a-string-python
    """
    OP_MAP = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Invert: operator.neg,
    }

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return Calc.OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])        

if __name__ == "__main__":
    app = Main()
    app.mainloop()
