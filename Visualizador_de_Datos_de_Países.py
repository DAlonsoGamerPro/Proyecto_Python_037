from tkinter import *
import requests
import json
root = Tk()
root.geometry("400x350")
root.title("V.D.P.")
root.config(bg="light sea green")

city_name_label = Label(root,text="Nombre de la Capital: ", font=("Helvetika", 18, "bold"), bg="light sea green", fg="white")
city_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry = Entry(root)
city_entry.place(relx=0.2,rely=0.25,anchor=CENTER)

contry_name = Label(root,text="País: ", font=("Helvetika", 10, "bold"), bg="light sea green", fg="white")
contry_name.place(relx=0.06,rely=0.33,anchor=W)

contry_region = Label(root,text="Región: ", font=("Helvetika", 10, "bold"), bg="light sea green", fg="white")
contry_region.place(relx=0.06,rely=0.42,anchor=W)

contry_language = Label(root,text="Lenguaje/Idioma: ", font=("Helvetika", 10, "bold"), bg="light sea green", fg="white")
contry_language.place(relx=0.06,rely=0.51,anchor=W)

contry_population = Label(root,text="Población: ", font=("Helvetika", 10, "bold"), bg="light sea green", fg="white")
contry_population.place(relx=0.06,rely=0.61,anchor=W)

contry_area = Label(root,text="Área: ", font=("Helvetika", 10, "bold"), bg="light sea green", fg="white")
contry_area.place(relx=0.06,rely=0.71,anchor=W)

btn_search = Button(root,text="Detalles de la Ciudad", bg="lime green")
btn_search.place(relx=0.2,rely=0.81,anchor=CENTER)

root.mainloop()