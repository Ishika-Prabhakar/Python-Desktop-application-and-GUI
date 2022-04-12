from tkinter import Tk,Button,Label,DoubleVar,Entry
from typing import Text

window = Tk()
window.title("Height Conversion App")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width=False,height=False)

def convert():
    value = float(ft_Entry.get())
    cm = value*30.48
    cmt_value.set("%.4f" % cm)


def clear():
    ft_value.set("")
    cmt_value.set("")


ft_ldl = Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_ldl.grid(column=0,row=0,padx=15,pady=15)

ft_value = DoubleVar()
ft_Entry = Entry(window,textvariable=ft_value,width=14)
ft_Entry.grid(column=1,row=0)
ft_Entry.delete(0,'end')

cmt_ldl = Label(window,text="Centimeter",bg = "brown",fg = "white",width = 14)
cmt_ldl.grid(column=0,row=1)

cmt_value = DoubleVar()
cmt_Entry = Entry(window,textvariable=cmt_value,width=14)
cmt_Entry.grid(column=1,row=1,pady=30)
cmt_Entry.delete(0,'end')


convert_btn = Button(window,text="Convert",bg="blue",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)

clear_btn = Button(window,text='Clear',bg="blue",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)





window.mainloop()