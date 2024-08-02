from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

root=Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)


current_x = 0
current_y = 0
color="black"

def locate_xy(work):
    global current_x,current_y

    current_x=work.x
    current_y=work.y

def addline(work):
    global current_x,current_y

    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),
                       fill= color, capstyle=ROUND,smooth=True)
    current_x,current_y=work.x,work.y

def show_color(new_color):
    global color

    color=new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()


def insertimage():
    global filename
    global f_img

    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",
                                        filetype=(("PNG file","*.png"),("All file","new.txt")))

    f_img=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180,50,image=f_img)
    root.bind("<B3-Motion>",my_callback)

def my_callback(event):
    global f_img

    f_img=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(event.x,event.y,image=f_img)


#icon
image_icon = PhotoImage(file="D:\whiteboard project\logo.png")
root.iconphoto(False,image_icon)

#sidebar
color_box = PhotoImage(file="D:\whiteboard project\color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="D:\whiteboard project\eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

importimage= PhotoImage(file="addimage.png")
Button(root, image=importimage, bg="white",command=insertimage).place(x=30,y=450)




colors=Canvas(root,bg="#fff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id=colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))


    id=colors.create_rectangle((10,40,30,60),fill="#458B00")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#458B000'))


    id=colors.create_rectangle((10,70,30,90),fill="#9932CC")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#9932CC'))


    id=colors.create_rectangle((10,100,30,120),fill="#FF1493")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#FF1493'))


    id=colors.create_rectangle((10,130,30,150),fill="#EE0000")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#EE0000'))


    id=colors.create_rectangle((10,160,30,180),fill="#27408B")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#27408B'))


    id=colors.create_rectangle((10,190,30,210),fill="#00C5CD")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#00C5CD'))


    id=colors.create_rectangle((10,220,30,240),fill="#FFFF00")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#FFFF00'))


    id=colors.create_rectangle((10,250,30,270),fill="#98FB98")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#98FB98'))


    id=colors.create_rectangle((10,280,30,300),fill="#FF8000")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('#FF8000'))






display_pallete()



#mainscreen
canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)


canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)



##########################
current_value=tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


slider = ttk.Scale(root, from_=0,to=100, orient="horizontal", command=slider_changed,variable=current_value)
slider.place(x=30,y=530)                   



value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)







root.mainloop()
