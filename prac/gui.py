#create GUI login
from tkinter import *

exp=""
def convert(x):
    weight=float(x)
    global exp
    exp=str(weight*1000.0)
    equation.set(exp)
    print(exp)
    
gui=Tk()
gui.configure(background="red")
gui.title("Converter")

equation=StringVar()
expression_field=Entry(gui,textvariable=equation)
expression_field.grid(columnspan=5,ipadx=70)

button_convert=Button(gui,text='Convert',fg='white',bg='blue',command=lambda: convert(expression_field.get()),height=1,width=10)
button_convert.grid(row=1,column=2)

v=StringVar(gui,"1")
radio_button=RadioButton(gui,text='toggle',variable=v,value=False)
radio_button.grid(row=2,column=2)

gui.mainloop()
