# Calculadora básica v3

# librerías necesarias
from tkinter import *

from matplotlib.pyplot import text
from sqlalchemy import column
from torch import equal


# Pantalla principal
root = Tk()

root.configure( bg="black" )
root.title("Calculadora-v3")
root.geometry('350x170')

# Entry para la entrada de datos
equation = StringVar()
expression_entry = Entry( root, textvariable=equation )
expression_entry.grid( row=0, columnspan=4, sticky='nswe' )


# Colores en hexadecimal: https://www.colorhexa.com/color-names
# ******* Botones de row 1**********
btn_7 = Button( root, text=" 7 ", fg="#fff", bg="#666")
btn_7.grid( row=1, column=0, sticky='nswe' )

btn_8 = Button( root, text=" 8 ", fg="#fff", bg="#666")
btn_8.grid( row=1, column=1, sticky='nswe' )

btn_9 = Button( root, text=" 9 ", fg="#fff", bg="#666")
btn_9.grid( row=1, column=2, sticky='nswe' )

# ******* Botones de row 2**********
btn_4 = Button( root, text=" 4 ", fg="#fff", bg="#666")
btn_4.grid( row=2, column=0, sticky='nswe' )

btn_5 = Button( root, text=" 5 ", fg="#fff", bg="#666")
btn_5.grid( row=2, column=1, sticky='nswe' )

btn_6 = Button( root, text=" 6 ", fg="#fff", bg="#666")
btn_6.grid( row=2, column=2, sticky='nswe' )


# ******* Botones de row 3**********
btn_1 = Button( root, text=" 1 ", fg="#fff", bg="#666")
btn_1.grid( row=3, column=0, sticky='nswe' )

btn_2 = Button( root, text=" 2 ", fg="#fff", bg="#666")
btn_2.grid( row=3, column=1, sticky='nswe' )

btn_3 = Button( root, text=" 3 ", fg="#fff", bg="#666")
btn_3.grid( row=3, column=2, sticky='nswe' )

# ********** Botones de row 4 **********

btn_0 = Button( root, text=" 0 ", fg="#fff", bg="#008000")
btn_0.grid( row=4, column=0, sticky='nswe', columnspan=2 )

# *********Punto decimal ***********
btn_dot = Button( root, text=" . ", fg="#fff", bg="#cc5500")
btn_dot.grid( row=4, column=2, sticky='nswe' )

# Botones de operadores matemáticos
plus = Button( root, text=' + ', fg="#fff", bg='#007aa5' )
plus.grid( row=1, column=3, sticky='nswe' )

minus = Button( root, text=' - ', fg="#fff", bg='#007aa5' )
minus.grid( row=2, column=3, sticky='nswe' )

multiplication = Button( root, text=' * ', fg="#fff", bg='#007aa5' )
multiplication.grid( row=3, column=3, sticky='nswe' )

div = Button( root, text=' / ', fg="#fff", bg='#007aa5' )
div.grid( row=4, column=3, sticky='nswe' )

# Botón de clear y de igual
equal = Button( root, text=" = ", fg="#fff", bg="#e03c31")
equal.grid( row=5, column=0, sticky='nswe', columnspan=2 )

clear = Button( root, text=" clear ", fg="#fff", bg="#002e63")
clear.grid( row=5, column=2, sticky='nswe', columnspan=2 )


root.mainloop()




