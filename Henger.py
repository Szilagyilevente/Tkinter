from tkinter import *
foablak=Tk()

Sugar=Label(foablak, text='Sugár (cm):')
Sugar.grid()
Sugarmezo=Entry(foablak)
Sugarmezo.grid()
Magassag=Label(foablak, text='Magasság (cm):')
Magassag.grid()
Magasmezo=Entry(foablak)
Magasmezo.grid()
Kiszámít=Button(foablak, text='Kiszámít', command=osszeg)
Kiszámít.grid()

foablak.mainloop()
