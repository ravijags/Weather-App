from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fe7d7c237769e4a48b5dea1f8995957f").json()
    w_label1.config(text=data['weather'][0]['main'])
    wb_label1.config(text=data['weather'][0]['description'])
    temp_label1.config(text=int(data['main']['temp'] - 273.15))  # Convert Kelvin to Celsius
    per_label1.config(text=data['main']['pressure'])

win=Tk()
win.title("Weather")
win.config(bg='blue')
win.geometry("500x570")

name_label = Label(win,text="Weather App",font=("Arial", 20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name=[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

com=ttk.Combobox(win,text="Weather App",values=list_name ,font=("Arial", 10,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text="Weather Climate",font=("Arial", 20,))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",font=("Arial", 20,))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("Arial", 17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text="",font=("Arial", 17))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature",font=("Arial", 20,))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",font=("Arial", 20,))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label = Label(win,text="Pressure",font=("Arial", 20,))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",font=("Arial", 20,))
per_label1.place(x=250,y=470,height=50,width=210)
                    
done_button= Button(win,text="Done",font=("Arial", 10,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()
