from tkinter import *
window = Tk()
window.title("MQTT Dashboard")
window.geometry('500x440') # Width, Height
window.resizable(False,False) # Width, Height
window.configure(bg="white")
# Header image
canvas = Canvas(window, width=500,height=188)
canvas.place(x=0,y=0)
img = PhotoImage(file="head_img.png")
canvas.create_image(0,0,anchor=NW,image=img)
# Display "suhu" image
canvas2 = Canvas(window,width=500,height=252)
canvas2.place(x=0,y=189)
img2 = PhotoImage(file="temp_img.png")
canvas2.create_image(0,0,anchor=NW,image=img2)

# Label °C
temp_label = Label(window,

text=" °C",
bg="white",
fg="black",
font=("Helvetica", 50))
temp_label.place(x=310,y=300)
# Label Value Suhu
hum_label = Label(window,

text="38",bg="white",fg="black", font=("Helvetica", 100))

hum_label.place(x=250, y=320, anchor=CENTER)
window.mainloop()