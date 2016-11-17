from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from PIL import Image,ImageTk,ImageFilter
import datetime

global temp1
if __name__ == "__main__":
    top = Tk()
    top.geometry("1350x700")
    #top.configure(background='pink')
    
    #adding the image
    temp=Image.open(askopenfilename(parent=top, initialdir="E:/",title='Choose an image.'))
    temp = temp.resize((170,170))
    #temp=temp.rotate(90)
    img = ImageTk.PhotoImage(temp)
    
    #panel = Label(top, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    #function to be called when mouse is clicked
    #def printcoords(event):
        #outputting x and y coords to console
        #print (event.x,event.y)
    #mouseclick event
    #panel.bind("<Button 1>",printcoords
    def rot90():
        global temp1
        #im = Image.open("aka.jpg")
        temp1=temp.rotate(90)
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1
        #panel = Label(top, image = img,width=10,height=10)
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        #tkMessageBox.showinfo("HELLO","AKASH")

    def rot180():
        global temp1
        temp1=temp.rotate(180)
        #im = Image.open("aka.jpg")
        #img.rotate(180).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def rot270():
        global temp1
        temp1=temp.rotate(270)
        #im = Image.open("aka.jpg")
        #img.rotate(270).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def color1():
        global temp1
        temp1=temp.convert("L")
        #img = Image.open("aka.jpg")
        #img.convert("L").show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def resize1():
        global temp1
        temp1=temp.resize((200,200))
        #im = Image.open("aka.jpg")
        #img.resize((128,128)).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter1():
        global temp1
        temp1=temp.filter(ImageFilter.SHARPEN)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter2():
        global temp1
        temp1=temp.filter(ImageFilter.BLUR)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter3():
        global temp1
        temp1=temp.filter(ImageFilter.CONTOUR)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter4():
        global temp1
        temp1=temp.filter(ImageFilter.EDGE_ENHANCE)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter5():
        global temp1
        temp1=temp.filter(ImageFilter.EMBOSS)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter6():
        global temp1
        temp1=temp.filter(ImageFilter.FIND_EDGES)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def filter7():
        global temp1
        temp1=temp.filter(ImageFilter.SMOOTH)
        #im = Image.open("aka.jpg")
        #img.filter(ImageFilter.DETAIL).show()
        img1 = ImageTk.PhotoImage(temp1)
        panel.configure(image = img1)
        panel.image = img1

    def save():
        #file name formate : year hour(24hr formate) minutes seconds
        date_string = datetime.datetime.now().strftime("%Y%H%M%S")
        temp1.save(date_string + ".jpeg")
        tkMessageBox.showinfo("Info","Image Saved")

    var = StringVar()
    label = Label(top, textvariable=var, relief=FLAT, pady=5)
    var.set("~~Photo Editor~~")
    label.config(font=("Courier", 15))
    label.pack()

    B1=Button(top, text="Rotate Image - 90 deg",command=rot90,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Rotate Image - 180 deg",command=rot180,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Rotate Image - 270 deg",command=rot270,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Re-size Image",command=resize1,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Black and White Image",command=color1,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Blur Image",command=filter2, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Sharpen Image",command=filter1, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Emboss Image",command=filter5, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Contour Image",command=filter3, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Enhance Edge",command=filter4, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Smooth Image",command=filter7, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="Find Edges",command=filter6, padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    B1=Button(top, text="SAVE IMAGE",command=save,padx=50, width=40, borderwidth=5, relief=RIDGE, fg="white", bg="orange")
    B1.config(font=('helvetica', 9))
    B1.pack(pady=2)

    panel = Label(top, image = img)
    panel.pack(pady=5)
    
    top.mainloop()
