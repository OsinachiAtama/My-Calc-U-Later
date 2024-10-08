import tkinter as tk 
from tkinter import ttk
import math

root = tk.Tk()
style = ttk.Style(root)

root.configure(bg = "black")
root.geometry("350x420")

calculation = ""

def add_to_calculation(symbol): 
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))


def evaluate_calculation(): 
    try: 
        solution = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(solution))

    except:
        clear_field()
        entry.insert(0, "Error")
  

def clear_field(): 
    entry.delete(0, tk.END)



entry = tk.Entry(root, width = 16, font = ('Courier', 24), bg = 'black', fg = 'white', highlightthickness = 0, border = None )
entry.grid(columnspan = 5, padx = 20, pady = 20)

def sin_function(): 
    try: 
        value = float(entry.get())
        result = math.sin(math.radians(float(value))) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass

def cos_function(): 
    try: 
        value = float(entry.get())
        result = math.cos(math.radians(float(value))) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass

def tan_function(): 
    try: 
        value = float(entry.get())
        result = math.tan(math.radians(float(value))) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass

def arcsin_function(): 
    try: 
        value = float(entry.get())
        result = math.degrees(math.asin(value)) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass
   
def arccos_function(): 
    try: 
        value = float(entry.get())
        result = math.degrees(math.acos(value)) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass
   
def arctan_function(): 
    try: 
        value = float(entry.get())
        result = math.degrees(math.atan(value)) #math.radians converts the angle from degrees to radians because the sine function expects the input in radians  
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")
    
    pass

def square_function(): 
    try: 
        value = float(entry.get())
        result = value**2
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")

    pass

def sqrt_function(): 
    try: 
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    
    except: 
       entry.delete(0, tk.END)
       entry.insert(0,"Error")

    pass




bstyle = {'font': ('Courier', 14), 'bg':'black', 'fg':'white'}

#Attaching functions and commands to buttons

btn_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 5, **bstyle )
btn_1.grid(row = 2, column = 1, padx = 5, pady = 5)

btn_2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 5, **bstyle )
btn_2.grid(row = 2, column = 2, padx = 5, pady = 5)

btn_3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 5, **bstyle )
btn_3.grid(row = 2, column = 3, padx = 5, pady = 5)

btn_4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 5,**bstyle )
btn_4.grid(row = 3, column = 1, padx = 5, pady = 5)

btn_5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 5, **bstyle )
btn_5.grid(row = 3, column = 2, padx = 5, pady = 5)

btn_6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 5,**bstyle )
btn_6.grid(row = 3, column = 3, padx = 5, pady = 5)

btn_7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 5, **bstyle )
btn_7.grid(row = 4, column = 1, padx = 5, pady = 5)

btn_8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 5, **bstyle )
btn_8.grid(row = 4, column = 2, padx = 5, pady = 5)

btn_9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 5, **bstyle)
btn_9.grid(row = 4, column = 3, padx = 5, pady = 5)

btn_0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 5, **bstyle )
btn_0.grid(row = 5, column = 1, padx = 5, pady = 5)

#Attaching operand buttons to functions

btn_plus = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 5,**bstyle )
btn_plus.grid(row = 2, column = 4, padx = 5, pady = 5)

btn_minus = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 5,**bstyle )
btn_minus.grid(row = 3, column = 4, padx = 5, pady = 5)

btn_multiply = tk.Button(root, text = "*", command = lambda: add_to_calculation("*"), width = 5, **bstyle )
btn_multiply.grid(row = 4, column = 4, padx = 5, pady = 5)

btn_obracket = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 5, **bstyle )
btn_obracket.grid(row = 5, column = 2, padx = 5, pady = 5)

btn_cbracket = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 5, **bstyle )
btn_cbracket.grid(row = 5, column = 3, padx = 5, pady = 5)

btn_divide = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 5, **bstyle )
btn_divide.grid(row = 5, column = 4, padx = 5, pady = 5)

#Attaching trig functions to buttons
btn_sine = tk.Button(root, text = "sin", command = sin_function, width = 5, **bstyle )
btn_sine.grid(row = 6, column = 1, padx = 5, pady = 5)

btn_cos = tk.Button(root, text = "cos", command = cos_function, width = 5, **bstyle )
btn_cos.grid(row = 6, column = 2, padx = 5, pady = 5) 

btn_tan = tk.Button(root, text = "tan", command = tan_function, width = 5, **bstyle )
btn_tan.grid(row = 6, column = 3, padx = 5, pady = 5)

btn_sq = tk.Button(root, text = "x²", command = square_function, width = 5, **bstyle )
btn_sq.grid(row = 6, column = 4, padx = 5, pady = 5)

btn_asine = tk.Button(root, text = "asin", command = arcsin_function, width = 5, **bstyle )
btn_asine.grid(row = 7, column = 1, padx = 5, pady = 5)

btn_acos = tk.Button(root, text = "acos", command = arccos_function, width = 5, **bstyle )
btn_acos.grid(row = 7, column = 2, padx = 5, pady = 5)

btn_atan = tk.Button(root, text = "atan", command = arctan_function, width = 5, **bstyle )
btn_atan.grid(row = 7, column = 3, padx = 5, pady = 5)

btn_sqrt = tk.Button(root, text = "√x", command = sqrt_function, width = 5, **bstyle)
btn_sqrt.grid(row = 7, column = 4, padx = 5, pady = 5)

btn_clear = tk.Button(root, text = "A/C", command = clear_field, width = 5,**bstyle )
btn_clear.grid(row = 8, column = 1, padx = 5, pady = 5)

btn_dot = tk.Button(root, text = ".", command = lambda: add_to_calculation("."), width = 5, **bstyle )
btn_dot.grid(row = 8, column = 2, padx = 5, pady = 5)

btn_equal = tk.Button(root, text = "=", command = evaluate_calculation, width = 5, **bstyle )
btn_equal.grid(row = 8, column = 3, padx = 5, pady = 5)




root.mainloop()
