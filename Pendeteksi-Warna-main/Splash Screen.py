from tkinter import *
from PIL import ImageTk, Image

root = Tk()
height = 400
width = 500

width = root.winfo_screenwidth()
height = root.winfo_screenheight()


# Memasukan Sumber Gambar
image = "Data/Logo.png"
image = Image.open(image)

# Merubah Ukuran Gambar (lebar,tinggi), agar membuat tidak ada border)
resized = image.resize((500,400), Image.ANTIALIAS)

#membuat Canvas
image = ImageTk.PhotoImage(resized)
canvas = Canvas(root, height=height*0.8, width=width*0.8)
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# Membuat Tidak ada frame 
root.overrideredirect(True)
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))


# Menjalankan Splash screen dengan itungan 5000 milisecond lalu tutup
root.after(5000, root.destroy)
root.mainloop()
