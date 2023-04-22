from tkinter import *
from tkinter import filedialog
from pathlib import Path



def abrir():
    archivo = filedialog.askopenfilename(filetypes=(("Arcivos de texto", "*.txt"),("Todos", "*.*")))
    
    return archivo

archivo1 = Path(abrir())

print(archivo1)

#cont = open(archivo1)
#print(cont.read())


print(9 == "9")
