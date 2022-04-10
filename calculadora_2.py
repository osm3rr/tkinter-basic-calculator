# Diseño de una calculadora calculadora
# bodeguera básica 

# --- Librerías necesarias 
from tkinter import *

base_screen = Tk()

# titulo de la ventana
base_screen.title('Calculadora bodeguera')

# Frame base
base_frame = Frame(base_screen)

base_frame.pack()



# ----- result screen ----
# https://www.pythontutorial.net/tkinter/tkinter-stringvar/

# Se define el tipo de variable,
# que estará ingresando en la pantalla

number_screen = StringVar()



result_screen = Entry(base_frame, 
                      textvariable= number_screen,
                      fg='yellow',
                      bg='black',
                      justify='right',
                      width=30)

# * textvariable: define el tipo de 
# variable que será el dato de entrada.
# * width: define el tamaño del widget

# * justify: alinea el texto, 
# que aparece en el widget.
# 

result_screen.grid(row=1, column=1,
                   padx=10, pady=10,
                   columnspan=4)
# columnspan, define el número de columnas
# que se pueden abarcar por el widget



#---- Row 1 ----
button_7 = Button(base_frame, text= "7",
                  width=3)
button_7.grid(row=2, column=1)

button_8 = Button(base_frame, text= "8",
                  width=3)
button_8.grid(row=2, column=2)

button_9 = Button(base_frame, text= "9",
                  width=3)
button_9.grid(row=2, column=3)

button_div = Button(base_frame, text= "/",
                  width=3)
button_div.grid(row=2, column=4)



#---- Row 2 ----
button_4 = Button(base_frame, text= "4",
                  width=3)
button_4.grid(row=3, column=1)

button_5 = Button(base_frame, text= "5",
                  width=3)
button_5.grid(row=3, column=2)

button_6 = Button(base_frame, text= "6",
                  width=3)
button_6.grid(row=3, column=3)

button_mult = Button(base_frame, text= "x",
                  width=3)
button_mult.grid(row=3, column=4)




#---- Row 3 ----
button_1 = Button(base_frame, text= "1",
                  width=3)
button_1.grid(row=4, column=1)

button_2 = Button(base_frame, text= "2",
                  width=3)
button_2.grid(row=4, column=2)

button_3 = Button(base_frame, text= "3",
                  width=3)
button_3.grid(row=4, column=3)

button_sub = Button(base_frame, text= "-",
                  width=3)
button_sub.grid(row=4, column=4)


#---- Row 4 ----

button_0 = Button(base_frame, text= "0",
                  width=3)
button_0.grid(row=5, column=1)

button_comma = Button(base_frame, text= ",",
                  width=3)
button_comma.grid(row=5, column=2)

button_equal = Button(base_frame, text= "=",
                  width=3, bg='DarkGreen')
button_equal.grid(row=5, column=3)

button_sum = Button(base_frame, text= "+",
                  width=3)
button_sum.grid(row=5, column=4)





base_screen.mainloop()