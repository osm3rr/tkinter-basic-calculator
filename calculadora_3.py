# Calculadora básica v3

# librerías necesarias
from tkinter import *
import tkinter.font as font


# Pantalla principal
root = Tk()

root.configure( bg="black" )
root.title("Calculadora-v3")
root.geometry('270x180')

my_font = font.Font( family='Helvetica' , size=14)

equation = StringVar()

# Second part: funciones para realizar las operaciones.
def press(btn):
    return equation.set( equation.get() + str( btn ) )
    #print( equation.get() )


def equal_press():
    try:
        #total = str(eval(equation.get()))
        
        return equation.set( str(eval(equation.get())) )
    
    except:
        return equation.set("ERROR")

# Clear funcion
def clear():
    return equation.set('')
        

# Data entry
expression_entry = Entry( root, textvariable=equation )
expression_entry.grid( row=0, columnspan=4, sticky='nswe' )


# Hexadecimal Colors: https://www.colorhexa.com/color-names
# ******* Buttons row 1**********
btn_7 = Button( root, text=" 7 ", fg="#fff", bg="#666", command=lambda: press(7) )
btn_7.grid( row=1, column=0, sticky='nswe' )
btn_7['font'] = my_font

btn_8 = Button( root, text=" 8 ", fg="#fff", bg="#666", command=lambda: press(8))
btn_8.grid( row=1, column=1, sticky='nswe' )
btn_8['font'] = my_font

btn_9 = Button( root, text=" 9 ", fg="#fff", bg="#666", command=lambda: press(9))
btn_9.grid( row=1, column=2, sticky='nswe' )
btn_9['font'] = my_font

# ******* Buttons row 2**********
btn_4 = Button( root, text=" 4 ", fg="#fff", bg="#666", command=lambda: press(4))
btn_4.grid( row=2, column=0, sticky='nswe' )
btn_4['font'] = my_font

btn_5 = Button( root, text=" 5 ", fg="#fff", bg="#666", command=lambda: press(5))
btn_5.grid( row=2, column=1, sticky='nswe' )
btn_5['font'] = my_font

btn_6 = Button( root, text=" 6 ", fg="#fff", bg="#666", command=lambda: press(6))
btn_6.grid( row=2, column=2, sticky='nswe' )
btn_6['font'] = my_font

# ******* Buttons row 3**********
btn_1 = Button( root, text=" 1 ", fg="#fff", bg="#666", command=lambda: press(1))
btn_1.grid( row=3, column=0, sticky='nswe' )
btn_1['font'] = my_font

btn_2 = Button( root, text=" 2 ", fg="#fff", bg="#666", command=lambda: press(2))
btn_2.grid( row=3, column=1, sticky='nswe' )
btn_2['font'] = my_font

btn_3 = Button( root, text=" 3 ", fg="#fff", bg="#666", command=lambda: press(3))
btn_3.grid( row=3, column=2, sticky='nswe' )
btn_3['font'] = my_font

# ********** Buttons row 4 **********

btn_0 = Button( root, text=" 0 ", fg="#fff", bg="#008000", command=lambda: press(0))
btn_0.grid( row=4, column=0, sticky='nswe', columnspan=2 )
btn_0['font'] = my_font

# *********decimal dot ***********
btn_dot = Button( root, text=" . ", fg="#fff", bg="#cc5500", command=lambda: press('.'))
btn_dot.grid( row=4, column=2, sticky='nswe' )
btn_dot['font'] = my_font

# math operator
plus = Button( root, text=' + ', fg="#fff", bg='#007aa5' , command=lambda: press('+'))
plus.grid( row=1, column=3, sticky='nswe' )
plus['font'] = my_font

minus = Button( root, text=' - ', fg="#fff", bg='#007aa5' , command=lambda: press('-'))
minus.grid( row=2, column=3, sticky='nswe' )
minus['font'] = my_font

multiplication = Button( root, text=' * ', fg="#fff", bg='#007aa5' , command=lambda: press('*'))
multiplication.grid( row=3, column=3, sticky='nswe' )
multiplication['font'] = my_font

div = Button( root, text=' / ', fg="#fff", bg='#007aa5' , command=lambda: press('/'))
div.grid( row=4, column=3, sticky='nswe' )
multiplication['font'] = my_font

# equal button
equal = Button( root, text=" = ", fg="#fff", bg="#e03c31", command=equal_press)
equal.grid( row=5, column=0, sticky='nswe', columnspan=2 )
equal['font'] = my_font

# Clear button
clear = Button( root, text=" clear ", fg="#fff", bg="#002e63", command=clear)
clear.grid( row=5, column=2, sticky='nswe', columnspan=2 )
clear['font'] = my_font

root.mainloop()