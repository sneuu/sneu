from tkinter import *
import tkinter as tk
fenetre=Tk()


x=1
y=1
x=int(x)
y=int(y)

t=IntVar() 
bouton1=Radiobutton(fenetre, text="Lettre verte", variable=t, value=1)
bouton2=Radiobutton(fenetre, text="Lettre prioritaire", variable=t, value=2)
bouton3=Radiobutton(fenetre, text="Ecopli", variable=t, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

t.get()


p=IntVar() 
bouton20=Radiobutton(fenetre, text="< 20g", variable=p, value=1)
bouton50=Radiobutton(fenetre, text="< 50g", variable=p, value=2)
bouton100=Radiobutton(fenetre, text="< 100g", variable=p, value=3)
bouton20.pack()
bouton50.pack()
bouton100.pack()

p.get()


canvas = tk.Canvas(fenetre, width=50, height=50)
canvas.pack()
i = 0 # ou toute autre valeur initiale
# utiliser une variable tk :
i_var = tk.StringVar()
i_var.set(str(i))
# affichage de i sur le canvas en (20, 20) :
text_i = canvas.create_text(20, 20, text=i_var.get())
def updateEverySecond():
    global i
    # pour l'exemple :
    if t.get()==1 and p.get()==1:
        i=0.57
    elif t.get()==1 and p.get()==2:
        i=0.60
    elif t.get()==1 and p.get()==3:
        i=0.55
    elif t.get()==2 and p.get()==1:
        i=1.40
    elif t.get()==2 and p.get()==2:
        i=1.00
    elif t.get()==2 and p.get()==3:
        i=0.78
    elif t.get()==3 and p.get()==1:
        i=1.40
    elif t.get()==3 and p.get()==2:
        i=1.45
    elif t.get()==3 and p.get()==3:
        i=1.00
    else:
        i=0
    
    # ou toute autre façon de mettre i à jour
    i_var.set(str(i)+" €")
    canvas.itemconfigure(text_i, text=i_var.get())
    fenetre.after(1000, updateEverySecond)
updateEverySecond()

fenetre.mainloop()
