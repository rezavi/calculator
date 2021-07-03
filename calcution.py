from tkinter import *
from tkinter import ttk


win = Tk()
def click_button(number):
    input_entry.insert(END,number)


#--------------------***BACK_END OF ClEAR  BUTTON***-----------------#
def clear():
    input_entry.delete(0, END)


#--------------------***BACK_END OF ADD BUTTON***-----------------#
def add_button():
    global f_num
    global sign
    f_num = input_entry.get()
    sign = "additional"
    input_entry.delete(0, END)


#--------------------***BACK_END OF SUBMISSION BUTTON***-----------------#
def mines_button():
    global f_num
    global sign
    f_num = input_entry.get()
    sign = "submission"
    input_entry.delete(0, END)


#--------------------***BACK_END OF MULTIPLE  BUTTON***-----------------#
def multi_button():
    global f_num
    global sign
    f_num = input_entry.get()
    sign = "multiple"
    input_entry.delete(0, END)


#--------------------***BACK_END OF DIVISION BUTTON***-----------------#
def divi_button():
    global f_num
    global sign
    f_num = input_entry.get()
    sign = "division"
    input_entry.delete(0, END)


#--------------------***BACK_END OF RESULT BUTTON***-----------------#
def equal_button():
    
    current = input_entry.get()
    input_entry.delete(0, END)

    if sign == "additional":
        input_entry.insert(END, float(f_num) + float(current))

    elif sign == "submission":
        input_entry.insert(END, float(f_num) - float(current))
    
    elif sign == "multiple":
        input_entry.insert(END, float(f_num) * float(current))
    
    elif sign == "division":
        input_entry.insert(END, float(f_num) // float(current))
        

#---------------UI------------------#
top_frame = Frame(win, bg = '#090622' ,borderwidth=0).place(x = 0 , y = 0 , width= 350, height= 100)
input_entry = Entry(top_frame,bg = "#0d0831", font = "Tahoma 19 bold", highlightbackground="yellow",fg = "#e3d965")
input_entry.place(x = 15 , y = 15 ,width=320, height=70,)
center_frame = Frame(win, bg = '#050315' ,borderwidth=20).place(x = 0 , y =  100 , width= 350, height= 350)


#-----------------------------***photo of number ***----------------------------------------#
img0 = PhotoImage(file="/home/reza/Downloads/calc_pic/0.png")
img1 = PhotoImage(file="/home/reza/Downloads/calc_pic/1.png",)
img2 = PhotoImage(file="/home/reza/Downloads/calc_pic/2.png")
img3 = PhotoImage(file="/home/reza/Downloads/calc_pic/3.png")
img4 = PhotoImage(file="/home/reza/Downloads/calc_pic/4.png")
img5 = PhotoImage(file="/home/reza/Downloads/calc_pic/5.png")
img6 = PhotoImage(file="/home/reza/Downloads/calc_pic/6.png")
img7 = PhotoImage(file="/home/reza/Downloads/calc_pic/7.png")
img8 = PhotoImage(file="/home/reza/Downloads/calc_pic/8.png")
img9 = PhotoImage(file="/home/reza/Downloads/calc_pic/9.png")


#---------------------------------*** photo of 4 action ***------------------------------_#
img_dot = PhotoImage(file="/home/reza/Downloads/calc_pic/dot.png")
img_equal = PhotoImage(file="/home/reza/Downloads/calc_pic/mosavi5.png")
img_mines = PhotoImage(file="/home/reza/Downloads/calc_pic/menha.png")
img_multi = PhotoImage(file="/home/reza/Downloads/calc_pic/zarb.png")
img_plus = PhotoImage(file="/home/reza/Downloads/calc_pic/plus.png")
img_div = PhotoImage(file="/home/reza/Downloads/calc_pic/tagsim.png")
img_reset = PhotoImage(file = "/home/reza/Downloads/calc_pic/reset4.png")


#--------------------***Button of number ***---------------------#
btn1 = Button(center_frame,image = img7,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground= "#050315",command = lambda: click_button(7))
btn1.place(x = 5 , y = 170,)
btn2 = Button(center_frame,image = img8,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground= "#050315",command = lambda: click_button(8))
btn2.place(x = 95 , y = 170,)
btn3 = Button(center_frame,image = img9,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground= "#050315",command = lambda: click_button(9))
btn3.place(x = 185 , y = 170,)
btn4 = Button(center_frame,image = img4,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground="#050315",command = lambda: click_button(4))
btn4.place(x = 5 , y = 240)
btn5 = Button(center_frame,image = img5,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(5))
btn5.place(x = 95 , y = 240)
btn6 = Button(center_frame,image = img6,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(6))
btn6.place(x = 185 , y = 240)
btn7 = Button(center_frame,image = img1,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(1))
btn7.place(x = 5 , y = 310,)
btn8 = Button(center_frame,image = img2,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(2))
btn8.place(x = 95 , y = 310,)
btn9 = Button(center_frame,image = img3,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(3))
btn9.place(x = 185 , y = 310,)
btn0 = Button(center_frame,image = img0,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button(0))
btn0.place(x = 95 , y = 380,)
btn_dot = Button(center_frame,image = img_dot,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground= "#050315",command = lambda: click_button('.'))
btn_dot.place(x = 5 , y = 380,)


#----------------------***Button of 4 action***---------------------------#
btn_equal = Button(center_frame,image = img_equal,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground="#050315",command = equal_button)
btn_equal.place(x = 185, y = 382,)
btn_mines = Button(center_frame,image = img_mines,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground= "#050315",command = mines_button)
btn_mines.place(x = 275 , y = 173)
btn_multi = Button(center_frame,image = img_multi,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground= "#050315",command= multi_button)
btn_multi.place(x = 275 , y = 242,)
btn_plus = Button(center_frame,image = img_plus,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground="#050315",command = add_button)
btn_plus.place(x = 275 , y = 311)
btn_div = Button(center_frame,image = img_div,borderwidth= 0,bg = "#050315", highlightbackground="#050315",
activebackground="#050315", command= divi_button)
btn_div.place(x = 275 , y = 106)
btn_reset = Button(center_frame,image = img_reset,borderwidth= 0,bg = "#050315", highlightbackground="#050315"
,activebackground="#050315", command = clear)
btn_reset.place(x = 7 , y = 101)


#--------------***Config Win***----------------------#
icon_photo = PhotoImage(file = "/home/reza/Downloads/10471853.png")
win.iconphoto(False,icon_photo)
win.geometry("350x450") 
win.mainloop()

