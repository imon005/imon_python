import tkinter as tk
 
win = tk.Tk()
 

win.geometry("312x333")
 

win.resizable(0, 0)
 

win.title("Calculator")
 

 
input = ""
 

display_text = tk.StringVar()
 

def click_button(item):
    global input
    input = input + str(item)
    display_text.set(input)
 

def clear_button(): 
    global input
    input = "" 
    display_text.set("")
 

def equal_button():
    global input
    result = str(eval(input))
    display_text.set(result)
    input = ""
     

  
input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
  
input_frame.pack(side = tk.TOP)
 

  
input_field = tk.Entry(input_frame, font=('arial', 25, 'bold'), textvariable = display_text, width=50, bg="white", bd=0, justify=tk.RIGHT)
  
input_field.grid(row=0, column=0)
  
input_field.pack(ipady=10) 

  
btns_frame = tk.Frame(win, width=312, height=272.2, bg="blue")
  
btns_frame.pack()
 

  
clear_btn = tk.Button(btns_frame, text = "AC", fg = "black", width = 32, height = 3, bd = 0, bg = "gold", cursor = "hand2", command = lambda: clear_button()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
  
divide_btn = tk.Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: click_button("/")).grid(row = 0, column = 3, padx = 1, pady = 1)  
 
btn_9 = tk.Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click_button(9)).grid(row = 1, column = 0, padx = 1, pady = 1)
  
btn_7 = tk.Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button(7)).grid(row = 1, column = 2, padx = 1, pady = 1)
  
btn_8 = tk.Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: click_button(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
  

  
multiply_btn = tk.Button(btns_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: click_button("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

  
btn_4 = tk.Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(4)).grid(row = 2, column = 2, padx = 1, pady = 1)
  
btn_5 = tk.Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
  
btn_6 = tk.Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(6)).grid(row = 2, column = 0, padx = 1, pady = 1)
  
minus_btn = tk.Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "brown", cursor = "hand2", command = lambda: click_button("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 

  
btn_1 = tk.Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: click_button(1)).grid(row = 3, column = 2, padx = 1, pady = 1)
  
btn_2 = tk.Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: click_button(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
  
btn_3 = tk.Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: click_button(3)).grid(row = 3, column = 0, padx = 1, pady = 1)
  
plus_btn = tk.Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click_button("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 

  
btn_0 = tk.Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
  
point_btn = tk.Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "purple", cursor = "hand2", command = lambda: click_button(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
  
equals_btn = tk.Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "light blue", cursor = "hand2", command = lambda: equal_button()).grid(row = 4, column = 3, padx = 1, pady = 1)
 

win.mainloop()
