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
Terfogat=Label(foablak, text='Térfogat:')
Terfogat.grid()
Terfogatmezo=Entry(foablak)
Terfogatmezo.grid()
Vashenger=Label(foablak, text='Vashenger')
Vashenger.grid()
Vashengermezo=Entry(foablak)
Vashengermezo.grid()
Fahenger=Label(foablak, text='Fahenger')
Fahenger.grid()
Fahengermezo=Entry(foablak)
Fahengermezo.grid()
foablak.mainloop()
