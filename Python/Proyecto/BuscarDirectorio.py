from tkinter import *
from tkinter import filedialog
from pathlib import Path



def abrir():
    archivo = filedialog.askopenfilename(filetypes=(("Arcivos de texto", "*.txt"),("Todos", "*.*")))
    Ruta = Path(archivo)
    return Ruta
