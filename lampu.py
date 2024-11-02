from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("AMIKOM Monitoring Dashboard")
window.geometry('540x600')  # Increased width to accommodate the layout
window.resizable(False, False)
window.configure(bg="white")

# Header image
canvas = Canvas(window, width=500, height=150)
canvas.grid(row=0, column=0, columnspan=4)  # Span across all columns
img = PhotoImage(file="head_img.png") 
canvas.create_image(0, 0, anchor=NW, image=img)



# Function to resize images
def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)

# Display "suhu" image
canvas_suhu = Canvas(window, width=300, height=150)
canvas_suhu.grid(row=1, column=0)
img_suhu_resized = resize_image("temp_img.png", 300, 150)
canvas_suhu.create_image(0, 0, anchor=NW, image=img_suhu_resized)

# Label °C
temp_label = Label(window,
                   text="Temperature",
                   bg="white",
                   fg="black",
                   font=("Helvetica", 15))
temp_label.grid(row=1, column=1)

# Label Value Suhu
temp_value_label = Label(window,
                         text="38 °C",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 20))
temp_value_label.grid(row=1, column=2)

# Display "lampu" image
canvas_lampu = Canvas(window, width=300, height=150)
canvas_lampu.grid(row=2, column=0)
img_lampu_resized = resize_image("lamp_img.png", 200, 150)
canvas_lampu.create_image(0, 0, anchor=NW, image=img_lampu_resized)

# Label Lampu
lampu_label = Label(window,
                    text="Lamp Status: ON",
                    bg="white",
                    fg="black",
                    font=("Helvetica", 15))
lampu_label.grid(row=2, column=1)

# Display "kelembapan" image
canvas_kelembapan = Canvas(window, width=300, height=150)
canvas_kelembapan.grid(row=3, column=0)
img_kelembapan_resized = resize_image("humidity_img.png", 200, 150)
canvas_kelembapan.create_image(0, 0, anchor=NW, image=img_kelembapan_resized)

# Label Kelembapan
kelembapan_label = Label(window,
                         text="Humidity",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 15))
kelembapan_label.grid(row=3, column=1)

# Label Value Kelembapan
kelembapan_value_label = Label(window,
                               text="60%",
                               bg="white",
                               fg="black",
                               font=("Helvetica", 20))
kelembapan_value_label.grid(row=3, column=2)

window.mainloop()
