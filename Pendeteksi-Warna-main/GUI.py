from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image
from Pendeteksi_Gambar import Playgambar
from Pendeteksi_Video import Playvideo

root = Tk()
var = StringVar()
filename_record = {}

def mulai():
    if var.get() == "Image":
        try:
            Playgambar(filename_record)
        except:
            messagebox.showinfo(title='File Tidak Ditemukan', message='Input File terlebih Dahulu')

    elif var.get() == "Video" :
        Playvideo()


def OpenFile(file):
    file['gambar1'] =  filedialog.askopenfilename(title = "Select file",filetypes = ( ("jpg files","*.jpg"), ("WMV files","*.wmv"), ("AVI files","*.avi") ))
    my_label.config(text=file)
    
def print_selection():
    Label1.config(text='U Chose ' + var.get())
   
    
# Membuat Judul Aplikasi   
root.title('Color Detection')
    
# Membuat Ukuran Background GUI
canvas = Canvas(root, height=400, width=500,bg='Azure2')
canvas.pack()


# Membuat Label Widget
Label1 = Label(root, bg='white', width=40, height = 1 ,text='Chose The Media')
Label1.place(x=110,y=11)

# Membuat Frame
frame = Frame(root,bg="white")
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

# Membuat label didalam frame
my_label = Label(frame,bg="light sky blue", text="File Name", width = 25,)
my_label.place(x=190,y=13)

# Membuat Radio Button pada frame
r1 = Radiobutton(frame,width=15, text='Image Detector', variable=var, value='Image', command=print_selection)
r1.place(x=5,y=10)

r2 = Radiobutton(frame,width=15, text='Video Detector ', variable=var, value='Video', command=print_selection)
r2.place(x=5,y=40)

# Membuat Tombol
mybtn = Button(frame,  text = 'Select image file', command=lambda: OpenFile(filename_record))
mybtn.place(x=145,y=10)

button2 = Button(frame, text ='Start', width = 25, command=mulai)
button2.pack()
button2.place(relx=0.28,rely=0.9)

root.mainloop()

