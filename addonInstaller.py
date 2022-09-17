import shutil
import tkinter as tk
from tkinter import ttk
from tkinter  import filedialog


app = tk.Tk()

def button_command():
    directory_path = filedialog.askdirectory()
    labelPath = ttk.Label(text=directory_path)
    labelPath.place(x=90, y=100, height=40)
    labelPath['background'] = '#eb34e5'
    shutil.copytree('./files/', directory_path, dirs_exist_ok=True)
    print(directory_path)
    
def installation():
    print('test')

app.title("Addon installer")
app.config(width=600, height=350)
app['background'] = '#eb34e5'

label = ttk.Label(text="Browse directory to install the addons:")
label.place(x=20, y=20)

button = ttk.Button(text="Install")
button.place(x=250, y=18)
button.config(command=button_command)

app.mainloop()