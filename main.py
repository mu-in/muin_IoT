from tkinter import *
from PIL import Image, ImageTk
import cv2

cam = cv2.VideoCapture(0)

def onClick():
    cvt_img = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
    cvt_size = cv2.resize(cvt_img,dsize=(426,240),interpolation=cv2.INTER_AREA)
    
    img = Image.fromarray(cvt_size)
    imgtk = ImageTk.PhotoImage(image=img)
    
    picture.imgtk = imgtk
    picture.configure(image=imgtk)

    text.config(text='무야호~~')
    
# ------------ tkinter ------------
tk = Tk()
tk.title('muin')
tk.geometry('650x430+30+30') # 가로 x 세로 + x좌표 + y좌표
tk.resizable(False,False) # 크기 변경 불가

frame1 = Frame(tk,highlightbackground='black',highlightthickness=1)
frame1.config(width=450,height=270)
frame1.place(x=100,y=35)

frame2 = Frame(tk,highlightbackground='black',highlightthickness=1)
frame2.config(width=450,height=35)
frame2.place(x=100,y=320)

picture = Label(tk)
picture.grid(row=10,columns=10)
picture.place(x=112,y=50)

text = Label(tk)
text.place(x=105,y=325)

btn = Button(tk, width=15,command=onClick)
btn.config(text='captrue!')
btn.place(x=250,y=380)

tk.mainloop()